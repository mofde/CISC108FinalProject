'''
Players are presented with a large grid of small squares and a palette of colors
Players can click the palette to choose a different active color
When a player clicks a square on the grid, that square's color changes
You should be able to create pixel art images
Change log:
  - 0.0.6: Added try/except around all functions to handle stupid Pyglet bug.
  - 0.0.5: Added rule to type checker about primitive values in World.
  - 0.0.4: Added on key_release
  - 0.0.3: Allow int in World checks for float type.
  - 0.0.2: Added assert_type, World checks, mock game runner
  - 0.0.1: Initial version
'''
__VERSION__ = '0.0.6'
import arcade, math, random
from cisc108_game import Cisc108Game
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Coloring Squares"
WINDOW_CENTER_X = int(WINDOW_WIDTH/2)
WINDOW_CENTER_Y = int(WINDOW_HEIGHT/2)
FONT_SIZE = 30
BOX_WIDTH = 50
World = {
    'cursor_color': type(arcade.color.RED),
    'color': [type(arcade.color.RED)],
    'target': int,
    'filled': [bool],
    'numbers': [int],
    'color_panel': [str]
}
INITIAL_WORLD = {
    'cursor_color': arcade.color.BLACK,
    'color': [arcade.color.RED, arcade.color.BLUE, arcade.color.RED, arcade.color.GREEN, arcade.color.RED, arcade.color.GREEN, arcade.color.RED, arcade.color.GREEN, arcade.color.RED],
    'target': 0,
    'filled': [False, False, False, False, False, False, False, False, False],
    'numbers': [1, 3, 1, 2, 1, 2, 1, 2, 1],
    'color_panel': ['red', 'green', 'blue']
}
def to_screen_x(index: int, list_size: int) -> int:
    """
    Given an index in the list, and the number of elements in the
    list, compute the X coordinate of the box on the screen.
    Args:
        index (int): The index within the list.
        list_size (int): The number of elements in the list.
    Returns:
        int: The horizontal position of the index on the screen.
    """
    boxes_left_x = WINDOW_CENTER_X - (list_size/2 * BOX_WIDTH)
    index_offset = index * BOX_WIDTH
    return int(boxes_left_x + index_offset)
def draw_instructions(target: int):
    '''
    Draws the first set of instructions for the game at the
    top-left of the screen.
    Args:
        target (int): The index that the player needs to click.
    '''
    arcade.draw_text("Click on the box to color a box", 0, WINDOW_HEIGHT-FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
    arcade.draw_text("in. Something interesting will", 0, WINDOW_HEIGHT-2 * FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
    arcade.draw_text("happen. When you have no", 0, WINDOW_HEIGHT-3 * FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
    arcade.draw_text("more boxes to click, press 'r'", 0, WINDOW_HEIGHT-4 * FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
    arcade.draw_text("to restart.", 0, WINDOW_HEIGHT-5 * FONT_SIZE,
                     arcade.color.WHITE, FONT_SIZE, anchor_x='left')
def draw_world(world: World):
    '''
    Draw the world.
    Args:
        world (World): The current state of the world.
    '''
    draw_instructions(world['target'])
    x = 150.0
    y = 150.0
    for i in range(len(world['color'])):
        if world['filled'][i]:
            arcade.draw_xywh_rectangle_filled(x, y, BOX_WIDTH, BOX_WIDTH, world['color'][i])
            arcade.draw_xywh_rectangle_outline(x, y, BOX_WIDTH, BOX_WIDTH, arcade.color.WHITE)  
        else:
            arcade.draw_xywh_rectangle_outline(x, y, BOX_WIDTH, BOX_WIDTH, arcade.color.WHITE)
            arcade.draw_text(str(world['numbers'][i]), x+5, y+5, arcade.color.WHITE, FONT_SIZE)
        x = x + BOX_WIDTH
        if x > (150.0 + BOX_WIDTH * 2):
            x = 150.0
            y = y + BOX_WIDTH
def update_world(world: World):
    """
    Do nothing to update_world.
    Args:
        world (World): The current world to update.
    """
def handle_key(world: World, key: int):
    """
    Process keyboard input
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key.
    """
    x = 150.0
    y = 150.0
    if key == ord('r'):
        world['filled'] = [False, False, False, False, False, False, False, False, False]
def get_square_index(x: int, y: int) -> int:
    """
    Given an x coordinate on the screen and the number of elements in the
    list, compute the index that this position refers to in the list.
    The X position is expected to be within the boxes drawn on the screen
    or result will be meaningless.
    Effectively, this is the inverse of to_screen_x, converting the drawn
    position to the boxes index.
    Args:
        x (int): The x position on the screen
        y (int): The y position on the screen.
    Returns:
        int: The index in the list.
    """
    xi = x-150
    official_xi = int(xi/BOX_WIDTH)
    yi = y-300
    official_yi = int(yi/BOX_WIDTH)
    i = official_xi + official_yi * 3 + 6
    if (i >= 0) and (i <= 8):
        return i
    else:
        return None
def handle_mouse(world: World, x: int, y: int, button: str):
    """
    Process mouse clicks by determining if the player clicked
    the Y position between the drawn boxes.
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked.
    """
    clicked_at = get_square_index(x, y)
    if clicked_at != None:
        if 150 < x < 150 + BOX_WIDTH * 3:
            if 150 < y < 150 + BOX_WIDTH * 3:
                world['cursor_color'] = world['color'][clicked_at]
                world['filled'][clicked_at] = True
def handle_motion(world: World, x: int, y: int):
    """
    Handle mouse motion.
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """
def handle_release(world: World, key: int):
    """
    The game does nothing when a keyboard key is released.
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the released keyboard key (use ord and chr).
    """
if __name__ == '__main__':
    Cisc108Game(World, WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, INITIAL_WORLD,
                draw_world, update_world, handle_key, handle_mouse,
                handle_motion, handle_release)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()