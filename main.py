import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import requests
import json
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ind_day = 0
        self.v_max = 2

        self.T = 25
        self.oxi = 30

        self.k = math.sin((-math.pi / 2) + ((math.pi * (self.T + 0.5) * self.oxi) / 40))

        self.r = requests.get('https://dt.miet.ru/ppo_it_final/judge2', headers={"X-Auth-Token": "629q2skt"})

        # json.dump(self.r.json(), open('data.json', 'w', encoding='utf8'))


        self.index_task = 0
        self.index_pint = 0
        self.points = self.r.json()['message'][self.index_task]['points']

        for i in range(len(self.r.json()['message'])):
            self.ui.comboBox_task.addItem(str(i + 1))

        self.up_task(self.index_task)

        self.ui.comboBox_task.currentIndexChanged.connect(self.up_task)
        self.ui.comboBox_points.currentIndexChanged.connect(self.up_point)

    def up_task(self, value):

        self.index_task = int(value)
        self.points = self.r.json()['message'][self.index_task]['points']

        self.ui.comboBox_points.clear()
        for i in range(len(self.points)):
            self.ui.comboBox_points.addItem(str(i + 1))

        self.sum_sh = sum([i['SH'] for i in self.points])
        self.sum_distance = sum([i['distance'] for i in self.points])

        self.task_info = {
            'взять SH'       : self.sum_sh + 8,
            'вся дистанция'  : self.sum_distance,
            'количество дней': self.sum_distance / self.v_max
        }

        self.ui.plainTextEdit_task_info.setPlainText(json.dumps(self.task_info, ensure_ascii=False, indent=4))

    def get_last_g(self, value):
        if value < 1:
            return 1
        else:
            prm = self.get_last_g(value - 1)
            return prm + (prm * self.k)

    def up_point(self, value):
        self.index_pint = value

        self.sum_sh = sum([i['SH'] for i in self.points]) + 8
        self.sum_distance = sum([i['distance'] for i in self.points])

        sum_to_point = 0
        sum_d_to_point = 0

        for i in self.points[:value + 1]:
            sum_to_point += i['SH']
            sum_d_to_point += i['distance']

        self.day = (sum_d_to_point / self.sum_distance) * (self.sum_distance / self.v_max)

        self.u = 2 * (0.8 / 80) * (200 / (sum_to_point + 192))

        self.data_infp = {
            'ТОЧКА '      : value + 1,
            'день'        : self.day,
            'выгрузить SH': self.points[value]['SH'],
            'останется SH': self.sum_sh - sum_to_point,
            'масса'       : sum_to_point + 192,
            'скорость'    : self.u,
            'generation'  : self.get_last_g(value),
            'oxi': self.oxi
        }
        self.ui.plainTextEdit_data_info.setPlainText(json.dumps(self.data_infp, ensure_ascii=False, indent=4))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    # print(get_data())
    main()