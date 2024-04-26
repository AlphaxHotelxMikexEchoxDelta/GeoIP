from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import requests
import sys

# Fenetre de la map
class Map(QWidget):
    def __init__(self, latitude, longitude):
        super(Map, self).__init__()
        self.initUI(latitude, longitude)

    def initUI(self, latitude, longitude):
        self.browser = QWebEngineView()
        # Lien pour la map
        self.browser.setUrl(QUrl(f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}#map=16/{latitude}/{longitude}"))
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle("Client")
        
        # Label et boîte de saisie @IP
        self.ip_label = QLabel("Enter IP address:", self)
        self.ip_label.move(10, 30)
        self.ip_text = QLineEdit(self)
        self.ip_text.move(10, 60)
        self.ip_text.setText("8.8.8.8")
        self.ip_label.adjustSize()
        
        # Label et boîte de saisie API KEY
        self.api_key_label = QLabel("Enter API key:", self)
        self.api_key_label.move(10, 90)
        self.api_key_text = QLineEdit(self)
        self.api_key_text.move(10, 120)
        self.api_key_text.setText("KEYKEY")
        self.api_key_label.adjustSize()
        
        # Bouton envoi requete
        self.button = QPushButton("Send", self)
        self.button.move(10, 150)
        self.button.clicked.connect(self.on_click)
        self.button.adjustSize()

    def getMap(self, res):
        latitude = res.get("latitude")
        longitude = res.get("longitude")
        if latitude is not None and longitude is not None:
            self.map_window = Map(latitude, longitude)
            self.map_window.show()

    def on_click(self):
        ip_address = self.ip_text.text()
        api_key = self.api_key_text.text()

        if not ip_address:
            QMessageBox.about(self, "Error", "Please enter the IP address")
        else:
            res = self.__query(ip_address, api_key)
            if res:
                self.getMap(res)

    def __query(self, ip_address, api_key):
        url = f"http://127.0.0.1:8000/ip/{ip_address}?key={api_key}"
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        elif r.status_code == requests.codes.OK:
            return r.json()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
