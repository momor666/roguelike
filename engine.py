import libtcodpy as tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

font_path = 'arial12x12.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)

# Initialize the Window
window_title = 'Roguelike'
fullscreen = False
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
con = tcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT) # Offscreen console

tcod.sys_set_fps(LIMIT_FPS)
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

class Object:
    """ This is a generic object, eg the player, a monster, an item """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Move by the given distance
        self.x += dx
        self.y += dy

    def draw(self):
        # Set the color and then draw the char that represents the object at that position
        tcod.console_set_default_foreground(con, self.color)
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

    def clear(self):
        # Erase the character that represents this object
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

def handle_keys():
    global player_x, player_y

    # Realtime:
    #key = tcod.console_check_for_keypress()

    # Turn Based:
    key = tcod.console_wait_for_keypress(True)

    # Alt + Enter: toggle fullscreen
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    elif key.vk == tcod.KEY_ESCAPE:
        return True  # Exit Game

    # Player Movement
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y = player_y - 1
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y = player_y + 1
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x = player_x - 1
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x = player_x + 1

# Create the player
player = Object(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', tcod.white)

# Create an NPC
npc = Object(SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 2, '@', tcod.yellow)

# List of objects
objects = [npc, player]

while not tcod.console_is_window_closed():

    # Draw all objects in the list
    for object in objects:
        object.draw()

    # Blit the contents of 'con' to the root console and present it
    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0) # Push to the root console
    tcod.console_flush() # Present changes to the screen

    # Erase all objects at their old locations, before they move
    for object in objects:
        object.clear()

    # Handle keys and exit game if required:
    tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)
    exit = handle_keys()
    if exit:
        break




