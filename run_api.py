from fastapi import FastAPI, UploadFile
from app.audio_transcriber import transcribe_audio
from app.sentiment_analyzer import analyze_sentiment
import uvicorn

app = FastAPI()

@app.post("/analyze-audio/")
async def analyze_audio(file: UploadFile):
    temp_path = "temp.wav"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    text = transcribe_audio(temp_path)
    sentiment = analyze_sentiment(text)
    return {"transcription": text, "sentiment": sentiment}

if __name__ == "__main__":
    uvicorn.run("run_api:app", host="0.0.0.0", port=8000, reload=True)