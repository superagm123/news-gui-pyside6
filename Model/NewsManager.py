import requests
from PySide6.QtCore import Slot, QRunnable
from Model.NewsManagerSignals import NewsSignals


class NewsManager(QRunnable):
    def __init__(self, url: str):
        super().__init__()
        self.signals = NewsSignals()
        self.url = url 

    @Slot()
    def run(self):
        try: 
            response = requests.get(self.url)
            data = response.json()['hits']
        except requests.exceptions.RequestException as error:
            self.signals.error.emit(error)
        else:
            self.signals.finished.emit(data)