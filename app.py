import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt, QUrl, QThreadPool
from View.MainWindow import Ui_MainWindow
from Model.NewsManager import NewsManager
from Model.NewsListwidget import NewsWidget


URL = 'https://hn.algolia.com/api/v1/search?tags=front_page'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread_pool = QThreadPool()
        self.newsList.itemClicked.connect(self.show_post)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fetch_news()

    def fetch_news(self):
        news_manager = NewsManager(url=URL)
        news_manager.signals.finished.connect(self.fetch_successful)
        news_manager.signals.error.connect(self.fetch_failed)
        self.thread_pool.start(news_manager)
        
    def fetch_successful(self, response: list):
        for post in response:
            item = QListWidgetItem()
            widget = NewsWidget()
            widget.post_title.setText(post['title'])
            widget.post_author.setText(f"Author: {post['author']}")
            widget.post_comments.setText(f"Comments: {post['num_comments']}")
            item.setData(Qt.UserRole, str(post['url']))
            self.newsList.insertItem(self.newsList.count(),  item)
            self.newsList.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())

    def fetch_failed(self, error: str):
        print(error)

    def show_post(self):
        selected_post = self.newsList.currentItem()
        if selected_post:
            url = selected_post.data(Qt.UserRole)
            self.newsWebViewer.load(QUrl(url))


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()