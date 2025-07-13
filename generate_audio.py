from gtts import gTTS
import os

samples = {
    "satisfait": "Merci beaucoup, je suis très content du service.",
    "neutre": "Je voulais juste avoir des informations sur mon abonnement.",
    "mecontent": "Je suis très déçu, rien ne fonctionne correctement."
}

os.makedirs("data/sample_audio", exist_ok=True)

for label, text in samples.items():
    tts = gTTS(text, lang='fr')
    tts.save(f"data/sample_audio/{label}.mp3")

print("✅ Audios générés dans data/sample_audio/")