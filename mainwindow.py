# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
import platform
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_form import Ui_MainWindow
from PySide6.QtCore import QTimer
from schedule import scheduleHandling
from music import musicHandling
from utilities import utilitiesHandling 

if platform.system() == "Windows":
    USB_PATH = "C:/Users/gs200/Desktop/Dzwonek"
    AMP_OUTPUT_PIN = 25  # Numer GPIO zgodny z WiringPi (zamiast GPIO numer)

else:
    USB_PATH = "/media/orangepi/"
    AMP_OUTPUT_PIN = 25  # Numer GPIO zgodny z WiringPi (zamiast GPIO numer)


utilities = utilitiesHandling(AMP_OUTPUT_PIN)
scheduleData = scheduleHandling()
music = musicHandling(USB_PATH)

class MainWindow(QMainWindow):
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settingsScheduleIndex = 0
        self.alarmActive = False

        for i, button in enumerate(self.ui.gbtnScreens.buttons()):
            self.ui.gbtnScreens.setId(button,i)
        def changePage(self, button_id):
            self.ui.stackedWidget.setCurrentIndex(button_id)

        self.ui.btnSchedule.pressed.connect(self.updateScheduleSettings)
        self.ui.btnMain.pressed.connect(self.updateOccurencesList)
        self.ui.btnSettings.pressed.connect(self.btnSettings)
        
        self.ui.btnPrev.pressed.connect(self.btnPrev)
        self.ui.btnNext.pressed.connect(self.btnNext)        
        self.ui.btnAdd.pressed.connect(self.btnAdd)
        self.ui.btnSaveChanges.pressed.connect(self.btnSave)
        self.ui.btnDelete.pressed.connect(self.btnDelete)

        self.ui.btnStartAlarm.pressed.connect(self.btnStartAlarm)
        self.ui.btnStartBell.pressed.connect(self.btnStartBell)
        self.ui.btnStartPrebell.pressed.connect(self.btnStartPrebell)
        self.ui.btnWeekendMode.pressed.connect(self.btnWeekendMode)

        timer = QTimer(self)
        timer.timeout.connect(self.clock05s)
        timer.start(500)
        
    def clock05s(self):
        currentTime = datetime.now().strftime("%H:%M")
        self.ui.lblClock.setText(currentTime)
        scheduleData.checkSchedule()
        self.ui.lblNextOccurence.setText(f"Następne wystąpienie: {scheduleData.nextOccurrence}")

    def btnSettings(self):
        self.ui.lblBellFileName.setText(f"Plik dzwonka:\n{music.musicFileNameBell}")
        self.ui.lblPrebellFileName.setText(f"Plik przeddzwonka:\n{music.musicFileNamePrebell}")
        self.ui.lblAlarmFileName.setText(f"Plik alarmu:\n{music.musicFileNameAlarm}")

    def btnPrev(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex-1 if self.settingsScheduleIndex > 1 else len(scheduleData.data["bellSchedule"])-1
        self.updateScheduleSettings()

    def btnNext(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex+1 if self.settingsScheduleIndex < len(scheduleData.data["bellSchedule"])-1 else 0
        self.updateScheduleSettings()
        
    def btnAdd(self):
        scheduleData.addSchedule()
        self.updateScheduleSettings()
            
    def btnDelete(self):
        scheduleData.deleteSchedule(self.settingsScheduleIndex)
        self.updateScheduleSettings()    

    def btnStartAlarm(self):
        if not self.alarmActive:
            utilities.amp_relay(True)
            self.ui.btnStartAlarm.setStyleSheet("QPushButton{background-color: #3030d0}")
            self.ui.btnStartAlarm.setText("Wyłącz alarm")
            music.playAlarm()
            self.alarmActive = True
        else:
            utilities.amp_relay(False)
            self.ui.btnStartAlarm.setStyleSheet("QPushButton{background-color: #ff3300}")
            self.ui.btnStartAlarm.setText("Uruchom alarm")
            music.stopAlarm()
            self.alarmActive = False

    def btnWeekendMode(self):
        if not scheduleData.noWeekend:
            scheduleData.noWeekend = True
            self.ui.btnWeekendMode.setStyleSheet("QPushButton{background-color: #3030d0}")
            self.ui.btnWeekendMode.setText("Wyłącz pracę\nw weekendy")
        else:
            scheduleData.noWeekend = False
            self.ui.btnWeekendMode.setStyleSheet("QPushButton{background-color: #3158de}")
            self.ui.btnWeekendMode.setText("Załącz pracę\nw weekendy")
    

    def btnStartBell(self):
        music.playBell()

    def btnStartPrebell(self):
        music.playPrebell()

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

    def updateScheduleSettings(self):
        index = self.settingsScheduleIndex
        bellNumber = len(scheduleData.data["bellSchedule"])
        active = scheduleData.data["bellActive"][index]
        hour, minute = map(int, scheduleData.data["bellSchedule"][index].split(":"))
        interval = scheduleData.data["prebellIntervals"][index]
        
        self.ui.sboxHour.setValue(hour)
        self.ui.sboxMinute.setValue(minute)
        self.ui.sboxInterval.setValue(interval)
        self.ui.lblScheduleIndex.setText("Dzwonek %d z %d:" %(index+1, bellNumber))
        self.ui.cboxActive.setChecked(active)

    def btnSave(self):
        index = self.settingsScheduleIndex
        hour = self.ui.sboxHour.value()
        minute = self.ui.sboxMinute.value()
        scheduleData.data["bellSchedule"][index] = f"{hour}:{minute}"
        scheduleData.data["bellActive"][index] = self.ui.cboxActive.isChecked()
        scheduleData.data["prebellIntervals"][index] = self.ui.sboxInterval.value()

        print(scheduleData.data["bellSchedule"][index])
        print(scheduleData.data["bellActive"][index])
        print(scheduleData.data["prebellIntervals"][index])
        scheduleData.saveScheduleToJson()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    #widget.showFullScreen()
    sys.exit(app.exec())

