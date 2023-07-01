import edge_tts
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from pygame import mixer

class TextToSpeech:

    def __init__(self, text,langauge, fileName):
        self.text = text
        self.language = langauge
        self.fileName = fileName
    
    async def synthesis(self) -> None:
        """
        Take a text and save to filename.mp3 by synthsizing the text.
        Args:
            text: Which would synthesis to sound.
            langauge: Language 
            fileName: File name which synthesis sound save.
        Return:
            None
        """
        voice_model = "am-ET-MekdesNeural" if self.language != "English" else "en-US-AriaNeural"
        communicate = edge_tts.Communicate(self.text, voice_model)
        await communicate.save(self.fileName)
    
    async def play(self) -> None:
        """
        Play the synthesis sound.
        Args:
            fileName: File name of synthesis sound.
        Return:
            None
        """
        mixer.init()
        mixer.music.load(self.fileName)
        mixer.music.play()