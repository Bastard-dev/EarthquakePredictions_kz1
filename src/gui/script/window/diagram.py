from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget, QGridLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from params import MODELS_DIR, ARTIFACTS_FOR_PAPERS_DIR



class DiagramTab():
    @staticmethod
    def get_layout(main):
        layout = QVBoxLayout(main)
        grid_layout = QGridLayout()

        image_paths = [MODELS_DIR + 'feature_importance.png',
                       MODELS_DIR + 'feature_importance.png',
                       ARTIFACTS_FOR_PAPERS_DIR + 'jointplot_depth_mag.png']


        row = 0
        col = 0
        for path in image_paths:
            pixmap = QPixmap(path)

            pixmap_scaled = pixmap.scaled(pixmap.width() // 3, pixmap.height() // 3)
            label = QLabel()
            label.setPixmap(pixmap_scaled)
            grid_layout.addWidget(label, row, col)
            col += 1


        layout.addLayout(grid_layout)
        return layout

