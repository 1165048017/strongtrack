# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 864)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QVBoxLayout()
        self.SideBar.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.SideBar.setSpacing(6)
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(120, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.button_landmarks = QtWidgets.QPushButton(self.centralwidget)
        self.button_landmarks.setEnabled(False)
        self.button_landmarks.setObjectName("button_landmarks")
        self.verticalLayout_3.addWidget(self.button_landmarks)
        self.button_train = QtWidgets.QPushButton(self.centralwidget)
        self.button_train.setEnabled(False)
        self.button_train.setObjectName("button_train")
        self.verticalLayout_3.addWidget(self.button_train)
        self.button_weld = QtWidgets.QPushButton(self.centralwidget)
        self.button_weld.setEnabled(False)
        self.button_weld.setObjectName("button_weld")
        self.verticalLayout_3.addWidget(self.button_weld)
        self.button_neutral = QtWidgets.QPushButton(self.centralwidget)
        self.button_neutral.setEnabled(False)
        self.button_neutral.setObjectName("button_neutral")
        self.verticalLayout_3.addWidget(self.button_neutral)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox)
        self.button_setKeypose = QtWidgets.QPushButton(self.centralwidget)
        self.button_setKeypose.setEnabled(False)
        self.button_setKeypose.setObjectName("button_setKeypose")
        self.verticalLayout_5.addWidget(self.button_setKeypose)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.SideBar.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.SideBar)
        self.RightBar = QtWidgets.QVBoxLayout()
        self.RightBar.setObjectName("RightBar")
        self.vidholder = QtWidgets.QHBoxLayout()
        self.vidholder.setObjectName("vidholder")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMouseTracking(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vidholder.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.RightBar.addLayout(self.vidholder)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.RightBar.addWidget(self.horizontalSlider)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_prevFrame = QtWidgets.QPushButton(self.centralwidget)
        self.button_prevFrame.setEnabled(False)
        self.button_prevFrame.setObjectName("button_prevFrame")
        self.horizontalLayout_3.addWidget(self.button_prevFrame)
        self.button_playPause = QtWidgets.QPushButton(self.centralwidget)
        self.button_playPause.setEnabled(False)
        self.button_playPause.setObjectName("button_playPause")
        self.horizontalLayout_3.addWidget(self.button_playPause)
        self.button_nextFrame = QtWidgets.QPushButton(self.centralwidget)
        self.button_nextFrame.setEnabled(False)
        self.button_nextFrame.setObjectName("button_nextFrame")
        self.horizontalLayout_3.addWidget(self.button_nextFrame)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.RightBar.addLayout(self.verticalLayout)
        self.RightBar.setStretch(0, 50)
        self.RightBar.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.RightBar)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Video = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video.setObjectName("actionOpen_Video")
        self.actionNew_Model = QtWidgets.QAction(MainWindow)
        self.actionNew_Model.setEnabled(False)
        self.actionNew_Model.setObjectName("actionNew_Model")
        self.actionLoad_Model = QtWidgets.QAction(MainWindow)
        self.actionLoad_Model.setEnabled(False)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionPrevious_Model = QtWidgets.QAction(MainWindow)
        self.actionPrevious_Model.setEnabled(False)
        self.actionPrevious_Model.setObjectName("actionPrevious_Model")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setEnabled(False)
        self.actionExport.setObjectName("actionExport")
        self.actionStream_OSC = QtWidgets.QAction(MainWindow)
        self.actionStream_OSC.setEnabled(False)
        self.actionStream_OSC.setObjectName("actionStream_OSC")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionQuick_Video = QtWidgets.QAction(MainWindow)
        self.actionQuick_Video.setObjectName("actionQuick_Video")
        self.menuFile.addAction(self.actionOpen_Video)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Model)
        self.menuFile.addAction(self.actionLoad_Model)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuData.addAction(self.actionExport)
        self.menuData.addAction(self.actionStream_OSC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Train Landmarks:"))
        self.button_landmarks.setText(_translate("MainWindow", "Set Landmarks (F)"))
        self.button_train.setText(_translate("MainWindow", "Train Model (T)"))
        self.button_weld.setText(_translate("MainWindow", "Weld Lips (W)"))
        self.button_neutral.setText(_translate("MainWindow", "Neutral Lips (N)"))
        self.label_3.setText(_translate("MainWindow", "Extraction poses:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Neutral"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Jaw Open"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Closed Smile"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Smile Left"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Smile Right"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Mouth Frown"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Lip Funnel"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Lip Pucker"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Brows Up"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Brows Down"))
        self.button_setKeypose.setText(_translate("MainWindow", "Set Keypose"))
        self.label.setText(_translate("MainWindow", "Select \'Open Video\' from the File menu to get started"))
        self.button_prevFrame.setText(_translate("MainWindow", "Prev. Frame (A)"))
        self.button_playPause.setText(_translate("MainWindow", "Pause/Play (Space)"))
        self.button_nextFrame.setText(_translate("MainWindow", "Next Frame (D)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuData.setTitle(_translate("MainWindow", "Stream/Export"))
        self.actionOpen_Video.setText(_translate("MainWindow", "Open Video..."))
        self.actionNew_Model.setText(_translate("MainWindow", "New Model..."))
        self.actionLoad_Model.setText(_translate("MainWindow", "Load Model..."))
        self.actionPrevious_Model.setText(_translate("MainWindow", "Previous Model"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionStream_OSC.setText(_translate("MainWindow", "Stream OSC..."))
        self.actionDocumentation.setText(_translate("MainWindow", "Docs (web link)"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionQuick_Video.setText(_translate("MainWindow", "Quick Video"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
