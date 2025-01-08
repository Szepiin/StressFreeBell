import datetime
import os
import platform


class utilitiesHandling:
    def __init__(self, AMP_OUTPUT_PIN):
        self._ampOutputPin = AMP_OUTPUT_PIN

    def set_system_time(self, hour, minute):     
        now = datetime.now()
        new_time = now.replace(hour=int(hour), minute=int(minute))
        
        if platform.system() == "Windows":
            os.system(f"time {new_time.strftime('%H:%M')}")
        else:
            os.system(f"sudo date +%T -s \"{new_time.strftime('%H:%M')}\"")

    def is_time_valid(self):
        now = datetime.now()
        min_valid_date = datetime(2025, 1, 1)
        return now > min_valid_date

    def amp_relay(self, state):
        if platform.system() == "Windows":
            print(f"Relay state: {state}")
        else:
            os.system(f"gpio mode {self._ampOutputPin} out")
            os.system(f"gpio write {self._ampOutputPin} {state}")
