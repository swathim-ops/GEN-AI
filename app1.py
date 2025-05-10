import streamlit as st
import requests

# Replace with your actual D-ID API key
API_KEY = "your_real_api_key"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

st.title("Text to Video (Avatar)")

text_input = st.text_input("Enter text for the avatar to speak:")

if st.button("Generate Video"):
    # Example presenter_id (you can list presenters via D-ID API if needed)
    payload = {
        "script": {
            "type": "text",
            "input": text_input,
            "provider": {"type": "microsoft", "voice_id": "en-US-AriaNeural"},
            "ssml": False
        },
        "config": {
            "fluent": True,
            "pad_audio": 0.5,
            "stitch": True
        },
        "source_url": "https://create.d-id.com/images/default-presenter.png"  # Replace with real image or presenter if needed
    }

    response = requests.post("https://api.d-id.com/talks", json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        video_url = response.json().get("result_url")
        st.video(video_url)
    else:
        st.error(f"Video generation failed: {response.text}")
