import sys
import threading

import speech_recognition
import pyttsx3 as tts

class Assistant:
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 200)

        # self.assistant = GenericAssistant()

        # threading.Thread(target=self.run_assistant).start()
        # self.root.mainloop()

    def run_assistant(self):
        while True:
            # try:
            with speech_recognition.Microphone() as mic:

                print("Fale algo...")
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic)
                voices = self.speaker.getProperty('voices')
                self.speaker.setProperty('voice', voices[3].id)

                try:
                    # Reconhece o áudio usando o Google Speech Recognition
                    texto = self.recognizer.recognize_google(audio, language="pt-BR")
                    print(f"Você disse: {texto}")
                    if 'oi' in texto.lower():
                        self.speaker.say("Oi!, tudo bem!?")
                        self.speaker.runAndWait()

                    
                    if 'suas vozes' in texto.lower():
                        voices = self.speaker.getProperty('voices')
                        for voz in voices:
                            print("ID: ", voz.id)
                            print("Nome: ", voz.name)
                            print("Idioma: ", voz.languages)
                            print("Gênero: ", voz.gender)
                            print("``````````````````````````````````````````````````````````````````")

                except speech_recognition.exceptions.UnknownValueError:
                    print("Não foi possível entender o áudio.")
                except speech_recognition.exceptions.RequestError as e:
                    print(f"Erro ao fazer a requisição ao serviço Google Speech Recognition: {e}")
               

Assistant()
Assistant().run_assistant()