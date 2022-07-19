# main.py

import morse_code

button = morse_code.button
message = 'The words of the Preacher, the son of David, king in Jerusalem. Vanity of vanities, saith the Preacher, vanity of vanities; all is vanity. What profit hath a man of all his labour which he taketh under the sun?'
while button.value() == 0:
    morse_code.morse_blink(str(message))
