# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.train_tab = QWidget()
        self.train_tab.setObjectName(u"train_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.train_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_task = QComboBox(self.train_tab)
        self.comboBox_task.setObjectName(u"comboBox_task")

        self.verticalLayout_2.addWidget(self.comboBox_task)

        self.comboBox_points = QComboBox(self.train_tab)
        self.comboBox_points.setObjectName(u"comboBox_points")

        self.verticalLayout_2.addWidget(self.comboBox_points)

        self.plainTextEdit_task_info = QPlainTextEdit(self.train_tab)
        self.plainTextEdit_task_info.setObjectName(u"plainTextEdit_task_info")
        self.plainTextEdit_task_info.setEnabled(True)
        self.plainTextEdit_task_info.setMouseTracking(False)
        self.plainTextEdit_task_info.setTabletTracking(False)
        self.plainTextEdit_task_info.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit_task_info.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit_task_info.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_task_info.setTabChangesFocus(False)
        self.plainTextEdit_task_info.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit_task_info.setReadOnly(True)
        self.plainTextEdit_task_info.setOverwriteMode(False)
        self.plainTextEdit_task_info.setBackgroundVisible(False)
        self.plainTextEdit_task_info.setCenterOnScroll(False)

        self.verticalLayout_2.addWidget(self.plainTextEdit_task_info)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back = QPushButton(self.train_tab)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.lineEdit_day = QLineEdit(self.train_tab)
        self.lineEdit_day.setObjectName(u"lineEdit_day")

        self.horizontalLayout_3.addWidget(self.lineEdit_day)

        self.btn_for = QPushButton(self.train_tab)
        self.btn_for.setObjectName(u"btn_for")

        self.horizontalLayout_3.addWidget(self.btn_for)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.plainTextEdit_data_info = QPlainTextEdit(self.train_tab)
        self.plainTextEdit_data_info.setObjectName(u"plainTextEdit_data_info")
        self.plainTextEdit_data_info.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.plainTextEdit_data_info)

        self.tabWidget.addTab(self.train_tab, "")
        self.classer_tab = QWidget()
        self.classer_tab.setObjectName(u"classer_tab")
        self.horizontalLayout = QHBoxLayout(self.classer_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.classer_tab, "")
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.data_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget.addTab(self.data_tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0430\u0431\u043b\u044c", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.plainTextEdit_task_info.setPlainText("")
        self.plainTextEdit_task_info.setPlaceholderText("")
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"    <    ", None))
        self.btn_for.setText(QCoreApplication.translate("MainWindow", u"    >    ", None))
        self.plainTextEdit_data_info.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.train_tab), QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.classer_tab), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0435\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

