from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        container = QWidget # Main window
        self.setWindowTitle("Web browser")
        self.setGeometry(100, 60, 1000, 800)

        urlLabel = QLabel(self) # Label prior to search bar
        urlLabel.setText('URL: ')

        self.line = QLineEdit(self) # search bar
        # line.returnPressed.connect(self.prompt_site(url=line.text))
        self.line.move(50, 0)
        self.line.resize(800, 32)

        self.show()
        self.trigger_line_edit()

    def prompt_site(self, url, *kwargs):
        # QtWebEngineWidgets.QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

    def default_url(self):
    # User Did something
        self.line.setText("www.google.com")

    def trigger_line_edit(self):
        # Store Value
        val = self.line.text()
        print(val)

        self.default_url()
        # Print Value to show the value was copied
        print(val)

        # Store new value
        val = self.line.text()
        print(val)
        self.prompt_site(url=val)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()