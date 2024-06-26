# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        #Form.resize(658, 774)
        self.setFixedSize(620, 774)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        #Form.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(16.0)
        Form.setStyleSheet("QPushButton {\n"
"    background-color: rgb(225, 58, 255);\n"
"    border-style: outset;\n"
"    border-width: 14px;\n"
"    border-radius: 10px;\n"
"    border-color: green;\n"
"    font: bold 30px;\n"
"    min-width: 10em;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 611, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_widgets = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_widgets.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_widgets.setObjectName("verticalLayout_widgets")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(3)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_widgets.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.T_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.T_label_2.setFont(font)
        self.T_label_2.setLineWidth(3)
        self.T_label_2.setTextFormat(QtCore.Qt.RichText)
        self.T_label_2.setObjectName("T_label_2")
        self.horizontalLayout_4.addWidget(self.T_label_2, 0, QtCore.Qt.AlignHCenter)
        self.T_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.T_lineEdit.setMaxLength(6)
        self.T_lineEdit.setObjectName("T_lineEdit")
        self.horizontalLayout_4.addWidget(self.T_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.T_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.T_label.setFont(font)
        self.T_label.setLineWidth(3)
        self.T_label.setTextFormat(QtCore.Qt.RichText)
        self.T_label.setObjectName("T_label")
        self.horizontalLayout_2.addWidget(self.T_label, 0, QtCore.Qt.AlignHCenter)
        self.m_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.m_lineEdit.setMaxLength(6)
        self.m_lineEdit.setObjectName("m_lineEdit")
        self.horizontalLayout_2.addWidget(self.m_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.T_label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.T_label_4.setFont(font)
        self.T_label_4.setLineWidth(3)
        self.T_label_4.setTextFormat(QtCore.Qt.RichText)
        self.T_label_4.setObjectName("T_label_4")
        self.horizontalLayout_7.addWidget(self.T_label_4, 0, QtCore.Qt.AlignHCenter)
        self.n_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.horizontalLayout_7.addWidget(self.n_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_buton_plotBZ = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buton_plotBZ.setObjectName("horizontalLayout_buton_plotBZ")
        self.clickHere_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clickHere_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clickHere_pushButton.sizePolicy().hasHeightForWidth())
        self.clickHere_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clickHere_pushButton.setFont(font)
        self.clickHere_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clickHere_pushButton.setMouseTracking(False)
        self.clickHere_pushButton.setTabletTracking(False)
        self.clickHere_pushButton.setStyleSheet("QPushButton#evilButton {\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    border-color: beige;\n"
"    font: bold 10px;\n"
"    min-width: 10em;\n"
"    padding: 1px;\n"
"}")
        self.clickHere_pushButton.setObjectName("clickHere_pushButton")
        self.horizontalLayout_buton_plotBZ.addWidget(self.clickHere_pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_buton_plotBZ)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(3)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.seebeck_output_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.seebeck_output_label.setEnabled(True)
        self.seebeck_output_label.setText("")
        self.seebeck_output_label.setObjectName("seebeck_output_label")
        self.horizontalLayout_10.addWidget(self.seebeck_output_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.T_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.T_label_3.setFont(font)
        self.T_label_3.setLineWidth(3)
        self.T_label_3.setTextFormat(QtCore.Qt.RichText)
        self.T_label_3.setObjectName("T_label_3")
        self.horizontalLayout_10.addWidget(self.T_label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_10)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 690, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: yellow;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.label_8.setLineWidth(3)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 690, 541, 31))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Seebeck Coefficient calculator (by aymen mahmoudi) V 1.0"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><img src=\":/pic/equation.gif\" width=\"400\" height=\"150\"/></p></body></html>"))
        self.T_label_2.setText(_translate("Form", "<html><head/><body><p>Temerature (K)</p></body></html>"))
        self.T_lineEdit.setText(_translate("Form", "14"))
        self.T_lineEdit.setPlaceholderText(_translate("Form", "T en Kelvin"))
        self.T_label.setText(_translate("Form", "<html><head/><body><p>Relative effective mass</p></body></html>"))
        self.m_lineEdit.setText(_translate("Form", "0.2"))
        self.m_lineEdit.setPlaceholderText(_translate("Form", "Effective mass"))
        self.T_label_4.setText(_translate("Form", "<html><head/><body><p>Density (10<span style=\" vertical-align:super;\">19</span>cm<span style=\" vertical-align:super;\">-3</span>)</p></body></html>"))
        self.n_lineEdit.setText(_translate("Form", "6"))
        self.n_lineEdit.setPlaceholderText(_translate("Form", "density"))
        self.clickHere_pushButton.setToolTip(_translate("Form", "this is toolTIP"))
        self.clickHere_pushButton.setText(_translate("Form", "Calculate"))
        self.label_6.setText(_translate("Form", "Result "))
        self.T_label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; text-decoration: underline; color:#aa0000;\">uV/K </span></p></body></html>"))
        self.label_8.setText(_translate("Form", "Kholala xD -- dream team 2022"))
import picture_ressource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
