from datetime import datetime, timedelta
import json
import os

class scheduleHandling:
    def __init__(self):

        self.data = {
            "bellSchedule": [],
            "prebellIntervals": [],
            "bellActive": []
        }

        self.noWeekend = True
        self.nextOccurrence = None
        
        self.timeTo = {
            "turnAmpOn": False,
            "playBell": False,
            "playPrebell": False,
            "turnAmpOff": False
        }

        self.dialogs = {
            "tooManyBells": False,
            "bellAdded": False,
        }

        self._privete_scheduleLocation = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files/schedule.json")

        self._loadScheduleFromJson()
        self.checkSchedule()


    def checkSchedule(self):
        currentTime = datetime.now().strftime("%H:%M")
       
        if self.noWeekend and datetime.now().weekday() >= 5:
            return

        for entry in self.data["bellSchedule"]:
            index = self.data["bellSchedule"].index(entry)
            if self.data["bellActive"][index]:

                bellTime = datetime.strptime(self.data["bellSchedule"][index], "%H:%M")
                prebellTime = bellTime - timedelta(minutes=self.data["prebellIntervals"][index])
                turnAmpOnTime = prebellTime - timedelta(seconds=10)
                turnAmpOffTime = bellTime + timedelta(minutes=1)

                self.timeTo["playBell"] = currentTime == bellTime
                self.timeTo["playPrebell"] = currentTime == prebellTime
                self.timeTo["turnOnAmp"] = currentTime == turnAmpOnTime
                self.timeTo["turnAmpOff"] = currentTime == turnAmpOffTime

                prevBellTimeStrg = self.data["bellSchedule"][index-1] if index >=1 else '00:00'
                bellTimeStrg = self.data["bellSchedule"][index]

        future_times = [t for t in self.data["bellSchedule"] if t > currentTime]
        if future_times:
            self.nextOccurrence = min(future_times)
        else:
            self.nextOccurrence = min(self.data["bellSchedule"])

    def _loadScheduleFromJson(self):
        if os.path.exists(self._privete_scheduleLocation):
            with open(self._privete_scheduleLocation, 'r') as f:
                dataToRead = json.load(f)
                self.data["bellSchedule"] = dataToRead.get('bell_schedule', [])
                self.data["prebellIntervals"] = dataToRead.get('pre_bell_intervals', [])
                self.data["bellActive"] = dataToRead.get('pre_bell_active', [])
                self.noWeekend = dataToRead.get('no_weekend', True)
                

    def saveScheduleToJson(self):
        dataToSave = {
            'bell_schedule': self.data["bellSchedule"],
            'pre_bell_intervals': self.data["prebellIntervals"],
            'pre_bell_active': self.data["bellActive"],
            'no_weekend': self.noWeekend
        }
        with open(self._privete_scheduleLocation, 'w') as f:
            json.dump(dataToSave, f, indent=4)

    def addSchedule(self):
        self.dialogs["toManyBells"] = len(self.data['bellSchedule']) >= 24
        if self.dialogs["toManyBells"]:
            return
        defaultTime = datetime.now().strftime("%H:%M")
        self.data["bellSchedule"].append(defaultTime)
        self.data["prebellIntervals"].append(1)
        self.data["bellActive"].append(True)

        sorted_data = sorted(zip(self.data["bellSchedule"], self.data["prebellIntervals"], self.data["bellActive"]),
                            key=lambda x: datetime.strptime(x[0], "%H:%M"))
        
        self.data["bellSchedule"], self.data["prebellIntervals"], self.data["bellActive"] = (
            list(t) for t in zip(*sorted_data)
        )        

        self.saveScheduleToJson()
        self.dialogs["bellAdded"] = True

    def deleteSchedule(self, index):
        del self.data["bellSchedule"][index]
        del self.data["prebellIntervals"][index]
        del self.data["bellActive"][index]

        self.saveScheduleToJson()

