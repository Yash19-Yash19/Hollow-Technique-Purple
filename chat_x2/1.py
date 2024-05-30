import streamlit as st
import json
import pyttsx3
import speech_recognition as sr
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import sounddevice as sd
import soundfile as sf
import tempfile
import os

# Load model & tokenizer
model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Load context from JSON file
data_path = "context.json"  # Update with your JSON file path
with open(data_path, "r") as f:
    context_data = json.load(f)
    context = context_data["context"]

# Define Streamlit app
def main():
    st.title("Chatbot Web Application")
    st.write("Enter your question below:")

    user_input = st.text_input("Question:")
    voice_input = st.checkbox("Voice Input")

    if voice_input:
        st.write("Speak your question...")

        # Function to record audio
        def record_audio():
            fs = 44100
            seconds = 5
            with tempfile.NamedTemporaryFile(delete=False) as tmp_audio:
                tmp_filename = tmp_audio.name
                print(f"Recording audio to {tmp_filename}")
                my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()
                sf.write(tmp_filename, my_recording, fs)
            return tmp_filename

        tmp_audio_file = record_audio()

        # Function to transcribe audio using Google Speech Recognition
        def transcribe_audio(audio_file):
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                st.error(f"Error with speech recognition service: {e}")
                return None

        user_input = transcribe_audio(tmp_audio_file)

        # Clean up temporary audio file
        os.remove(tmp_audio_file)

        if user_input:
            st.write("You said:", user_input)
        else:
            st.write("Sorry, I could not understand your audio.")

    if st.button("Ask"):
        if user_input.strip() != "":
            QA_input = {'question': user_input, 'context': context}
            res = nlp(QA_input)
            st.write("Answer:", res['answer'])

            # Voice Output
            voice_output = st.checkbox("Voice Output")
            if voice_output:
                engine = pyttsx3.init()
                engine.say("The answer is " + res['answer'])
                engine.runAndWait()

if __name__ == "__main__":
    main()
