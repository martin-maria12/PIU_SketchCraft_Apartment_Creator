
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class UI_HelpWindow(object):

    def home(self, main_w, create_w):
        main_w.show()
        create_w.close()

    def setupUi(self, MainWindow, BackWindow):
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

        self.title_label = QLabel("Ghid de utilizare", central_widget)
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(30)
        self.title_label.setStyleSheet("color: #e06797")
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.title_label, 0, 0, 1, 3)  # 0- linia, 0-coloana, 1-nr de randuri, 3-nr coloane

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

        text_edit = QTextEdit("""
        <p>1. Selectati configuratia apartamentului: incepeti prin a alege tipul de apartament - standard (cu dimensiuni prestabilite) sau personalizat. </p>

        <p>2. Alegeti numarul de camere: decideti daca doriti un apartament cu o camera, doua sau trei camere. </p>

        <p>3. Personalizati inceperile: selectati incaperea pe care doriti sa o amenajati. In cazul apartamentului personalizat, introduceti dimensiunile camerei si plasati usi si ferestre dupa preferinte. </p>

        <p>4. Adaugati mobilier si accesorii: folositi meniul din dreapta pentru a alege piese de mobilier si accesorii. Trageti si plasati obiectele in scena, rotiti-le pentru a se potrivi perfect si stergeti-le daca este necesar. Pentru a roti sau sterge obiectele, veti apasa butonul click-dreapta al mouse-ului. Obiectele nu pot fi suprapuse (exceptie plantele ce pot fi puse pe mobilier si covoarele care pot fi puse sub mobilier) si sunt limitate la spatiul incaperii. </p>

        <p>5. Salvati configuratia: dupa ce ati terminat amenajarea unei camere, folositi butonul "Save" pentru a salva scena. Alegeti locul si numele fisierului in fereastra de dialog. </p>

        <p>6. Navigati intre camere: utilizati butoanele "NextRoom" si "PreviousRoom" pentru a naviga intre camerele amenajate sau pentru a accesa o camera goala. </p>

        <center><p style='color: red;'>Atentie! Daca apasati butonul de back se vor pierde toate configuratiile camerelor deja amenajate! </p>

        """, central_widget)

        text_edit.setFont(QFont("Agbalumo", 13))
        text_edit.setStyleSheet("""
            color: #e06797; 
            background-color: transparent; 
            margin: 5px 10px 2px 10px;
            border: none;
        """)
        text_edit.setAlignment(Qt.AlignLeft)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit, 1, 0, 1, 3)

        back_button_layout = QHBoxLayout()

        button_back = QPushButton("Back")
        button_back.setFont(QFont("Agbalumo", 10))
        button_back.setStyleSheet(button_back_style)
        button_back.setCursor(Qt.PointingHandCursor)

        back_button_layout.addWidget(button_back)
        back_button_layout.setAlignment(Qt.AlignLeft)

        button_back.clicked.connect(lambda: self.home(BackWindow, MainWindow))
        layout.setContentsMargins(100, 30, 100, 10)
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(5)
        layout.addLayout(back_button_layout, 2, 0, 1, 1)

        MainWindow.setLayout(layout)