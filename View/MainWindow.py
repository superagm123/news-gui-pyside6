# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowwLgTBi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 721)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newsList = QListWidget(self.centralwidget)
        self.newsList.setObjectName(u"newsList")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(15)
        self.newsList.setFont(font)

        self.horizontalLayout.addWidget(self.newsList)

        self.newsWebViewer = QWebEngineView(self.centralwidget)
        self.newsWebViewer.setObjectName(u"newsWebViewer")
        self.newsWebViewer.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout.addWidget(self.newsWebViewer)

        self.horizontalLayout.setStretch(0, 30)
        self.horizontalLayout.setStretch(1, 70)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"News", None))
    # retranslateUi

