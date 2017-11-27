"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Vikram Hari.
"""
########################################################################
# TODO: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

bigTurtle = rg.SimpleTurtle('turtle')
bigTurtle.Pen = rg.Pen('midnight blue', 3)
bigTurtle.speed = 10

smallTurtle = rg.SimpleTurtle()
smallTurtle.Pen = rg.Pen('midnight blue', 7)
smallTurtle.speed = 20

size = 200

for k in range(18):
    bigTurtle.draw_square(size)

    bigTurtle.pen_up()
    bigTurtle.forward(20)

    bigTurtle.pen_down()
    size = size - 12

window.close_on_mouse_click()
