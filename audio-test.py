from gtts import gTTS

text = "Bonjour Rahaf, je t’aime"

tts = gTTS(text=text, lang="fr")

tts.save("voice.mp3")

print("audio saved successfully")