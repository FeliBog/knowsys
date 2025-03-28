from platform import uname, architecture
from psutil import *

class Info:
    def __init__(self):
        self.update()

class Processor(Info):
    def update(self):
        self.name = uname().machine
        self.architecture = architecture()[0]
        self.boottime = boot_time()
        freq = cpu_freq()
        self.freq = [freq.current, freq.min, freq.max]
        phys = cpu_count(False)
        logic = cpu_count()
        self.cores = [phys, logic, logic//phys]
        self.percent = cpu_percent()
class RAM(Info):
    def update(self):
        usage = virtual_memory()
        self.total = usage.total
        self.used = usage.used
        self.free = usage.free
        self.percent = usage.percent
class Battery(Info):
    def update(self):
        info = sensors_battery()
        if info.secsleft <= 0: self.discharge = None
        else: self.discharge = info.secsleft
        self.ispower = info.power_plugged

if __name__ == "__main__":
    import time
    battery = Battery()
    while 1:
        battery.update()
        print(f"{battery.discharge} seconds")
        time.sleep(1)