import pygame as py
import random
import os 

score1 = 0
score2 = 0

sound = os.path.abspath('sounds/hit.wav')

py.mixer.init()

hitsound = py.mixer.Sound(sound)
class Ball(py.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = py.Surface((15, 15), py.SRCALPHA)
        py.draw.ellipse(self.surf, (255, 255, 255), (0, 0, 15, 15))
        self.rect = self.surf.get_rect(center=(width // 2, height // 2))
        self.width = width
        self.height = height
        self.speed = [4, 4]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def check_collision(self, player1, player2, width, height, score1, score2):
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]
            hitsound.play()
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.speed[0] = -self.speed[0]
            hitsound.play()
        if self.rect.right >= width: 
            self.rect.x, self.rect.y = width // 2 - 10, height // 2 - 10
            self.speed = [4, 4]
            score1 += 1
            hitsound.play()
        if self.rect.left <= 0:
            self.rect.x, self.rect.y = width // 2 - 10, height // 2 - 10
            self.speed = [-4, 4]
            score2 += 1
            hitsound.play()
        
        
        return score1, score2
            
