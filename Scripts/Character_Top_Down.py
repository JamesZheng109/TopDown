#Imports
import pygame
from Text import *
from Wrapper import textwrapper
pygame.init()
class Entity():
    def __init__(self,screen,x:int,y:int,vel:int,sprites:dict,default:str,xoffset:int=0,yoffset:int=0,widthoffset:int=0,heightoffset:str=0):
        '''Make Entity object'''
        #Variable
        self.screen=screen
        self.index=0
        self.state=''
        self.direction=''
        self.collide=False
        #Coordinates
        self.x=x
        self.y=y
        self.vel=vel
        #Image stuff
        self.sprites=sprites
        self.image=sprites[default][0]
        self.xoffset=xoffset
        self.yoffset=yoffset
        self.widthoffset=widthoffset
        self.heightoffset=heightoffset
    def set_state(self,key:str):
        '''Assigns value of key to self.state assuming self.sprites has it as a key'''
        if key in self.sprites.keys():
            self.state=key
        elif key not in self.sprites.keys():
            raise KeyError(f'{key} is not in the dictionary. Please double check spelling')
    def get_info(self,info):
        '''returns info based on specified class attribute'''
        return info
    def add_sprites(self,sprite_key:str,manysprites:list=None,onesprite=None):
        '''Adds sprites to self.sprites dictionary with sprite_key as the key
sprite_key=key associated with the dictionary
manysprites=add list of sprites associtated with the sprite_key key
onesprite=add one sprite to associtaed with the sprite_key key'''
        if manysprites is not None or onesprite is not None:
            if manysprites is not None:
                if sprite_key not in self.sprites.keys():
                    self.sprites[sprite_key]=manysprites
                elif sprite_key in self.sprites.keys():
                    self.sprite[sprite_key]+=manysprites
            elif onesprite is not None:
                if sprite_key not in self.sprites.keys():
                    self.sprites[sprite_key]=onesprite
                elif sprite_key in self.sprites.keys():
                    self.sprites[sprite_key].append(onesprite)
    def remove_sprites(self,sprite_key:str,allsprites=None,onesprite=None):
        '''removes allsprite or onespirte based on sprite_key from self.sprites
sprite_key=key associated with the dictionary
allsprites=remove list of sprites associtated with the sprite_key key
onesprite=remove one sprite to associated with the sprite_key key'''
        #Delete entire dictionary key
        if allsprites is None or onesprite is None:
            self.sprites.pop(sprite_key)
        elif allsprites is not None and onesprite is not None:
            if allsprites is not None and allsprites in self.sprites[sprite_key]:
                self.sprites[sprite_key].clear(allsprites)
            elif onesprite is not None and onesprite in self.sprites[sprite_key]:
                self.sprites[sprite_key].remove(onesprite)
    def draw(self,speed:float,showhitbox=False,showindex=False):
        '''Draws player based on self.sprites
speed=float to state how fast entity will move
showhitbox=boolean to determine whether hitbox will be shown'''
        if not self.collide:
            self.index+=speed
        elif self.collide:
            self.index+=0
        #Index Check
        if int(self.index)>=len(self.sprites[self.state]):
            self.index=0
        #Draw Image
        self.image=self.screen.blit(self.sprites[self.state][int(self.index)],(self.x,self.y))
        self.rect=self.get_info(self.image)
        self.rect.width+=self.widthoffset
        self.rect.height+=self.heightoffset
        self.rect.x+=self.xoffset
        self.rect.y+=self.yoffset
        #Draw hitbox check
        if showhitbox:
            pygame.draw.rect(self.screen,(255,0,0),self.rect,1)
        if showindex:
            print(self.index)
class Player(Entity):
    def __init__(self,screen,x:int,y:int,vel:int,sprites:dict,default:str,xoffset:int=0,yoffset:int=0,widthoffset:int=0,heightoffset:int=0):
        #Entity Class setup
        super().__init__(screen,x,y,vel,sprites,default,xoffset,yoffset,widthoffset,heightoffset)
        self.set_state(default)
        #Player class variables
        self.move_multiplier=1
        self.control=True
        self.run=False
    def action(self,control,unicode):
        '''Player controls pass through button (ex: pygame.K_q) for additional actions
'''
        if self.control:
            if unicode in control.keys():
                control[unicode]()
    def controls(self,run,up,down,left,right):
        '''Player controls pass through button and change directions with keys
run,up,down,left,right ex: pygame.K_a to assign the a key to either up, down, left,or right
'''
        if self.control:
            #player collision check
            if self.collide:
                self.move_multiplier=0
            elif not self.collide:
                self.move_multiplier=1
            #Check for specified keyboard input and move player
            key=pygame.key.get_pressed()
            if not key[run]:
                self.run=False
            elif key[run] and not self.collide:
                self.run=True
            if self.run and not self.collide:
                self.move_multiplier=2
            if key[up]:
                self.set_state("Move_Back")
                self.y-=self.vel*self.move_multiplier
                self.direction="up"
            elif key[down]:
                self.set_state("Move_Front")
                self.y+=self.vel*self.move_multiplier
                self.direction="down"
            elif key[left]:
                self.set_state("Move_Left")
                self.x-=self.vel*self.move_multiplier
                self.direction="left"
            elif key[right]:
                self.set_state("Move_Right")
                self.x+=self.vel*self.move_multiplier
                self.direction="right"
            #Check to see what direction the player is facing
            else:
                if self.direction=="down":
                    self.set_state("Idle_Front")
                elif self.direction=="up":
                    self.set_state("Idle_Back")
                elif self.direction=="left":
                    self.set_state("Idle_Left")
                elif self.direction=="right":
                    self.set_state("Idle_Right")
class NPC(Entity):
    def __init__(self,screen,x:int,y:int,vel:int,sprites:dict,default:str,xoffset:int=0,yoffset:int=0,widthoffset:int=0,heightoffset:int=0):
        '''Make NPC object'''
        #Entity class setup
        super().__init__(screen,x,y,vel,sprites,default,xoffset,yoffset,widthoffset,heightoffset)
        self.set_state(default)
        #NPC class variables
        self.x_vel=0
        self.y_vel=0
        self.talked=False
        self.timer=0
        self.dialogue=0
    def collison(self,player):
        '''Collison detection for NPC object make sure to call NPC.draw before this function
or get an error
player=player object to check against NPC object'''
        #self.NPC_hitbox=self.get_info(self.rect)
        #self.player_hitbox=player.get_info(player.rect)
        #Checks if player and npc have collided
        if self.collide:
            self.x_vel=0
            self.y_vel=0
            self.index=0
            #Check if player and npc are facing each other
            if self.x>player.x and player.direction=='right':
                player.collide=True
            elif self.y>player.y and player.direction=='down':
                player.collide=True
            elif self.x<player.x and player.direction=='left':
                player.collide=True
            elif self.y<player.y and player.direction=='up':
                player.collide=True
            else:
                player.collide=False
        elif not self.collide:
            self.collide=False
            player.collide=False
    def linearpath(self,firstpoint:list,secondpoint:list,orientation:str='vertical'):
        '''firstpoint & secondpoint=points where NPC will go the opposite direction
firstpoint & secondpoint format:([x1 or y1,key])
orientation=whether NPC will go left and right or up and down
orientation options:'vertical' or 'horizontal'
'''
        self.x+=self.x_vel
        self.y+=self.y_vel
        if not self.collide:
            #Check if npc has reached a specified point and change directions if so
            if orientation=='vertical':
                if self.y==firstpoint[0]:
                    self.y_vel=self.vel
                    self.direction='down'
                    self.set_state(firstpoint[1])
                elif self.y==secondpoint[0]:
                    self.y_vel=-self.vel
                    self.direction='up'
                    self.set_state(secondpoint[1])
                elif self.direction=='down':
                    self.y_vel=self.vel
                    self.direction='down'
                    self.set_state(firstpoint[1])
                elif self.direction=='up':
                    self.y_vel=-self.vel
                    self.direction='up'
                    self.set_state(secondpoint[1])
            elif orientation=='horizontal':
                if self.x==firstpoint[0]:
                    self.x_vel=self.vel
                    self.direction='left'
                    self.set_state(firstpoint[1])
                elif self.x==secondpoint[0]:
                    self.x_vel=-self.vel
                    self.direction='right'
                    self.set_state(secondpoint[1])
                elif self.direction=='left':
                    self.x_vel=self.vel
                    self.direction='left'
                    self.set_state(firstpoint[1])
                elif self.direction=='right':
                    self.x_vel=-self.vel
                    self.direction='right'
                    self.set_state(secondpoint[1])
    def square_path(self,firstpoint:list,secondpoint:list,thirdpoint:list,fourthpoint:list):
        '''Move NPC in a square path based on specified 4 points
Parameter format for each position:(x,y,key)
firstpoint=Top-Left Corner
secondpoint=Top-Right Corner
thirdpoint=Bottom-Right Corner
fourthpoint=Bottom-Left Corner'''
        self.x+=self.x_vel
        self.y+=self.y_vel
        if not self.collide:
            #Check if npc has reached a specified point and change directions if so
            if self.x>=firstpoint[0] and self.x<secondpoint[0] and self.y==firstpoint[1] and self.y<thirdpoint[1]:
                self.set_state(firstpoint[2])
                self.direction='right'
                self.x_vel=self.vel
                self.y_vel=0
            elif self.x==secondpoint[0] and self.x>firstpoint[0] and self.y>=secondpoint[1] and self.y<thirdpoint[1]:
                self.set_state(secondpoint[2])
                self.direction='down'
                self.x_vel=0
                self.y_vel=self.vel
            elif self.x<=thirdpoint[0] and self.x>fourthpoint[0] and self.y==thirdpoint[1] and self.y>firstpoint[1]:
                self.set_state(thirdpoint[2])
                self.direction='left'
                self.x_vel=-self.vel
                self.y_vel=0
            elif self.x==fourthpoint[0] and self.y<=fourthpoint[1] and self.y>firstpoint[1]:
                self.set_state(fourthpoint[2])
                self.direction='up'
                self.x_vel=0
                self.y_vel=-self.vel
    def rotate(self,limit:int,rate:int,loop:list):
        '''Rotates NPC after self.timer reaches limit
limit=How long until NPC changes directions
rate=How fast self.timer will increase
loop=4 directions the NPC will turn
loop format: ((key_1,direction_1),(key_2,direction_2)
(key_3,direction_3),(key_4,direction_4))'''
        if len(loop)!=4:
            raise ValueError('Need 4 elements for this to work')
        self.timer+=rate
        if self.timer>=limit and self.timer<limit*2 and self.timer<limit*3 and self.timer<limit*4:
            self.set_state(loop[0][0])
            self.direction=loop[0][1]
        elif self.timer>=limit*2 and self.timer<limit*3 and self.timer<limit*4 and self.timer>limit:
            self.set_state(loop[1][0])
            self.direction=loop[1][1]
        elif self.timer>=limit*3 and self.timer<limit*4 and self.timer>limit and self.timer>limit*2:
            self.set_state(loop[2][0])
            self.direction=loop[2][1]
        elif self.timer>=limit*4:
            self.set_state(loop[3][0])
            self.direction=loop[3][1]
            self.timer=0
    def talk(self,dialogue:dict,state=None):
        '''dialogue=dictionary with keys being numbers and the content being a tuple with the list of speakers &dialogues
dialogue format: {number:([name],[dialogue],[portrait_image],background_image,sfx)}
state=dict key for NPC state
'''
       #Check if player is talking to NPC
        if self.talked:
            #Makes sure self.dialoue does not exceed key number
            if self.dialogue>=len(dialogue.keys()):
                self.dialogue=0
            #Loop through dictionary and output dialogue based on dialogue number matching dictionary key
            textwrapper(self.screen,speaker=dialogue[self.dialogue][0],dialogue=dialogue[self.dialogue][1],image=dialogue[self.dialogue][2],
                        background=dialogue[self.dialogue][3],sound=dialogue[self.dialogue][4])
            self.talked=False
            if state!=None:
                self.set_state(state)
            #Increments dialogue counter
            if self.dialogue!=len(dialogue.keys()):
                self.dialogue+=1
        
if __name__=="__main__":pass

