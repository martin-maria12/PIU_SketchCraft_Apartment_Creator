
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from floorPlannerPersonalized import FloorplannerPersonalizedApp
from popup import UI_MessageWindow

class UI_SelectRoomPersonalizedWindow(object):
    def __init__(self, num_rooms):
        self.num_rooms = num_rooms

    def openApartament1RoomBedroom(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length,width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="bedroom", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1RoomKitchen(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="kitchen", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1RoomBathroom(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="bathroom", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1RoomLivingRoom(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="LivingRoom", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1Corridor1(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="corridor1", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1Corridor2(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="corridor2", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1Corridor3(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="corridor3", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def openApartament1RoomBedroom2(self, SelectW, nrr):
        custom_dialog = UI_MessageWindow()
        result = custom_dialog.exec_()

        if result == QDialog.Accepted:
            print("OK")
            length, width = custom_dialog.get_measurements()
            print(length, width)

            if length is not None and width is not None:
                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room="bedroom2", nr_rooms=nrr, length=length, width=width)
                self.ui.setupUi(self.window, SelectW)
                self.ui.goBack = SelectW
                self.window.show()
                SelectW.hide()

        elif result == QDialog.Rejected:
            print("Anulare.")

    def home(self, main_w, create_w):
        main_w.show()
        create_w.close()

    def setupUi(self, SelectRoomWindow, CreateWindow):
        SelectRoomWindow.setObjectName("SelectRoomWindow")
        SelectRoomWindow.setFixedSize(1500, 850)
        SelectRoomWindow.setWindowTitle("SketchCraft Apartment Creator")
        background_pixmap = QPixmap('Imagini/background2.jpg')
        background_image = background_pixmap.scaled(SelectRoomWindow.size(), Qt.KeepAspectRatioByExpanding)
        palette = SelectRoomWindow.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        SelectRoomWindow.setPalette(palette)

        central_widget = QWidget(SelectRoomWindow)
        SelectRoomWindow.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        title_label = QLabel('Select the room you want to customize')
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
                             margin-left: 25px;
                             margin-right: 25px;
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

        if self.num_rooms == 1:
            button_kitchen = QPushButton('Kitchen')
            button_kitchen.setFont(QFont("Agbalumo", 20))
            button_kitchen.setStyleSheet(button_style)
            button_kitchen.setCursor(Qt.PointingHandCursor)
            button_kitchen.clicked.connect(lambda: self.openApartament1RoomKitchen(SelectRoomWindow,1))

            button_bathroom = QPushButton('Bathroom')
            button_bathroom.setFont(QFont("Agbalumo", 20))
            button_bathroom.setStyleSheet(button_style)
            button_bathroom.setCursor(Qt.PointingHandCursor)
            button_bathroom.clicked.connect(lambda: self.openApartament1RoomBathroom(SelectRoomWindow,1))

            button_bedroom = QPushButton('Bedroom')
            button_bedroom.setFont(QFont("Agbalumo", 20))
            button_bedroom.setStyleSheet(button_style)
            button_bedroom.setCursor(Qt.PointingHandCursor)
            button_bedroom.clicked.connect(lambda: self.openApartament1RoomBedroom(SelectRoomWindow,1))

            button_corridor = QPushButton('Corridor')
            button_corridor.setFont(QFont("Agbalumo", 20))
            button_corridor.setStyleSheet(button_style)
            button_corridor.setCursor(Qt.PointingHandCursor)
            button_corridor.clicked.connect(lambda: self.openApartament1Corridor1(SelectRoomWindow,1))

            button_layout.addWidget(button_corridor)
            button_layout.addWidget(button_kitchen)
            button_layout.addWidget(button_bathroom)
            button_layout.addWidget(button_bedroom)

        if self.num_rooms == 2:
            button_kitchen = QPushButton('Kitchen')
            button_kitchen.setFont(QFont("Agbalumo", 20))
            button_kitchen.setStyleSheet(button_style)
            button_kitchen.setCursor(Qt.PointingHandCursor)
            button_kitchen.clicked.connect(lambda: self.openApartament1RoomKitchen(SelectRoomWindow,2))

            button_bathroom = QPushButton('Bathroom')
            button_bathroom.setFont(QFont("Agbalumo", 20))
            button_bathroom.setStyleSheet(button_style)
            button_bathroom.setCursor(Qt.PointingHandCursor)
            button_bathroom.clicked.connect(lambda: self.openApartament1RoomBathroom(SelectRoomWindow,2))

            button_bedroom = QPushButton('Bedroom')
            button_bedroom.setFont(QFont("Agbalumo", 20))
            button_bedroom.setStyleSheet(button_style)
            button_bedroom.setCursor(Qt.PointingHandCursor)
            button_bedroom.clicked.connect(lambda: self.openApartament1RoomBedroom(SelectRoomWindow,2))

            button_living_room = QPushButton('Living Room')
            button_living_room.setFont(QFont("Agbalumo", 20))
            button_living_room.setStyleSheet(button_style)
            button_living_room.setCursor(Qt.PointingHandCursor)
            button_living_room.clicked.connect(lambda: self.openApartament1RoomLivingRoom(SelectRoomWindow,2))
            button_layout.addWidget(button_living_room)

            button_corridor2 = QPushButton('Corridor')
            button_corridor2.setFont(QFont("Agbalumo", 20))
            button_corridor2.setStyleSheet(button_style)
            button_corridor2.setCursor(Qt.PointingHandCursor)
            button_corridor2.clicked.connect(lambda: self.openApartament1Corridor2(SelectRoomWindow,2))

            button_layout.addWidget(button_corridor2)
            button_layout.addWidget(button_kitchen)
            button_layout.addWidget(button_bathroom)
            button_layout.addWidget(button_bedroom)

        if self.num_rooms == 3:
            button_kitchen = QPushButton('Kitchen')
            button_kitchen.setFont(QFont("Agbalumo", 20))
            button_kitchen.setStyleSheet(button_style)
            button_kitchen.setCursor(Qt.PointingHandCursor)
            button_kitchen.clicked.connect(lambda: self.openApartament1RoomKitchen(SelectRoomWindow,3))

            button_bathroom = QPushButton('Bathroom')
            button_bathroom.setFont(QFont("Agbalumo", 20))
            button_bathroom.setStyleSheet(button_style)
            button_bathroom.setCursor(Qt.PointingHandCursor)
            button_bathroom.clicked.connect(lambda: self.openApartament1RoomBathroom(SelectRoomWindow,3))

            button_bedroom = QPushButton('Bedroom')
            button_bedroom.setFont(QFont("Agbalumo", 20))
            button_bedroom.setStyleSheet(button_style)
            button_bedroom.setCursor(Qt.PointingHandCursor)
            button_bedroom.clicked.connect(lambda: self.openApartament1RoomBedroom(SelectRoomWindow,3))

            button_living_room2 = QPushButton('Living Room')
            button_living_room2.setFont(QFont("Agbalumo", 20))
            button_living_room2.setStyleSheet(button_style)
            button_living_room2.setCursor(Qt.PointingHandCursor)
            button_living_room2.clicked.connect(lambda: self.openApartament1RoomLivingRoom(SelectRoomWindow,3))
            button_layout.addWidget(button_living_room2)

            button_bedroom2 = QPushButton('Bedroom2')
            button_bedroom2.setFont(QFont("Agbalumo", 20))
            button_bedroom2.setStyleSheet(button_style)
            button_bedroom2.setCursor(Qt.PointingHandCursor)
            button_bedroom2.clicked.connect(lambda: self.openApartament1RoomBedroom2(SelectRoomWindow,3))
            button_layout.addWidget(button_bedroom2)

            button_corridor3 = QPushButton('Corridor')
            button_corridor3.setFont(QFont("Agbalumo", 20))
            button_corridor3.setStyleSheet(button_style)
            button_corridor3.setCursor(Qt.PointingHandCursor)
            button_corridor3.clicked.connect(lambda: self.openApartament1Corridor3(SelectRoomWindow,3))

            button_layout.addWidget(button_corridor3)
            button_layout.addWidget(button_kitchen)
            button_layout.addWidget(button_bathroom)
            button_layout.addWidget(button_bedroom)

        back_button_layout = QHBoxLayout()

        button_back = QPushButton("Back")
        button_back.setFont(QFont("Agbalumo", 15))
        button_back.setStyleSheet(button_back_style)
        button_back.setCursor(Qt.PointingHandCursor)

        back_button_layout.addWidget(button_back)
        back_button_layout.setAlignment(Qt.AlignLeft)

        button_back.clicked.connect(lambda: self.home(CreateWindow, SelectRoomWindow))
        main_layout.addLayout(button_layout)

        image_label = QLabel()
        pixmap = QPixmap('Imagini/sofa_img.png')
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(image_label)
        main_layout.addLayout(back_button_layout, 0)
        SelectRoomWindow.setLayout(main_layout)