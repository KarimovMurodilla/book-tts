import requests


class Muxlisa:
    def __init__(self):
        self.__api = "https://api.muxlisa.uz/v1/tts/?text="
    
    def text_to_speech(self, text):
        url = self.__api + text
        resp = requests.get(url)
        audio_file_bytes = resp.content

        return audio_file_bytes

