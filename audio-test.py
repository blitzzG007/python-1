from gtts import gTTS

text = "メッシとロナウドは、史上最高のサッカー選手の二人であり、彼らの素晴らしいキャリア、独特なプレースタイル、数え切れないほどのゴール、そして忘れられない瞬間の数々によって、二人のライバル関係はサッカー史上最も有名な物語の一つとなっています。"

tts = gTTS(text=text, lang="ja")

tts.save("voice.mp3")

print("audio saved successfully")