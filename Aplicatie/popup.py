
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout

class UI_MessageWindow(QDialog):

    def get_measurements(self):
        length_text = self.length_input.text().strip()
        print(length_text)

        width_text = self.width_input.text().strip()
        print(width_text)

        if not length_text or not width_text:
            print("Nu au fost introduse lungimea si latimea camerei")
            length=1000
            width=700
            return length,width

        try:
            length = int(length_text)
            if length > 1200:
                print("Prea mare lungimea, maximul trebuie să fie 1200")
                length = 1200

            width = int(width_text)
            if width > 700:
                print("Prea mare lățimea, maximul trebuie să fie 700")
                width = 700

            if length < 700:
                print("Prea mica lungimea, minimul trebuie să fie 700")
                length = 700

            if width < 350:
                print("Prea mica lățimea, minimul trebuie să fie 350")
                width = 350

            return length, width

        except ValueError:
            print("Eroare în dialog la numere")
            return None

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialog")
        self.setGeometry(300, 300, 500, 450)
        background_pixmap = QPixmap("Imagini/background2.jpg")
        background_image = background_pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(20)

        label = QLabel("Enter the measurements/preferences")
        title_font = QFont()
        title_font.setFamily("Agbalumo")
        title_font.setPointSize(20)
        label.setStyleSheet("color: #e06797")
        title_font.setBold(False)
        label.setFont(title_font)
        label.setAlignment(Qt.AlignCenter)

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

        layout1 = QHBoxLayout()

        label2 = QLabel("700 < Length <= 1200")
        label2.setStyleSheet("color: #e06797")
        label2.setFont(title_font)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel("350 < Width <= 700")
        label3.setStyleSheet("color: #e06797")
        label3.setFont(title_font)
        label3.setAlignment(Qt.AlignCenter)

        length_label = QLabel("Length:")
        length_label.setStyleSheet("color: #e06797")
        length_label.setFont(title_font)
        self.length_input = QLineEdit()
        self.length_input.setFixedHeight(40)
        self.length_input.setFixedWidth(400)
        self.length_input.setAlignment(Qt.AlignCenter)

        layout1.addWidget(length_label)
        layout1.addWidget(self.length_input)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)
        layout1.setAlignment(Qt.AlignLeft)

        layout2 = QHBoxLayout()
        width_label = QLabel("Width:")
        width_label.setStyleSheet("color: #e06797")
        width_label.setFont(title_font)
        self.width_input = QLineEdit()
        self.width_input.setFixedHeight(40)
        self.width_input.setFixedWidth(400)
        self.width_input.setAlignment(Qt.AlignCenter)

        layout2.addWidget(width_label)
        layout2.addWidget(self.width_input)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.setSpacing(0)
        layout2.setAlignment(Qt.AlignLeft)

        ok_button = QPushButton("OK")
        ok_button.setFont(QFont("Agbalumo", 14))
        ok_button.setStyleSheet(button_style)
        ok_button.setCursor(Qt.PointingHandCursor)

        cancel_button = QPushButton("Cancel")
        cancel_button.setFont(QFont("Agbalumo", 14))
        cancel_button.setStyleSheet(button_style)
        cancel_button.setCursor(Qt.PointingHandCursor)

        ok_button.clicked.connect(self.accept)

        cancel_button.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        self.setLayout(layout)