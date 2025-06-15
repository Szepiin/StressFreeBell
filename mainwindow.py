# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
import platform
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QStackedWidget
from ui_form import Ui_MainWindow
from PySide6.QtCore import QTimer, Qt

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

        self.updateOccurrencesList()

        self.ui.btnSchedule.pressed.connect(self.btnSchedule)
        self.ui.btnMain.pressed.connect(self.btnMain)
        self.ui.btnSettings.pressed.connect(self.btnSettings)
        self.ui.btnClock.pressed.connect(self.btnClock)
        
        self.ui.btnPrev.pressed.connect(self.btnPrev)
        self.ui.btnNext.pressed.connect(self.btnNext)        
        self.ui.btnAdd.pressed.connect(self.btnAdd)
        self.ui.btnSaveChanges.pressed.connect(self.btnSave)
        self.ui.btnDelete.pressed.connect(self.btnDelete)

        self.ui.btnStartAlarm.pressed.connect(self.btnStartAlarm)
        self.ui.btnStartBell.pressed.connect(self.btnStartBell)
        self.ui.btnStartPrebell.pressed.connect(self.btnStartPrebell)
        self.ui.btnWeekendMode.pressed.connect(self.btnWeekendMode)

        self.ui.btnClose.pressed.connect(QApplication.quit)

        timer = QTimer(self)
        timer.timeout.connect(self.clock05s)
        timer.start(500)


    def ampRelayHandling(self):
        if scheduleData.timeTo["turnAmpOn"]:
            utilities.amp_relay(True)
        if scheduleData.timeTo["turnAmpOff"]:
            utilities.amp_relay(False)


    def clock05s(self):
        currentTime = datetime.now().strftime("%H:%M")
        self.ui.lblClock.setText(currentTime)
        scheduleData.checkSchedule()
        self.ui.lblNextOccurence.setText(f"Następne wystąpienie: {scheduleData.nextOccurrence}")
        self.ampRelayHandling()


    def show_popup(self, text="Tekst", cancelButton=False):
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #d3d3d3;  /* Szare tło */
                border: 2px solid #a9a9a9; /* Ramka */

            }
            QMessageBox QLabel {
                color: black;             /* Kolor tekstu */
                font-size: 20px;          /* Większa czcionka */

            }
            QMessageBox QPushButton {
                background-color: white;  /* Kolor przycisków */
                color: black;             /* Kolor tekstu na przyciskach */
                font-size: 16px;          /* Czcionka przycisków */
                padding: 10px 15px;        /* Odstępy */
                border: 1px solid #a9a9a9;
                border-radius: 5px;
                width: 60px;
                height: 30px;
            }
        """)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) if cancelButton else msg.setStandardButtons(QMessageBox.Ok)
        msg.button(QMessageBox.Cancel).setText("Anuluj")
        response = msg.exec()
        if response == QMessageBox.Ok:
            return True
        else:
            return False

    def btnSettings(self):
        self.ui.lblBellFileName.setText(f"Plik dzwonka: {music.musicFileNameBell}")
        self.ui.lblPrebellFileName.setText(f"Plik przeddzwonka: {music.musicFileNamePrebell}")
        self.ui.lblAlarmFileName.setText(f"Plik alarmu: {music.musicFileNameAlarm}")
        self.ui.stackedWidget.setCurrentIndex(2)

    def btnMain(self):
        self.updateOccurrencesList()
        self.ui.stackedWidget.setCurrentIndex(0)

    def btnSchedule(self):
        self.updateScheduleSettings()
        self.ui.stackedWidget.setCurrentIndex(1)

    def btnClock(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def btnPrev(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex-1 if self.settingsScheduleIndex >= 1 else len(scheduleData.data["bellSchedule"])-1
        self.updateScheduleSettings()

    def btnNext(self):
        self.settingsScheduleIndex = self.settingsScheduleIndex+1 if self.settingsScheduleIndex < len(scheduleData.data["bellSchedule"])-1 else 0
        self.updateScheduleSettings()
        
    def btnAdd(self):
        scheduleData.addSchedule()
        self.updateScheduleSettings()
            
    def btnDelete(self):
        delScheduleTime = scheduleData.data["bellSchedule"][self.settingsScheduleIndex]
        if self.show_popup(f"Czy na pewno chcesz usunąć dzwonek o {delScheduleTime}?", True):
            scheduleData.deleteSchedule(self.settingsScheduleIndex)
            self.updateScheduleSettings()
            self.show_popup("Dzwonek usunięty", False)
        else:
            self.show_popup("Dzwonek zachowany", False)
            return
        

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
            self.ui.btnWeekendMode.setText("Praca w weekendy\nzałączona")
        else:
            scheduleData.noWeekend = False
            self.ui.btnWeekendMode.setStyleSheet("QPushButton{background-color: #3158de}")
            self.ui.btnWeekendMode.setText("Praca w weekendy\nwyłączona")
    





    def btnStartBell(self):
        music.playBell()

    def btnStartPrebell(self):
        music.playPrebell()

    def updateOccurrencesList(self):
        self.ui.listOccurencesL.clear()
        self.ui.listOccurencesR.clear()
        occurrencesList = []
        for entry in scheduleData.data["bellSchedule"]:
            index = scheduleData.data["bellSchedule"].index(entry)
            occurrencesList.append("Dzwonek %d: %s - %s" %(index+1, scheduleData.data["bellSchedule"][index], "Aktywny" if scheduleData.data["bellActive"][index] else "Nieaktywny"))
        
        for i in range(0, len(occurrencesList), 2):  
            col1 = occurrencesList[i]  
            col2 = occurrencesList[i + 1] if i + 1 < len(occurrencesList) else ""  
            col1a = QListWidgetItem(col1)
            col2a = QListWidgetItem(col2)

            col1a.setTextAlignment(Qt.AlignCenter)
            col2a.setTextAlignment(Qt.AlignCenter)

            self.ui.listOccurencesL.addItem(col1a)
            self.ui.listOccurencesR.addItem(col2a)

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
        self.show_popup("Zapisać zmainy?", False)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.show()
#    widget.showFullScreen()
    sys.exit(app.exec())

