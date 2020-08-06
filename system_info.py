# -*- coding: utf-8 -*-
import systemInfo
import sys
from PyQt5 import QtWidgets
_author_ = 'luwt'
_date_ = '2018/7/22 23:53'


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = systemInfo.Ui_widget()
    ui.show()
    sys.exit(app.exec_())
