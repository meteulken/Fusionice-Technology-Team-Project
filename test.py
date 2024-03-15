import speech_recognition as sr

def dinle():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleme başladı...")
        while True:
            audio_data = recognizer.listen(source)
            try:
                recognized_text = recognizer.recognize_google(audio_data, language="tr-TR")
                print("Duyulan Kelimeler:", recognized_text)
            except sr.UnknownValueError:
                print("Anlaşılamayan ses")
            except sr.RequestError as e:
                print("Google API isteği başarısız oldu; {0}".format(e))

if __name__ == "__main__":
    dinle()
