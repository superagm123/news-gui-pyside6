from PySide6.QtCore import Signal, QObject


class NewsSignals(QObject):
    finished = Signal(list)
    error = Signal(str)