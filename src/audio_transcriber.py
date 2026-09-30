def transcribe_audio(audio_file):
    """
    Mock interface for Whisper local NPU execution.
    Replace with ONNX Runtime Whisper QNN engine call in deployment.
    """
    file_name = audio_file.name
    
    transcript = f"[On-Device Audio Transcription for {file_name}]\nDiscussion focused on project delivery deadlines, Snapdragon NPU integration, and offline privacy safeguards."
    
    summary = """
    - **Key Takeaway 1:** All model processing runs on Hexagon NPU.
    - **Key Takeaway 2:** Zero cloud latency and no subscription required.
    - **Action Item:** Finalize submission details on Unstop portal.
    """
    return transcript, summary
