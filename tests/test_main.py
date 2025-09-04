# pylint: disable=E0611, W0612

from PySide6.QtWidgets import QApplication
from main import MainWindow


def test_main_window_title():
    if os.environ.get("CI"):
        pytest.skip("Skipping GUI test in CI environment")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert window.windowTitle() == "PySide6 template"
