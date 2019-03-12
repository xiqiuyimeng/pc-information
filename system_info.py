# -*- coding: utf-8 -*-
from pc import systemInfo
from PyQt5 import QtWidgets
_author_ = 'luwt'
_date_ = '2018/7/22 23:53'


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = systemInfo.Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
