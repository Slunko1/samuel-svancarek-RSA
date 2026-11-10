import sys

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

from pathlib import Path
import RSA

SCRIPT_DIR = Path(__file__).resolve().parent
UI_PATH = SCRIPT_DIR / ("RSA_GUI.ui")
FONT_PATH = SCRIPT_DIR / "ARCADECLASSIC.ttf"

class UiScreen(QDialog):

	def __init__(self):
		super(UiScreen, self).__init__()
		loadUi(UI_PATH, self)

		self.radioButton_Encrypt.setChecked(True)

		self.pushButton.clicked.connect(self.spracuj)

	def spracuj(self):
		if self.radioButton_Encrypt.isChecked():
			plain_text = self.textEdit_plainText.toPlainText()

			if plain_text == "":
				QMessageBox.warning(self, "Bad input", "Plain Text cannot be empty")
				return

			cipher_text, private_key, public_key, binary_text = RSA.encrypt(plain_text)

			self.textEdit_publicKey.setPlainText(str(public_key))
			self.textEdit_privateKey.setPlainText(str(private_key))
			self.textEdit_binaryText.setPlainText(str(binary_text))
			self.textEdit_cipheredText.setPlainText(str(cipher_text))

		elif self.radioButton_Decrypt.isChecked():
			plain_text = self.textEdit_plainText.toPlainText()
			if plain_text == "":
				QMessageBox.warning(self, "Bad input", "Plain Text cannot be empty")
				return

			private_key = self.textEdit_privateKey.toPlainText()

			if private_key == "":
				QMessageBox.warning(self, "Bad input", "Private Key cannot be empty")
				return


			private_key = private_key.replace("(", " ").replace(")", " ")

			n, d = private_key.split(",")

			decrypted_text = RSA.decrypt(plain_text, int(d), int(n))

			self.textEdit_cipheredText.setPlainText(str(decrypted_text))

if __name__ == "__main__":
	app = QApplication(sys.argv)

	# nacitanie fontu
	#QFontDatabase.addApplicationFont(str(FONT_PATH))

	ui = UiScreen()
	ui.setFixedSize(ui.size())
	ui.show()

	sys.exit(app.exec())
