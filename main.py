import sys
import ntpath
import threading
# from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QFileDialog
)
# from PyQt5.uic import loadUi

from UI.main_window import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.shift = 5
        self.file = ""
        self.newFile = ""
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_About.triggered.connect(self.about)
        self.action_Open_File.triggered.connect(self.openFileNameDialog)
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.btn_decrypt.clicked.connect(self.decrypt)

    def about(self):
        QMessageBox.about(
            self,
            "Ceaser Cipher",
            "<p>A sample app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>"
            "<p>Created by:</p>"
            "<p>- Soliman Ali Soliman</p>"
            "<p>- Abdelrahman Mahmoud Mohamed</p>"
        )

    def openFileNameDialog(self):
        self.statusbar.showMessage('Open file dialog opened')
        filePath, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt);;" "All files (*.*)")
        if filePath:
            head, tail = ntpath.split(filePath)
            self.statusbar.showMessage(f"{tail} opened")
            self.file = filePath
            self.btn_encrypt.setEnabled(True)
            self.btn_decrypt.setEnabled(True)

    def file_save(self, data):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)",)
        if fileName:
            self.statusbar.showMessage('Saving new file')
            self.write_data_thread(data, fileName=fileName)

    def write_data_thread(self, data, fileName):
        thread = threading.Thread(target=self.write_data, args=(data, fileName))
        thread.start()

    def write_data(self, data, fileName):
        file = open(fileName,'w')
        for item in data:
            file.write(item)
            file.write("\n")
        file.close()
        self.btn_encrypt.setEnabled(False)
        self.btn_decrypt.setEnabled(False)

    def encrypt(self):
        self.statusbar.showMessage('Start encryption')
        encryption = []
        x=""
        file = self.file
        with open(file) as f:
            self.statusbar.showMessage('Start read file')
            lines = [line.rstrip() for line in f]
            print(lines)
        for text in lines:
            #text.upper()
            x=""
            for c in text:
                # check if character is an uppercase letter
                if c.isupper():
                    # find the position in 0-25
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("A")
                    # perform the shift
                    new_index = (c_index + self.shift) % 26
                    # convert to new character
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)
                    # append to encrypted string
                    x = x + new_character
                else:
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("a")
                    # perform the shift
                    new_index = (c_index + self.shift) % 26
                    # convert to new character
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)
                    # append to encrypted string
                    x = x + new_character
            encryption.append(x)
        print(encryption)
        self.file_save(encryption)
        self.statusbar.showMessage('Encryption completed!')
        # return encryption

    def decrypt(self):
        self.statusbar.showMessage('Start decryption')
        decrypttion = []
        file = self.file
        with open(file) as f:
            self.statusbar.showMessage('Start read file')
            lines = [line.rstrip() for line in f]
        for text in lines:
            #text.upper()
            x=""
            for c in text:
                # check if character is an uppercase letter
                if c.isupper():
                    # find the position in 0-25
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("A")
                    # perform the shift
                    new_index = (c_index - self.shift) % 26
                    # convert to new character
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)
                    # append to encrypted string
                    x = x + new_character
                else:
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("a")
                    # perform the shift
                    new_index = (c_index - self.shift) % 26
                    # convert to new character
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)
                    # append to encrypted string
                    Decrypted  = Decrypted +list(new_character)
                    x = x + new_character
            decrypttion.append(x)
        print(decrypttion)
        self.file_save(decrypttion)
        self.statusbar.showMessage('Decryption completed!')
        # return decrypttion

# ?=======================================================================================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())