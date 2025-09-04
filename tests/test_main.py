# pylint: disable=E0611, W0612

import os
import pytest

from PySide6.QtWidgets import QApplication
from main import MainWindow


def test_main_window_title():
    if os.environ.get("CI") == "true" or os.environ.get("GITHUB_ACTIONS") == "true":
        pytest.skip("Skipping GUI test in CI environment")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert window.windowTitle() == "PySide6 template"
