# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/denis/Documents/qgis/plugins/qWat/ui_PipeEdit.ui'
#
# Created: Thu Dec  8 14:59:26 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PipeEdit(object):
    def setupUi(self, PipeEdit):
        PipeEdit.setObjectName(_fromUtf8("PipeEdit"))
        PipeEdit.resize(313, 326)
        PipeEdit.setWindowTitle(QtGui.QApplication.translate("PipeEdit", "Pipes", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.browseFrame = QtGui.QFrame(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseFrame.sizePolicy().hasHeightForWidth())
        self.browseFrame.setSizePolicy(sizePolicy)
        self.browseFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.browseFrame.setObjectName(_fromUtf8("browseFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.browseFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.previousButton = QtGui.QPushButton(self.browseFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.previousButton.setText(QtGui.QApplication.translate("PipeEdit", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.gridLayout_2.addWidget(self.previousButton, 0, 0, 1, 1)
        self.fidListCombo = QtGui.QComboBox(self.browseFrame)
        self.fidListCombo.setEditable(True)
        self.fidListCombo.setObjectName(_fromUtf8("fidListCombo"))
        self.gridLayout_2.addWidget(self.fidListCombo, 0, 1, 1, 1)
        self.nextButton = QtGui.QPushButton(self.browseFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.nextButton.setText(QtGui.QApplication.translate("PipeEdit", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.gridLayout_2.addWidget(self.nextButton, 0, 3, 1, 1)
        self.currentPosLabel = QtGui.QLabel(self.browseFrame)
        self.currentPosLabel.setText(QtGui.QApplication.translate("PipeEdit", "0/0", None, QtGui.QApplication.UnicodeUTF8))
        self.currentPosLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentPosLabel.setObjectName(_fromUtf8("currentPosLabel"))
        self.gridLayout_2.addWidget(self.currentPosLabel, 0, 2, 1, 1)
        self.zoomCheck = QtGui.QCheckBox(self.browseFrame)
        self.zoomCheck.setText(QtGui.QApplication.translate("PipeEdit", "zoom to current pipe", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomCheck.setObjectName(_fromUtf8("zoomCheck"))
        self.gridLayout_2.addWidget(self.zoomCheck, 1, 0, 1, 4)
        self.gridLayout_3.addWidget(self.browseFrame, 0, 0, 1, 1)
        self.editTabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.editTabWidget.setEnabled(True)
        self.editTabWidget.setObjectName(_fromUtf8("editTabWidget"))
        self.tab_general = QtGui.QWidget()
        self.tab_general.setObjectName(_fromUtf8("tab_general"))
        self.editTabWidget.addTab(self.tab_general, _fromUtf8(""))
        self.tab_schema = QtGui.QWidget()
        self.tab_schema.setObjectName(_fromUtf8("tab_schema"))
        self.gridLayout = QtGui.QGridLayout(self.tab_schema)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.schemaWidget = QtGui.QWidget(self.tab_schema)
        self.schemaWidget.setEnabled(False)
        self.schemaWidget.setObjectName(_fromUtf8("schemaWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.schemaWidget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.schemaWidget)
        self.label_2.setText(QtGui.QApplication.translate("PipeEdit", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.schema_idParentLineEdit = QtGui.QLineEdit(self.schemaWidget)
        self.schema_idParentLineEdit.setObjectName(_fromUtf8("schema_idParentLineEdit"))
        self.gridLayout_4.addWidget(self.schema_idParentLineEdit, 0, 2, 1, 2)
        self.schema_forceViewCombo = QtGui.QComboBox(self.schemaWidget)
        self.schema_forceViewCombo.setObjectName(_fromUtf8("schema_forceViewCombo"))
        self.schema_forceViewCombo.addItem(_fromUtf8(""))
        self.schema_forceViewCombo.setItemText(0, QtGui.QApplication.translate("PipeEdit", "auto", None, QtGui.QApplication.UnicodeUTF8))
        self.schema_forceViewCombo.addItem(_fromUtf8(""))
        self.schema_forceViewCombo.setItemText(1, QtGui.QApplication.translate("PipeEdit", "visible", None, QtGui.QApplication.UnicodeUTF8))
        self.schema_forceViewCombo.addItem(_fromUtf8(""))
        self.schema_forceViewCombo.setItemText(2, QtGui.QApplication.translate("PipeEdit", "invisible", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_4.addWidget(self.schema_forceViewCombo, 4, 2, 1, 2)
        self.schema_cancelButton = QtGui.QPushButton(self.schemaWidget)
        self.schema_cancelButton.setText(QtGui.QApplication.translate("PipeEdit", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.schema_cancelButton.setObjectName(_fromUtf8("schema_cancelButton"))
        self.gridLayout_4.addWidget(self.schema_cancelButton, 3, 3, 1, 1)
        self.schema_selectButton = QtGui.QPushButton(self.schemaWidget)
        self.schema_selectButton.setText(QtGui.QApplication.translate("PipeEdit", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.schema_selectButton.setObjectName(_fromUtf8("schema_selectButton"))
        self.gridLayout_4.addWidget(self.schema_selectButton, 2, 3, 1, 1)
        self.schema_deleteButton = QtGui.QPushButton(self.schemaWidget)
        self.schema_deleteButton.setText(QtGui.QApplication.translate("PipeEdit", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.schema_deleteButton.setObjectName(_fromUtf8("schema_deleteButton"))
        self.gridLayout_4.addWidget(self.schema_deleteButton, 1, 2, 3, 1)
        self.label_4 = QtGui.QLabel(self.schemaWidget)
        self.label_4.setText(QtGui.QApplication.translate("PipeEdit", "Force view", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.schemaWidget, 0, 0, 1, 2)
        self.editTabWidget.addTab(self.tab_schema, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.editTabWidget, 2, 0, 1, 1)
        PipeEdit.setWidget(self.dockWidgetContents)

        self.retranslateUi(PipeEdit)
        self.editTabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.schema_deleteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.schema_idParentLineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(PipeEdit)

    def retranslateUi(self, PipeEdit):
        self.editTabWidget.setTabText(self.editTabWidget.indexOf(self.tab_general), QtGui.QApplication.translate("PipeEdit", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.editTabWidget.setTabText(self.editTabWidget.indexOf(self.tab_schema), QtGui.QApplication.translate("PipeEdit", "Schema", None, QtGui.QApplication.UnicodeUTF8))

