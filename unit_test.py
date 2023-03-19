import unittest
import main
from PySide6.QtWidgets import QApplication
from ui import Ui_MainWindow
import sys


class TestUI(unittest.TestCase):

    def test_ui(self):
        app2 = QApplication(sys.argv)
        window = main.MainWindow()
        window.show()

        assert issubclass(window.ui.__class__, Ui_MainWindow)


if __name__ == '__main__':
    unittest.main()