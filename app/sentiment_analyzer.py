from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    if "1" in label or "2" in label:
        return "mécontent"
    elif "3" in label:
        return "neutre"
    else:
        return "satisfait"