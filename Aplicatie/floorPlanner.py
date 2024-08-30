
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, \
    QGraphicsScene, QGraphicsView, QHBoxLayout, QLabel, QGraphicsRectItem, QGraphicsItem, QMenu, QFileDialog, \
    QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QBrush, QColor, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets
from furnitureItem import FurnitureItem


class FloorplannerApp(QMainWindow):
    def __init__(self, room: str, nr_rooms):
        super().__init__()
        self.room = room
        self.nr_rooms = nr_rooms

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
        self.ui_select = None
        self.selected_item = None

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

    def addItemToScene(self, pixmap, item_type):
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

        if "covor" in item_name:
            item_type = "Carpet"
        elif "plant" in item_name:
            item_type = "Plant"

        else:
            item_type = "Furniture"

        print(item_type)
        self.addItemToScene(pixmap, item_type)

    def previousRoom(self,windowS, windowF):
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
                print(f"apartament 2 room {next_room}")
            elif current_room == "kitchen":
                next_room = "corridor2"
                print(f"apartament 2 room {next_room}")
            elif current_room == "bathroom":
                next_room = "kitchen"
                print(f"apartament 2 room {next_room}")
            elif current_room == "bedroom":
                next_room = "bathroom"
                print(f"apartament 2 room {next_room}")
            elif current_room == "LivingRoom":
                next_room = "bedroom"
                print(f"apartament 2 room {next_room}")

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
            print(f"Next Room: {next_room} ")
            self.window = QtWidgets.QMainWindow()
            if next_room in ROOMS.keys():
                self.ui = ROOMS[next_room]
            else:
                self.ui = FloorplannerApp(room=f"{next_room}", nr_rooms=self.nr_rooms)
            self.ui.setupUi(self.window, windowS)
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
                print(f"apartament 2 room {next_room}")
            elif current_room == "kitchen":
                next_room = "bathroom"
                print(f"apartament 2 room {next_room}")
            elif current_room == "bathroom":
                next_room = "bedroom"
                print(f"apartament 2 room {next_room}")
            elif current_room == "bedroom":
                next_room = "LivingRoom"
                print(f"apartament 2 room {next_room}")
            elif current_room == "LivingRoom":
                next_room = "corridor2"
                print(f"apartament 2 room {next_room}")

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
            print(f"Next Room: {next_room} ")
            self.window = QtWidgets.QMainWindow()
            if next_room in ROOMS.keys():
                self.ui = ROOMS[next_room]
                print(next_room)
            else:
                self.ui = FloorplannerApp(room=f"{next_room}", nr_rooms=self.nr_rooms)
            self.ui.setupUi(self.window, windowS)
            self.ui.loadFurniture()
            self.ui.goBack = windowS
            self.ui.ui_select = self
            self.window.show()
            windowF.hide()
        else:
            print("There is no next room.")

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
            list_widget.setIconSize(QSize(200,200))

        list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_widget.itemClicked.connect(self.item_clicked)

        self.list_layout.addWidget(list_widget)
        self.sidebar_layout.addLayout(self.list_layout)

    def createFurnitureItem(self, name, image_paths):
        button_meniu = QPushButton(name)
        button_meniu.setFont(QFont("Agbalumo", 15))
        button_meniu.setStyleSheet(self.button_style)
        button_meniu.setCursor(Qt.PointingHandCursor)
        button_meniu.clicked.connect(lambda: self.showImageList(image_paths))
        self.sidebar_layout.addWidget(button_meniu)

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
        self.view.setFixedSize(1000, 700)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        door_width = 20
        door_height = 250
        door = QGraphicsRectItem(0, 0, door_width, door_height)
        brown_color = QColor(139, 69, 19)
        door.setBrush(QBrush(brown_color))
        door.setZValue(0.1)




        window_width = 20
        window_height = 200
        window = QGraphicsRectItem(0, 0, window_width, window_height)
        window.setZValue(0.1)
        blue_color = QColor(173, 216, 230)
        window.setBrush(QBrush(blue_color))

        if self.room == "bedroom" or self.room == "bedroom2":
            floor_texture = QGraphicsPixmapItem(QPixmap("Imagini/Bedroom/floor3.jpg"))
            floor_texture.setPos(0, 0)
            scale_factor_w = self.scene.width() / floor_texture.pixmap().width()
            scale_factor_height = self.scene.height() / floor_texture.pixmap().height()
            floor_texture.setScale(scale_factor_w)

            self.view.scene().addItem(floor_texture)

            if self.room == "bedroom":
                door.setPos(0, self.view.height() - door_height - 60)
            elif self.room == "bedroom2":
                door.setPos(0, 60)

            self.scene.addItem(door)

            window.setPos(self.view.width() - window_width, self.view.height() - window_height - 120)
            self.scene.addItem(window)

            second_window = QGraphicsRectItem(0, 0, window_width, window_height)
            second_window.setBrush(QBrush(blue_color))
            second_window.setZValue(0.1)

            second_window.setPos(self.view.width() - window_width, self.view.height() - window_height - 400)
            self.scene.addItem(second_window)

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
            self.button_previous.clicked.connect(lambda:self.previousRoom(SelectRoomWindow, floorWindow))

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
            background_texture = QPixmap("Imagini/Kitchen/repeatFloor2.png")
            background_brush = QBrush(background_texture)
            self.scene.setBackgroundBrush(background_brush)

            door.setPos(self.view.width() - door_width, self.view.height() - door_height - 60)
            self.scene.addItem(door)

            window.setPos(0, self.view.height() - window_height - 300)
            self.scene.addItem(window)

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
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow,floorWindow))

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
            background_texture = QPixmap("Imagini/Bathroom/floor2.jpg")
            background_brush = QBrush(background_texture)
            self.scene.setBackgroundBrush(background_brush)

            door.setRotation(90)
            door.setPos((self.view.width() - door_width) / 2 + 140, self.view.height() - 22)
            self.scene.addItem(door)

            window.setRotation(90)
            window.setPos((self.view.width() - window_width) / 2 + 100, 0)
            self.scene.addItem(window)

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
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow,floorWindow))
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
            floor_texture = QGraphicsPixmapItem(QPixmap("Imagini/Living Room/floor.jpg"))
            floor_texture.setPos(0, 0)
            scale_factor_w = self.scene.width() / floor_texture.pixmap().width()
            scale_factor_height = self.scene.height() / floor_texture.pixmap().height()
            floor_texture.setScale(scale_factor_height)
            self.view.scene().addItem(floor_texture)

            door.setPos(self.view.width() - door_width, self.view.height() - door_height - 350)
            self.scene.addItem(door)

            window.setPos(0, self.view.height() - window_height - 150)
            self.scene.addItem(window)

            second_window = QGraphicsRectItem(0, 0, window_width, window_height)
            second_window.setBrush(QBrush(blue_color))
            second_window.setRotation(90)
            second_window.setZValue(0.1)
            second_window.setPos(self.view.width() - window_height - 400, self.view.height() - 22)
            self.scene.addItem(second_window)

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
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow,floorWindow))

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
            floor_texture = QGraphicsPixmapItem(QPixmap("Imagini/Living Room/floor.jpg"))
            floor_texture.setPos(0, 0)
            scale_factor_w = self.scene.width() / floor_texture.pixmap().width()
            scale_factor_height = self.scene.height() / floor_texture.pixmap().height()
            floor_texture.setScale(scale_factor_height)
            self.view.scene().addItem(floor_texture)

            if self.room == "corridor1":
                self.view.setFixedSize(600, 500)
                self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

                door.setRotation(90)
                door.setPos((self.view.width() - door_width) / 2 + 140, 0)
                self.scene.addItem(door)

                second_door = QGraphicsRectItem(0, 0, door_width, door_height)
                second_door.setBrush(QBrush(brown_color))
                second_door.setZValue(0.1)
                second_door.setPos(self.view.width() - door_width, self.view.height() - door_height - 100)
                self.scene.addItem(second_door)

                third_door = QGraphicsRectItem(0, 0, door_width, door_height)
                third_door.setBrush(QBrush(brown_color))
                third_door.setZValue(0.1)
                third_door.setPos(0, self.view.height() - door_height - 200)
                self.scene.addItem(third_door)

            elif self.room == "corridor2" or self.room == "corridor3":
                self.view.setFixedSize(600, 700)
                self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

                door.setRotation(90)
                door.setPos((self.view.width() - door_width) / 2 + 140, 0)
                self.scene.addItem(door)

                second_door = QGraphicsRectItem(0, 0, door_width, door_height)
                second_door.setZValue(0.1)
                second_door.setBrush(QBrush(brown_color))
                second_door.setPos(self.view.width() - door_width, self.view.height() - door_height - 400)
                self.scene.addItem(second_door)

                third_door = QGraphicsRectItem(0, 0, door_width, door_height)
                third_door.setBrush(QBrush(brown_color))
                third_door.setZValue(0.1)
                third_door.setPos(0, self.view.height() - door_height - 400)
                self.scene.addItem(third_door)

                fourth_door = QGraphicsRectItem(0, 0, door_width, door_height)
                fourth_door.setBrush(QBrush(brown_color))
                fourth_door.setZValue(0.1)
                fourth_door.setPos(0, self.view.height() - door_height - 50)
                self.scene.addItem(fourth_door)

                if self.room == "corridor3":
                    fifth_door = QGraphicsRectItem(0, 0, door_width, door_height)
                    fifth_door.setBrush(QBrush(brown_color))
                    fifth_door.setZValue(0.1)
                    fifth_door.setPos(self.view.width() - door_width, self.view.height() - door_height - 50)
                    self.scene.addItem(fifth_door)

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
            self.button_next.clicked.connect(lambda: self.nextRoom(SelectRoomWindow,floorWindow))

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



ROOMS: dict[str, FloorplannerApp] = {}