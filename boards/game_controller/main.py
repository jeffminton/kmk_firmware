from kb import KMKKeyboard

from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())

# Uncomment below if you're using encoder
encoder_handler = EncoderHandler()

keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

# Uncomment below if you're having RGB
rgb_ext = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=30,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
)
keyboard.extensions.append(rgb_ext)

# Edit your layout below
# Currently, that's a default QMK Kyria Layout - https://config.qmk.fm/#/splitkb/kyria/rev1/LAYOUT
ENT_LALT = KC.MT(KC.ENT, KC.LALT)

_______ = KC.TRNS
XXXXXXX = KC.NO


keyboard.keymap = [
    # WASD Layer
    [
        KC.GRAVE_ESC,   KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5, 
        KC.TAB,         KC.Q,           KC.W,           KC.E,           KC.R,           KC.T,
        KC.LCTRL,       KC.A,           KC.S,           KC.D,           KC.F,           KC.LT(2, KC.G),
        KC.LSFT,        KC.Z,           KC.X,           KC.C,           KC.V,           KC.LT(5, KC.B),
        XXXXXXX,        KC.LCTRL,       KC.LGUI,        ENT_LALT,       KC.SPC,         KC.LT(4, KC.MUTE)
    ],
    # Arrow Layer
    [
        KC.GRAVE_ESC,   KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5, 
        KC.TAB,         KC.Q,           KC.UP,          KC.E,           KC.R,           KC.T,
        KC.LCTRL,       KC.LEFT,        KC.DOWN,        KC.RIGHT,       KC.F,           KC.LT(2, KC.G),
        KC.LSFT,        KC.Z,           KC.X,           KC.C,           KC.V,           KC.LT(5, KC.B),
        XXXXXXX,        KC.LCTRL,       KC.LGUI,        ENT_LALT,       KC.SPC,         KC.LT(4, KC.MUTE)
    ],
    # REDO SHIFT Z Layer
    [
        _______,        _______,        _______,        _______,        _______,        _______, 
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        KC.LT(3, KC.B),
        XXXXXXX,        _______,        _______,        _______,        _______,        _______
    ],
    # REDO Y Layer
    [
        _______,        _______,        _______,        _______,        _______,        _______, 
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        _______,
        XXXXXXX,        _______,        _______,        _______,        _______,        _______
    ],
    # FULL Layer Switch Layer
    [
        _______,        KC.TO(0),       KC.TO(1),       _______,        _______,        _______, 
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        _______,
        _______,        _______,        _______,        _______,        _______,        _______,
        XXXXXXX,        _______,        _______,        _______,        _______,        _______
    ],
    # Change Brightness Layer
    [
        KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,    KC.RGB_MODE_BREATHE_RAINBOW,    KC.RGB_MODE_KNIGHT, KC.RGB_MODE_SWIRL, 
        _______,            _______,                _______,                _______,                        _______,            _______,
        _______,            _______,                _______,                _______,                        _______,            _______,
        _______,            _______,                _______,                _______,                        _______,            _______,
        XXXXXXX,            _______,                _______,                _______,                        _______,            _______
    ],
]

# Uncomment below if using an encoder
# Edit your encoder layout below
encoder_handler.map = (
    ( ( KC.VOLD, KC.VOLU, ), ),
    ( ( KC.VOLD, KC.VOLU, ), ),
    ( ( KC.LCTL( KC.Z ), KC.LCTL( KC.LSFT( KC.Z ) ), ), ),
    ( ( KC.LCTL( KC.Z ), KC.LCTL( KC.Y ), ), ),
    ( ( KC.VOLD, KC.VOLU, ), ),
    ( ( KC.RGB_VAD, KC.RGB_VAI, ), ),
)

if __name__ == '__main__':
    keyboard.go()

