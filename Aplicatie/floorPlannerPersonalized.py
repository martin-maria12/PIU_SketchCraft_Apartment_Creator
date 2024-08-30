
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, \
    QGraphicsScene, QGraphicsView, QHBoxLayout, QLabel, QGraphicsRectItem, QGraphicsItem, QMenu, QFileDialog, QDialog
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QBrush, QColor, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets
from furnitureItem import FurnitureItem
from popup import UI_MessageWindow
import os

class FloorplannerPersonalizedApp(QMainWindow):

    def __init__(self, room,nr_rooms,length,width):
        super().__init__()
        self.length=length
        self.width=width
        self.room = room
        self.nr_rooms=nr_rooms
        self.button_style = """
                               QPushButton {
                                   color: #e06797;
                                   background-color: #f4bfd4;
                                   border: 2px solid #e995b7;
                                   border-radius: 15px;
                                   margin-left: 20px;
                                   margin-right: 20px;
                                   padding: 3px 20px;
                               }
                               QPushButton:hover {
                                   background-color: #e995b7;
                                   border-color:#f4bfd4;
                                   color: #f4bfd4;
                               }
                           """
        self.list_layout = None
        self.selected_item = None
        self.floorList=[]
        if room not in ROOMS.keys():
            self.list_layout = None
            self.furnitureList = []
            ROOMS[room] = self
        else:
            self.list_layout = ROOMS[room].list_layout
            self.furnitureList = ROOMS[room].furnitureList

    def loadFurniture(self):
        for furniture_item in self.furnitureList:
            self.scene.addItem(furniture_item)
    def loadFloorTexture(self):
        for floor in self.floorList:
            background_texture = QPixmap(floor)
            background_brush = QBrush(background_texture)
            self.scene.setBackgroundBrush(background_brush)

    def save_scene(self):
        #self.save_scene_to_jpg(self.scene, "output.jpg")
        file_dialog = QFileDialog(self)
        file_dialog.setDefaultSuffix("jpg")
        file_dialog.setNameFilter("JPEG files (*.jpg)")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)

        if file_dialog.exec_() == QFileDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            self.save_scene_to_jpg(self.scene, file_name)

    def save_scene_to_jpg(self, scene, filename):
        pixmap = QPixmap(scene.width(), scene.height())
        pixmap.fill(Qt.white)

        painter = QPainter(pixmap)
        scene.render(painter)
        pixmap.save(filename, "JPG")

        painter.end()

    def home(self, main_w, select_w):
        main_w.show()
        select_w.close()
        global ROOMS
        ROOMS = {}

    def addItemToScene(self, pixmap,item_type):
        for item in self.scene.selectedItems():
            item.setSelected(False)

        furniture_item = FurnitureItem(pixmap,item_type)
        furniture_item.setPos(100, 100)
        furniture_item.setFlag(QGraphicsItem.ItemIsSelectable)
        self.scene.addItem(furniture_item)
        self.selected_item = furniture_item
        self.furnitureList.append(furniture_item)

    def contextMenuEvent(self, event):
        if self.selected_item:
            context_menu = QMenu(self)

            rotate_action = context_menu.addAction("Rotate")
            delete_action = context_menu.addAction("Delete")

            action = context_menu.exec_(self.mapToGlobal(event.pos()))

            if action == rotate_action:
                self.rotateSelectedItem()
            elif action == delete_action:
                self.removeSelectedItem()

    def rotateSelectedItem(self):
        if self.selected_item:
            current_rotation = self.selected_item.rotation()
            self.selected_item.setRotation(current_rotation + 90)

    def removeSelectedItem(self):
        print("Removing selected item")
        selected_items = self.scene.selectedItems()

        for item in selected_items:
            self.scene.removeItem(item)

    def item_clicked(self, item: QListWidgetItem):
        icon: QIcon = item.icon()
        pixmap = icon.pixmap(icon.availableSizes()[0])

        item_name = item.text()
        print("item clicked : ", item_name)

        if "covor" in item_name:
            item_type = "Carpet"
        elif "plant" in item_name:
            item_type = "Plant"

        else:
            item_type = "Furniture"

        print(item_type)
        self.addItemToScene(pixmap, item_type)

    def showImageList(self, image_paths):
        if self.list_layout:
            self.list_layout.deleteLater()

        self.list_layout = QHBoxLayout()
        list_widget = QListWidget()

        for path in image_paths:
            item = QListWidgetItem()
            icon = QIcon()
            pixmap = QPixmap(path)
            icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
            item.setText(path)
            item.setForeground(QColor("transparent"))

            print(item.text())
            list_widget.addItem(item)
            list_widget.setIconSize(QSize(200, 200))

        list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_widget.itemClicked.connect(self.item_clicked)

        self.list_layout.addWidget(list_widget)
        self.sidebar_layout.addLayout(self.list_layout)

    def showImageListFloor(self, image_paths):
        if self.list_layout:
            self.list_layout.deleteLater()

        self.list_layout = QHBoxLayout()
        list_widget = QListWidget()

        for path in image_paths:
            item = QListWidgetItem()
            icon = QIcon()
            pixmap = QPixmap(path)
            icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
            item.setText(path)
            item.setForeground(QColor("transparent"))

            print(item.text())
            list_widget.addItem(item)
            list_widget.setIconSize(QSize(200, 200))

        list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_widget.itemClicked.connect(self.floorTextureScene)

        self.list_layout.addWidget(list_widget)
        self.sidebar_layout.addLayout(self.list_layout)

    def previousRoom(self, windowS, windowF):
        current_room = self.room
        next_room = ""
        print(self.nr_rooms)

        if self.nr_rooms == 1:
            print("apartament 1 room")
            if current_room == "corridor1":
                next_room = "bedroom"
            elif current_room == "kitchen":
                next_room = "corridor1"
            elif current_room == "bathroom":
                next_room = "kitchen"
            elif current_room == "bedroom":
                next_room = "bathroom"

        if self.nr_rooms == 2:
            print("apartament 2 room")
            if current_room == "corridor2":
                next_room = "LivingRoom"
            elif current_room == "kitchen":
                next_room = "corridor2"
            elif current_room == "bathroom":
                next_room = "kitchen"
            elif current_room == "bedroom":
                next_room = "bathroom"
            elif current_room == "LivingRoom":
                next_room = "bedroom"

        if self.nr_rooms == 3:
            print("apartament 3 room")
            if current_room == "corridor3":
                next_room = "bedroom2"
            elif current_room == "kitchen":
                next_room = "corridor3"
            elif current_room == "bathroom":
                next_room = "kitchen"
            elif current_room == "bedroom":
                next_room = "bathroom"
            elif current_room == "LivingRoom":
                next_room = "bedroom"
            elif current_room == "bedroom2":
                next_room = "LivingRoom"

        if next_room != "":
            custom_dialog = UI_MessageWindow()
            result = custom_dialog.exec_()

            if result == QDialog.Accepted:
                print("OK")
                length, width = custom_dialog.get_measurements()
                print(length, width)

                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room=f"{next_room}", nr_rooms=self.nr_rooms, length=length, width=width)
                self.ui.setupUi(self.window, windowS)
                self.ui.goBack = windowS
                self.ui.ui_select = self
                self.window.show()
                windowF.hide()
            elif result == QDialog.Rejected:
                self.window = QtWidgets.QMainWindow()
                if next_room in ROOMS.keys():
                    self.ui = ROOMS[next_room]
                else:
                    self.ui = FloorplannerPersonalizedApp(room=f"{next_room}", nr_rooms=self.nr_rooms,length=1000,width=700)
                self.ui.setupUi(self.window, windowS)
                self.ui.loadFloorTexture()
                self.ui.loadFurniture()
                self.ui.goBack = windowS
                self.ui.ui_select = self
                self.window.show()
                windowF.hide()
        else:
            print("There is no next room.")

    def nextRoom(self, windowS, windowF):
        current_room = self.room
        next_room = ""
        print(self.nr_rooms)

        if self.nr_rooms == 1:
            print("apartament 1 room")
            if current_room == "corridor1":
                next_room = "kitchen"
            elif current_room == "kitchen":
                next_room = "bathroom"
            elif current_room == "bathroom":
                next_room = "bedroom"
            elif current_room == "bedroom":
                next_room = "corridor1"

        if self.nr_rooms == 2:
            print("apartament 2 room")
            if current_room == "corridor2":
                next_room = "kitchen"
            elif current_room == "kitchen":
                next_room = "bathroom"
            elif current_room == "bathroom":
                next_room = "bedroom"
            elif current_room == "bedroom":
                next_room = "LivingRoom"
            elif current_room == "LivingRoom":
                next_room = "corridor2"

        if self.nr_rooms == 3:
            print("apartament 3 room")
            if current_room == "corridor3":
                next_room = "kitchen"
            elif current_room == "kitchen":
                next_room = "bathroom"
            elif current_room == "bathroom":
                next_room = "bedroom"
            elif current_room == "bedroom":
                next_room = "LivingRoom"
            elif current_room == "LivingRoom":
                next_room = "bedroom2"
            elif current_room == "bedroom2":
                next_room = "corridor3"

        if next_room != "":
            custom_dialog = UI_MessageWindow()
            result = custom_dialog.exec_()

            if result == QDialog.Accepted:
                print("OK")
                length, width = custom_dialog.get_measurements()
                print(length, width)

                self.window = QtWidgets.QMainWindow()
                self.ui = FloorplannerPersonalizedApp(room=f"{next_room}", nr_rooms=self.nr_rooms, length=length,
                                                      width=width)
                self.ui.setupUi(self.window, windowS)
                self.ui.goBack = windowS
                self.ui.ui_select = self
                self.window.show()
                windowF.hide()

            elif result == QDialog.Rejected:
                self.window = QtWidgets.QMainWindow()
                if next_room in ROOMS.keys():
                    self.ui = ROOMS[next_room]
                else:
                    self.ui = FloorplannerPersonalizedApp(room=f"{next_room}", nr_rooms=self.nr_rooms, length=1000,width=700)
                self.ui.setupUi(self.window, windowS)
                self.ui.loadFloorTexture()
                self.ui.loadFurniture()
                self.ui.goBack = windowS
                self.ui.ui_select = self
                self.window.show()
                windowF.hide()
        else:
            print("There is no next room.")

    def createFurnitureItem(self, name, image_paths):
        button_meniu = QPushButton(name)
        button_meniu.setFont(QFont("Agbalumo", 15))
        button_meniu.setStyleSheet(self.button_style)
        button_meniu.setCursor(Qt.PointingHandCursor)
        button_meniu.clicked.connect(lambda: self.showImageList(image_paths))
        self.sidebar_layout.addWidget(button_meniu)

    def floorTexture(self,name,path):
        button_meniu=QPushButton(name)
        button_meniu.setFont(QFont("Agbalumo", 15))
        button_meniu.setStyleSheet(self.button_style)
        button_meniu.setCursor(Qt.PointingHandCursor)
        button_meniu.clicked.connect(lambda: self.showImageListFloor(path))
        self.sidebar_layout.addWidget(button_meniu)

    def floorTextureScene(self,item:QListWidgetItem):
        item_name = item.text()
        file_name2 = os.path.splitext(os.path.basename(item_name))[0]
        print("opt 3 ", file_name2)
        background_texture = QPixmap(item_name)
        background_brush = QBrush(background_texture)
        self.floorList.append(item_name)
        self.scene.setBackgroundBrush(background_brush)


    def setupUi(self, floorWindow, SelectRoomWindow):
        floorWindow.setObjectName("SelectRoomWindow")
        floorWindow.setFixedSize(1500, 850)
        floorWindow.setWindowTitle("SketchCraft Apartment Creator")
        floorWindow.keyPressEvent=self.keyPressEvent
        background_pixmap = QPixmap('Imagini/background2.jpg')
        background_image = background_pixmap.scaled(floorWindow.size(), Qt.KeepAspectRatioByExpanding)
        palette = floorWindow.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        floorWindow.setPalette(palette)

        self.scene = QGraphicsScene(floorWindow)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(self.length, self.width)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        if self.room == "bedroom" or self.room == "bedroom2":
            self.sidebar_layout = QVBoxLayout()
            self.sidebar_widget = QWidget()
            self.sidebar_widget.setLayout(self.sidebar_layout)
            self.sidebar_widget.setMaximumWidth(250)
            # Exemplu de adăugare a unor imagini asociate cu un buton
            self.createFurnitureItem("Bed",
                                     ["Imagini/Bedroom/be_pat.png",
                                      "Imagini/Bedroom/be_pat1.png",
                                      "Imagini/Bedroom/be_pat2.png",
                                      "Imagini/Bedroom/be_pat3.png"])
            self.createFurnitureItem("Nightstand",
                                     ["Imagini/Bedroom/be_noptiera.png",
                                      "Imagini/Bedroom/be_noptiera1.png",
                                      "Imagini/Bedroom/be_noptiera2.png",
                                      "Imagini/Bedroom/be_noptiera3.png"])
            self.createFurnitureItem("Dresser",
                                     ["Imagini/Bedroom/be1_comoda.png"])
            self.createFurnitureItem("Wardrobe",
                                     ["Imagini/Bedroom/be_dulap.png",
                                      "Imagini/Bedroom/be_dulap1.png"])
            self.createFurnitureItem("Accessories",
                                     ["Imagini/Accessories/ba_covor.png",
                                      "Imagini/Accessories/ba_covor1.png",
                                      "Imagini/Accessories/be_covor.png",
                                      "Imagini/Accessories/ba_plant.png",
                                      "Imagini/Accessories/k_plant1.png",
                                      "Imagini/Accessories/k_plant2.png",
                                      "Imagini/Accessories/k_plant3.png",
                                      "Imagini/Accessories/k_plant4.png",
                                      "Imagini/Accessories/l_plant.png",
                                      "Imagini/Accessories/l_plant1.png"])
            self.createFurnitureItem("Door",
                                     ["Imagini/Bedroom/be_door1.png",
                                      "Imagini/Bedroom/be_door2.png",
                                      "Imagini/Bedroom/be_door3.png"])
            self.createFurnitureItem("Window",
                                     ["Imagini/Accessories/geam1.png",
                                      "Imagini/Accessories/geam2.png"])

            self.floorTexture("Floor",["Imagini/Bedroom/floor3.jpg",
                                              "Imagini/Kitchen/repeatFloor2.png",
                                              "Imagini/Bathroom/floor2.jpg",
                                              "Imagini/Living Room/floor.jpg"])

            self.main_layout = QVBoxLayout()
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.view)
            self.layout.addWidget(self.sidebar_widget)

            self.back_button_layout = QHBoxLayout()
            self.button_back = QPushButton("Back")
            self.button_back.setFont(QFont("Agbalumo", 15))
            self.button_back.setStyleSheet(self.button_style)
            self.button_back.setCursor(Qt.PointingHandCursor)

            self.button_save = QPushButton("Save")
            self.button_save.setFont(QFont("Agbalumo", 15))
            self.button_save.setStyleSheet(self.button_style)
            self.button_save.setCursor(Qt.PointingHandCursor)

            self.button_back.clicked.connect(lambda: self.home(SelectRoomWindow, floorWindow))

            self.button_save.clicked.connect(self.save_scene)

            self.button_next = QPushButton("Next Room")
            self.button_next.setFont(QFont("Agbalumo", 15))
            self.button_next.setStyleSheet(self.button_style)
            self.button_next.setCursor(Qt.PointingHandCursor)
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow, floorWindow))

            self.button_previous = QPushButton("Previous Room")
            self.button_previous.setFont(QFont("Agbalumo", 15))
            self.button_previous.setStyleSheet(self.button_style)
            self.button_previous.setCursor(Qt.PointingHandCursor)
            self.button_previous.clicked.connect(lambda: self.previousRoom(SelectRoomWindow, floorWindow))

            self.back_button_layout.addWidget(self.button_back)
            self.back_button_layout.addWidget(self.button_save)
            self.back_button_layout.addWidget(self.button_previous)
            self.back_button_layout.addWidget(self.button_next)
            self.back_button_layout.setAlignment(Qt.AlignLeft)

            title_label = QLabel('Bedroom')
            title_font = QFont()
            title_font.setFamily("Agbalumo")
            title_font.setPointSize(20)
            title_label.setStyleSheet("color: #e06797")
            title_font.setBold(True)
            title_label.setFont(title_font)
            title_label.setAlignment(Qt.AlignCenter)

            self.main_layout.addWidget(title_label)
            self.main_layout.addLayout(self.layout)
            self.main_layout.addLayout(self.back_button_layout)

            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)

            floorWindow.setCentralWidget(self.main_widget)

        if self.room == "kitchen":
            self.sidebar_layout = QVBoxLayout()
            self.sidebar_widget = QWidget()
            self.sidebar_widget.setLayout(self.sidebar_layout)
            self.sidebar_widget.setMaximumWidth(250)

            self.createFurnitureItem("Gas cooker",
                                     ["Imagini/Kitchen/k_aragaz.png",
                                      "Imagini/Kitchen/k_aragaz1.png",
                                      "Imagini/Kitchen/k_aragaz2.png",
                                      "Imagini/Kitchen/k_aragaz3.png"])
            self.createFurnitureItem("Sink",
                                     ["Imagini/Kitchen/k_chiuveta.png",
                                      "Imagini/Kitchen/k_chiuveta1.png",
                                      "Imagini/Kitchen/k_chiuveta2.png",
                                      "Imagini/Kitchen/k_chiuveta3.png"])
            self.createFurnitureItem("Cabinet",
                                     ["Imagini/Kitchen/k_dulap_cu_sertare.png",
                                      "Imagini/Kitchen/k_dulap_mare.png",
                                      "Imagini/Kitchen/k_dulap_mic.png"])
            self.createFurnitureItem("Refrigerator",
                                     ["Imagini/Kitchen/k_frigider.png",
                                      "Imagini/Kitchen/k_frigider1.png",
                                      "Imagini/Kitchen/k_frigider2.png"])
            self.createFurnitureItem("Table",
                                     ["Imagini/Kitchen/k_masa.png",
                                      "Imagini/Kitchen/k_masa1.png",
                                      "Imagini/Kitchen/k_masa2.png",
                                      "Imagini/Kitchen/k_masa3.png",
                                      "Imagini/Kitchen/k_masa4.png"])
            self.createFurnitureItem("Accessories",
                                     ["Imagini/Accessories/ba_covor.png",
                                      "Imagini/Accessories/ba_covor1.png",
                                      "Imagini/Accessories/be_covor.png",
                                      "Imagini/Accessories/ba_plant.png",
                                      "Imagini/Accessories/k_plant1.png",
                                      "Imagini/Accessories/k_plant2.png",
                                      "Imagini/Accessories/k_plant3.png",
                                      "Imagini/Accessories/k_plant4.png",
                                      "Imagini/Accessories/l_plant.png",
                                      "Imagini/Accessories/l_plant1.png"])
            self.createFurnitureItem("Door",
                                     ["Imagini/Kitchen/be_door1.png",
                                      "Imagini/Kitchen/be_door2.png",
                                      "Imagini/Kitchen/be_door3.png"])
            self.createFurnitureItem("Window",
                                     ["Imagini/Accessories/geam1.png",
                                      "Imagini/Accessories/geam2.png"])

            self.floorTexture("Floor", ["Imagini/Bedroom/floor3.jpg",
                                        "Imagini/Kitchen/repeatFloor2.png",
                                        "Imagini/Bathroom/floor2.jpg",
                                        "Imagini/Living Room/floor.jpg"])

            self.main_layout = QVBoxLayout()
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.view)
            self.layout.addWidget(self.sidebar_widget)

            self.back_button_layout = QHBoxLayout()
            self.button_back = QPushButton("Back")
            self.button_back.setFont(QFont("Agbalumo", 15))
            self.button_back.setStyleSheet(self.button_style)
            self.button_back.setCursor(Qt.PointingHandCursor)

            self.button_save = QPushButton("Save")
            self.button_save.setFont(QFont("Agbalumo", 15))
            self.button_save.setStyleSheet(self.button_style)
            self.button_save.setCursor(Qt.PointingHandCursor)

            self.button_back.clicked.connect(lambda: self.home(SelectRoomWindow, floorWindow))

            self.button_save.clicked.connect(self.save_scene)

            self.button_next = QPushButton("Next Room")
            self.button_next.setFont(QFont("Agbalumo", 15))
            self.button_next.setStyleSheet(self.button_style)
            self.button_next.setCursor(Qt.PointingHandCursor)
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow, floorWindow))

            self.button_previous = QPushButton("Previous Room")
            self.button_previous.setFont(QFont("Agbalumo", 15))
            self.button_previous.setStyleSheet(self.button_style)
            self.button_previous.setCursor(Qt.PointingHandCursor)
            self.button_previous.clicked.connect(lambda: self.previousRoom(SelectRoomWindow, floorWindow))

            self.back_button_layout.addWidget(self.button_back)
            self.back_button_layout.addWidget(self.button_save)
            self.back_button_layout.addWidget(self.button_previous)
            self.back_button_layout.addWidget(self.button_next)
            self.back_button_layout.setAlignment(Qt.AlignLeft)

            title_label = QLabel('Kitchen')
            title_font = QFont()
            title_font.setFamily("Agbalumo")
            title_font.setPointSize(20)
            title_label.setStyleSheet("color: #e06797")
            title_font.setBold(True)
            title_label.setFont(title_font)
            title_label.setAlignment(Qt.AlignCenter)

            self.main_layout.addWidget(title_label)
            self.main_layout.addLayout(self.layout)
            self.main_layout.addLayout(self.back_button_layout)

            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)

            floorWindow.setCentralWidget(self.main_widget)

        if self.room == "bathroom":
            self.sidebar_layout = QVBoxLayout()
            self.sidebar_widget = QWidget()
            self.sidebar_widget.setLayout(self.sidebar_layout)
            self.sidebar_widget.setMaximumWidth(250)

            self.createFurnitureItem("Bidet",
                                     ["Imagini/Bathroom/ba_bideu.png",
                                      "Imagini/Bathroom/ba_bideu1.png"])
            self.createFurnitureItem("Sink",
                                     ["Imagini/Bathroom/ba_chiuveta.png",
                                      "Imagini/Bathroom/ba_chiuveta1.png",
                                      "Imagini/Bathroom/ba_chiuveta2.png"])
            self.createFurnitureItem("Bathtub",
                                     ["Imagini/Bathroom/ba_cada.png",
                                      "Imagini/Bathroom/ba_cada1.png",
                                      "Imagini/Bathroom/ba_cada2.png",
                                      "Imagini/Bathroom/ba_cada3.png"])
            self.createFurnitureItem("Toilet",
                                     ["Imagini/Bathroom/ba_wc.png",
                                      "Imagini/Bathroom/ba_wc1.png"])
            self.createFurnitureItem("Accessories",
                                     ["Imagini/Accessories/ba_covor.png",
                                      "Imagini/Accessories/ba_covor1.png",
                                      "Imagini/Accessories/be_covor.png",
                                      "Imagini/Accessories/ba_plant.png",
                                      "Imagini/Accessories/k_plant1.png",
                                      "Imagini/Accessories/k_plant2.png",
                                      "Imagini/Accessories/k_plant3.png",
                                      "Imagini/Accessories/k_plant4.png",
                                      "Imagini/Accessories/l_plant.png",
                                      "Imagini/Accessories/l_plant1.png"])
            self.createFurnitureItem("Door",
                                     ["Imagini/Bathroom/be_door1.png",
                                      "Imagini/Bathroom/be_door2.png",
                                      "Imagini/Bathroom/be_door3.png"])
            self.createFurnitureItem("Window",
                                     ["Imagini/Accessories/geam1.png",
                                      "Imagini/Accessories/geam2.png"])

            self.floorTexture("Floor", ["Imagini/Bedroom/floor3.jpg",
                                        "Imagini/Kitchen/repeatFloor2.png",
                                        "Imagini/Bathroom/floor2.jpg",
                                        "Imagini/Living Room/floor.jpg"])

            self.main_layout = QVBoxLayout()
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.view)
            self.layout.addWidget(self.sidebar_widget)

            self.back_button_layout = QHBoxLayout()
            self.button_back = QPushButton("Back")
            self.button_back.setFont(QFont("Agbalumo", 15))
            self.button_back.setStyleSheet(self.button_style)
            self.button_back.setCursor(Qt.PointingHandCursor)

            self.button_save = QPushButton("Save")
            self.button_save.setFont(QFont("Agbalumo", 15))
            self.button_save.setStyleSheet(self.button_style)
            self.button_save.setCursor(Qt.PointingHandCursor)

            self.button_back.clicked.connect(lambda: self.home(SelectRoomWindow, floorWindow))

            self.button_save.clicked.connect(self.save_scene)

            self.button_next = QPushButton("Next Room")
            self.button_next.setFont(QFont("Agbalumo", 15))
            self.button_next.setStyleSheet(self.button_style)
            self.button_next.setCursor(Qt.PointingHandCursor)
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow, floorWindow))

            self.button_previous = QPushButton("Previous Room")
            self.button_previous.setFont(QFont("Agbalumo", 15))
            self.button_previous.setStyleSheet(self.button_style)
            self.button_previous.setCursor(Qt.PointingHandCursor)
            self.button_previous.clicked.connect(lambda: self.previousRoom(SelectRoomWindow, floorWindow))

            self.back_button_layout.addWidget(self.button_back)
            self.back_button_layout.addWidget(self.button_save)
            self.back_button_layout.addWidget(self.button_previous)
            self.back_button_layout.addWidget(self.button_next)
            self.back_button_layout.setAlignment(Qt.AlignLeft)

            title_label = QLabel('Bathroom')
            title_font = QFont()
            title_font.setFamily("Agbalumo")
            title_font.setPointSize(20)
            title_label.setStyleSheet("color: #e06797")
            title_font.setBold(True)
            title_label.setFont(title_font)
            title_label.setAlignment(Qt.AlignCenter)

            self.main_layout.addWidget(title_label)
            self.main_layout.addLayout(self.layout)
            self.main_layout.addLayout(self.back_button_layout)

            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)

            floorWindow.setCentralWidget(self.main_widget)

        if self.room == "LivingRoom":
            self.sidebar_layout = QVBoxLayout()
            self.sidebar_widget = QWidget()
            self.sidebar_widget.setLayout(self.sidebar_layout)
            self.sidebar_widget.setMaximumWidth(250)

            self.createFurnitureItem("Desk",
                                     ["Imagini/Living Room/birou.png",
                                      "Imagini/Living Room/l_birou.png"])
            self.createFurnitureItem("Sofa",
                                     ["Imagini/Living Room/l_canapea.png",
                                      "Imagini/Living Room/l_canapea1.png",
                                      "Imagini/Living Room/l_canapea2.png",
                                      "Imagini/Living Room/l_canapea3.png"])
            self.createFurnitureItem("Armchair",
                                     ["Imagini/Living Room/l_fotoliu.png",
                                      "Imagini/Living Room/l_fotoliu1.png",
                                      "Imagini/Living Room/l_fotoliu2.png",
                                      "Imagini/Living Room/l_fotoliu3.png"])
            self.createFurnitureItem("Coffee table",
                                     ["Imagini/Living Room/l_masuta.png",
                                      "Imagini/Living Room/l_masuta1.png",
                                      "Imagini/Living Room/l_masuta2.png"])
            self.createFurnitureItem("TV table",
                                     ["Imagini/Living Room/l_masuta_tv.png",
                                      "Imagini/Living Room/l_masuta_tv1.png"])
            self.createFurnitureItem("Chair",
                                     ["Imagini/Living Room/l_scaun.png",
                                      "Imagini/Living Room/l_scaun1.png",
                                      "Imagini/Living Room/l_scaun2.png"])
            self.createFurnitureItem("Accessories",
                                     ["Imagini/Accessories/ba_covor.png",
                                      "Imagini/Accessories/ba_covor1.png",
                                      "Imagini/Accessories/be_covor.png",
                                      "Imagini/Accessories/ba_plant.png",
                                      "Imagini/Accessories/k_plant1.png",
                                      "Imagini/Accessories/k_plant2.png",
                                      "Imagini/Accessories/k_plant3.png",
                                      "Imagini/Accessories/k_plant4.png",
                                      "Imagini/Accessories/l_plant.png",
                                      "Imagini/Accessories/l_plant1.png"])
            self.createFurnitureItem("Door",
                                     ["Imagini/Living Room/be_door1.png",
                                      "Imagini/Living Room/be_door2.png",
                                      "Imagini/Living Room/be_door3.png"])
            self.createFurnitureItem("Window",
                                     ["Imagini/Accessories/geam1.png",
                                      "Imagini/Accessories/geam2.png"])

            self.floorTexture("Floor", ["Imagini/Bedroom/floor3.jpg",
                                        "Imagini/Kitchen/repeatFloor2.png",
                                        "Imagini/Bathroom/floor2.jpg",
                                        "Imagini/Living Room/floor.jpg"])

            self.main_layout = QVBoxLayout()
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.view)
            self.layout.addWidget(self.sidebar_widget)

            self.back_button_layout = QHBoxLayout()
            self.button_back = QPushButton("Back")
            self.button_back.setFont(QFont("Agbalumo", 15))
            self.button_back.setStyleSheet(self.button_style)
            self.button_back.setCursor(Qt.PointingHandCursor)

            self.button_save = QPushButton("Save")
            self.button_save.setFont(QFont("Agbalumo", 15))
            self.button_save.setStyleSheet(self.button_style)
            self.button_save.setCursor(Qt.PointingHandCursor)

            self.button_back.clicked.connect(lambda: self.home(SelectRoomWindow, floorWindow))

            self.button_save.clicked.connect(self.save_scene)

            self.button_next = QPushButton("Next Room")
            self.button_next.setFont(QFont("Agbalumo", 15))
            self.button_next.setStyleSheet(self.button_style)
            self.button_next.setCursor(Qt.PointingHandCursor)
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow, floorWindow))

            self.button_previous = QPushButton("Previous Room")
            self.button_previous.setFont(QFont("Agbalumo", 15))
            self.button_previous.setStyleSheet(self.button_style)
            self.button_previous.setCursor(Qt.PointingHandCursor)
            self.button_previous.clicked.connect(lambda: self.previousRoom(SelectRoomWindow, floorWindow))

            self.back_button_layout.addWidget(self.button_back)
            self.back_button_layout.addWidget(self.button_save)
            self.back_button_layout.addWidget(self.button_previous)
            self.back_button_layout.addWidget(self.button_next)
            self.back_button_layout.setAlignment(Qt.AlignLeft)

            title_label = QLabel('Living Room')
            title_font = QFont()
            title_font.setFamily("Agbalumo")
            title_font.setPointSize(20)
            title_label.setStyleSheet("color: #e06797")
            title_font.setBold(True)
            title_label.setFont(title_font)
            title_label.setAlignment(Qt.AlignCenter)

            self.main_layout.addWidget(title_label)
            self.main_layout.addLayout(self.layout)
            self.main_layout.addLayout(self.back_button_layout)

            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)

            floorWindow.setCentralWidget(self.main_widget)

        if self.room == "corridor1" or self.room == "corridor2" or self.room == "corridor3":
            #if self.room == "corridor1":
                #self.view.setFixedSize(600, 500)
                #self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

            #elif self.room == "corridor2" or self.room == "corridor3":
                #self.view.setFixedSize(600, 700)
                #self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

            self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

            self.sidebar_layout = QVBoxLayout()
            self.sidebar_widget = QWidget()
            self.sidebar_widget.setLayout(self.sidebar_layout)
            self.sidebar_widget.setMaximumWidth(250)

            self.createFurnitureItem("Accessories",
                                     ["Imagini/Accessories/ba_covor.png",
                                      "Imagini/Accessories/ba_covor1.png",
                                      "Imagini/Accessories/be_covor.png",
                                      "Imagini/Accessories/ba_plant.png",
                                      "Imagini/Accessories/k_plant1.png",
                                      "Imagini/Accessories/k_plant2.png",
                                      "Imagini/Accessories/k_plant3.png",
                                      "Imagini/Accessories/k_plant4.png",
                                      "Imagini/Accessories/l_plant.png",
                                      "Imagini/Accessories/l_plant1.png"])
            self.createFurnitureItem("Door",
                                     ["Imagini/Accessories/be_door1.png",
                                      "Imagini/Accessories/be_door2.png",
                                      "Imagini/Accessories/be_door3.png"])
            self.createFurnitureItem("Window",
                                     ["Imagini/Accessories/geam1.png",
                                      "Imagini/Accessories/geam2.png"])

            self.floorTexture("Floor", ["Imagini/Bedroom/floor3.jpg",
                                        "Imagini/Kitchen/repeatFloor2.png",
                                        "Imagini/Bathroom/floor2.jpg",
                                        "Imagini/Living Room/floor.jpg"])

            self.main_layout = QVBoxLayout()
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.view)
            self.layout.addWidget(self.sidebar_widget)

            self.back_button_layout = QHBoxLayout()
            self.button_back = QPushButton("Back")
            self.button_back.setFont(QFont("Agbalumo", 15))
            self.button_back.setStyleSheet(self.button_style)
            self.button_back.setCursor(Qt.PointingHandCursor)
            self.button_back.clicked.connect(lambda: self.home(SelectRoomWindow, floorWindow))

            self.button_save = QPushButton("Save")
            self.button_save.setFont(QFont("Agbalumo", 15))
            self.button_save.setStyleSheet(self.button_style)
            self.button_save.setCursor(Qt.PointingHandCursor)

            self.button_save.clicked.connect(self.save_scene)

            self.button_next = QPushButton("Next Room")
            self.button_next.setFont(QFont("Agbalumo", 15))
            self.button_next.setStyleSheet(self.button_style)
            self.button_next.setCursor(Qt.PointingHandCursor)
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow, floorWindow))

            self.button_previous = QPushButton("Previous Room")
            self.button_previous.setFont(QFont("Agbalumo", 15))
            self.button_previous.setStyleSheet(self.button_style)
            self.button_previous.setCursor(Qt.PointingHandCursor)
            self.button_previous.clicked.connect(lambda: self.previousRoom(SelectRoomWindow, floorWindow))

            self.back_button_layout.addWidget(self.button_back)
            self.back_button_layout.addWidget(self.button_save)
            self.back_button_layout.addWidget(self.button_previous)
            self.back_button_layout.addWidget(self.button_next)
            self.back_button_layout.setAlignment(Qt.AlignLeft)

            title_label = QLabel('Corridor')
            title_font = QFont()
            title_font.setFamily("Agbalumo")
            title_font.setPointSize(20)
            title_label.setStyleSheet("color: #e06797")
            title_font.setBold(True)
            title_label.setFont(title_font)
            title_label.setAlignment(Qt.AlignCenter)

            self.main_layout.addWidget(title_label)
            self.main_layout.addLayout(self.layout)
            self.main_layout.addLayout(self.back_button_layout)

            self.main_widget = QWidget()
            self.main_widget.setLayout(self.main_layout)

            floorWindow.setCentralWidget(self.main_widget)
ROOMS: dict[str, FloorplannerPersonalizedApp] = {}