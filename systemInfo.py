# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import webbrowser
from datetime import datetime
import time
import psutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import image_rc


class Ui_widget(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_widget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("widget")
        self.resize(500, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inner_widget = QtWidgets.QWidget(self.frame)
        self.inner_widget.setObjectName("inner_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inner_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.blank_top = QtWidgets.QLabel(self.inner_widget)
        self.blank_top.setObjectName("blank_top")
        self.verticalLayout_3.addWidget(self.blank_top)
        self.title = QtWidgets.QLabel(self.inner_widget)
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.desc = QtWidgets.QLabel(self.inner_widget)
        self.desc.setObjectName("desc")
        self.verticalLayout_3.addWidget(self.desc)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_cpu_logical = QtWidgets.QLabel(self.inner_widget)
        self.label_cpu_logical.setObjectName("label_cpu_logical")
        self.gridLayout.addWidget(self.label_cpu_logical, 0, 0, 1, 1)
        self.cpu_logical_value = QtWidgets.QLabel(self.inner_widget)
        self.cpu_logical_value.setObjectName("cpu_logical_value")
        self.gridLayout.addWidget(self.cpu_logical_value, 0, 1, 1, 1)
        self.label_cpu_physical = QtWidgets.QLabel(self.inner_widget)
        self.label_cpu_physical.setObjectName("label_cpu_physical")
        self.gridLayout.addWidget(self.label_cpu_physical, 1, 0, 1, 1)
        self.cpu_physical_value = QtWidgets.QLabel(self.inner_widget)
        self.cpu_physical_value.setObjectName("cpu_physical_value")
        self.gridLayout.addWidget(self.cpu_physical_value, 1, 1, 1, 1)
        self.label_cpu_load = QtWidgets.QLabel(self.inner_widget)
        self.label_cpu_load.setObjectName("label_cpu_load")
        self.gridLayout.addWidget(self.label_cpu_load, 2, 0, 1, 1)
        self.cpu_load_value = QtWidgets.QLabel(self.inner_widget)
        self.cpu_load_value.setObjectName("cpu_load_value")
        self.gridLayout.addWidget(self.cpu_load_value, 2, 1, 1, 1)
        self.label_memory_total = QtWidgets.QLabel(self.inner_widget)
        self.label_memory_total.setObjectName("label_memory_total")
        self.gridLayout.addWidget(self.label_memory_total, 3, 0, 1, 1)
        self.memory_total_value = QtWidgets.QLabel(self.inner_widget)
        self.memory_total_value.setObjectName("memory_total_value")
        self.gridLayout.addWidget(self.memory_total_value, 3, 1, 1, 1)
        self.label_memory_total_available = QtWidgets.QLabel(self.inner_widget)
        self.label_memory_total_available.setObjectName("label_memory_total_available")
        self.gridLayout.addWidget(self.label_memory_total_available, 4, 0, 1, 1)
        self.memory_total_available_value = QtWidgets.QLabel(self.inner_widget)
        self.memory_total_available_value.setObjectName("memory_total_available_value")
        self.gridLayout.addWidget(self.memory_total_available_value, 4, 1, 1, 1)
        self.label_memory_total_used = QtWidgets.QLabel(self.inner_widget)
        self.label_memory_total_used.setObjectName("label_memory_total_used")
        self.gridLayout.addWidget(self.label_memory_total_used, 5, 0, 1, 1)
        self.memory_total_used_value = QtWidgets.QLabel(self.inner_widget)
        self.memory_total_used_value.setObjectName("memory_total_used_value")
        self.gridLayout.addWidget(self.memory_total_used_value, 5, 1, 1, 1)
        self.label_memory_percent = QtWidgets.QLabel(self.inner_widget)
        self.label_memory_percent.setObjectName("label_memory_percent")
        self.gridLayout.addWidget(self.label_memory_percent, 6, 0, 1, 1)
        self.memory_percent_value = QtWidgets.QLabel(self.inner_widget)
        self.memory_percent_value.setObjectName("memory_percent_value")
        self.gridLayout.addWidget(self.memory_percent_value, 6, 1, 1, 1)
        self.label_system_start_time = QtWidgets.QLabel(self.inner_widget)
        self.label_system_start_time.setObjectName("label_system_start_time")
        self.gridLayout.addWidget(self.label_system_start_time, 7, 0, 1, 1)
        self.system_start_time_value = QtWidgets.QLabel(self.inner_widget)
        self.system_start_time_value.setObjectName("system_start_time_value")
        self.gridLayout.addWidget(self.system_start_time_value, 7, 1, 1, 1)
        self.label_now = QtWidgets.QLabel(self.inner_widget)
        self.label_now.setObjectName("label_now")
        self.gridLayout.addWidget(self.label_now, 8, 0, 1, 1)
        self.now_value = QtWidgets.QLabel(self.inner_widget)
        self.now_value.setObjectName("now_value")
        self.gridLayout.addWidget(self.now_value, 8, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)

        self.blank = QtWidgets.QLabel(self.inner_widget)
        self.blank.setObjectName("blank")
        self.verticalLayout_3.addWidget(self.blank)

        self.gridLayout_button = QtWidgets.QGridLayout()
        self.gridLayout_button.setObjectName("gridLayout_button")
        self.button_blank_left = QtWidgets.QLabel(self.inner_widget)
        self.button_blank_left.setObjectName("button_blank_left")
        self.gridLayout_button.addWidget(self.button_blank_left, 0, 1, 1, 1)
        self.contact_button = QtWidgets.QPushButton(self.inner_widget)
        self.contact_button.setObjectName("contact_button")
        self.gridLayout_button.addWidget(self.contact_button, 0, 0, 1, 1)
        self.exit_button = QtWidgets.QPushButton(self.inner_widget)
        self.exit_button.setObjectName("exit_button")
        self.gridLayout_button.addWidget(self.exit_button, 0, 3, 1, 1)
        self.button_blank_right = QtWidgets.QLabel(self.inner_widget)
        self.button_blank_right.setObjectName("button_blank_right")
        self.gridLayout_button.addWidget(self.button_blank_right, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_button)
        self.inner_widget.setLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.inner_widget)
        self.verticalLayout.addWidget(self.frame)

        self.contact_button.clicked.connect(self.contact)
        self.contact_button.setToolTip("前往作者github主页")
        self.exit_button.clicked.connect(self.close)
        self.exit_button.setToolTip("退出程序")

        # 创建并启用子线程
        self.thread_1 = Worker()
        self.thread_1.info.connect(self.set_value)
        self.thread_1.start()

        self.setWindowOpacity(0.95)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("#frame{border-style:solid;border-radius:30px;border-image:url(:/window.jpg);}"
                           "QLabel{font-size:19px;font-family:楷体;font-weight:300;qproperty-wordWrap:true;}"
                           "#desc{font-size:16px;}"
                           "#title{font-size:25px;qproperty-alignment:AlignHCenter;}"
                           "QPushButton{font-size:20px;font-family:楷体;font-weight:500px;color:black;"
                           "background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0, "
                           "stop:0 lightgreen,stop:1 SpringGreen);border-radius:8px;border-style:outset;border-width:2px;"
                           "border-color:Thistle;padding-top:1px;padding-left:1px;padding-bottom:3px;padding-right:3px;}"
                           "QPushButton:hover{background-color:LimeGreen;}"
                           "QPushButton:pressed{background-color:green;border-style:inset;padding-top:3px;"
                           "padding-left:3px}")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText("查询系统信息")
        self.label_cpu_logical.setText("cpu逻辑核心：")
        self.label_cpu_physical.setText("cpu物理核心：")
        self.label_cpu_load.setText("cpu负载：")
        self.label_memory_total.setText("内存总量：")
        self.label_memory_total_available.setText("可用内存总量：")
        self.label_memory_total_used.setText("已用内存总量：")
        self.label_memory_percent.setText("内存使用百分比：")
        self.label_system_start_time.setText("系统开机时间：")
        self.label_now.setText("当前时间：")

        self.desc.setText("作者：夕秋一梦\n描述：查询系统信息小工具，仅做参考，了解更多，请点击下方联系作者\n")
        self.blank.setText("")
        self.button_blank_left.setText("")
        self.contact_button.setText("联系作者")
        self.exit_button.setText("退出")
        self.button_blank_right.setText("")

    def set_value(self, values):
        self.cpu_logical_value.setText(values.get("cpu_logical_value"))
        self.cpu_physical_value.setText(values.get("cpu_physical"))
        self.cpu_load_value.setText(values.get("cpu_load"))
        self.memory_total_value.setText(values.get("memory_total"))
        self.memory_total_available_value.setText(values.get("memory_total_available"))
        self.memory_total_used_value.setText(values.get("memory_total_used"))
        self.memory_percent_value.setText(values.get("memory_percent"))
        self.system_start_time_value.setText(values.get("system_start_time"))
        self.now_value.setText(values.get("now"))

    def contact(self):
        webbrowser.open("https://github.com/xiqiuyimeng/pc-information")


class Worker(QThread):

    # 定义信号
    info = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.info.emit(self.get_system_info())
            time.sleep(1)

    def get_system_info(self):
        pc_mem = psutil.virtual_memory()
        div_gb_factor = (1024.0 ** 3)
        cpu_logical_count = psutil.cpu_count()
        cpu_physical_count = psutil.cpu_count(logical=False)
        cpu_load = psutil.cpu_percent()
        memory_total = round(float(pc_mem.total / div_gb_factor), 4)
        memory_total_available = round(float(pc_mem.available / div_gb_factor), 4)
        memory_total_used = round(float(pc_mem.used / div_gb_factor), 4)
        memory_percent = round(float(pc_mem.percent), 4)
        system_start_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "cpu_logical_value": f"{cpu_logical_count}个",
            "cpu_physical": f"{cpu_physical_count}个",
            "cpu_load": f"{cpu_load}%",
            "memory_total": f"{memory_total}GB",
            "memory_total_available": f"{memory_total_available}GB",
            "memory_total_used": f"{memory_total_used}GB",
            "memory_percent": f"{memory_percent}%",
            "system_start_time": system_start_time,
            "now": now
        }
