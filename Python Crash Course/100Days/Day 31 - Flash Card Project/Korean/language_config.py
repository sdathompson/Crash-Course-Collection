from dataclasses import dataclass


@dataclass
class LanguageConfig:
    display_name: str  # e.g. "Korean"
    lang_code: str  # gTTS language code e.g. "ko"
    bg_color: str  # Tkinter bg color
    flipped_bg_color : str
    csv_path: str  # Path to the CSV
    word_col: str  # Column name for the target language word
    translation_col: str  # Column name for the English translation
    temp_filename: str  # Temp mp3 filename e.g. "korean_temp.mp3"