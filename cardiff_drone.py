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
from time import sleep


class Drone(libardrone.ARDrone):
    def __init__(self):
        super(Drone, self).__init__()
        x=2
    
    def sleep(self):
        sleep(0.5)
    
    def move_forward(self):
        super(Drone, self).move_forward()
        self.sleep()
        super(Drone, self).hover()  

    def move_backward(self):
        super(Drone, self).move_backward()
        self.sleep()
        super(Drone, self).hover()

    def move_left(self):
        super(Drone, self).move_left()
        self.sleep()
        super(Drone, self).hover()

    def move_right(self):
        super(Drone, self).move_right()
        self.sleep()
        super(Drone, self).hover()

    def turn_left(self):
        super(Drone, self).turn_left()
        self.sleep()
        super(Drone, self).hover()

    def turn_right(self):
        super(Drone, self).turn_right()
        self.sleep()
        super(Drone, self).hover()


    def move_up(self):
        super(Drone, self).move_up()
        self.sleep()
        super(Drone, self).hover()

    def move_down(self):
        super(Drone, self).move_down()
        self.sleep()
        super(Drone, self).hover()

