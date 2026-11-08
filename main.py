import sys

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

from pathlib import Path

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


    elif self.radioButton_Decrypt.isChecked():


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # nacitanie fontu
    QFontDatabase.addApplicationFont(str(FONT_PATH))

    ui = UiScreen()
    ui.setFixedSize(ui.size())
    ui.show()

    try:
        sys.exit(app.exec())
    except:
        print("exiting")