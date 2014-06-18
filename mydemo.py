import cd 
import time

d = cd.Drone()
d.team_name = "will"
d.takeoff()
d.turn_right()
d.move_forward()
d.move_forward()
p = d.image
d.save_photo(p)
d.move_down()
d.move_right()
p2 = d.image
d.save_photo(p2)

d.move_backward()

d.land()


d.halt()
