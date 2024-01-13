import sys
import psutil
import winreg
import pyuac

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        cpu_info = psutil.cpu_freq()
        max_frequency = cpu_info.max
        print(f"CPU_Control_Turbo")

        self.ui.max_ghz.setText(f"{int(max_frequency + 300)}")
        self.ui.done.clicked.connect(self.clock)

    def clock(self):
        print("Управление максимальной частотой процесса разблокировано.")
        registry_key_path = r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\75b0ae3f-bce0-45a7-8c89-c9611c25e100"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Attributes", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(key)


if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        app = QApplication()
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
