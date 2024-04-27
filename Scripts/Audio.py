import pygame
pygame.init()
def play_sfx(sound):
    '''play sfx'''
    noise=pygame.mixer.Sound(sound)
    noise.play(0)
def play_music(song):
    '''play song'''
    song=pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
def pause_music(state:0):
    '''pauses and unpauses based on state'''
    if state==0:
        pygame.mixer.music.pause()
    elif state==1:
        pygame.mixer.music.unpause()
    elif state==2:
        pygame.mixer.stop()
if __name__=='__main__':
    pass
