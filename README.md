# 🎧 Détection Automatique de Sentiment Vocal

## 📌 Objectif
Transcrire les appels vocaux en texte avec **Wav2Vec2.0** et analyser le sentiment via **BERT**.

## 🚀 Utilisation

### 1. Interface Gradio
```bash
python run_gradio.py
```

### 2. API REST
```bash
uvicorn run_api:app --reload
```

### 3. Génération Audio (localement)
```bash
python generate_audio.py
```

## 🔗 Modèles utilisés
- Wav2Vec2.0: https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self
- BERT Sentiment: https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment