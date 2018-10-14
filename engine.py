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

tcod.sys_set_fps(LIMIT_FPS)
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

def handle_keys():
    global player_x, player_y

    key = tcod.console_check_for_keypress()
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt + Enter: toggle fullscreen
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


while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
    tcod.console_flush() # present the changes to the screen