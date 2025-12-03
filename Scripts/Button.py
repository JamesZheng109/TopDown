#Imports
import pygame
pygame.init()
class button():
    def __init__ (self,window,box_color,x:int,y:int,width:int,height:int,text:str,text_color,alpha=255):
        '''Make a button using Rect
window=pass variable used to make pygame window
box_color=color the button will be
x=x location the button will be placed
y=y location the button will be placed
width=How wide the texbox will be
height=How high the texbox will be
text=Words to display on button
text_color=color text will be'''
        #Variables
        self.window=window
        ##Button info
        self.x=x
        self.y=y
        self.box_color=box_color
        self.width=width
        self.height=height
        self.clicked=False
        self.text=text
        self.text_color=text_color
        self.textfont=pygame.font.SysFont('timesnewroman',50)
        self.textrender=self.textfont.render(self.text,False,self.text_color)
        #Surface
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.surface.set_alpha(alpha)
    def draw(self,act):
        '''Draws button instance onto window'''
        self.window.blit(self.surface,(self.x,self.y))
        ##Button info
        Box=pygame.Rect((0,0),(self.width,self.height))
        ##Button display
        pygame.draw.rect(self.surface,(self.box_color),Box)
        ##Display Text
        self.surface.blit(self.textrender,(int(self.width/2)-int(self.textrender.get_width()/2),int(self.height/2)-int(self.textrender.get_height()/2)))
        #Mouse detection
        if Box_display.collidepoint((pygame.mouse.get_pos()[0]-self.x,pygame.mouse.get_pos()[1]-self.y)):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True;act()
            else:
                self.clicked=False
    def delete_button(self,Display_W,Display_H):
        '''Move and shrink button and moves it elsewhere'''
        self.x=Display_W+1
        self.y=Display_H+1
        self.width=0
        self.height=0


