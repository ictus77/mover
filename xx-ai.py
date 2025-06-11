from pynput.mouse import Button, Controller
import time

mouse = Controller()

print('The current pointer position is {0}'.format(mouse.position))

# home page: 
time.sleep(10)
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# uptime
mouse.move(550, 240)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(10)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# remediation
mouse.move(850, 240)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(10)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# incidents
mouse.move(1150, 240)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(10)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# onboarding
mouse.move(1550, 240)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(10)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# best practices
mouse.move(1550, 410)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(20)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# un changes
mouse.move(1550, 580)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(20)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

# backup fail
mouse.move(1150, 750)
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(20)

# home page: 
mouse.position = (100, 130) 
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)