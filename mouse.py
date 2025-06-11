from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(100, 85)
time.sleep(5)

mouse.press(Button.left)
mouse.release(Button.left)

mouse.move(1727, -56)
time.sleep(3)

mouse.press(Button.left)
mouse.release(Button.left)