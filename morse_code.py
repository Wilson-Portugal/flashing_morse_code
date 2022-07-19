# morse code module
# morse_code.py
# Wilson Portugal, July 19, 2022

import machine
import utime

# using the button (on Pico knockoff) allows the script to be
# terminated without completing

button=machine.Pin(23, machine.Pin.IN)
led = machine.Pin(25, machine.Pin.OUT)

# set this value (in seconds) to set timing for morsecode blinking
morse_unit = 0.10

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def morse_encode(message):
    message = message.strip()
    while message.find('  ') >= 0:
        message = message.replace('  ', ' ')
    message = message.upper()
    morse = ''
    for letter in message:
        if letter != ' ':
            if letter in MORSE_CODE_DICT:
                morse += MORSE_CODE_DICT[letter] + ' '
        else:
            morse += ', '
    return morse.strip()

def morse_blink(message):
    if button.value() == 1:
        return
    morse = morse_encode(message)
    for character in morse:
        if button.value() == 1:
            return
        if character == '.':
            led_on()
            utime.sleep(morse_unit)
            led_off()
            utime.sleep(morse_unit)
        elif character == '-':
            led_on()
            utime.sleep(morse_unit*3)
            led_off()
            utime.sleep(morse_unit)
        elif character == ' ':
            utime.sleep(morse_unit*2)
        elif character == ',':
            utime.sleep(morse_unit*4)

def led_on():
    led.value(1)

def led_off():
    led.value(0)

# turn off the led to start with
led_off()
