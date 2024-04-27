import pygame,sys
from Audio import play_sfx
from Button import button
pygame.init()
#Classes
class textbox():
    def __init__(self,window,name:str,text:str,text_color:str,box_color:str,box_x:int,box_y:int,width:int,height:int,name_x:int,name_y:int,text_x:int,text_y:int):
        '''Make a textbox using Rect and Sysfont
window=pass varibale used to make pygame window
name=Name of the person who is speaking
text=text for the texbox
text_color=color the text variable will display as
box_color=color the texbox will be
box_x=x location the textbox will be placed
box_y=y location the textbox will be placed
width=How wide the texbox will be
height=How high the texbox will be
name_x=x location the name variable will be placed
name_y=y location the name variable will be placed
text_x=x location the text variable will be placed
text_y=y location the text variable will be placed'''
        #Variables
        self.window=window
        ##Name,Text, and Text_color
        self.name=name
        self.text=text
        self.text_color=text_color
        ##Textbox's x, y, and color
        self.box_x=box_x
        self.box_y=box_y
        self.box_color=box_color
        ##Textbox's width and height
        self.width=width
        self.height=height
        ##Name's x and y
        self.name_x=name_x
        self.name_y=name_y
        ##Text's x and y
        self.text_x=text_x
        self.text_y=text_y
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
    def draw(self,namefontsize:int,textfontsize:int):
        '''Draws textbox instance onto window
namefontsize=font size of the name
textfontsize=font size of the text'''
        #Speaker's name info
        Namefont=pygame.font.SysFont('timesnewroman',namefontsize)
        Namerender=Namefont.render(self.name,False,self.text_color)
        #Text info
        Textfont=pygame.font.SysFont('timesnewroman',textfontsize)
        Textrender=Textfont.render(self.text,False,self.text_color)
        #Backgroundbox info and display it
        Backgroundbox=pygame.Rect((0,0),(self.width,self.height))
        self.window.blit(self.surface,(self.box_x,self.box_y))
        Backgroundbox_display=pygame.draw.rect(self.surface,(self.box_color),Backgroundbox)
        #Display Name and Text
        Name_display=self.surface.blit(Namerender,(self.name_x,self.name_y))
        Text_display=self.surface.blit(Textrender,(self.text_x,self.text_y))
#Functions
def speech(window,name:list,namefontsize:int,text:list,textfontsize:int,text_color:str,box_color:str,box_x:int,box_y:int,width:int,height:int,name_x:int,name_y:int,text_x:int,text_y:int,image:list=[],background=None,
           sound:list=[],default_sfx=None,advance_button=pygame.K_e):
    '''Create dialogue loop
window=pygame.display variable
name=list indicating order in which character speaks
namefontsize=font size of the name
text=list indicating order in which line is shown
textfontsize=font size of the text
text_color=color of the text
box_color=color of the textbox
box_x=x coordinate of textbox
box_y=y coordinate of textbox
width=width of textbox
height=height of textbox
name_x=x coordinate of name
name_y=y coordinate of name
text_x=x coordinate of text
text_y=y coordinate of text
image=list of character portraits in order they should display
-format:[(image,x,y),(imagen,xn,yn)]
sound=list of sound effects to play in stated order
-''=play nothing (assuming default_sfx=None)
default_sfx=sfx that one wishes to play by default
background=background image
advance_button=pygame key event to advance the dialogue
'''
    count=0
    a=textbox(window,name[count],text[count],text_color,box_color,box_x,box_y,width,height,name_x,name_y,text_x,text_y)
    b=button(window,'yellow',1300,20,150,100,'Skip','black')
    run=True
    def end():
        nonlocal run
        run=False
        if default_sfx!=None:
            play_sfx(default_sfx)
    while run:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif events.type==pygame.KEYDOWN:
                if events.key==advance_button:
                    count+=1
                    if count>=len(name) or count>=len(text):
                        count-=1
                        run=False
                    if count<=len(sound) and sound!=[]:
                        if sound[count]!='':
                            play_sfx(sound[count])
                        elif sound[count]=='' and default_sfx!=None:
                            play_sfx(default_sfx)
                    elif sound==[] and default_sfx!=None:
                        play_sfx(default_sfx)
        if isinstance(background,str) or isinstance(background,tuple):
            window.fill(background)
        elif background!=None:
            window.blit(background,(0,0))
        if len(image)>0:
            if len(image[count])==3:
               x=image[count][1]
               y=image[count][2]
               pic=image[count][0]
            elif image[count]==[]:
               x=window.get_width()
               y=window.get_height()
               pic=pygame.Surface((0,0))
            window.blit(pic,(x,y))
        a.draw(namefontsize,textfontsize)
        b.draw(end)
        pygame.display.update()
        a.name=name[count]
        a.text=text[count]
if __name__=='__main__':pass
