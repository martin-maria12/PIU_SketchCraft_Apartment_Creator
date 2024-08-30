
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from selectRoomPersonalized import UI_SelectRoomPersonalizedWindow

class UI_CreatePersonalizedWindow(object):

    def openSelectRoom1(self,createW):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_SelectRoomPersonalizedWindow(num_rooms=1)
        self.ui.setupUi(self.window, createW)
        self.window.show()
        self.ui.goBack = createW
        createW.hide()

    def openSelectRoom2(self,createW):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_SelectRoomPersonalizedWindow(num_rooms=2)
        self.ui.setupUi(self.window, createW)
        self.window.show()
        self.ui.goBack = createW
        createW.hide()

    def openSelectRoom3(self, createW):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_SelectRoomPersonalizedWindow(num_rooms=3)
        self.ui.setupUi(self.window, createW)
        self.window.show()
        self.ui.goBack = createW
        createW.hide()

    def home(self, main_w, create_w):
        main_w.show()
        create_w.close()

    def setupUi(self,CreateWindow, MainWindow):
        CreateWindow.setObjectName("CreateWindow")
        CreateWindow.setFixedSize(1500, 850)
        CreateWindow.setWindowTitle("SketchCraft Apartment Creator")
        background_pixmap = QPixmap('Imagini/background2.jpg')
        background_image = background_pixmap.scaled(CreateWindow.size(), Qt.KeepAspectRatioByExpanding)
        palette = CreateWindow.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        CreateWindow.setPalette(palette)

        central_widget = QWidget(CreateWindow)
        CreateWindow.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        title_label = QLabel('Select number of rooms')
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(34)
        title_label.setStyleSheet("color: #e06797")
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        button_layout = QHBoxLayout()

        button_style = """
                         QPushButton {
                             color: #e06797;
                             background-color: #f4bfd4;
                             border: 2px solid #e995b7;
                             border-radius: 15px;
                             margin-left: 40px;
                             margin-right: 40px;
                         }
                         QPushButton:hover {
                             background-color: #e995b7;
                             border-color:#f4bfd4;
                             color: #f4bfd4;
                         }
                        """
        button_back_style = """
                             QPushButton {
                                 color: #e06797;
                                 background-color: #f4bfd4;
                                 border: 2px solid #e995b7;
                                 border-radius: 15px;
                                 margin-left: 40px;
                                 margin-right: 40px;
                                 padding: 3px 20px;
                             }
                             QPushButton:hover {
                                 background-color: #e995b7;
                                 border-color:#f4bfd4;
                                 color: #f4bfd4;
                             }
                            """

        button_1room = QPushButton('1 Room')
        button_1room.setFont(QFont("Agbalumo", 20))
        button_1room.setStyleSheet(button_style)
        button_1room.setCursor(Qt.PointingHandCursor)

        button_1room.clicked.connect(lambda: self.openSelectRoom1(CreateWindow))

        button_2rooms = QPushButton('2 Rooms')
        button_2rooms.setFont(QFont("Agbalumo", 20))
        button_2rooms.setStyleSheet(button_style)
        button_2rooms.setCursor(Qt.PointingHandCursor)

        button_2rooms.clicked.connect(lambda: self.openSelectRoom2(CreateWindow))

        button_3rooms = QPushButton('3 Rooms')
        button_3rooms.setFont(QFont("Agbalumo", 20))
        button_3rooms.setStyleSheet(button_style)
        button_3rooms.setCursor(Qt.PointingHandCursor)

        button_3rooms.clicked.connect(lambda: self.openSelectRoom3(CreateWindow))

        back_button_layout = QHBoxLayout()

        button_back = QPushButton("Back")
        button_back.setFont(QFont("Agbalumo", 15))
        button_back.setStyleSheet(button_back_style)
        button_back.setCursor(Qt.PointingHandCursor)

        back_button_layout.addWidget(button_back)
        back_button_layout.setAlignment(Qt.AlignLeft)

        button_layout.addWidget(button_1room)
        button_layout.addWidget(button_2rooms)
        button_layout.addWidget(button_3rooms)

        button_back.clicked.connect(lambda: self.home(MainWindow,CreateWindow))

        main_layout.addLayout(button_layout)

        image_label = QLabel()
        pixmap = QPixmap('Imagini/sofa_img.png')
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_label)
        main_layout.addLayout(back_button_layout, 0)
        CreateWindow.setLayout(main_layout)