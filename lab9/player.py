import pygame 
import os
import sys

pygame.init()
screen = pygame.display.set_mode((600,400))
purpur = (255, 0, 255)
black = (0, 0, 0)
font=pygame.font.SysFont(None, 40)
lybrary = ['/Users/Admin/Desktop/STUDY/python/lab9/songs/__I Wanna Be Yours__ Arctic Monkeys.mp3', 
           '/Users/Admin/Desktop/STUDY/python/lab9/songs/Hotel Ugly - Shut Up My Moms Calling.mp3', 
           '/Users/Admin/Desktop/STUDY/python/lab9/songs/Lana Del Rey - Young and Beautiful (128kbps).mp3',
           '/Users/Admin/Desktop/STUDY/python/lab9/songs/Yes To Heaven - Lana Del Rey __ Lyrics (128kbps).mp3']
current_track = 0
running = True
running_song = True

def start_music(track):
    pygame.mixer.music.load(lybrary[track])
    pygame.mixer.music.play()

def play_music(running_song):
    if running_song:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

start_music(current_track)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running_song = not running_song
                play_music(running_song)
            elif event.key==pygame.K_RIGHT:
                current_track+=1
                if current_track==len(lybrary):
                    current_track=0
                start_music(current_track)
            elif event.key==pygame.K_LEFT:
                current_track-=1
                if current_track<0:
                    current_track=len(lybrary)-1
                start_music(current_track)
               



pygame.quit()

