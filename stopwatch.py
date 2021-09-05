# Python Project: Stopwatch

import simplegui
# define global variables
interval = 100
counter = 0
calcounter = 0
correct = 0

# define helper function format that converts time
    
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    counter2 =counter%600
    
    A = str(counter//600)
    B = str(counter2//100)
    counter4 = str(counter2//10)
    counter3 = str(counter2)
    C = counter4[-1]
    D = counter3[-1]
    
    counter = A + ":" + B + C + "." + D
    return counter

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global calcounter
    global correct
    global counter
    if timer.is_running() == True:
        timer.stop()
        calcounter += 1
        if counter%10 == 0:
            correct += 1
    if timer.is_running() == False:
        timer.stop()
        calcounter = calcounter
    
    
def reset():
    global counter
    global correct
    global calcounter
    counter = 0
    correct = 0
    calcounter = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [50,100], 32, "White")
    canvas.draw_text(str(correct)+"/", [140,20],32, "White")
    canvas.draw_text(str(calcounter), [165,20],32, "White")
# create frame
frame = simplegui.create_frame("Timer", 200, 200)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# start frame
frame.start()


# Please remember to review the grading rubric
