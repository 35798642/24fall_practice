
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from MainWindow import Ui_MainWindow


def main():
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()
    w.paintEngine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
