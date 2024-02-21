import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
from params import ARTIFACTS_FOR_PAPERS_DIR


class MapTab():
    @staticmethod
    def get_layout(main):
        layout = QVBoxLayout(main)

        pixmap = QPixmap(ARTIFACTS_FOR_PAPERS_DIR + 'map.png')
        pixmap_resized = pixmap.scaled(1642, 644)

        image = QLabel()
        image.setPixmap(pixmap_resized)
        layout.addWidget(image)

        image.setPixmap(pixmap_resized)
        image.setAlignment(Qt.AlignCenter)
        layout.addWidget(image)



        return layout