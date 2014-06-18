#!/usr/bin/env python

# Copyright (c) 2014 Will Webberley / Cardiff University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# This module is designed to provide a further wrapper to the libardrone.py 
# module, for the purposes of being used in undergraudate recruitment
# and engagement for the School of Computer Science & Informatics at
# Cardiff University.
#
# More specifically, it allows the drone to be controlled more programmatically,
# by only running commands for a short period of time, rather than indefinitely
# after the method is called.
# This is achieved by sleeping the thread for a short time after each command,
# and then returning the drone to a hovering state. 
# For example, if drone.move_forward() is called, the drone will move forwards
# for a short while before returning to hover. The thread will block while
# moving forwards so several commands one after another have time to execute.
#
# This class is very ugly and hacked together quickly. 
# Read on at your own risk (please don't).


import libardrone
import sqlite3, uuid, inspect
from time import sleep, time
from PIL import Image


class Drone(libardrone.ARDrone):
    def __init__(self):
        super(Drone, self).__init__()
        self.trial_id = uuid.uuid4()
        self.team_name = "demo"
        self.photo_count = 0
        self.speed = 0.25
        try:
            frame = inspect.stack()[1]
            self.module = inspect.getmodule(frame[0]).__file__
            self.code_lines = self.get_line_count()
        except:
            pass
        self.start_time = int(time())

    def get_line_count(self):
        source = open(self.module, "r")
        lines = source.readlines()
        count = 0   
        for line in lines:
            if line.strip() != "":
                count += 1
        return count
        
    def sleep(self):
        sleep(1)
        super(Drone, self).hover()
        sleep(0.2)

    def take_photo(self):
        return self.image   
        self.photo = ""
        while self.photo != "" or self.photo != None:
            self.photo = self.image
        return self.photo
        

    def save_photo(self, photo):
        if photo == None:
            return
        #try:
        dim = (320,240)
        pimg = Image.fromstring('RGB', dim, photo)
        pimg.save("%s.png" % (str(self.team_name)+"_"+str(self.trial_id)+"_"+str(self.photo_count+1)))    
        self.photo_count += 1
        #except Exception:
         #   print Exception
         #   return
    
    def record_trial(self):
        con = sqlite3.connect("results.db")
        c = con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS results(team_name TEXT, photo_count INT, time INT, code_lines INT, attempt INT, attempt_id TEXT)")
        previous_results = len(c.execute("SELECT time FROM results WHERE team_name = ?", [self.team_name]).fetchall())
        c.execute("INSERT INTO results VALUES(?,?,?,?,?,?)", [self.team_name, self.photo_count, self.time_taken, self.code_lines, previous_results, str(self.trial_id)])
        con.commit()
        con.close()

    def halt(self):
        self.end_time = int(time())
        self.time_taken = self.end_time - self.start_time
        if self.team_name != 'demo':
            self.record_trial()
        super(Drone, self).halt()

    def takeoff(self):
        super(Drone, self).takeoff()
        sleep(5)
    
    def move_forward(self):
        super(Drone, self).move_forward()
        sleep(1.0)
        super(Drone, self).hover()
        sleep(2)

    def move_backward(self):
        super(Drone, self).move_backward()
        sleep(1.0)
        super(Drone, self).hover()
        sleep(2)

    def move_left(self):
        super(Drone, self).move_left()
        sleep(1.0)
        self.sleep()

    def move_right(self):
        super(Drone, self).move_right()
        sleep(1.0)
        self.sleep()

    def turn_left(self):
        self.speed = 0.6
        super(Drone, self).turn_left()
        sleep(1)
        super(Drone, self).hover()
        self.speed = 0.2

    def turn_right(self):
        self.speed = 0.9
        super(Drone, self).turn_right()
        sleep(1.2)
        super(Drone, self).hover()
        self.speed = 0.2

    def move_up(self):
        super(Drone, self).move_up()
        self.sleep()

    def move_down(self):
        super(Drone, self).move_down()
        self.sleep()
