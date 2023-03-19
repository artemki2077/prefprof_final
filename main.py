import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import requests
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ind_day = 0
        self.v_max = 2

        self.r = requests.get('https://dt.miet.ru/ppo_it_final', headers={"X-Auth-Token": "629q2skt"})

        self.index_task = 0
        self.index_pint = 0
        self.points = self.r.json()['message'][self.index_task]['points']

        for i in range(len(self.r.json()['message'])):
            self.ui.comboBox_task.addItem(str(i + 1))

        self.up_task(self.index_task)

        self.ui.comboBox_task.currentIndexChanged.connect(self.up_task)
        self.ui.comboBox_points.currentIndexChanged.connect(self.up_point)



        self.ui.btn_for.clicked.connect(self.day_up)
        self.ui.btn_back.clicked.connect(self.day_down)



        self.ui.lineEdit_day.setText(str(self.ind_day))

    def day_up(self):
        self.ind_day += 1

        self.ui.lineEdit_day.setText(str(self.ind_day))

    def day_down(self):
        self.ind_day -= 1

        if self.ind_day == -1:
            self.ind_day = 0

        self.ui.lineEdit_day.setText(str(self.ind_day))

    def up_task(self, value):
        self.index_task = int(value)
        self.points = self.r.json()['message'][self.index_task]['points']

        print(self.points)
        self.ui.comboBox_points.clear()
        for i in range(len(self.points)):
            self.ui.comboBox_points.addItem(str(i + 1))

        self.sum_sh = sum([i['SH'] for i in self.points])
        self.sum_distance = sum([i['distance'] for i in self.points])

        self.task_info = {
            'взять SH'     : self.sum_sh + 8,
            'вся дистанция': self.sum_distance,
            'количество дней': self.sum_distance / self.v_max
        }

        self.ui.plainTextEdit_task_info.setPlainText(json.dumps(self.task_info, ensure_ascii=False, indent=4))
    
    def up_point(self, value):
        self.index_pint = value


        sum_to_point = 0
        for i in range(value):
            sum_to_point += self.points[i]
        print(f'{value}: {sum_to_point}')
        self.data_infp = {
            'ТОЧКА ': value + 1,
            'выгрузить SH': self.points[value]['SH'],
            'останется SH': self.sum_sh -
        }
        self.ui.plainTextEdit_data_info.setPlainText(json.dumps(self.data_infp, ensure_ascii=False, indent=4))
        


if __name__ == "__main__":
    # print(get_data())
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())