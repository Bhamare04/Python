from gtts import gTTS

text = "Hello, My name is Kartik and I am a software developer. I love coding and creating new projects."
tts = gTTS(text=text, lang='en')
tts.save("voice.mp3")