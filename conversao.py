import comtypes
import pyttsx3


def text_to_speech(texto):
    # Inicializar o COM antes de usar o pyttsx3
    comtypes.CoInitialize()
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


text_to_speech('Olá, mundo, Python é incrível!')
