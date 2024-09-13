import urllib.parse
import speech_recognition as sr
from curl_cffi import requests


from django.core.files.uploadedfile import UploadedFile

import io
import speech_recognition as sr

def audio_to_text(audio_file: UploadedFile) -> str:
    # try:
        recognizer = sr.Recognizer()
        
        # Menggunakan io.BytesIO untuk membaca file audio
        audio_file_io = io.BytesIO(audio_file.read())
        
        with sr.AudioFile(audio_file_io) as source:
            audio = recognizer.record(source)
        
        return recognizer.recognize_google(audio)
    # except ValueError as e:
    #     print(f"Error recognizing audio: {e}")
    #     return 
    # except Exception as e:
    #     print(f"Error processing audio: {e}")
    #     return 



def generate_tts_url(text, language='id-ID', speed=1):
    base_url = 'https://translate.google.com/translate_tts'
    params = {
        'ie': 'UTF-8',
        'tl': language,
        'client': 'tw-ob',
        'q': text,
        'ttsspeed': speed
    }
    url = base_url + '?' + urllib.parse.urlencode(params)
    return url


def text_to_audio(text):
    
    tts_url = generate_tts_url(text=text)
    response = requests.get(tts_url, impersonate="chrome120")
    response.raise_for_status()
    
    audio = f'audio.mp3'
    with open(audio, 'wb') as audio_file:
        audio_file.write(response.content)
    
    return audio