import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
    )

    row_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, )

    
    diode_orientation = DiodeOrientation.COL2ROW
    rgb_pixel_pin = board.GP28
    encoder_pin_0 = board.GP1
    encoder_pin_1 = board.GP2
    
