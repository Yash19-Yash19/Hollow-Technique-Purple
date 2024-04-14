import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for speech input
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)  # Adjust the timeout value as needed
                print("Recognizing...")
                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio)
                print("You said:", text)
            except sr.WaitTimeoutError:
                print("Timeout. Listening again...")
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize_speech()
