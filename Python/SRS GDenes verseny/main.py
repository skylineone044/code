#!/usr/bin/env python3
"""Selective RUBBISH collection simulator 2021"""

import sys
import random
import pygame
import time

'''
TODO & NOTES

[PENDING]     use DICTIONARIES for data storage
[PENDING]     fix sound sound_effects
[DONE]        scale background with resolution
[DONE]        re-enable music
[DONE]        make on-click actions worth points
[DONE]        make global var names UPPER_CASE
[DONE]        use a class for the RUBBISH objects
[DONE]        use a class for the rubbish objects
[DONE]        make global var names UPPER_CASE
[DONE]        center the cursor on the trash image
[DONE]        make an ICON for the game
[REVISE]      use time modules timer? stopwatch? functionality for game timer
[CANCELLED]   move everythong to game.py, use main.py as an init thing?
[CANCELLED]   add trail of trash while in the air

'''

# Started  7:52 am, 2020.02.01

pygame.init()
pygame.font.init()

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT
PADDING_Y = 40
PADDING_X = 200
NUMBER_OF_BINS = 4

CLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Selective RUBBISH collection simulator 2021')
ICON = pygame.image.load("assets/icon.png")
pygame.display.set_icon(ICON)
SPEED = [1, 1]
BG = pygame.image.load("assets/bg.png")
BG = pygame.transform.scale(BG, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
FONT = pygame.font.Font("assets/comic.ttf", 32)
TIME = pygame.time.get_ticks()
POINTS = 0

DEBUG = True


def debuginfo(info):
    """just prints when set to true"""
    if DEBUG:
        print(info)


class Rubbish:
    """This is a "method". (a function in a class) this one is special: runs automatically when you
    create a new object in this class: e.g. MAIN_RUBBISH = Rubbish("assets/RUBBISH/paper_2.png")
    and makes stuff so you can have custom data types for each thing you make so MAIN_RUBBISH will
    automatically have MAIN_RUBBISH.obj, MAIN_RUBBISH.rect, MAIN_RUBBISH.SIZE, so you dont have to
    make it for every object manually, taking up lots of lines
    """

    def __init__(self, filename, rubbish_type):
        self.obj = pygame.image.load(filename)
        self.rect = self.obj.get_rect()
        self.size = (self.obj.get_size())
        # THIS IS OVERWRITTEN BY THE BIN POS CALCULATOR FUNCTION ON PURPOSE
        self.pos = [0, 0]
        self.rubbish_type = rubbish_type

# Made a list countaining all current trash textures and
# the main RUBBISH is randomly chosen from said list


ALL_RUBBISH = [Rubbish("assets/rubbish/paper_1.png", "paper"),
               Rubbish("assets/rubbish/paper_2.png", "paper"),
               Rubbish("assets/rubbish/glass_1.png", "glass"),
               Rubbish("assets/rubbish/glass_2.png", "glass"),
               Rubbish("assets/rubbish/metal_1.png", "metal"),
               Rubbish("assets/rubbish/metal_2.png", "metal"),
               Rubbish("assets/rubbish/plastic_1.png", "plastic"),
               Rubbish("assets/rubbish/plastic_2.png", "plastic")]

BIN_METAL = Rubbish("assets/bin_metal.png", "metal")
BIN_GLASS = Rubbish("assets/bin_glass.png", "glass")
BIN_PAPER = Rubbish("assets/bin_paper.png", "paper")
BIN_PLASTIC = Rubbish("assets/bin_plastic.png", "plastic")

ALL_BINS = [BIN_METAL, BIN_GLASS, BIN_PAPER, BIN_PLASTIC]

MUSIC = ["assets/sounds/music_1.mp3",
         "assets/sounds/music_2.mp3",
         "assets/sounds/music_3.mp3",
         "assets/sounds/music_4.mp3"]
CURRENT_MUSIC = random.choice(MUSIC)
pygame.mixer.music.load(CURRENT_MUSIC)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(0)

SOUNDS_METAL = ["assets/sounds/metal_1.ogg",
                "assets/sounds/metal_2.ogg"]

SOUNDS_GLASS = ["assets/sounds/glass_1.ogg",
                "assets/sounds/glass_2.ogg"]

SOUNDS_PLASTIC = ["assets/sounds/plastic_1.ogg",
                  "assets/sounds/plastic_2.ogg"]

SOUNDS_PAPER = ["assets/sounds/paper_1.ogg",
                "assets/sounds/paper_2.ogg"]

SOUNDS_FX = ["assets/sounds/fx_pop.ogg",
             "assets/sounds/fx_error.ogg"]

SOUNDS = [SOUNDS_METAL, SOUNDS_GLASS, SOUNDS_PLASTIC, SOUNDS_PAPER, SOUNDS_FX]

def bin_position_calculator(num_of_bins):
    """calculates the positions of the bins"""
    sample_size = [BIN_METAL.size[0], BIN_METAL.size[1]]
    bins_y = (DISPLAY_HEIGHT/2 - sample_size[1]/2)
    max_width = DISPLAY_WIDTH - 2*PADDING_X
    distance = (max_width / num_of_bins) + (PADDING_X / num_of_bins)

    BIN_GLASS.pos = (PADDING_X + 0*distance, bins_y)
    BIN_METAL.pos = ((PADDING_X + 1*distance), bins_y)
    BIN_PAPER.pos = ((PADDING_X + 2*distance), bins_y)
    BIN_PLASTIC.pos = ((PADDING_X + 3*distance), bins_y)


bin_position_calculator(NUMBER_OF_BINS)


def blit_all(points):
    """the main game loop"""
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BIN_METAL.obj, BIN_METAL.pos)
    SCREEN.blit(BIN_GLASS.obj, BIN_GLASS.pos)
    SCREEN.blit(BIN_PAPER.obj, BIN_PAPER.pos)
    SCREEN.blit(BIN_PLASTIC.obj, BIN_PLASTIC.pos)
    SCREEN.blit(point_text_renderer(points), (10, 0))
    SCREEN.blit(game_timer(), (10, 50))
    SCREEN.blit(MAIN_RUBBISH.obj, rubbish_relocator())


def game_timer():
    """this creates the timer text to be displayed"""
    seconds = str(int((pygame.time.get_ticks() - TIME) / 1000))
    time_counter = FONT.render(
        "Eltelt ido: " + seconds + " masodperc", False, (0, 0, 0))
    return time_counter


def rubbish_relocator():
    """this makes the current rubbish be tied to the mouse cursor"""
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_wrtieable = [mouse_pos[0], mouse_pos[1]]
    main_rubbish_pos = (mouse_pos_wrtieable[0] - (MAIN_RUBBISH.size[0] / 2),
                        mouse_pos_wrtieable[1] - (MAIN_RUBBISH.size[1] / 2))
    return main_rubbish_pos


def point_text_renderer(points):
    """makes the text for renddering with the points"""
    point_text = FONT.render(f"Pontok: {points}", True, (0, 0, 0))
    return point_text


def collision_detector(mouse_pos, target, points, bin_type):
    """checkt wether or not the click is inside the target area"""
    if target[0][0] < mouse_pos[0] < target[0][1]:
        if target[1][0] < mouse_pos[1] < target[1][1]:
            debuginfo("CORRECT HIT")
            points += 1
            debuginfo(f"POINTS: {points}")
            sound_effectplayer(bin_type)
            main(points)


def target_area_calculator(rubbish_bin):
    """calculates the target area for the correct bin"""
    target_x_min = rubbish_bin.pos[0]
    target_x_max = rubbish_bin.pos[0] + rubbish_bin.size[0]

    target_y_min = rubbish_bin.pos[1]
    target_y_max = rubbish_bin.pos[1] + rubbish_bin.size[1]

    return (target_x_min, target_x_max), (target_y_min, target_y_max)


def bin_selector():
    """finds out which is the correct bin for the randomly selected rubbish"""
    for i in range(len(ALL_BINS)):
        if ALL_BINS[i].rubbish_type == MAIN_RUBBISH.rubbish_type:
            selected_bin = ALL_BINS[i]
            return selected_bin


def click_handler(event, target, points, bin_type):
    """handles click releases"""
    if event.type == pygame.MOUSEBUTTONUP:
        collision_detector(pygame.mouse.get_pos(), target, points, bin_type)


def new_rubbish_maker():
    """creates the ryubbish object"""
    global MAIN_RUBBISH
    MAIN_RUBBISH = random.choice(ALL_RUBBISH)
    time.sleep(0.1)
    sound_effectplayer("new_item")

def sound_effectplayer(object_type):
    """plays the sound effects"""
    global sound_effect
    debuginfo(f"MUSIC OBJECT TYPE: {object_type}")
    if object_type == "metal":
        sound_effect = pygame.mixer.Sound(random.choice(SOUNDS_METAL))
        debuginfo(f"EFFECT: {sound_effect}")
    elif object_type == "plastic":
        sound_effect = pygame.mixer.Sound(random.choice(SOUNDS_PLASTIC))
        debuginfo(f"EFFECT: {sound_effect}")
    elif object_type == "paper":
        sound_effect = pygame.mixer.Sound(random.choice(SOUNDS_PAPER))
        debuginfo(f"EFFECT: {sound_effect}")
    elif object_type == "glass":
        sound_effect = pygame.mixer.Sound(random.choice(SOUNDS_GLASS))
        debuginfo(f"EFFECT: {sound_effect}")
    elif object_type == "bad":
        sound_effect = pygame.mixer.Sound(SOUNDS_FX[1])
        debuginfo(f"EFFECT: {sound_effect}")
    elif object_type == "new_item":
        sound_effect = pygame.mixer.Sound(SOUNDS_FX[0])
    sound_effect.play()

def main(points):
    """main"""
    new_rubbish_maker()

    while True:
        rbin = bin_selector()
        target = target_area_calculator(rbin)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            click_handler(event, target, points, rbin.rubbish_type)
            blit_all(points)
            pygame.display.flip()


if __name__ == "__main__":
    main(POINTS)
