import pygame
import os
import time
import threading
from mutagen import mp3


class musicHandling:
    def __init__(self, filesPath):
        pygame.mixer.init()
        self.soundFilesPath = filesPath
        self._sampleSoundLocation = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files/sampleSound.mp3")
        self._musicFileBell = self._find_mp3_file("1")
        self._musicFilePrebell = self._find_mp3_file("2")
        self._musicFileAlarm = self._find_mp3_file("0")
        self.musicFileNameBell = os.path.basename(self._musicFileBell)
        self.musicFileNamePrebell= os.path.basename(self._musicFilePrebell)
        self.musicFileNameAlarm= os.path.basename(self._musicFileAlarm)
  

    def _find_mp3_file(self, start_letter):
        for root, dirs, files in os.walk(self.soundFilesPath):
            for filename in files:
                if filename.endswith(".mp3") and filename.startswith(start_letter):
                    return os.path.join(root, filename)
        return self._sampleSoundLocation


    def _play_music_thread(self, file):
        if file and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(self._get_mp3_length(file)+1)
            pygame.mixer.music.stop()

    def _play_music(self, file):
        pygame.mixer.music.stop()
        threading.Thread(target=self._play_music_thread(file)).start()

    def _play_alarm_thread(self, file):
        if file and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(99999)       
            
    def _play_alarm(self, file):
        pygame.mixer.music.stop()
        threading.Thread(target=self._play_alarm_thread(file)).start()

    def _get_mp3_length(self, file_path):
        audio = mp3.Open(file_path)
        return audio.info.length

    def playBell(self):
        self._play_music(self._musicFileBell)

    def playPrebell(self):
        self._play_music(self._musicFilePrebell)

    def playAlarm(self):
        self._play_alarm_thread(self._musicFileAlarm)    

    def stopAlarm(self):
        pygame.mixer.music.stop()

