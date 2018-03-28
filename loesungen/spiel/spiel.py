"""
Beispiel-Spiel
"""
from tilegamelib import Game
from tilegamelib import TiledMap
from tilegamelib.sprites import Sprite
from tilegamelib import Frame
from tilegamelib.vector import UP, DOWN, LEFT, RIGHT
from tilegamelib.config import config
from pygame import Rect
import pygame
import random
import time


config.FRAME = Rect(10, 10, 660, 550)  # Position + Größe des Spielfeldes

MAZE = open('level.txt').read()

class MazeGame:

    def __init__(self):
        self.game = Game()
        self.map = TiledMap(self.game)
        self.map.set_map(MAZE)
        self.fruechte = self.fruechte_zaehlen(MAZE)
        self.sprite = Sprite(self.game, 'b.pac_right', (1, 1), speed=4)
        self.geist = Sprite(self.game, 'b.ghost_center', (8, 8), speed=4)
        self.game.event_loop(figure_moves=self.move,
                             draw_func=self.draw)        

    def fruechte_zaehlen(self, level):
        """Zählt die einzusammelnden Obststücke"""
        return len([c for c in level if c in "abcdefgh"])

    def draw(self):
        """
        Alles bewegen und zeichnen. 
        Wird von event_loop() regelmäßig aufgerufen
        """ 
        self.map.draw()
        self.sprite.move()
        self.sprite.draw()
        self.geist_bewegen()
        self.geist.draw()
        self.frucht_fressen()
        self.kollision()
    
    def geist_bewegen(self):
        """Bewegt den Geist, aber nicht durch Wände"""
        if self.geist.finished:
            richtung = random.choice([UP, DOWN, LEFT, RIGHT])
            neues_feld = self.geist.pos + richtung
            if self.map.at(neues_feld) != '#':
                self.geist.add_move(richtung)
        self.geist.move()

    def kollision(self):
        """Prüft, ob Geist und Spieler auf dem gleichen Feld sind."""
        if self.sprite.pos == self.geist.pos:
            self.game.frame.print_text('VERLOREN!!!', (50, 400))
            pygame.display.update()
            time.sleep(5)
            self.game.exit()
            
    def frucht_fressen(self):
        """Mampft ein Obststück weg"""
        if self.map.at(self.sprite.pos) in 'abcdefgh':
            self.map.set_tile(self.sprite.pos, '.')
            self.fruechte -= 1
            if self.fruechte == 0:
                self.game.frame.print_text('GEWONNEN!!!', (50, 400))
                pygame.display.update()
                time.sleep(5)
                self.game.exit()

    def move(self, direction):
        """Bewegt die Spielfigur. Wird von event_loop()
        aufgerufen, wenn Pfeiltaste gedrückt"""
        neues_feld = self.sprite.pos + direction
        if self.sprite.finished and \
           not self.map.at(neues_feld) == '#':
            self.sprite.add_move(direction)
        

if __name__ == '__main__':  # Python-Ausdrucksweise für "Hier ist das Hauptprogramm"
    maze = MazeGame()

