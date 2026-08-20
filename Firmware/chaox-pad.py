# freaky_2 macropad firmware
# KMK + CircuitPython
#
# Hardware:
#   4x4 matrix
#   Columns: D0, D1, D2, D3
#   Rows: TX, RX, SCK, MISO
#   Diodes: COL2ROW
#   Encoder A: MOSI / D10
#   Encoder B: SCL / D5
#   Encoder button: SDA / D4

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros


keyboard = KMKKeyboard()

# Matrix
keyboard.col_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
)

keyboard.row_pins = (
    board.TX,
    board.RX,
    board.SCK,
    board.MISO,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Modules
layers = Layers()
encoder = EncoderHandler()
macros = Macros()

keyboard.modules = [
    layers,
    encoder,
    macros,
]


# Shortcuts
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
CUT = KC.LCTL(KC.X)
UNDO = KC.LCTL(KC.Z)
REDO = KC.LCTL(KC.Y)

# Text macros. Change these whenever you want.
HELLO = KC.MACRO("Hello from CHAOX!")
PYTHON = KC.MACRO("print('Hello from CHAOX!')")
GITHUB = KC.MACRO("https://github.com/")


# Layers
BASE = 0
MACRO_LAYER = 1
NUMPAD = 2

TO_MACROS = KC.TG(MACRO_LAYER)
TO_NUMPAD = KC.TG(NUMPAD)


# Main layer
# [ ESC | COPY | PASTE | CUT  ]
# [ UNDO|  A   |  B   |  C    ]
# [  D  |  E   |  F   |  G    ]
# [  H  |  I   | MACRO| NUMPAD]
base_layer = [
    KC.ESC, COPY,  PASTE, CUT,
    UNDO,   KC.A,  KC.B,  KC.C,
    KC.D,   KC.E,  KC.F,  KC.G,
    KC.H,   KC.I,  TO_MACROS, TO_NUMPAD,
]


# Macro / shortcut layer
macro_layer = [
    HELLO,   PYTHON, GITHUB, KC.BSPC,
    KC.TAB,  KC.ENT, KC.SPC, KC.DEL,
    KC.LCTL, KC.LALT, KC.LGUI, KC.LSFT,
    KC.HOME, KC.END, KC.UP, TO_MACROS,
]


# Numpad layer
numpad_layer = [
    KC.P7, KC.P8, KC.P9, KC.PSLS,
    KC.P4, KC.P5, KC.P6, KC.PAST,
    KC.P1, KC.P2, KC.P3, KC.PPLS,
    KC.P0, KC.PDOT, KC.PENT, TO_NUMPAD,
]


keyboard.keymap = [
    base_layer,
    macro_layer,
    numpad_layer,
]


# Rotary encoder
# Base: volume down / volume up / mute
# Macro layer: previous tab / next tab / close tab
# Numpad: minus / plus / enter
encoder.pins = (
    (board.MOSI, board.SCL, board.SDA, False),
)

encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ((KC.LCTL(KC.LSHIFT(KC.TAB)),
      KC.LCTL(KC.TAB),
      KC.LCTL(KC.W)),),
    ((KC.PMNS, KC.PPLS, KC.PENT),),
]


if __name__ == "__main__":
    keyboard.go()
