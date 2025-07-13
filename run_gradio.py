import gradio as gr
from app.audio_transcriber import transcribe_audio
from app.sentiment_analyzer import analyze_sentiment

def audio_sentiment_pipeline(audio_file):
    text = transcribe_audio(audio_file)
    sentiment = analyze_sentiment(text)
    return f"Transcription: {text}\n\nSentiment: {sentiment}"

gr.Interface(
    fn=audio_sentiment_pipeline,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Détection de Sentiment Vocal"
).launch()