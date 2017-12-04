import explorerhat
import guizero


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


app = guizero.App("Buggy controller")
drive = guizero.PushButton(app, forwards, text="Forwards")
reverse = guizero.PushButton(app, backwards, text="Reverse")
go_left = guizero.PushButton(app, left, text="Left")
go_right = guizero.PushButton(app, right, text="Right")
brake = guizero.PushButton(app, stop, text="Stop")


app.display()
