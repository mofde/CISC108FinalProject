'''
Tests for my CISC108 final project.
Change log:
  - 0.0.6: Added try/except around all functions to handle stupid Pyglet bug.
  - 0.0.5: Added rule to type checker about primitive values in World.
  - 0.0.4: Added on key_release
  - 0.0.3: Allow int in World checks for float type
  - 0.0.2: Added assert_type, World checks, mock game runner
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.6'
from cisc108 import assert_equal
from cisc108_game import assert_type
from project_starter import *
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_CENTER_X = int(WINDOW_WIDTH/2)
WINDOW_CENTER_Y = int(WINDOW_HEIGHT/2)
FONT_SIZE = 30
BOX_WIDTH = 50
W0 = {
    'cursor_color': arcade.color.BLACK,
    'color': [arcade.color.RED, arcade.color.BLUE, arcade.color.RED, arcade.color.GREEN, arcade.color.RED, arcade.color.GREEN, arcade.color.RED, arcade.color.GREEN, arcade.color.RED],
    'target': 0,
    'filled': [False, False, False, False, False, False, False, False, False],
    'numbers': [1, 3, 1, 2, 1, 2, 1, 2, 1],
    'color_panel': ['red', 'green', 'blue']
}
assert_equal(to_screen_x(0, 3), 175)
assert_equal(to_screen_x(1, 3), 225)
assert_equal(to_screen_x(2, 3), 275)
handle_key(W0, 'r')
assert_equal(W0['filled'], [False, False, False, False, False, False, False, False, False])
assert_equal(get_square_index(200, 400), None)
assert_equal(get_square_index(250, 450), None)
assert_equal(get_square_index(500, 500), None)
assert_equal(get_square_index(175, 175), 0)
assert_equal(get_square_index(225, 175), 1)
assert_equal(get_square_index(275, 175), 2)
assert_equal(get_square_index(175, 225), 3)
assert_equal(get_square_index(225, 225), 4)
assert_equal(get_square_index(275, 225), 5)
assert_equal(get_square_index(175, 275), 6)
assert_equal(get_square_index(225, 275), 7)
assert_equal(get_square_index(275, 275), 8)
handle_mouse(W0, 200, 400, 'black')
assert_equal(W0['cursor_color'], arcade.color.BLACK)
handle_mouse(W0, 250, 450, 'black')
assert_equal(W0['cursor_color'], arcade.color.BLACK)
handle_mouse(W0, 500, 500, 'black')
assert_equal(W0['cursor_color'], arcade.color.BLACK)
handle_mouse(W0, 175, 175, 'red')
assert_equal(W0['cursor_color'], arcade.color.RED)
assert_equal(W0['filled'][get_square_index(175, 175)], True)
handle_mouse(W0, 225, 175, 'blue')
assert_equal(W0['cursor_color'], arcade.color.BLUE)
assert_equal(W0['filled'][get_square_index(225, 175)], True)
handle_mouse(W0, 275, 175, 'red')
assert_equal(W0['cursor_color'], arcade.color.RED)
assert_equal(W0['filled'][get_square_index(275, 175)], True)
handle_mouse(W0, 175, 225, 'green')
assert_equal(W0['cursor_color'], arcade.color.GREEN)
assert_equal(W0['filled'][get_square_index(175, 225)], True)
handle_mouse(W0, 225, 225, 'red')
assert_equal(W0['cursor_color'], arcade.color.RED)
assert_equal(W0['filled'][get_square_index(225, 225)], True)
handle_mouse(W0, 275, 225, 'green')
assert_equal(W0['cursor_color'], arcade.color.GREEN)
assert_equal(W0['filled'][get_square_index(275, 225)], True)
handle_mouse(W0, 175, 275, 'red')
assert_equal(W0['cursor_color'], arcade.color.RED)
assert_equal(W0['filled'][get_square_index(175, 275)], True)
handle_mouse(W0, 225, 275, 'green')
assert_equal(W0['cursor_color'], arcade.color.GREEN)
assert_equal(W0['filled'][get_square_index(225, 275)], True)
handle_mouse(W0, 275, 275, 'red')
assert_equal(W0['cursor_color'], arcade.color.RED)
assert_equal(W0['filled'][get_square_index(225, 275)], True)