from gtts import gTTS

text = "Messi and Ronaldo are two of the greatest footballers of all time, and their incredible careers, unique playing styles, countless goals, and unforgettable moments have made their rivalry one of the most famous stories in football history."

tts = gTTS(text=text, lang="en")

tts.save("voice.mp3")

print("audio saved successfully")