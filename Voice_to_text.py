import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something\n")

        audio = r.listen(source)

        try:
            print(r.recognize_google(audio))

        except Exception as e:
            print("Error: "+str(e))


while True:
    if __name__ == "__main__":
        main()
    k = 0xff
    if k == 27:
        break