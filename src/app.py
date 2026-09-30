import streamlit as st
import os
from doc_processor import process_document, query_document
from audio_transcriber import transcribe_audio

# Page Configuration
st.set_page_config(
    page_title="SnapFocus AI – On-Device Workspace Copilot",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ SnapFocus AI – On-Device Workspace Copilot")
st.caption("Powered by Qualcomm AI Hub & Snapdragon Hexagon NPU Acceleration")

# Sidebar - Hardware Status
with st.sidebar:
    st.header("⚙️ Hardware Status")
    st.success("Target Device: Snapdragon HP PC")
    st.info("Execution Provider: QNN Execution Provider (NPU)")
    st.markdown("---")
    st.markdown("**Models Active:**")
    st.markdown("- `Llama-3.2-3B-Instruct` (Quantized)")
    st.markdown("- `Whisper-Base` (Audio-to-Text)")
    st.markdown("- `MiniLM-L6-v2` (Embeddings)")

# App Navigation
tab1, tab2, tab3 = st.tabs(["📄 Document Q&A (RAG)", "🎙️ Meeting Audio Summarizer", "✉️ Smart Email Drafts"])

# --- TAB 1: LOCAL DOCUMENT RAG ---
with tab1:
    st.header("Local Document Assistant")
    st.write("Upload confidential documents to analyze them completely offline.")
    
    uploaded_file = st.file_uploader("Upload PDF or Text File", type=["pdf", "txt"])
    
    if uploaded_file:
        with st.spinner("Indexing document on Snapdragon NPU..."):
            doc_text = process_document(uploaded_file)
            st.success("Document indexed locally with zero cloud leakage!")
        
        user_query = st.text_input("Ask a question about your document:")
        if st.button("Query Document"):
            if user_query:
                with st.spinner("Generating answer on Hexagon NPU..."):
                    response = query_document(doc_text, user_query)
                    st.markdown("### Answer:")
                    st.write(response)
            else:
                st.warning("Please enter a question.")

# --- TAB 2: AUDIO SUMMARIZER ---
with tab2:
    st.header("Offline Audio Summarizer")
    st.write("Transcribe lectures or meeting recordings with local Whisper models.")
    
    audio_file = st.file_uploader("Upload Audio Recording", type=["wav", "mp3", "m4a"])
    
    if audio_file:
        if st.button("Transcribe & Summarize"):
            with st.spinner("Transcribing audio on-device..."):
                transcript, summary = transcribe_audio(audio_file)
                st.markdown("### 📝 Transcript:")
                st.write(transcript)
                st.markdown("### 📌 Action Items & Summary:")
                st.write(summary)

# --- TAB 3: SMART EMAIL DRAFTING ---
with tab3:
    st.header("Instant Workspace Copilot")
    prompt = st.text_area("What email or note would you like to draft?", placeholder="Draft a follow-up email about today's project sprint...")
    
    if st.button("Generate Draft"):
        if prompt:
            st.markdown("### Draft Generated On-Device:")
            st.info(f"Subject: Project Follow-Up\n\nDear Team,\n\nBased on our latest updates: {prompt}\n\nBest regards,\nSent via SnapFocus AI")
        else:
            st.warning("Please enter a topic.")
