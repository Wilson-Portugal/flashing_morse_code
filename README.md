# flashing_morse_code

I wrote this project in MicroPython 1.19.1 on a Pico RP2040 thing that I bought from AliExpress.

What I was thinking of when I wrote this is to make the secondary LED on the Pico board flash out Morse code messages. It seemed like a simple idea. I needed a method to encode a text message into Morse code. I found a dictionary file on the web, and I wrapped my own code around it. I then added a second method to convert these dashes and dots to light flashes with a dash being three times longer than a dot. I got this to work. I needed to add a line to make sure it would skip any characters that are not in my dictionary. I then wrote a Main.py file to blink out a message when the Pico unit fired up. It was long and I wanted it to stop. The Pico unit I have has a third extra button and I programmed for it to act as a BREAK key.

Next, I want to code another unit to read the flashes. More to come.
