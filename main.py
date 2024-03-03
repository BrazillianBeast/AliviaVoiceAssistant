import os
import sys
import threading
import pygame
import speech_recognition
import pyttsx3 as tts
from modules import actions
# from transformers import AutoProcessor, BarkModel
# from transformers import AutoProcessor, BarkModel

# os.environ["SUNO_OFFLOAD_CPU"] = "True"
# os.environ["SUNO_USE_SMALL_MODELS"] = "True"

class Assistant:
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 200)
        pygame.init()

    # @abstractmethod
    def wake_sound(self):
        # Carrega o arquivo de áudio
        pygame.mixer.music.load('./rise.mp3')
        # Reproduz o áudio
        pygame.mixer.music.play()
        # Espera até que a música termine
        pygame.time.delay(5000)
        # Para a reprodução
        pygame.mixer.music.stop()
        # Finaliza o pygame
        # pygame.quit()

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
                    if 'lucy' in texto.lower():
                        self.wake_sound()
                        # self.speaker.say("Olá!, como posso te ajudar!?")
                        # self.speaker.runAndWait()
                        

                    elif 'você pode me ajudar' in texto.lower():
                        self.speaker.say("Você pode me perguntar como está a temperatura, ou me pedir para realizar alguma ação como abrir o youtube ou netflix!")
                        self.speaker.runAndWait()

                    elif 'comida favorita' in texto.lower():
                        self.speaker.say("Essa é uma pergunta difícil,mas eu gosto muito de sorvetes!?")
                        self.speaker.runAndWait()

                    elif 'youtube' in texto.lower():
                        actions.open_youtube()
                    
                    elif 'netflix' in texto.lower():
                        actions.open_netflix()

                    elif 'spotify' in texto.lower():
                        actions.open_spotify()

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