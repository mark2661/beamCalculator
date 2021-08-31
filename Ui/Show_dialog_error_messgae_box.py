from PyQt5.QtWidgets import QMessageBox


def showDialogErrorMessageBox():
    msg = QMessageBox()
    msg.setText("InvalidInput")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()