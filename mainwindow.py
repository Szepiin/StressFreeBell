# This Python file uses the following encoding: utf-8
import sys
import time
import pygame
import os
from datetime import datetime, timedelta
import threading
import platform
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_form import Ui_MainWindow
from PySide6.QtCore import QTimer, QTime, Signal, Qt
from schedule import scheduleHandling

if platform.system() == "Windows":
    USB_PATH = "C:/Users/gs200/Desktop/Dzwonek"
    SCHEDULE_FILE = "Files/schedule.json"
    SAMPLE_MUSIC = "Files/sampleSound.mp3"
else:
    USB_PATH = "/media/orangepi/"
    SCHEDULE_FILE = "/media/orangepi/Bell/schedule.json"
    SAMPLE_MUSIC = "/media/orangepi/Bell/sampleSound.mp3"

    AMP_OUTPUT_PIN = 25  # Numer GPIO zgodny z WiringPi (zamiast GPIO numer)
    os.system(f"gpio mode {AMP_OUTPUT_PIN} out")


scheduleData = scheduleHandling()

class MainWindow(QMainWindow):
    settingsScheduleIndex = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        for i, button in enumerate(self.ui.gbtnScreens.buttons()):
            self.ui.gbtnScreens.setId(button,i)
        def changePage(self, button_id):
            self.ui.stackedWidget.setCurrentIndex(button_id)

        self.ui.btnSchedule.pressed.connect(self.updateScheduleSettings(self.settingsScheduleIndex))
        self.ui.btnMain.pressed.connect(self.updateOccurencesList())
        
        self.ui.btnPrev.pressed.connect(self.btnPrev)
        self.ui.btnNext.pressed.connect(self.btnNext)        
        self.ui.btnAdd.pressed.connect(self.btnAdd)
        self.ui.btnSaveChanges.pressed.connect(scheduleData.saveScheduleToJson())
        self.ui.btnDelete.pressed.connect(self.btnDelete)

        timer = QTimer(self)
        timer.timeout.connect(self.clock05s)
        timer.start(500)

        
    def clock05s(self):
        currentTime = datetime.now().strftime("%H:%M")
        self.ui.lblClock.setText(currentTime)
        self.ui.lblNextOccurence.setText(f"Następne wystąpienie: {scheduleData.nextOccurrence}")


    def btnPrev(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex-1 if self.settingsScheduleIndex > 1 else len(scheduleData.data["bellSchedule"])-1
        self.updateScheduleSettings(self.settingsScheduleIndex)

    def btnNext(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex+1 if self.settingsScheduleIndex < len(scheduleData.data["bellSchedule"])-1 else 0
        self.updateScheduleSettings(self.settingsScheduleIndex)
        
    def btnAdd(self):
        scheduleData.addSchedule()
        self.updateScheduleSettings(self.settingsScheduleIndex)
            
    def btnDelete(self):
        scheduleData.deleteSchedule(self.settingsScheduleIndex)
        self.updateScheduleSettings(self.settingsScheduleIndex)    



    def updateOccurencesList(self):
        self.ui.listOccurencesL.clear()
        self.ui.listOccurencesR.clear()
        ocurrencesList = []
        for entry in scheduleData.data["bellSchedule"]:
            index = scheduleData.data["bellSchedule"].index(entry)
            ocurrencesList.append("Dzwonek %d: %s - %s" %(index+1, scheduleData.data["bellSchedule"][index], "Aktywny" if scheduleData.data["bellActive"][index] else "Nieaktywny"))
        
        for i in range(0, len(ocurrencesList), 2):  
            col1 = ocurrencesList[i]  
            col2 = ocurrencesList[i + 1] if i + 1 < len(ocurrencesList) else ""  
            self.ui.listOccurencesL.addItem(col1)
            self.ui.listOccurencesR.addItem(col2)

    def updateScheduleSettings(self, index):
        bellNumber = len(scheduleData.data["bellSchedule"])
        active = scheduleData.data["bellActive"][index]
        hour, minute = map(int, scheduleData.data["bellSchedule"][index].split(":"))
        interval = scheduleData.data["prebellIntervals"][index]
        
        self.ui.sboxHour.setValue(hour)
        self.ui.sboxMinute.setValue(minute)
        self.ui.sboxInterval.setValue(interval)
        self.ui.lblScheduleIndex.setText("Dzwonek %d z %d:" %(index+1, bellNumber))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

