import pygame,sys
from time import sleep
pygame.init()
#Draw stuff
def character_draw_order(player,entity_list,hitbox=False):
    '''Figures out the order to draw entities base on y coordinates
player=Player entity
entity_list=Entity instances for the function to handle
hitbox=Bool that determines if hitboxes are drawn'''
    y_coord=[player.y]
    #Get sorted y coordinates
    [y_coord.append(NPC.y) for NPC in entity_list]
    y_coord.sort()
    already_drawn=False
    #order NPC y coordinates and draw
    for y in y_coord:
        for NPC in entity_list:
            if y==NPC.y and y==player.y:
                if not already_drawn:
                    player.draw(1)
                    already_drawn=True
                NPC.draw(1)
            elif y==NPC.y:
                NPC.draw(1)
            elif y==player.y and not already_drawn:
                player.draw(1)
                already_drawn=True
#Wall Collision
def collision(player,obstacle_list,window=None,hitbox=False):
    '''Collison check for static non-NPC objects
player=player object
obstacle_list=list of obstacles function will check for
hitbox=Bool that determines if hitboxes are drawn'''
    #Get Player Info
    rect=player.get_info(player.rect)
    pushback=1
    #Run Check
    if player.run:
        pushback=2
    for obstacle in obstacle_list:
        #Draw hitbox check
        if hitbox and window!=None:
            pygame.draw.rect(window,'pink',obstacle)
        #Collision check
        if rect.colliderect(obstacle):
            if player.direction=='right':
                player.x-=player.vel*pushback
            elif player.direction=='left':
                player.x+=player.vel*pushback
            elif player.direction=='up':
                player.y+=player.vel*pushback
            elif player.direction=='down':
                player.y-=player.vel*pushback
#NPC Stuff
##NPC collision
def NPC_Hitbox_Updater(player,entity_list:list,hitbox=False,yoffset=0,heightoffset=0):
    '''Handles NPC hitbox shape and draws all entities onto screen
player=Player entity
entity_list=Entity instances for the function to handle
window=screen variable if hitbox needs to be drawn
hitbox=boolean to display NPC's hitboxes
yoffset=lowerhitbox when player's y is higher than NPC's y
heightoffset=Changes height of the hitbox
'''
    #Draws all entities onto screen
    if entity_list==[]:
        player.draw(1,hitbox)
    elif entity_list!=[]:
        character_draw_order(player,entity_list,hitbox)
    for NPC in entity_list:
        #Set heightoffset
        if heightoffset!=0:
            NPC.heightoffset=heightoffset
        #Check coordinate and set yoffset
        if player.y>NPC.y:
            NPC.yoffset=0
        else:
            NPC.yoffset=yoffset
def NPC_collision(player,entity_list):
    '''Handles NPC collison
player=Player entity
entity_list=Entity instances for the function to handle
'''
    #Get Player Hitbox Info
    rect=player.get_info(player.rect)
    for NPC in entity_list:
        #Get NPC Hitbox Info
        rect2=NPC.get_info(NPC.rect)
        #Collison check
        if rect.colliderect(rect2):
            NPC.collide=True
            #Move NPC to end of list because collision part only affects last NPC in entity_list for some reason
            entity_list.append(entity_list.pop(entity_list.index(NPC)))
        elif not rect.colliderect(rect2):
            NPC.collide=False
        NPC.collison(player)
##Talk to NPC
def NPC_Talk_Handler(player,entity_list:list,talk_key:'varaible assigned with pygame.event.get()'):
    '''Handles player and NPC interaction when player speaks with NPC
player=Player class object
entity_list=Entity instances for function to handle
talk_key=varaible assigned with pygame.event.get()
idle_keys=Keys to NPC's state dictionary (left,right,down,up)
'''
    #Loop through entity list
    for npcs in entity_list:
        #Check if player and NPC are next to each other and if player talks to NPC
        if npcs.collide and talk_key.key==pygame.K_e:
            #Adjust NPC direction based on player direction
            if player.direction=='right' and npcs.x>player.x or player.direction=='left' and npcs.x<player.x or player.direction=='up' and npcs.y<player.y or player.direction=='down' and npcs.y>player.y:
                        if player.direction=='right':
                            npcs.set_state("Idle_Left")
                        elif player.direction=='left':
                            npcs.set_state("Idle_Right")
                        elif player.direction=='up':
                            npcs.set_state("Idle_Front")
                        elif player.direction=='down':
                            npcs.set_state("Idle_Back")
                        npcs.talked=True
#Player Cutscene Control
def move(entity,state=(),x:int=None,y:int=None,run=False):
    '''Function to have enitity move to a specificied x or y coordinate
entity=Entity Instance that shall be controlled for the cutscene
state=List indicate moving state and idle state
x=specified x location entity will go to
y=specified y location entity will go to
run=flag to run or not'''
    if run:
        move_multiplier=2
    elif not run:
        move_multiplier=1
    entity.set_state(state[0])
    #If Changing x coordinate
    if isinstance(x,int):
        if entity.x>x:
            move=-entity.vel
        elif entity.x<x:
            move=entity.vel
        if entity.x!=x:
            entity.x+=move*move_multiplier
        elif entity.x==x:
            entity.set_state(state[1])
    #If Changing y coordinate
    if isinstance(y,int):
        if entity.y>y:
            move=-entity.vel
        elif entity.y<y:
            move=entity.vel
        if entity.y!=y:
            entity.y+=move*move_multiplier
        elif entity.y==y:
            entity.set_state(state[1])
#Same Image Different Color
def color_object(imagefile,color):
    '''Takes an image and colors it in
    image=image to be colored in
    color=desired color to fill in'''
    colored=pygame.Surface(imagefile.get_size())
    colored.fill(color)
    result=imagefile.copy()
    result.blit(colored,(0,0),special_flags=pygame.BLEND_MULT)
    return result,imagefile.get_size()
if __name__=='__main__':
    pass
