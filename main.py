# pylint: disable=E0611

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSystemTrayIcon,
    QLabel,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtGui import QIcon, QAction, QFont, QPixmap
from PySide6.QtCore import Qt

from utils.utils import load_csv, resource_path


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        self.file_menu = QMenu("File", self)
        self.file_menu.addAction(QAction("Item", self))
        self.addMenu(self.file_menu)


class SystemTrayMenu:
    def __init__(self, main_window, main_app):
        self.tray_icon = QSystemTrayIcon(QIcon("assets/logo/logo.ico"), main_window)
        self.tray_menu = QMenu()

        quit_action = QAction("Quit", main_window)
        quit_action.triggered.connect(main_app.quit)
        self.tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Large font label centered
        label = QLabel("PySide6 template")
        font = QFont()
        font.setPointSize(32)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # CSV contents centered below the label
        # csv_content = load_csv(resource_path("data/data.csv"))
        csv_content = load_csv("data/data.csv")
        csv_label = QLabel(csv_content)
        csv_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(csv_label)

        # Image centered below CSV
        image_label = QLabel()
        image_pixmap = QPixmap(resource_path("assets/images/image_example.png"))
        # image_pixmap = QPixmap("assets/images/image_example.png")
        image_label.setPixmap(image_pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 template")
        self.resize(800, 600)
        self.setWindowIcon(QIcon("assets/logo/logo.ico"))
        self.setMenuBar(MenuBar())

        MainWidget_instance = MainWidget()
        self.setCentralWidget(MainWidget_instance)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    tray_menu = SystemTrayMenu(window, app)
    sys.exit(app.exec())
