# -*- coding: utf-8 -*-
#_Author: Ziqi Li (liziqi1992@gmail.com)
#Generated using pyuic5 -x gui.ui -o gui.py


import os,sys

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd
from datetime import datetime
from mgwrlib.mgwr.gwr import GWR,MGWR
from mgwrlib.mgwr.sel_bw import Sel_BW
from mgwrlib.spglm.glm import GLM
from mgwrlib.spglm.family import Gaussian, Binomial, Poisson
from .outputs import *
from .loader import Ui_runningDialog
from .advanced import Ui_advDialog
from .summaryGUI import Ui_summaryDlg
#from .map import *
from time import sleep

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 618)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(764, 618))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/MGWR-pc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(289, 0, 191, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        self.variableList = QtWidgets.QListWidget(self.groupBox_2)
        self.variableList.setGeometry(QtCore.QRect(10, 20, 171, 351))
        self.variableList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.variableList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variableList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.variableList.setDragEnabled(False)
        self.variableList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.variableList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.variableList.setResizeMode(QtWidgets.QListView.Fixed)
        self.variableList.setObjectName("variableList")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 0, 261, 381))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.removeY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeY.setObjectName("removeY")
        self.gridLayout.addWidget(self.removeY, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.OffsetLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.OffsetLabel.setEnabled(False)
        self.OffsetLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OffsetLabel.setObjectName("OffsetLabel")
        self.gridLayout.addWidget(self.OffsetLabel, 1, 3, 1, 1)
        self.addY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addY.setObjectName("addY")
        self.gridLayout.addWidget(self.addY, 0, 1, 1, 1)
        self.responseLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.responseLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.responseLabel.setReadOnly(True)
        self.responseLabel.setObjectName("responseLabel")
        self.gridLayout.addWidget(self.responseLabel, 0, 3, 1, 1)
        self.addOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addOffset.setObjectName("addOffset")
        self.gridLayout.addWidget(self.addOffset, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.removeOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeOffset.setObjectName("removeOffset")
        self.gridLayout.addWidget(self.removeOffset, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(68, 80, 181, 296))
        self.groupBox_3.setObjectName("groupBox_3")
        self.localList = QtWidgets.QListWidget(self.groupBox_3)
        self.localList.setGeometry(QtCore.QRect(10, 20, 161, 271))
        self.localList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.localList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.localList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localList.setObjectName("localList")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_6)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 225, 56, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.removeLocal = QtWidgets.QToolButton(self.horizontalLayoutWidget_5)
        self.removeLocal.setObjectName("removeLocal")
        self.horizontalLayout_5.addWidget(self.removeLocal)
        self.addLocal = QtWidgets.QToolButton(self.horizontalLayoutWidget_5)
        self.addLocal.setObjectName("addLocal")
        self.horizontalLayout_5.addWidget(self.addLocal)
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 205, 271, 41))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 256, 19))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isGWRRBTN.setEnabled(True)
        self.isGWRRBTN.setCheckable(True)
        self.isGWRRBTN.setChecked(True)
        self.isGWRRBTN.setObjectName("isGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isGWRRBTN)
        self.isMGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isMGWRRBTN.setChecked(False)
        self.isMGWRRBTN.setObjectName("isMGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isMGWRRBTN)
        self.kernelDropdownGrou = QtWidgets.QGroupBox(Dialog)
        self.kernelDropdownGrou.setGeometry(QtCore.QRect(10, 250, 271, 51))
        self.kernelDropdownGrou.setObjectName("kernelDropdownGrou")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.kernelDropdownGrou)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 256, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fixedBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.fixedBox.setObjectName("fixedBox")
        self.fixedBox.addItem("")
        self.fixedBox.addItem("")
        self.horizontalLayout_3.addWidget(self.fixedBox)
        self.shapeBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.shapeBox.setObjectName("shapeBox")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.horizontalLayout_3.addWidget(self.shapeBox)
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 271, 166))
        self.groupBox_9.setObjectName("groupBox_9")
        self.bwDropdown = QtWidgets.QComboBox(self.groupBox_9)
        self.bwDropdown.setGeometry(QtCore.QRect(10, 20, 256, 21))
        self.bwDropdown.setObjectName("bwDropdown")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_9)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 236, 106))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.bwPreDefined = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwPreDefined.setEnabled(False)
        self.bwPreDefined.setObjectName("bwPreDefined")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bwPreDefined)
        self.bwMin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMin.setEnabled(False)
        self.bwMin.setObjectName("bwMin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bwMin)
        self.bwMax = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMax.setEnabled(False)
        self.bwMax.setObjectName("bwMax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bwMax)
        self.bwInterval = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwInterval.setEnabled(False)
        self.bwInterval.setObjectName("bwInterval")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bwInterval)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 50, 271, 156))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 125, 256, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isPrjCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isPrjCoorRBTN.setChecked(True)
        self.isPrjCoorRBTN.setObjectName("isPrjCoorRBTN")
        self.horizontalLayout.addWidget(self.isPrjCoorRBTN)
        self.isSphCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isSphCoorRBTN.setObjectName("isSphCoorRBTN")
        self.horizontalLayout.addWidget(self.isSphCoorRBTN)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 256, 101))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.removeYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeYCoor.setObjectName("removeYCoor")
        self.gridLayout_4.addWidget(self.removeYCoor, 2, 3, 1, 1)
        self.addID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addID.setObjectName("addID")
        self.gridLayout_4.addWidget(self.addID, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.idLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.idLabel.setText("")
        self.idLabel.setDragEnabled(True)
        self.idLabel.setReadOnly(True)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout_4.addWidget(self.idLabel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.yCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.yCoorLabel.setReadOnly(True)
        self.yCoorLabel.setObjectName("yCoorLabel")
        self.gridLayout_4.addWidget(self.yCoorLabel, 2, 1, 1, 1)
        self.addXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addXCoor.setObjectName("addXCoor")
        self.gridLayout_4.addWidget(self.addXCoor, 1, 2, 1, 1)
        self.removeXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeXCoor.setObjectName("removeXCoor")
        self.gridLayout_4.addWidget(self.removeXCoor, 1, 3, 1, 1)
        self.addYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addYCoor.setObjectName("addYCoor")
        self.gridLayout_4.addWidget(self.addYCoor, 2, 2, 1, 1)
        self.xCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.xCoorLabel.setReadOnly(True)
        self.xCoorLabel.setObjectName("xCoorLabel")
        self.gridLayout_4.addWidget(self.xCoorLabel, 1, 1, 1, 1)
        self.removeID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeID.setObjectName("removeID")
        self.gridLayout_4.addWidget(self.removeID, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 271, 51))
        self.groupBox.setObjectName("groupBox")
        self.openDataBTN = QtWidgets.QToolButton(self.groupBox)
        self.openDataBTN.setGeometry(QtCore.QRect(240, 20, 26, 21))
        self.openDataBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.openDataBTN.setObjectName("openDataBTN")
        self.openDataPath = QtWidgets.QLineEdit(self.groupBox)
        self.openDataPath.setGeometry(QtCore.QRect(11, 21, 221, 21))
        self.openDataPath.setObjectName("openDataPath")
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(290, 385, 461, 81))
        self.groupBox_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_10)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 381, 51))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_11 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_11.setObjectName("groupBox_11")
        self.optimCriDropdown = QtWidgets.QComboBox(self.groupBox_11)
        self.optimCriDropdown.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.optimCriDropdown.setObjectName("optimCriDropdown")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_11, 0, 2, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_12.setObjectName("groupBox_12")
        self.modelTypeDropdown = QtWidgets.QComboBox(self.groupBox_12)
        self.modelTypeDropdown.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.modelTypeDropdown.setObjectName("modelTypeDropdown")
        self.modelTypeDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.advancedBTN = QtWidgets.QToolButton(self.groupBox_10)
        self.advancedBTN.setGeometry(QtCore.QRect(400, 40, 56, 26))
        self.advancedBTN.setObjectName("advancedBTN")
        self.runBTN = QtWidgets.QPushButton(Dialog)
        self.runBTN.setGeometry(QtCore.QRect(615, 485, 121, 61))
        self.runBTN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.runBTN.setObjectName("runBTN")
        self.groupBox_13 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 470, 571, 81))
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_13)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 20, 551, 54))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saveBetasBTN = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.saveBetasBTN.setObjectName("saveBetasBTN")
        self.gridLayout_2.addWidget(self.saveBetasBTN, 1, 2, 1, 1)
        self.saveSumBTN = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.saveSumBTN.setObjectName("saveSumBTN")
        self.gridLayout_2.addWidget(self.saveSumBTN, 0, 2, 1, 1)
        self.betaFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.betaFileSavePath.setObjectName("betaFileSavePath")
        self.gridLayout_2.addWidget(self.betaFileSavePath, 1, 1, 1, 1)
        self.sumFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.sumFileSavePath.setReadOnly(True)
        self.sumFileSavePath.setObjectName("sumFileSavePath")
        self.gridLayout_2.addWidget(self.sumFileSavePath, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.predictionBox = QtWidgets.QGroupBox(Dialog)
        self.predictionBox.setGeometry(QtCore.QRect(10, 555, 571, 51))
        self.predictionBox.setObjectName("predictionBox")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.predictionBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 551, 23))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.predictInputEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.predictInputEdit.setObjectName("predictInputEdit")
        self.horizontalLayout_4.addWidget(self.predictInputEdit)
        self.openPredictionBTN = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.openPredictionBTN.setObjectName("openPredictionBTN")
        self.horizontalLayout_4.addWidget(self.openPredictionBTN)
        self.runBTN_2 = QtWidgets.QPushButton(Dialog)
        self.runBTN_2.setGeometry(QtCore.QRect(615, 570, 121, 31))
        self.runBTN_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.runBTN_2.setObjectName("runBTN_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MGWR"))
        self.groupBox_2.setTitle(_translate("Dialog", "Variable List"))
        self.groupBox_6.setTitle(_translate("Dialog", "Regression Variables"))
        self.removeY.setText(_translate("Dialog", "<"))
        self.label_5.setText(_translate("Dialog", "Offset"))
        self.addY.setText(_translate("Dialog", ">"))
        self.addOffset.setText(_translate("Dialog", ">"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.removeOffset.setText(_translate("Dialog", "<"))
        self.groupBox_3.setTitle(_translate("Dialog", "Local"))
        self.removeLocal.setText(_translate("Dialog", "<"))
        self.addLocal.setText(_translate("Dialog", ">"))
        self.groupBox_7.setTitle(_translate("Dialog", "GWR Mode"))
        self.isGWRRBTN.setText(_translate("Dialog", "GWR"))
        self.isMGWRRBTN.setText(_translate("Dialog", "MGWR"))
        self.kernelDropdownGrou.setTitle(_translate("Dialog", "Kernel"))
        self.fixedBox.setItemText(0, _translate("Dialog", "Adaptive"))
        self.fixedBox.setItemText(1, _translate("Dialog", "Fixed"))
        self.shapeBox.setItemText(0, _translate("Dialog", "Bisquare"))
        self.shapeBox.setItemText(1, _translate("Dialog", "Gaussian"))
        self.shapeBox.setItemText(2, _translate("Dialog", "Exponential"))
        self.groupBox_9.setTitle(_translate("Dialog", "Bandwidth"))
        self.bwDropdown.setItemText(0, _translate("Dialog", "Golden Section"))
        self.bwDropdown.setItemText(1, _translate("Dialog", "Interval Search"))
        self.bwDropdown.setItemText(2, _translate("Dialog", "Pre-defiend bandwidth"))
        self.label_6.setText(_translate("Dialog", "Pre-defined"))
        self.label_9.setText(_translate("Dialog", "Min"))
        self.label_10.setText(_translate("Dialog", "Max"))
        self.label_11.setText(_translate("Dialog", "Interval"))
        self.groupBox_4.setTitle(_translate("Dialog", "Location Variables"))
        self.isPrjCoorRBTN.setText(_translate("Dialog", "Projected"))
        self.isSphCoorRBTN.setText(_translate("Dialog", "Spherical"))
        self.removeYCoor.setText(_translate("Dialog", ">"))
        self.addID.setText(_translate("Dialog", "<"))
        self.label_3.setText(_translate("Dialog", "Y"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "X"))
        self.addXCoor.setText(_translate("Dialog", "<"))
        self.removeXCoor.setText(_translate("Dialog", ">"))
        self.addYCoor.setText(_translate("Dialog", "<"))
        self.removeID.setText(_translate("Dialog", ">"))
        self.groupBox.setTitle(_translate("Dialog", "Data Files"))
        self.openDataBTN.setText(_translate("Dialog", "..."))
        self.groupBox_10.setTitle(_translate("Dialog", "Model Options"))
        self.groupBox_11.setTitle(_translate("Dialog", "Optimization Criterion"))
        self.optimCriDropdown.setItemText(0, _translate("Dialog", "AICc"))
        self.optimCriDropdown.setItemText(1, _translate("Dialog", "AIC"))
        self.optimCriDropdown.setItemText(2, _translate("Dialog", "BIC"))
        self.optimCriDropdown.setItemText(3, _translate("Dialog", "CV"))
        self.groupBox_12.setTitle(_translate("Dialog", "Model Type"))
        self.modelTypeDropdown.setItemText(0, _translate("Dialog", "Gaussian"))
        self.advancedBTN.setText(_translate("Dialog", "Advanced"))
        self.runBTN.setText(_translate("Dialog", "Run"))
        self.groupBox_13.setTitle(_translate("Dialog", "Outputs"))
        self.saveBetasBTN.setText(_translate("Dialog", "..."))
        self.saveSumBTN.setText(_translate("Dialog", "..."))
        self.label_7.setText(_translate("Dialog", "Summary File"))
        self.label_8.setText(_translate("Dialog", "Parameter Estimates"))
        self.predictionBox.setTitle(_translate("Dialog", "Prediction (optional)"))
        self.openPredictionBTN.setText(_translate("Dialog", "..."))
        self.runBTN_2.setText(_translate("Dialog", "Help"))

    def update_label(self):
        current_time = self.elapsedTimeFormatter(self.time)
        self.loaderUI.label_2.setText(current_time)
    
    def elapsedTimeFormatter(self,time):
        secs = time.elapsed() / 1000
        mins = int((secs / 60) % 60)
        hours = int((secs / 3600))
        secs = int(secs % 60)
        return str(hours).zfill(2) + ':' + str(mins).zfill(2)  + ':' + str(secs).zfill(2)

    def addActionsToUI(self):
        
        self.greyOutLineEdit(self.OffsetLabel)
        self.greyOutLineEdit(self.bwPreDefined)
        self.greyOutLineEdit(self.bwMin)
        self.greyOutLineEdit(self.bwMax)
        self.greyOutLineEdit(self.bwInterval)
        

        self.openDataBTN.clicked.connect(self.openData)
        self.openPredictionBTN.clicked.connect(self.openPredictData)
        
        self.saveSumBTN.clicked.connect(lambda:self.getSaveFile(0))
        self.saveBetasBTN.clicked.connect(lambda:self.getSaveFile(1))
        
        self.addID.clicked.connect(lambda: self.addVariable(self.idLabel))
        self.removeID.clicked.connect(lambda: self.removeVariable(self.idLabel))
        
        self.addXCoor.clicked.connect(lambda: self.addVariable(self.xCoorLabel))
        self.removeXCoor.clicked.connect(lambda: self.removeVariable(self.xCoorLabel))
        
        self.addYCoor.clicked.connect(lambda: self.addVariable(self.yCoorLabel))
        self.removeYCoor.clicked.connect(lambda: self.removeVariable(self.yCoorLabel))
        
        self.addY.clicked.connect(lambda: self.addVariable(self.responseLabel))
        self.removeY.clicked.connect(lambda: self.removeVariable(self.responseLabel))
        
        self.addOffset.clicked.connect(lambda: self.addVariable(self.OffsetLabel))
        self.removeOffset.clicked.connect(lambda: self.removeVariable(self.OffsetLabel))
        
        self.addLocal.clicked.connect(self.addVarToLocal)
        self.removeLocal.clicked.connect(self.removeVarFromLocal)
    
        self.runBTN.clicked.connect(self.run_onclick)
        self.advancedBTN.clicked.connect(self.advancedOnClick)
        
        self.openDataPath.textChanged.connect(lambda: self.removeRed(self.openDataPath))
        self.sumFileSavePath.textChanged.connect(lambda: self.removeRed(self.sumFileSavePath))
        self.betaFileSavePath.textChanged.connect(lambda: self.removeRed(self.betaFileSavePath))
        
        self.responseLabel.textChanged.connect(lambda: self.removeRed(self.responseLabel))
        self.xCoorLabel.textChanged.connect(lambda: self.removeRed(self.xCoorLabel))
        self.yCoorLabel.textChanged.connect(lambda: self.removeRed(self.yCoorLabel))
        self.idLabel.textChanged.connect(lambda: self.removeRed(self.idLabel))
        
        self.bwMin.textChanged.connect(lambda: self.removeRed(self.bwMin))
        self.bwMax.textChanged.connect(lambda: self.removeRed(self.bwMax))
        self.bwPreDefined.textChanged.connect(lambda: self.removeRed(self.bwPreDefined))
        self.bwInterval.textChanged.connect(lambda: self.removeRed(self.bwInterval))
        
        self.isGWRRBTN.clicked.connect(self.gwrMode)
        self.isMGWRRBTN.clicked.connect(self.mgwrMode)
        
        self.isPrjCoorRBTN.clicked.connect(self.projCoors)
        self.isSphCoorRBTN.clicked.connect(self.sphCoors)
        
        
        validator = QtGui.QDoubleValidator()
        validator.setBottom(0)
        self.bwMin.setValidator(validator)
        self.bwMax.setValidator(validator)
        self.bwInterval.setValidator(validator)
        self.bwPreDefined.setValidator(validator)
        
        self.bwDropdown.currentIndexChanged.connect(self.changeSearchMethod)
        self.modelTypeDropdown.currentIndexChanged.connect(self.modelChanged)

        self.gwrMode()

        self.thread = AThread(self)
        self.thread.finished.connect(self.haha)
        self.runningWindow = QtWidgets.QDialog()
        
        self.runningDialog = QtWidgets.QDialog()
        self.loaderUI = Ui_runningDialog()
        self.loaderUI.setupUi(self.runningDialog)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.time = QtCore.QTime()
    
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))
    
    
        self.advDialog = QtWidgets.QDialog()
        self.advUI = Ui_advDialog()
        self.advUI.setupUi(self.advDialog)
        self.advUI.addActionsToUI()
            

    
    def openData(self):
        try:
            fileName,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile',self.path,"Excel(*.xls *.xlsx);;CSV (*.csv)")
            if fileName:
                self.openDataPath.setText(fileName)
                if fileName.endswith('.csv'):
                    self.data = pd.read_csv(fileName)
                    fields = self.data.columns.tolist()
                elif fileName.endswith('.xlsx') or fileName.endswith('.xls'):
                    self.data = pd.read_excel(fileName)
                    fields = self.data.columns.tolist()
                
                self.localList.clear()
                self.localList.addItem('Intercept')
                self.variableList.clear()
                self.idLabel.clear()
                self.xCoorLabel.clear()
                self.yCoorLabel.clear()
                self.responseLabel.clear()
                self.variableList.addItems(fields)
    
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Something went wrong when openning data. Please double check.')
            error_dialog.exec_()


    def openPredictData(self):
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))
        try:
            fileName,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile',self.path,"CSV (*.csv)")
            if fileName:
                self.predictInputEdit.setText(fileName)
                self.predictData = pd.read_csv(fileName)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Something went wrong when openning data. Please double check.')
            error_dialog.exec_()

    


    def addVariable(self,destination):
        if destination.text() and self.variableList.selectedItems():
            self.variableList.addItem(destination.text())
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(self.variableList.row(self.variableList.selectedItems()[0]))
            item = None
        elif not destination.text() and self.variableList.selectedItems():
            destination.setText(self.variableList.selectedItems()[0].text())
            item = self.variableList.takeItem(self.variableList.row(self.variableList.selectedItems()[0]))
            item = None

    def removeVariable(self,origin):
        if origin.text():
            item = self.variableList.addItem(origin.text())
            origin.setText("")

    def addVarToLocal(self):
        for item in self.variableList.selectedItems():
            self.localList.addItem(item.text())
            noneItem = self.variableList.takeItem(self.variableList.row(item))
            noneItem = None
            self.localList.setStyleSheet("QListWidget{border: 0px solid red;}")

    def removeVarFromLocal(self):
        for item in self.localList.selectedItems():
            self.variableList.addItem(item.text())
            noneItem = self.localList.takeItem(self.localList.row(item))
            noneItem = None

    def removeRed(self,lineEdit):
        lineEdit.setStyleSheet("")
    
    def greyOutLineEdit(self,lineEdit):
        lineEdit.setStyleSheet("background-color:LightGrey")
        lineEdit.setDisabled(True)
        lineEdit.clear()
    def deGreyOutLineEdit(self,lineEdit):
        lineEdit.setStyleSheet("")
        lineEdit.setDisabled(False)
    
    def changeSearchMethod(self,index):
        #golden section
        if index == 0:
            self.removeRed(self.bwMin)
            self.removeRed(self.bwMax)
            self.removeRed(self.bwInterval)
            self.removeRed(self.bwPreDefined)
            self.greyOutLineEdit(self.bwPreDefined)
            self.greyOutLineEdit(self.bwInterval)
            self.greyOutLineEdit(self.bwMin)
            self.greyOutLineEdit(self.bwMax)
        #interval
        elif index == 1:
            self.removeRed(self.bwPreDefined)
            self.greyOutLineEdit(self.bwPreDefined)
            self.deGreyOutLineEdit(self.bwInterval)
            self.deGreyOutLineEdit(self.bwMin)
            self.deGreyOutLineEdit(self.bwMax)
        #defined
        elif index == 2:
            self.removeRed(self.bwMin)
            self.removeRed(self.bwMax)
            self.removeRed(self.bwInterval)
            self.deGreyOutLineEdit(self.bwPreDefined)
            self.greyOutLineEdit(self.bwInterval)
            self.greyOutLineEdit(self.bwMin)
            self.greyOutLineEdit(self.bwMax)

    def modelChanged(self,index):
        #Gaussian
        if index == 0:
            self.removeVariable(self.OffsetLabel)
            self.greyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(False)
            self.removeOffset.setEnabled(False)
        #Binomial
        elif index == 1:
            self.removeVariable(self.OffsetLabel)
            self.greyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(False)
            self.removeOffset.setEnabled(False)
        #Poisson
        elif index == 2:
            self.deGreyOutLineEdit(self.OffsetLabel)
            self.addOffset.setEnabled(True)
            self.removeOffset.setEnabled(True)

    
    
    def gwrMode(self):

        #self.predictionBox.show()
        self.predictionBox.setEnabled(True)
        self.advancedBTN.setEnabled(False)
        
        self.modelTypeDropdown.clear()
        self.modelTypeDropdown.addItem("Gaussian")
        self.modelTypeDropdown.addItem("Binomial")
        self.modelTypeDropdown.addItem("Poisson")
        
        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        
        self.isGWR = True
        self.isMGWR = False

    
    def mgwrMode(self):
        self.predictionBox.setEnabled(False)
        self.advancedBTN.setEnabled(True)
        
        self.modelTypeDropdown.clear()
        self.modelTypeDropdown.addItem("Gaussian")
        
        self.isMGWR = True
        self.isGWR = False
    
    
    def projCoors(self):
        self.label_X.setText('X   ')
        self.label_Y.setText('Y   ')
    
    def sphCoors(self):
        self.label_X.setText('Lon')
        self.label_Y.setText('Lat')
    

    def advancedOnClick(self):
        if self.isMGWR:
            self.advUI.loadSettings()
            self.advDialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            self.advDialog.exec_()
    
    
    #Get 3 Save Paths for control, summary and betas
    def getSaveFile(self,ext):
        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(None, 'SaveFile',os.path.join(os.path.dirname(self.path),'GWR_session'))
        if fileName:
            if ext == 0:
                self.sumFileSavePath.setText(fileName+'_summary.txt')
                self.betaFileSavePath.setText(fileName + '_betas.csv')
            if ext == 1:
                self.betaFileSavePath.setText(fileName + '_betas.csv')

    
    
    #Getting all data for running model
    def preCheckEmptyFields(self):
        allSet = True
        if not self.openDataPath.text():
            self.openDataPath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.sumFileSavePath.text():
            self.sumFileSavePath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.betaFileSavePath.text():
            self.betaFileSavePath.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.responseLabel.text():
            self.responseLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.idLabel.text():
            self.idLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.xCoorLabel.text():
            self.xCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.yCoorLabel.text():
            self.yCoorLabel.setStyleSheet("border: 2px solid red;")
            allSet = False
        if not self.localList.count():
            self.localList.setStyleSheet("QListWidget{border: 2px solid red;}")
        
        if self.bwDropdown.currentText() == "Interval Search":
            if not self.bwMin.text():
                self.bwMin.setStyleSheet("border: 2px solid red;")
                allSet = False
            if not self.bwMax.text():
                self.bwMax.setStyleSheet("border: 2px solid red;")
                allSet = False
            if not self.bwInterval.text():
                self.bwInterval.setStyleSheet("border: 2px solid red;")
                allSet = False
        if self.bwDropdown.currentText() == "Pre-defined bandwidth":
            if not self.bwPreDefined.text():
                self.bwPreDefined.setStyleSheet("border: 2px solid red;")
                allSet = False


        return allSet

            
    def loadDataModel(self):
        if 1==1:
        #Load Variables
            self.id = self.data[[self.idLabel.text()]]
            self.data['Intercept'] = 1
            self.yName = self.responseLabel.text()
            self.XNames =  [str(self.localList.item(i).text()) for i in range(self.localList.count())]
            self.y = self.data[[self.responseLabel.text()]]
            self.X = self.data[self.XNames]
            self.xCoor = self.data[[self.xCoorLabel.text()]]
            self.yCoor = self.data[[self.yCoorLabel.text()]]
            self.comp_data = pd.concat([self.id,self.y, self.X, self.xCoor,self.yCoor],axis=1).dropna()
            self.id = self.comp_data[[self.idLabel.text()]].as_matrix().reshape(-1,1)
            self.y = self.comp_data[[self.responseLabel.text()]].as_matrix().reshape(-1,1)
            self.X = self.comp_data[self.XNames].as_matrix()
            self.xCoor = self.comp_data[[self.xCoorLabel.text()]].ix[:,0]
            self.yCoor = self.comp_data[[self.yCoorLabel.text()]].ix[:,0]
            
            self.nObs = len(self.comp_data.index)
            self.nMiss = len(self.data.index) - self.nObs
            self.coords = list(zip(self.xCoor,self.yCoor))
            self.offset = None
            
            
            if self.isPrjCoorRBTN.isChecked():
                self.coorType = False
            if self.isSphCoorRBTN.isChecked():
                self.coorType = True
        
    
            #Load Model Options:

            if self.bwDropdown.currentText() == "Golden Section":
                self.search = 'golden_section'
        
            elif self.bwDropdown.currentText() == "Interval Search":
                self.search = 'interval'
            else:
                self.search = 'preset'

            self.fixed = (self.fixedBox.currentText() == "Fixed")
            self.kernel = self.shapeBox.currentText().lower()
            self.criterion = self.optimCriDropdown.currentText()
            self.isGWR = self.isGWRRBTN.isChecked()
            self.isMGWR = self.isMGWRRBTN.isChecked()
            
            if self.modelTypeDropdown.currentText() == "Gaussian":
                self.family = Gaussian()
            elif self.modelTypeDropdown.currentText() == "Poisson":
                self.family = Poisson()
                self.offset = self.data[[self.OffsetLabel.text()]].as_matrix().reshape(-1,1)
            elif self.modelTypeDropdown.currentText() == "Binomial":
                self.family = Binomial()
            
            #MGWR Advanced Settings
            self.varSTD = self.advUI.varSTD
            if self.varSTD == 'On' and self.isMGWR:
                self.X = (self.X - np.mean(self.X, axis=0)) / np.std(self.X, axis=0)
                self.y = (self.y - np.mean(self.y, axis=0)) / np.std(self.y, axis=0)
                self.X[:,0] = 1
    
            self.SOC = self.advUI.soc
            self.initBeta = self.advUI.init
            self.tol_multi = float(self.advUI.converg)
            self.tol_gwr = 1e-05

            if self.initBeta == "GWR estimate":
                self.init_multi = True
            else:
                self.init_multi = False

            if self.SOC == "SOC-f":
                self.rss_score = False
            else:
                self.rss_score = True
        
        return True
        
    
    def run_onclick(self):
        
        #print(self.advUI.soc,self.advUI.init,self.advUI.converg,self.advUI.varSTD)
        if not self.preCheckEmptyFields():
            err_msg = QtWidgets.QMessageBox.critical(None, "Error", "Please fix inputs in red!")
            
            return
        
        if not self.loadDataModel():
            err_msg = QtWidgets.QMessageBox.critical(None, "Error", "Something wrong when loading variables to model. Please double check you data. No Missing values allowed.")
            return
    


        self.thread.start()

        self.time.start()
        self.timer.start(1000)  # every 10,000 milliseconds
        self.loaderUI.restartTimer()
        self.runningDialog.exec_()
    
    def haha(self):
        self.timer.stop()
        self.runningDialog.close()
        msg = QtWidgets.QMessageBox.information(None, "Success", "Running complete!\nTime Elapsed:\n" + self.elapsedTimeFormatter(self.time))
        
        summaryDlg = QtWidgets.QDialog()
        smyui = Ui_summaryDlg()
        smyui.setupUi(summaryDlg)
        smyui.loadText(self.sumFileSavePath.text())
        summaryDlg.exec_()
    

    
    #Run model
    def runGWR(self):
        
        self.begin_t = datetime.now()
        #self.GLMResult = GLM(self.y,self.X).fit()
        if self.isGWR:
            print ("running GWR")
            if self.search == 'golden_section':
                self.bw = Sel_BW(self.coords,self.y,self.X,kernel=self.kernel,fixed=self.fixed,family=self.family, offset=self.offset,constant=False,spherical=self.coorType).search(search_method='golden_section',criterion=self.criterion)
            
            elif self.search == 'interval':
                min = int(self.bwMin.text())
                max = int(self.bwMax.text())
                step = int(self.bwInterval.text())
                self.bw = Sel_BW(self.coords, self.y, self.X,kernel=self.kernel, fixed=self.fixed,family=self.family,offset=self.offset, constant=False,spherical=self.coorType).search(search_method='interval',bw_min=min,bw_max=max,interval=step,criterion=self.criterion)
                
            else:
                self.bw = int(self.bwPreDefined.text())
            
            self.results = GWR(self.coords, self.y, self.X, self.bw, fixed=self.fixed, kernel=self.kernel, family=self.family,offset=self.offset, constant=False,spherical=self.coorType).fit()
            
            self.end_t = datetime.now()
            outputGWR(self)
            
            """
            try:
                '''
                __init__(self, coords, y, X_loc, X_glob=None, family=Gaussian(),
                offset=None, kernel='bisquare', fixed=False, multi=False, constant=True)
                '''
                bw = Sel_BW(self.coords, self.y, self.X, kernel=self.kernel, fixed=self.fixed, constant = False)
            
                '''
                search(self, search='golden_section', criterion='AICc', bw_min=0.0,
                bw_max=0.0, interval=0.0, tol=1.0e-6, max_iter=200, init_multi=True,
                tol_multi=1.0e-5, rss_score=False, max_iter_multi=200)
                    '''
                bw = bw.search(search=self.search, criterion=self.criterion)
            
                self.results = GWR(self.coords, self.y, self.X, bw, fixed=self.fixed, kernel=self.kernel, constant = False).fit()
                self.saveBetasToCSVGWR(self.results)
                self.end_t = datetime.now()
                summaryGWR(self)
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Something went wrong when running GWR Model. Please double check your settings and data.')
                error_dialog.exec_()
            """
        
        if self.isMGWR:
            print ("running MGWR")
            self.bw = Sel_BW(self.coords, self.y, self.X, fixed=self.fixed,kernel=self.kernel, multi=True,constant=False,spherical=self.coorType)
            self.bws = self.bw.search(search_method='golden_section',criterion=self.criterion, rss_score=self.rss_score, tol_multi=self.tol_multi)
            self.results = MGWR(self.coords, self.y, self.X, self.bw, kernel=self.kernel, fixed=self.fixed,constant=False,spherical=self.coorType).fit()
            self.end_t = datetime.now()
                
            outputMGWR(self)



class AThread(QtCore.QThread):
    def __init__(self, Ui_Dialog, parent=None):
        super(QtCore.QThread, self).__init__()
        self.diag = Ui_Dialog
    def run(self):
        self.diag.runGWR()


class timerThread(QtCore.QThread):
    timeElapsed = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(timerThread, self).__init__(parent)
        self.timeStart = None
    
    def start(self, timeStart):
        self.timeStart = timeStart
        
        return super(timerThread, self).start()
    
    def run(self):
        while self.parent().isRunning():
            self.timeElapsed.emit(time.time() - self.timeStart)
            time.sleep(1)


