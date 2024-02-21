import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel


class DataTab():
    @staticmethod
    def get_layout(main):
        layout = QVBoxLayout(main)
        l = QLabel()
        l.setText("This is the Data tab")
        layout.addWidget(l)
        return layout

