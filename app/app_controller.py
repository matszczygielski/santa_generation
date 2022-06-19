from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie

from random import randint

from app.santa import Santa


class AppController(QMainWindow):
    def __init__(self) -> None:
        super(AppController, self).__init__()
        loadUi("ui/app.ui", self)

        self._santas = []

        # Set up gifs
        santa_movie = QMovie("ui/resources/santa-pic.png")
        self.rightgif_label.setMovie(santa_movie)
        self.leftgif_label.setMovie(santa_movie)
        santa_movie.start()

        # Set buttons handlers
        self.add_santa_button.clicked.connect(self._add_santa_handle)
        self.add_constrain_pick_button.clicked.connect(self._add_pick_constrain_handle)
        self.generate_button.clicked.connect(self._generate_handle)

        self.constrain_pick_left_input.currentIndexChanged.connect(self._pick_constrain_left_activated_handle)

        self._refresh_table()


    def _add_santa_handle(self):
        new_santa_name = self.add_santa_input.text()

        if not new_santa_name:
            return

        if new_santa_name not in [santa.name for santa in self._santas]:
            self._santas.append(Santa(new_santa_name))
            self.constrain_pick_left_input.addItem(new_santa_name)
            # Change current index to activate pick constrain signal
            self.constrain_pick_left_input.setCurrentIndex(self.constrain_pick_left_input.count() - 1)

        print(f"New santa {new_santa_name}")

        self.add_santa_input.setText("")

        self._refresh_table()


    def _add_pick_constrain_handle(self):
        if not self.constrain_pick_right_input.currentText():
            return

        l_santa_name = self.constrain_pick_left_input.currentText()
        r_santa_name = self.constrain_pick_right_input.currentText()

        saved_santa = next(s for s in self._santas if s.name == l_santa_name)

        if r_santa_name not in saved_santa.forbidden_santas:
            saved_santa.add_forbidden_santa(r_santa_name)
            print(f"New forbidden santa {r_santa_name} for {l_santa_name}")

            self._refresh_table()


    def _generate_handle(self):
        '''
        santa_draw_order = dict()

        for santa in self._santas:
            possible_draw_count = 0
            for s in self._santas:
                if s.name == santa.name:
                    continue
                if santa.name in s.forbidden_santas:
                    continue
                possible_draw_count += 1
            #santa_draw_order[]
        '''




        for santa in self._santas:
            if santa.has_drawn_santa():
                continue

            # Collect santas to draw
            santas_to_draw = []
            for search_santa in self._santas:
                if search_santa.is_owned:
                    continue

                if search_santa.name in santa.forbidden_santas:
                    continue

                if search_santa.name == santa.name:
                    continue

                santas_to_draw.append(search_santa.name)

            if not len(santas_to_draw):
                continue

            drawn_santa_idx = randint(0, len(santas_to_draw) - 1)
            drawn_santa = next(s for s in self._santas if s.name == santas_to_draw[drawn_santa_idx])

            santa.drawn_santa = drawn_santa.name
            drawn_santa.is_owned = True

        self._refresh_table()


    def _pick_constrain_left_activated_handle(self):
        self.constrain_pick_right_input.clear()

        for santa in self._santas:
            if santa.name == self.constrain_pick_left_input.currentText():
                continue
            self.constrain_pick_right_input.addItem(santa.name)


    def _refresh_table(self):
        self.santa_table.clearContents()
        self.santa_table.setRowCount(0)

        for idx, santa in enumerate(self._santas):
            self.santa_table.insertRow(idx)
            name_item = QtWidgets.QTableWidgetItem(santa.name)
            name_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.santa_table.setItem(idx, 0, name_item)

            forbidden_item = QtWidgets.QTableWidgetItem(", ".join(santa.forbidden_santas))
            forbidden_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.santa_table.setItem(idx, 1, forbidden_item)

            url_item = QtWidgets.QTableWidgetItem(santa.secret_url)
            url_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.santa_table.setItem(idx, 2, url_item)

        header = self.santa_table.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
