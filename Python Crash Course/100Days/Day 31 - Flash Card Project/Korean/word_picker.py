import random
import pandas


class WordPicker:
    def __init__(self, csv_path: str, word_col: str, translation_col: str):
        df = pandas.read_csv(csv_path)
        self._data = pandas.DataFrame(df)[[word_col, translation_col]]
        self.word_col = word_col
        self.translation_col = translation_col
        self._last_pair: tuple[str,str] | None = None

    def random_pair(self) -> tuple[str, str]:
        row = random.randint(0, self._data.shape[0] - 1)
        self._last_pair = self._data.iat[row, 0], self._data.iat[row, 1]
        return self._last_pair

    def last_pair(self) -> tuple[str, str]:
        if self._last_pair is None:
            raise RuntimeError("No word has been picked yet.")
        return self._last_pair

    @property
    def size(self) -> int:
        """Total number of words in the deck."""
        return self._data.shape[0]