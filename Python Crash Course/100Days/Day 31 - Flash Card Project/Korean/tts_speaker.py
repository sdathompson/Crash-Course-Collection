import threading
import pygame
import os
import time
from gtts import gTTS

class TTSSpeaker:
    def __init__(self, lang: str, temp_filename: str):
        self.lang = lang
        self.temp_path = os.path.join(os.getenv("TEMP"), temp_filename)
        self._lock = threading.Lock()

    def speak(self, text: str):
        """Speak the given text in a background thread."""
        threading.Thread(target=self._speak, args=(text,), daemon=True).start()

    def _speak(self, text: str):
        """Internal: generate and play TTS audio. Protected by a lock."""
        with self._lock:
            self._stop_playback()
            self._delete_temp()

            tts = gTTS(text=text, lang=self.lang)
            tts.save(self.temp_path)

            if not pygame.mixer.get_init():
                pygame.mixer.init()

            pygame.mixer.music.load(self.temp_path)
            pygame.mixer.music.play()

    def _stop_playback(self):
        """Stop pygame playback and wait for it to release the file."""
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            while pygame.mixer.music.get_busy():
                time.sleep(0.05)
            pygame.mixer.music.unload()

    def _delete_temp(self):
        """Delete the temp file with retry logic for locked files."""
        if not os.path.exists(self.temp_path):
            return

        for attempt in range(5):
            try:
                os.remove(self.temp_path)
                return
            except PermissionError:
                print(f"[TTSSpeaker] File locked, retrying... ({attempt + 1}/5)")
                time.sleep(0.3)

        raise RuntimeError(f"[TTSSpeaker] Could not delete temp file: {self.temp_path}")

    def stop(self):
        """Immediately stop any active playback."""
        self._stop_playback()