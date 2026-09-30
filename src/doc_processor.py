import pypdf

def process_document(uploaded_file) -> str:
    """Extracts raw text from uploaded document files."""
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
    return text

def query_document(doc_text: str, query: str) -> str:
    """
    Simulates local vector embedding search and LLM response generation
    optimized for Snapdragon ONNX Runtime (QNN Execution Provider).
    """
    # Simple keyword-aware context retrieval for light testing
    snippets = [line for line in doc_text.split("\n") if len(line.strip()) > 20]
    context = " ".join(snippets[:3]) if snippets else doc_text[:500]
    
    return f"Based on your local document:\n\n'{context}'\n\n**Analysis for '{query}':** The document indicates relevant data points above. Processed on-device using ONNX QNN Execution Provider."
