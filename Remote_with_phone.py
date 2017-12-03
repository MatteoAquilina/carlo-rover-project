import explorerhat
import bluedot


bd = bluedot.BlueDot()

# move function

def move(pos):
    if pos.top:
        forwards()
    elif pos.bottom:
        backwards()
    elif pos.right:
        right()
    elif pos.left:
        left()





# forward function 

def forwards():
    explorerhat.motor.forward(100)
    
#backward function
    
def backwards():
    explorerhat.motor.backward(100)

# left
def left():
    explorerhat.motor.stop()
    explorerhat.motor.one.forward(100)
# right

def right():
    explorerhat.motor.stop()
    explorerhat.motor.two.forward(100)

# stop
def stop():
    explorerhat.motor.stop()




bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop