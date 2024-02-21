import os

from data import DataTab
from map import MapTab
from diagram import DiagramTab
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel

# Creating the main window
class App(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.title = 'Earthquake Prediction KZ' #EPKZ
        self.left = 0
        self.top = 0
        self.width = width
        self.height = height
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Diagram")
        self.tabs.addTab(self.tab2, "Data")
        self.tabs.addTab(self.tab3, "Map")

        self.tab1.setLayout(DiagramTab.get_layout(self))
        self.tab2.setLayout(DataTab.get_layout(self))
        self.tab3.setLayout(MapTab.get_layout(self))

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    size = app.primaryScreen().size()
    ex = App(width=size.width(), height=size.height())
    sys.exit(app.exec_())