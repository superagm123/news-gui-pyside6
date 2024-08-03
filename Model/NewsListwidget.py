from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QFrame


class NewsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.post_title = QLabel()
        self.post_author = QLabel()
        self.post_comments = QLabel()
        self.setupUi()

    def setupUi(self):
        self.post_title.setWordWrap(True)
        frame = QFrame()
        frame.setFrameShape(QFrame.HLine)
        frame.setFrameShadow(QFrame.Sunken)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.post_author)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.post_comments)
        self.main_layout.addWidget(self.post_title)
        self.main_layout.addLayout(bottom_layout)
        self.main_layout.addWidget(frame)
        self.setLayout(self.main_layout)