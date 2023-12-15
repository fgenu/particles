import sys

from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication

from gui.mywindow import MyWindow
from simulation import Simulation


def main():
    app = QApplication(sys.argv)
    gui = MyWindow(Simulation())
    gui.show()
    timer = QTimer()
    timer.timeout.connect(gui.update_simulation)
    timer.setInterval(1)
    timer.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
