# Character_Top_Down.py
# License
All files excluding Spritesheet_class.py are licensed under the MIT license. [Christian037](https://github.com/ChristianD37) has authorized the use of the code in Spritesheet_class.py to anyone.
## Entity()
Make Entity object
## Paramters for Entity.__init__()
- screen=Which pygame surface the entity will be drawn on
- x=x coordinate
- y=y coordinate
- vel=velocity
- sprites=dictionary of entity animation(s) and state(s)
- default=default state when initalized
- xoffset=edit the x coordinate of the entity's image rect
- yoffset=edit the y coordinate of the entity's image rect
- widthoffset=edit the width of the entity's image rect
- heightoffset=edit the height of the enitity's image rect
## Parameter for Entity.set_state()
Assigns value of key to self.state assuming self.sprites has it as a key
- key=state the entity will switch to
## Parameter for Entity.get_info()
returns info based on specified class attribute
- info=class attribute one wishes to get (ex: self.vel)
## Parameters for Entity.add_sprites()
Adds sprites to self.sprites dictionary with sprite_key as the key
- sprite_key=key associated with the dictionary
- manysprites=add list of sprites associtated with the sprite_key key
- onesprite=add one sprite to associtaed with the sprite_key key
## Parameters for Entity.remove_sprites()
removes allsprite or onespirte based on sprite_key from self.sprites
- sprite_key=key associated with the dictionary
- allsprites=remove list of sprites associtated with the sprite_key key
- onesprite=remove one sprite to associated with the sprite_key key
## Parameters Entity.draw()
Draws player based on self.sprites
- speed=float to state how fast entity will move
- showhitbox=boolean to determine whether hitbox will be shown
## Player()
Makes Player Object and inherits attributes of Entity class
## Parameters for Player.__init__()
Same as Entity.__init__()
## Parameters for Player.controls()
Player controls pass through button (ex: pygame.K_a) for the following actions:
- run= Ability to move slightly faster
- up=Move up
- down=Move down
- left=Move left
- right=Move right
## Parameters for Player.action()
Player controls pass through button (ex: pygame.K_q) for additional actions
- control=dictionary with buttons as the key and function as the content
```
{'a':func1}
```
- unicode=the variable that represents pygame.event.get() and from that variable pass the variale.unicode ex:
```
for event in pygame.event.get():
  if events.type==pygame.KEYDOWN:
                Player.action(code,events.unicode)
```
  - for functions that require parameters use a lambda or get an error ex:
  ```
  {'b':lambda:[func2(parm1,parm2)}
  ```
## NPC
Makes NPC object and inherits attributes of Entity class
## Parameters for NPC.__init__()
Same as Entity.__init__()
## Parameter for NPC.collison()
Collison detection for NPC object make sure to call NPC.draw before this function or get an error
- player=Player object
## Parameters for NPC.linearpath()
Makes the NPC move in a straight line
- firstpoint=first point where NPC will go the opposite direction
- secondpoint=second point where NPC will go the opposite direction
  - firstpoint & secondpoint format:([x1 or y1,key])
- orientation=whether NPC will go left and right or up and down
  - orientation options:'vertical' or 'horizontal'
## Parameters for NPC.square_path()
Move NPC in a square path based on specified 4 points. Format: (x,y,key)
- firstpoint=Top-Left Corner
- secondpoint=Top-Right Corner
- thirdpoint=Bottom-Right Corner
- fourthpoint=Bottom-Left Corner
## Parameters for NPC.rotate()
Rotates NPC after self.timer reaches limit
- limit=How long until NPC changes directions
- rate=How fast self.timer will increase
- loop=4 directions the NPC will turn
  - loop format: ((key_1,direction_1),(key_2,direction_2),(key_3,direction_3),(key_4,direction_4))
## Parameters for NPC.talk()
- dialogue=dictionary with keys being numbers and the content being a tuple with the list of speakers &dialogues
  - dialogue format: {number:([name],[dialogue],[portrait_image],background_image,sfx)}
- state=dict key for NPC state
# Audio.py, Button.py, Text.py, & Wrapper.py
Refer to [here](https://github.com/JamesZheng109/Text) for info about these files.
# Spritesheet_class.py
File taken from [here](https://github.com/ChristianD37/YoutubeTutorials/tree/master/spritesheet)

Breakdown of the file [here](https://www.youtube.com/watch?v=ePiMYe7JpJo)

Make sure .json file has something like this:
```
{"frames":{
  "image0":{
    "frame":{"x":x,
            "y":y,
            "w":w,
            "h":h}
    },
  "imageN":{
    "frame":{"x":x,
            "y":y,
            "w":w,
            "h":h}
  }
}
```
- N=represents the total number of sprites in the spritesheet - 1
# Functions.py
## character_draw_order()
Figures out the order to draw entities base on y coordinates and then call the entities draw() in said order
### Parameters
- player=Player entity
- entity_list=Entity instances for the function to handle
- hitbox=Bool that determines if hitboxes are drawn
## collision()
Collison check for static non-NPC objects
### Parameters
- player=player object
- obstacle_list=list of obstacles function will check for
- hitbox=Bool that determines if hitboxes are drawn
## NPC_Hitbox_Updater()
Handles NPC hitbox shape and draws all entities onto screen
- player=Player entity
- entity_list=Entity instances for the function to handle
- window=screen variable if hitbox needs to be drawn
- hitbox=boolean to display NPC's hitboxes
- yoffset=lowerhitbox when player's y is higher than NPC's y
- heightoffset=Changes height of the hitbox
## NPC_collision()
Handles NPC collison and calls for NPC.collision()
- player=Player entity
- entity_list=Entity instances for the function to handle
## NPC_Talk_Handler()
Handles player and NPC interaction when player speaks with NPC
- player=Player class object
- entity_list=Entity instances for function to handle
- talk_key=varaible assigned with pygame.event.get()
- idle_keys=Keys to NPC's state dictionary (left,right,down,up)
## move()
Function to have enitity move to a specificied x or y coordinate
- entity=Entity Instance that shall be controlled for the cutscene
- state=List indicate moving state and idle state
- x=specified x location entity will go to
- y=specified y location entity will go to
- run=flag to run or not
## color_object()
Takes an image and colors it in
- image=image to be colored in
  - Make sure the image is already pass through pygame.image.load() and the object is colored white
- color=desired color to fill in
