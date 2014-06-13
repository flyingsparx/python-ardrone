import libardrone
from time import sleep

# This class is very ugly and hacked together quickly.
# Read on at your own risk (please don't).

class Drone(libardrone.ARDrone):
    def __init__(self):
        super(Drone, self).__init__()
    
    def sleep(self):
        sleep(0.5)
    
    def __getattr__(self, name):
        super(Drone, self).getattr(name)()
        print type(name)
        return None
        if name != 'land()' and name != 'halt()':
            self.sleep()
            super(Drone, self).hover()
        return None 
