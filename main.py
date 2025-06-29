import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

----- Pins -----
KEY_PINS = [board.D3, board.D4, board.D2, board.D1]  # adjust to your actual GPIOs

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

----- Keymap -----
keyboard.keymap = [
    [
        KC.Q,
        KC.W,
        KC.E,
        KC.R
    ]
]

----- Run it -----
if name == 'main':
    keyboard.go()
