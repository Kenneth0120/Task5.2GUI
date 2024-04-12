from tkinter import *
import tkinter.font
from gpiozero import PWMLED
import RPi.GPIO

# Setup GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
LED_PINS = {'red': 17, 'green': 27, 'blue': 22}
leds = {color: PWMLED(pin) for color, pin in LED_PINS.items()}

# Initialize main window
win = Tk()
win.title("LED Brightness Controller")
win.geometry("350x350")  # Adjust size to fit sliders

myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

def update_led_brightness(value, led):
    brightness = float(value) / 100  # Convert value to float and scale to 0-1
    led.value = brightness

def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Generate sliders and labels for each LED
for i, (color, led) in enumerate(leds.items()):
    Label(win, text=f"{color.capitalize()} LED", font=myFont).grid(row=i*2, column=0, padx=10, pady=5)
    slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=lambda value, led=led: update_led_brightness(value, led))
    slider.grid(row=i*2 + 1, column=0, padx=10, pady=5, sticky='ew')

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=2, width=6)
exitButton.grid(row=2*len(leds), column=0, pady=10)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
