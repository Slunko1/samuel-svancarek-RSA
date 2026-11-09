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

range_low = pow(10, 14)
range_high = pow(10, 15)

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

			p, q = 0, 0
			while p == 0 or q == 0:
				random_number = RSA.generate_random_number(range_low, range_high)
				if RSA.check_prime(random_number, 40):
					if p == 0:
						p = random_number
					elif random_number != p:
						q = random_number

			n = RSA.multiply(p, q)

			phi = RSA.euler(p, q)
			e = RSA.get_euler_e(phi)

			d = RSA.find_inverse(e, phi)

			ascii_text = RSA.convert_to_ascii(plain_text)
			binary_array = RSA.convert_ascii_to_binary(ascii_text)
			m = RSA.convert_binary_to_decimal(binary_array)

			if m >= n:
				QMessageBox.warning(self, "Error", "Message is too large")
				return

			cipher_test = RSA.encrypt(m, e, n)

			self.textEdit_cipheredText.setPlainText(str(cipher_test))

		elif self.radioButton_Decrypt.isChecked():
			return

if __name__ == "__main__":
	app = QApplication(sys.argv)

	# nacitanie fontu
	#QFontDatabase.addApplicationFont(str(FONT_PATH))

	ui = UiScreen()
	ui.setFixedSize(ui.size())
	ui.show()

	sys.exit(app.exec())
