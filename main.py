from os import name
import sys

from app import app
from app.app_controller import AppController


if __name__ == "__main__":
    app_controller = AppController()
    app_controller.show()
    sys.exit(app.exec_())
