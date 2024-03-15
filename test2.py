import threading
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

def kaydet(filename, duration, fs, channels):
    print("Kayıt başladı...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print("Kayıt tamamlandı.")

def dinle_forever():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleme başladı...")
        while True:
            audio_data = recognizer.listen(source, phrase_time_limit=2)  # 2 saniye boyunca dinle
            try:
                recognized_text = recognizer.recognize_google(audio_data, language="tr-TR")
                print("Duyulan Kelimeler:", recognized_text)
            except sr.UnknownValueError:
                print("Anlaşılamayan ses")
            except sr.RequestError as e:
                print("Google API isteği başarısız oldu; {0}".format(e))

def main():
    filename = "kayit.wav"  # Kaydedilecek dosyanın adı
    duration = 5  # Kayıt süresi (saniye cinsinden)
    fs = 44100  # Örnekleme frekansı (örneğin: 44100 Hz)
    channels = 2  # Kayıt kanal sayısı (1: mono, 2: stereo)

    kaydet_thread = threading.Thread(target=kaydet, args=(filename, duration, fs, channels))
    kaydet_thread.start()

    dinle_forever()

if __name__ == "__main__":
    main()
