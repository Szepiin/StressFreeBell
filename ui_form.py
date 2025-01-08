# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QCheckBox, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QSize(800, 480))
        MainWindow.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        MainWindow.setTabletTracking(True)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow, QWidget {\n"
"    background-color: #2b2b2b; /* T\u0142o ciemnoszare */\n"
"    color: #ffffff; /* Kolor tekstu bia\u0142y */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3158de; /* Ciemnoszare t\u0142o */\n"
"    color: #ffffff; /* Bia\u0142y tekst */\n"
"    border: 1px solid #3158b3; /* Szara ramka */\n"
"    border-radius: 5px; /* Zaokr\u0105glone rogi */\n"
"    padding: 5px; /* Wewn\u0119trzne odst\u0119py */\n"
"}\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 70, 800, 411))
        self.stackedWidget.setStyleSheet(u"QMainWindow, QWidget {\n"
"    background-color: #1f1f1f; /* T\u0142o ciemnoszare */\n"
"    color: #ffffff; /* Kolor tekstu bia\u0142y */\n"
"}\n"
"QPushButton {\n"
"    background-color: #3158de; /* Ciemnoszare t\u0142o */\n"
"    color: #ffffff; /* Bia\u0142y tekst */\n"
"    border: 1px solid #3158b3; /* Szara ramka */\n"
"    border-radius: 5px; /* Zaokr\u0105glone rogi */\n"
"    padding: 5px; /* Wewn\u0119trzne odst\u0119py */\n"
"}")
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"QFrame {\n"
"    color: #ffffff; /* Bia\u0142y tekst */\n"
"    background-color: #252525;\n"
"    border: 1px solid #454545; /* Szara ramka */\n"
"    border-radius: 5px; /* Zaokr\u0105glone rogi */\n"
"}")
        self.lblNextOccurence = QLabel(self.Main)
        self.lblNextOccurence.setObjectName(u"lblNextOccurence")
        self.lblNextOccurence.setGeometry(QRect(9, 5, 781, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblNextOccurence.setFont(font)
        self.lblNextOccurence.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblNextOccurence.setAutoFillBackground(False)
        self.lblNextOccurence.setFrameShape(QFrame.Shape.NoFrame)
        self.lblNextOccurence.setFrameShadow(QFrame.Shadow.Plain)
        self.lblNextOccurence.setLineWidth(0)
        self.lblNextOccurence.setMidLineWidth(0)
        self.lblNextOccurence.setTextFormat(Qt.TextFormat.AutoText)
        self.lblNextOccurence.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listOccurencesR = QListWidget(self.Main)
        self.listOccurencesR.setObjectName(u"listOccurencesR")
        self.listOccurencesR.setGeometry(QRect(405, 50, 386, 351))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.listOccurencesR.setFont(font1)
        self.listOccurencesR.viewport().setProperty("cursor", QCursor(Qt.CursorShape.BlankCursor))
        self.listOccurencesR.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listOccurencesR.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.listOccurencesR.setFrameShape(QFrame.Shape.Box)
        self.listOccurencesR.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listOccurencesR.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listOccurencesR.setAutoScroll(False)
        self.listOccurencesR.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listOccurencesR.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listOccurencesR.setItemAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listOccurencesL = QListWidget(self.Main)
        self.listOccurencesL.setObjectName(u"listOccurencesL")
        self.listOccurencesL.setGeometry(QRect(10, 50, 386, 351))
        self.listOccurencesL.setFont(font1)
        self.listOccurencesL.viewport().setProperty("cursor", QCursor(Qt.CursorShape.BlankCursor))
        self.listOccurencesL.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listOccurencesL.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.listOccurencesL.setFrameShape(QFrame.Shape.Box)
        self.listOccurencesL.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listOccurencesL.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listOccurencesL.setAutoScroll(False)
        self.listOccurencesL.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listOccurencesL.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.listOccurencesL.setItemAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.stackedWidget.addWidget(self.Main)
        self.Schedule = QWidget()
        self.Schedule.setObjectName(u"Schedule")
        self.Schedule.setStyleSheet(u"QFrame {\n"
"    color: #ffffff; /* Bia\u0142y tekst */\n"
"    background-color: #252525;\n"
"    border: 1px solid #454545; /* Szara ramka */\n"
"    border-radius: 5px; /* Zaokr\u0105glone rogi */\n"
"}\n"
"QLabel{\n"
"    background-color: #252525;\n"
"    border: 1px solid #454545; /* Szara ramka */\n"
"    border-radius: 10px; /* Zaokr\u0105glone rogi */\n"
"}")
        self.lblScheduleIndex = QLabel(self.Schedule)
        self.lblScheduleIndex.setObjectName(u"lblScheduleIndex")
        self.lblScheduleIndex.setGeometry(QRect(0, 5, 800, 41))
        self.lblScheduleIndex.setFont(font)
        self.lblScheduleIndex.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblScheduleIndex.setAutoFillBackground(False)
        self.lblScheduleIndex.setFrameShape(QFrame.Shape.NoFrame)
        self.lblScheduleIndex.setFrameShadow(QFrame.Shadow.Plain)
        self.lblScheduleIndex.setLineWidth(0)
        self.lblScheduleIndex.setMidLineWidth(0)
        self.lblScheduleIndex.setTextFormat(Qt.TextFormat.AutoText)
        self.lblScheduleIndex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameBellIndex = QFrame(self.Schedule)
        self.frameBellIndex.setObjectName(u"frameBellIndex")
        self.frameBellIndex.setGeometry(QRect(0, 340, 800, 70))
        self.frameBellIndex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameBellIndex.setFrameShadow(QFrame.Shadow.Raised)
        self.btnPrev = QPushButton(self.frameBellIndex)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setGeometry(QRect(10, 10, 190, 50))
        self.btnPrev.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.btnPrev.setFont(font2)
        self.btnNext = QPushButton(self.frameBellIndex)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(600, 10, 190, 50))
        self.btnNext.setMinimumSize(QSize(0, 50))
        self.btnNext.setFont(font2)
        self.frame = QFrame(self.Schedule)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(590, 50, 210, 286))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btnSaveChanges = QPushButton(self.frame)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnSaveChanges)
        self.btnSaveChanges.setObjectName(u"btnSaveChanges")
        self.btnSaveChanges.setGeometry(QRect(10, 130, 190, 50))
        self.btnSaveChanges.setMinimumSize(QSize(0, 50))
        self.btnSaveChanges.setFont(font2)
        self.btnAdd = QPushButton(self.frame)
        self.buttonGroup.addButton(self.btnAdd)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(10, 10, 190, 50))
        self.btnAdd.setMinimumSize(QSize(0, 50))
        self.btnAdd.setFont(font2)
        self.btnDelete = QPushButton(self.frame)
        self.buttonGroup.addButton(self.btnDelete)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(10, 70, 190, 50))
        self.btnDelete.setMinimumSize(QSize(0, 50))
        self.btnDelete.setFont(font2)
        self.frameParameters = QFrame(self.Schedule)
        self.frameParameters.setObjectName(u"frameParameters")
        self.frameParameters.setGeometry(QRect(0, 50, 586, 286))
        self.frameParameters.setStyleSheet(u"QToolButton {\n"
"	background-color: rgb(55,55,55);\n"
"    color: #ffffff; /* Bia\u0142y tekst */\n"
"    border: 4px solid #3158de;; /* Szara ramka */\n"
"    border-radius: 10px; /* Zaokr\u0105glone rogi */\n"
"    padding: 0px; /* Wewn\u0119trzne odst\u0119py */\n"
"}\n"
"QLabel{\n"
" border: 0px solid #3158b3; /* Szara ramka */\n"
" background: #303030;\n"
"}")
        self.frameParameters.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameters.setFrameShadow(QFrame.Shadow.Raised)
        self.frameHour = QFrame(self.frameParameters)
        self.frameHour.setObjectName(u"frameHour")
        self.frameHour.setGeometry(QRect(190, 5, 391, 141))
        self.frameHour.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: 3px solid #3158de;\n"
"    padding-right: 8px;\n"
"    padding-left: 8px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"    border-radius: 5px; \n"
"	background: #303030;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    width:40px;\n"
"    height: 40px;\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    width:40px;\n"
"    height: 40px;\n"
"}\n"
"")
        self.frameHour.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHour.setFrameShadow(QFrame.Shadow.Raised)
        self.lblHour = QLabel(self.frameHour)
        self.lblHour.setObjectName(u"lblHour")
        self.lblHour.setGeometry(QRect(20, 50, 81, 41))
        self.lblHour.setFont(font)
        self.lblHour.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblHour.setAutoFillBackground(False)
        self.lblHour.setStyleSheet(u"QLabel{\n"
" border: 0px solid #3158b3; /* Szara ramka */\n"
"}")
        self.lblHour.setFrameShape(QFrame.Shape.NoFrame)
        self.lblHour.setFrameShadow(QFrame.Shadow.Plain)
        self.lblHour.setLineWidth(0)
        self.lblHour.setMidLineWidth(0)
        self.lblHour.setTextFormat(Qt.TextFormat.AutoText)
        self.lblHour.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMinute = QLabel(self.frameHour)
        self.lblMinute.setObjectName(u"lblMinute")
        self.lblMinute.setGeometry(QRect(210, 50, 81, 41))
        self.lblMinute.setFont(font)
        self.lblMinute.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblMinute.setAutoFillBackground(False)
        self.lblMinute.setStyleSheet(u"QLabel{\n"
" border: 0px solid #3158b3; /* Szara ramka */\n"
"}")
        self.lblMinute.setFrameShape(QFrame.Shape.NoFrame)
        self.lblMinute.setFrameShadow(QFrame.Shadow.Plain)
        self.lblMinute.setLineWidth(0)
        self.lblMinute.setMidLineWidth(0)
        self.lblMinute.setTextFormat(Qt.TextFormat.AutoText)
        self.lblMinute.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sboxHour = QSpinBox(self.frameHour)
        self.sboxHour.setObjectName(u"sboxHour")
        self.sboxHour.setGeometry(QRect(10, 10, 181, 121))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.sboxHour.setFont(font3)
        self.sboxHour.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.sboxHour.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sboxHour.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.sboxHour.setStyleSheet(u"")
        self.sboxHour.setWrapping(False)
        self.sboxHour.setFrame(False)
        self.sboxHour.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sboxHour.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sboxHour.setKeyboardTracking(False)
        self.sboxHour.setProperty("showGroupSeparator", False)
        self.sboxHour.setMaximum(23)
        self.sboxMinute = QSpinBox(self.frameHour)
        self.sboxMinute.setObjectName(u"sboxMinute")
        self.sboxMinute.setGeometry(QRect(200, 10, 181, 121))
        self.sboxMinute.setFont(font3)
        self.sboxMinute.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.sboxMinute.setStyleSheet(u"")
        self.sboxMinute.setWrapping(False)
        self.sboxMinute.setFrame(False)
        self.sboxMinute.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sboxMinute.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sboxMinute.setKeyboardTracking(False)
        self.sboxMinute.setProperty("showGroupSeparator", False)
        self.sboxMinute.setMaximum(59)
        self.sboxHour.raise_()
        self.sboxMinute.raise_()
        self.lblMinute.raise_()
        self.lblHour.raise_()
        self.frameActive = QFrame(self.frameParameters)
        self.frameActive.setObjectName(u"frameActive")
        self.frameActive.setGeometry(QRect(5, 5, 181, 276))
        self.frameActive.setStyleSheet(u"")
        self.frameActive.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameActive.setFrameShadow(QFrame.Shadow.Raised)
        self.cboxActive = QCheckBox(self.frameActive)
        self.cboxActive.setObjectName(u"cboxActive")
        self.cboxActive.setGeometry(QRect(30, 120, 131, 51))
        self.cboxActive.setFont(font2)
        self.cboxActive.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cboxActive.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.cboxActive.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"	border: 4px solid #3158de;\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6363fc;\n"
" \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: #303030;\n"
"\n"
"}\n"
"\n"
"QCheckBox{\n"
"background-color: #252525;\n"
"}\n"
"\n"
"\n"
"/*\n"
"           QCheckBox::indicator {\n"
"                width: 40px;\n"
"                height: 40px;\n"
"border: 4px solid #3158de;\n"
"background-color: #202020;\n"
"    border-radius: 10px; \n"
"            }\n"
"           QCheckBox::indicator :checked{\n"
"                width: 40px;\n"
"                height: 40px;\n"
"border: 4px solid #3158de;\n"
"background-color: #202020;\n"
"    border-radius: 10px; \n"
"            }\n"
"     QCheckBox::indicator :unchecked{\n"
"                width: 40px;\n"
"                height: 40px;\n"
"border: 4px solid #3158de;\n"
"background-color: #505050;\n"
"    border-radius: 10px; \n"
""
                        "            }*/\n"
"")
        self.cboxActive.setCheckable(True)
        self.cboxActive.setChecked(False)
        self.frameInterval = QFrame(self.frameParameters)
        self.frameInterval.setObjectName(u"frameInterval")
        self.frameInterval.setGeometry(QRect(190, 150, 391, 131))
        self.frameInterval.setStyleSheet(u"")
        self.frameInterval.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInterval.setFrameShadow(QFrame.Shadow.Raised)
        self.lblInterval = QLabel(self.frameInterval)
        self.lblInterval.setObjectName(u"lblInterval")
        self.lblInterval.setGeometry(QRect(20, 20, 261, 91))
        self.lblInterval.setFont(font)
        self.lblInterval.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblInterval.setAutoFillBackground(False)
        self.lblInterval.setStyleSheet(u"")
        self.lblInterval.setFrameShape(QFrame.Shape.NoFrame)
        self.lblInterval.setFrameShadow(QFrame.Shadow.Plain)
        self.lblInterval.setLineWidth(0)
        self.lblInterval.setMidLineWidth(0)
        self.lblInterval.setTextFormat(Qt.TextFormat.AutoText)
        self.lblInterval.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblInterval.setWordWrap(True)
        self.sboxInterval = QDoubleSpinBox(self.frameInterval)
        self.sboxInterval.setObjectName(u"sboxInterval")
        self.sboxInterval.setGeometry(QRect(10, 10, 371, 111))
        self.sboxInterval.setFont(font3)
        self.sboxInterval.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.sboxInterval.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sboxInterval.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.sboxInterval.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"    border: 3px solid #3158de;\n"
"    padding-right: 8px;\n"
"    padding-left: 8px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"    border-radius: 5px; \n"
"	background: #303030;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    width:40px;\n"
"    height: 40px;\n"
"\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    width:40px;\n"
"    height: 40px;\n"
"}\n"
"")
        self.sboxInterval.setFrame(False)
        self.sboxInterval.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sboxInterval.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sboxInterval.setKeyboardTracking(False)
        self.sboxInterval.setDecimals(1)
        self.sboxInterval.setMinimum(0.500000000000000)
        self.sboxInterval.setMaximum(2.000000000000000)
        self.sboxInterval.setSingleStep(0.500000000000000)
        self.sboxInterval.raise_()
        self.lblInterval.raise_()
        self.stackedWidget.addWidget(self.Schedule)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.btnWeekendMode = QPushButton(self.Settings)
        self.btnWeekendMode.setObjectName(u"btnWeekendMode")
        self.btnWeekendMode.setGeometry(QRect(300, 310, 201, 61))
        self.btnWeekendMode.setMinimumSize(QSize(0, 50))
        self.btnWeekendMode.setFont(font2)
        self.btnWeekendMode.setStyleSheet(u"")
        self.btnWeekendMode.setCheckable(True)
        self.btnWeekendMode.setChecked(True)
        self.btnStartBell = QPushButton(self.Settings)
        self.btnStartBell.setObjectName(u"btnStartBell")
        self.btnStartBell.setGeometry(QRect(300, 230, 201, 61))
        self.btnStartBell.setMinimumSize(QSize(0, 50))
        self.btnStartBell.setFont(font2)
        self.btnStartPrebell = QPushButton(self.Settings)
        self.btnStartPrebell.setObjectName(u"btnStartPrebell")
        self.btnStartPrebell.setGeometry(QRect(300, 150, 201, 61))
        self.btnStartPrebell.setMinimumSize(QSize(0, 50))
        self.btnStartPrebell.setFont(font2)
        self.btnStartAlarm = QPushButton(self.Settings)
        self.btnStartAlarm.setObjectName(u"btnStartAlarm")
        self.btnStartAlarm.setGeometry(QRect(260, 20, 281, 101))
        self.btnStartAlarm.setMinimumSize(QSize(0, 50))
        self.btnStartAlarm.setFont(font2)
        self.btnStartAlarm.setStyleSheet(u"QPushButton{\n"
"background-color: #ff3300\n"
"}")
        self.lblBellFileName = QLabel(self.Settings)
        self.lblBellFileName.setObjectName(u"lblBellFileName")
        self.lblBellFileName.setGeometry(QRect(550, 230, 201, 61))
        self.lblBellFileName.setFont(font)
        self.lblBellFileName.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblBellFileName.setAutoFillBackground(False)
        self.lblBellFileName.setFrameShape(QFrame.Shape.NoFrame)
        self.lblBellFileName.setFrameShadow(QFrame.Shadow.Plain)
        self.lblBellFileName.setLineWidth(0)
        self.lblBellFileName.setMidLineWidth(0)
        self.lblBellFileName.setTextFormat(Qt.TextFormat.AutoText)
        self.lblBellFileName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblPrebellFileName = QLabel(self.Settings)
        self.lblPrebellFileName.setObjectName(u"lblPrebellFileName")
        self.lblPrebellFileName.setGeometry(QRect(550, 150, 201, 61))
        self.lblPrebellFileName.setFont(font)
        self.lblPrebellFileName.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblPrebellFileName.setAutoFillBackground(False)
        self.lblPrebellFileName.setFrameShape(QFrame.Shape.NoFrame)
        self.lblPrebellFileName.setFrameShadow(QFrame.Shadow.Plain)
        self.lblPrebellFileName.setLineWidth(0)
        self.lblPrebellFileName.setMidLineWidth(0)
        self.lblPrebellFileName.setTextFormat(Qt.TextFormat.AutoText)
        self.lblPrebellFileName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblAlarmFileName = QLabel(self.Settings)
        self.lblAlarmFileName.setObjectName(u"lblAlarmFileName")
        self.lblAlarmFileName.setGeometry(QRect(540, 40, 201, 61))
        self.lblAlarmFileName.setFont(font)
        self.lblAlarmFileName.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblAlarmFileName.setAutoFillBackground(False)
        self.lblAlarmFileName.setFrameShape(QFrame.Shape.NoFrame)
        self.lblAlarmFileName.setFrameShadow(QFrame.Shadow.Plain)
        self.lblAlarmFileName.setLineWidth(0)
        self.lblAlarmFileName.setMidLineWidth(0)
        self.lblAlarmFileName.setTextFormat(Qt.TextFormat.AutoText)
        self.lblAlarmFileName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.Settings)
        self.Clock = QWidget()
        self.Clock.setObjectName(u"Clock")
        self.Clock.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblClock = QLabel(self.Clock)
        self.lblClock.setObjectName(u"lblClock")
        self.lblClock.setGeometry(QRect(0, 60, 801, 191))
        font4 = QFont()
        font4.setPointSize(100)
        font4.setWeight(QFont.Medium)
        font4.setStyleStrategy(QFont.PreferDefault)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.lblClock.setFont(font4)
        self.lblClock.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnPlusHour = QToolButton(self.Clock)
        self.btnPlusHour.setObjectName(u"btnPlusHour")
        self.btnPlusHour.setGeometry(QRect(250, 50, 111, 41))
        self.btnPlusHour.setFont(font)
        self.btnPlusHour.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.btnPlusHour.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btnPlusHour.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.btnMinusHour = QToolButton(self.Clock)
        self.btnMinusHour.setObjectName(u"btnMinusHour")
        self.btnMinusHour.setGeometry(QRect(250, 240, 111, 41))
        self.btnMinusHour.setFont(font)
        self.btnMinusHour.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.btnMinusHour.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btnMinusHour.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.btnPlusMinute = QToolButton(self.Clock)
        self.btnPlusMinute.setObjectName(u"btnPlusMinute")
        self.btnPlusMinute.setGeometry(QRect(440, 50, 111, 41))
        self.btnPlusMinute.setFont(font)
        self.btnPlusMinute.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.btnPlusMinute.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btnPlusMinute.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.btnPlusMinute.setCheckable(False)
        self.btnPlusMinute.setChecked(False)
        self.btnPlusMinute.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btnPlusMinute.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.btnPlusMinute.setAutoRaise(False)
        self.btnPlusMinute.setArrowType(Qt.ArrowType.NoArrow)
        self.btnMinusMinute = QToolButton(self.Clock)
        self.btnMinusMinute.setObjectName(u"btnMinusMinute")
        self.btnMinusMinute.setGeometry(QRect(440, 240, 111, 41))
        self.btnMinusMinute.setFont(font)
        self.btnMinusMinute.setCursor(QCursor(Qt.CursorShape.BlankCursor))
        self.btnMinusMinute.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btnMinusMinute.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.btnSaveClock = QPushButton(self.Clock)
        self.btnSaveClock.setObjectName(u"btnSaveClock")
        self.btnSaveClock.setGeometry(QRect(305, 350, 190, 50))
        self.btnSaveClock.setMinimumSize(QSize(0, 50))
        self.btnSaveClock.setFont(font2)
        self.stackedWidget.addWidget(self.Clock)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 781, 61))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMain = QPushButton(self.layoutWidget)
        self.gbtnScreens = QButtonGroup(MainWindow)
        self.gbtnScreens.setObjectName(u"gbtnScreens")
        self.gbtnScreens.addButton(self.btnMain)
        self.btnMain.setObjectName(u"btnMain")
        self.btnMain.setMinimumSize(QSize(0, 50))
        self.btnMain.setFont(font2)

        self.horizontalLayout.addWidget(self.btnMain)

        self.btnSchedule = QPushButton(self.layoutWidget)
        self.gbtnScreens.addButton(self.btnSchedule)
        self.btnSchedule.setObjectName(u"btnSchedule")
        self.btnSchedule.setMinimumSize(QSize(0, 50))
        self.btnSchedule.setFont(font2)

        self.horizontalLayout.addWidget(self.btnSchedule)

        self.btnSettings = QPushButton(self.layoutWidget)
        self.gbtnScreens.addButton(self.btnSettings)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(0, 50))
        self.btnSettings.setFont(font2)

        self.horizontalLayout.addWidget(self.btnSettings)

        self.btnClock = QPushButton(self.layoutWidget)
        self.gbtnScreens.addButton(self.btnClock)
        self.btnClock.setObjectName(u"btnClock")
        self.btnClock.setMinimumSize(QSize(0, 50))
        self.btnClock.setFont(font2)

        self.horizontalLayout.addWidget(self.btnClock)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.gbtnScreens.idClicked.connect(self.stackedWidget.setCurrentIndex)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblNextOccurence.setText(QCoreApplication.translate("MainWindow", u"Brak nast\u0119pnego wyst\u0105pienia", None))
        self.lblScheduleIndex.setText(QCoreApplication.translate("MainWindow", u"Dzwonek", None))
        self.btnPrev.setText(QCoreApplication.translate("MainWindow", u"Poprzedni", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pny", None))
        self.btnSaveChanges.setText(QCoreApplication.translate("MainWindow", u"Zapisz zmiany", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Dodaj dzwonek", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 dzwonek", None))
        self.lblHour.setText(QCoreApplication.translate("MainWindow", u"Godzina:", None))
        self.lblMinute.setText(QCoreApplication.translate("MainWindow", u"Minuta:", None))
        self.cboxActive.setText(QCoreApplication.translate("MainWindow", u"Aktywny", None))
        self.lblInterval.setText(QCoreApplication.translate("MainWindow", u"Interwa\u0142 mi\u0119dzy dzwonkiem \n"
" a przeddzwonkiem:", None))
        self.btnWeekendMode.setText(QCoreApplication.translate("MainWindow", u"Prze\u0142\u0105cz\n"
"tryb weekendowy", None))
        self.btnStartBell.setText(QCoreApplication.translate("MainWindow", u"Uruchom dzwonek", None))
        self.btnStartPrebell.setText(QCoreApplication.translate("MainWindow", u"Uruchom \n"
" przeddzwonek", None))
        self.btnStartAlarm.setText(QCoreApplication.translate("MainWindow", u"Uruchom alarm", None))
        self.lblBellFileName.setText(QCoreApplication.translate("MainWindow", u"Dzwonek:\n"
"", None))
        self.lblPrebellFileName.setText(QCoreApplication.translate("MainWindow", u"Przedzwonek:\n"
"", None))
        self.lblAlarmFileName.setText(QCoreApplication.translate("MainWindow", u"Alarm:\n"
"", None))
        self.lblClock.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.btnPlusHour.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnMinusHour.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnPlusMinute.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnMinusMinute.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnSaveClock.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.btnMain.setText(QCoreApplication.translate("MainWindow", u"Ekran g\u0142\u00f3wny", None))
        self.btnSchedule.setText(QCoreApplication.translate("MainWindow", u"Harmonogram", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.btnClock.setText(QCoreApplication.translate("MainWindow", u"Zegar", None))
    # retranslateUi

