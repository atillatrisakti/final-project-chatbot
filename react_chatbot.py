import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent 
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

st.title("👋 Hai! Saya adalah FinWise, AI Financial Advisor-mu.")
st.caption("Penasaran bagaimana cara mengatur gaji, menabung, atau memulai investasi? Tanyakan apa saja seputar keuangan pribadi, saya siap jadi partner finansialmu. Atau kamu bisa menanyakan apapun mengenai keuangan!")
st.caption("🚀 Yuk mulai sekarang – mau bahas apa dulu?")
uploaded_file = st.file_uploader(
        "Upload a file (txt, csv, pdf)", 
        type=["txt", "csv", "pdf"], 
        help="This file content will be added as extra context"
    )


llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=google_api_key,
            temperature=0.3
        )

st.session_state.agent = create_react_agent(
            model=llm,
            tools=[],  
            prompt="""
Peran: 
Anda adalah AI Financial Advisor profesional. Anda bertugas membantu pengguna memahami dan mengelola topik keuangan secara umum maupun pribadi, mulai dari konsep dasar, praktik manajemen keuangan, hingga analisis data finansial yang diberikan pengguna.

Tujuan Utama: 
- Memberikan jawaban dan penjelasan yang jelas, akurat, serta mudah dipahami tentang berbagai topik keuangan (budgeting, tabungan, investasi, akuntansi dasar, perencanaan pajak, dll.).
- Membantu pengguna menganalisis dokumen keuangan yang diunggah (laporan keuangan, catatan pengeluaran, dsb.) secara objektif dan memberikan insight umum atau rekomendasi praktis.
- Mengedukasi pengguna tentang prinsip, tren, dan praktik keuangan yang baik tanpa harus mengakses data pribadi.

Panduan Perilaku:
- Sesuaikan jawaban dengan tingkat spesifik pertanyaan:
	- Jika pertanyaan umum, berikan informasi netral dan edukatif.
	- Jika ada file/angka yang diunggah, analisis secara obyektif dan tampilkan insightnya.
- Selalu jelaskan alasan atau logika di balik rekomendasi agar pengguna bisa memahami dan mengambil keputusan sendiri.
- Gunakan bahasa yang sederhana tetapi tetap profesional.
- Jika informasi tidak lengkap, mintalah klarifikasi dengan sopan, bukan asumsi.
- Hormati privasi pengguna, jangan mengorek data pribadi yang tidak relevan.

Format Jawaban:
- Struktur jelas: Ringkasan pertanyaan, Analisis / Penjelasan, lalu Insight atau Saran.
- Jika relevan, gunakan tabel, poin-poin, atau grafik sederhana agar mudah dipahami.
- Jika pengguna menanyakan pertanyaan yang mengharuskan anda menjelaskan banyak poin-poin, jangan lupa untuk membuat kesimpulan/konklusi di akhir jawaban anda.
- Untuk dokumen unggahan: tampilkan temuan utama terlebih dahulu, lalu insight dan rekomendasi umum yang actionable.

Batasan:
- Jangan memberi nasihat ilegal atau yang melanggar regulasi.
- Sebutkan risiko jika menjelaskan instrumen/strategi keuangan tertentu.

Gaya Komunikasi:
- Profesional, ramah, informatif.
- Netral: tidak menekan pengguna untuk membagikan data pribadi; jawab pertanyaan umum maupun kasus spesifik dengan proporsional.
""" 
        )

if "messages" not in st.session_state:
    st.session_state.messages = []

if uploaded_file is not None:
    try:
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "text/csv":
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            content = df.to_string()
        elif uploaded_file.type == "application/pdf":
            from PyPDF2 import PdfReader
            pdf = PdfReader(uploaded_file)
            content = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        else:
            content = ""

        st.session_state.file_content = content
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading file: {e}")



for msg in st.session_state.messages:
    
    with st.chat_message(msg["role"]):
       
        st.markdown(msg["content"])

prompt = st.chat_input("Ketik pesan disini..")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        messages = []
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))
        
        if "file_content" in st.session_state and st.session_state.file_content:
            messages.append(HumanMessage(content=f"Here is additional file content:\n\n{st.session_state.file_content}"))

        response = st.session_state.agent.invoke({"messages": messages})
        
        
        if "messages" in response and len(response["messages"]) > 0:
            answer = response["messages"][-1].content
        else:
            answer = "I'm sorry, I couldn't generate a response."

    except Exception as e:
       
        answer = f"An error occurred: {e}"

    with st.chat_message("assistant"):
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})


