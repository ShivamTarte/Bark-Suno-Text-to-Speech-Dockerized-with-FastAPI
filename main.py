from fastapi import FastAPI
from typing import Optional
from bark import SAMPLE_RATE, generate_audio
from scipy.io.wavfile import write as write_wav
from fastapi.responses import FileResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate_audio")
def generate_suno(text_prompt: str, history_prompt: Optional[str] = None):
    """
    Generate audio based on the given text prompt and optional history prompt.
    If history prompt is provided, it is used along with the text prompt.
    The generated audio is saved as a WAV file and returned as a response.
    """
    if history_prompt is None:
        audio = generate_audio(text_prompt)
    else:
        audio = generate_audio(text_prompt, history_prompt)

    # Save the audio as a WAV file
    audio_file = "output.wav"
    write_wav(audio_file, SAMPLE_RATE, audio)

    # Return the audio file as a response
    return FileResponse(audio_file, media_type="audio/wav", filename="output.wav")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)