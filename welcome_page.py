#!/usr/bin/python
import pygame
import pygame_gui
import webbrowser
from screeninfo import get_monitors

# This is only used if created an exe file using pyinstaller
# import sys
# import os


# def resource_path(relative_path):
#   try:
#        # PyInstaller creates a temp folder and stores path in _MEIPASS
#        base_path = sys._MEIPASS
#    except Exception:
#        base_path = os.path.abspath(".")

#    return os.path.join(base_path, relative_path)
# logo_url = resource_path(r'insert background path')


# This module gets the screen dimensions to be sure that the image is centered on the screen.

# if get_monitors throws an error, just comment it out and replace it with the following using your screen resolution
# width = 1920
# height = 1080

for m in get_monitors():
    if m.is_primary:
        width = m.width
        height = m.height

# Initialize the display
pygame.display.init()
pygame.init()

pygame.display.set_caption('Welcome Page')
# set the window to full screen
window_surface = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# Load image used for the background, make sure image is located in the same folder, or else replace with the file path
background = pygame.image.load('welcome_logo.png')
background = pygame.transform.scale(background, (height, height))
bg_height = background.get_height()
bg_width = background.get_width()

background.convert()

# define button size
wash_bt_width = 1000
wash_bt_height = 100
close_bt_width = 300
close_bt_height = 100

# Edit the font size in the theme.json file to change the font size of the buttons

manager = pygame_gui.UIManager((width, height), 'theme.json')

wash_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(((width / 2) - (wash_bt_width / 2), 5 * height / 6),
                              (wash_bt_width, wash_bt_height)),
    text='Click Here to Start Wash',
    manager=manager)
close_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50), (close_bt_width, close_bt_height)),
                                            text='Close',
                                            manager=manager)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == wash_button:
                print('Starting wash')
                # currently, this opens google as a placeholder. Change this line of code to change the button function.
                webbrowser.open('www.google.com')
            if event.ui_element == close_button:
                # close button shuts down the script
                print('Window Closed')
                is_running = False
                pygame.display.quit()
                pygame.quit()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, ((width / 2) - (bg_width / 2), (height / 2) - (bg_height / 2)))
    manager.draw_ui(window_surface)

    pygame.display.update()
