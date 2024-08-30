
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QFrame
from PyQt5.QtCore import Qt
from create import UI_CreateWindow
from createPersonalized import UI_CreatePersonalizedWindow
from PyQt5 import QtWidgets
import sys

from help import UI_HelpWindow


class MainWindow(object):

    def open_second_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_CreateWindow()
        self.ui.setupUi(self.window, w)
        self.window.show()
        self.ui.goBack = w
        w.hide()

    def open_second_personalized_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_CreatePersonalizedWindow()
        self.ui.setupUi(self.window, w)
        self.window.show()
        self.ui.goBack = w
        w.hide()

    def open_help_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_HelpWindow()
        self.ui.setupUi(self.window, w)
        self.window.show()
        self.ui.goBack = w
        w.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 850)
        MainWindow.setWindowTitle("SketchCraft Apartment Creator")
        background_pixmap = QPixmap('Imagini/background2.jpg')
        background_image = background_pixmap.scaled(MainWindow.size(), Qt.KeepAspectRatioByExpanding)
        palette = MainWindow.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        MainWindow.setPalette(palette)

        central_widget = QWidget(MainWindow)
        MainWindow.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        self.title_label = QLabel("SketchCraft  Apartment  Creator",central_widget)
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(34)
        self.title_label.setStyleSheet("color: #e06797")
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.title_label, 0, 0, 1, 3)  # 0- linia, 0-coloana, 1-nr de randuri, 3-nr coloane

        button_style = """
                                       QPushButton {
                                           color: #e06797;
                                           background-color: #f4bfd4;
                                           border: 2px solid #e995b7;
                                           border-radius: 15px;
                                           padding: 10px 30px;
                                       }
                                       QPushButton:hover {
                                           background-color: #e995b7;
                                           border-color:#f4bfd4;
                                           color: #f4bfd4;
                                       }
                                   """

        button_create_from_standard = QPushButton("Create from standard")
        button_create_from_standard.setFont(QFont("Agbalumo", 20))
        button_create_from_standard.setStyleSheet(button_style)
        button_create_from_standard.setCursor(Qt.PointingHandCursor)
        layout.addWidget(button_create_from_standard, 2, 1)

        button_create_from_standard.clicked.connect(self.open_second_window)

        button_create_custom_structure = QPushButton("Create custom structure")
        button_create_custom_structure.setFont(QFont("Agbalumo", 20))
        button_create_custom_structure.setStyleSheet(button_style)
        button_create_custom_structure.setCursor(Qt.PointingHandCursor)
        layout.addWidget(button_create_custom_structure, 3, 1)

        button_create_custom_structure.clicked.connect(self.open_second_personalized_window)

        button_help = QPushButton("Help")
        button_help.setFont(QFont("Agbalumo", 20))
        button_help.setStyleSheet(button_style)
        button_help.setCursor(Qt.PointingHandCursor)
        layout.addWidget(button_help, 4, 1)

        button_help.clicked.connect(self.open_help_window)

        image_container = QFrame(MainWindow)
        image_container.setFrameStyle(QFrame.NoFrame)
        layout.addWidget(image_container, 6, 1, 10, 2)

        image_label = QLabel(image_container)
        image_pixmap = QPixmap('Imagini/sofa_img.png')
        image_label.setPixmap(image_pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        layout.setContentsMargins(100, 30, 100, 10)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        MainWindow.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    uii = MainWindow()
    uii.setupUi(w)
    w.show()
    sys.exit(app.exec())