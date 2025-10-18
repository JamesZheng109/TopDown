import pygame
#Shaders
def color_object(imagefile,color):
    '''Takes an image and colors it in
    image=image to be colored in
    color=desired color to fill in'''
    colored=pygame.Surface(imagefile.get_size())
    colored.fill(color)
    result=imagefile.copy()
    result.blit(colored,(0,0),special_flags=pygame.BLEND_MULT)
    return result,imagefile.get_size()
def greyscale(image):
    '''Recolors image in a greyscale
image=pygame image object
'''
    image_bytes=bytearray(pygame.image.tostring(image,'RGBA'))
    for i in range(0,len(image_bytes),4):
        average=round((image_bytes[i]+image_bytes[i+1]+image_bytes[i+2])/3)
        image_bytes[i]=average
        image_bytes[i+1]=average
        image_bytes[i+2]=average
    return pygame.image.fromstring(bytes(image_bytes),image.get_size(),'RGBA')
def blacken_image(image):
    '''Recolors image entirely black
image=pygame image object
'''
    image_bytes=bytearray(pygame.image.tostring(image,'RGBA'))
    value=43
    for i in range(0,len(image_bytes),4):
        image_bytes[i]=value
        image_bytes[i+1]=value
        image_bytes[i+2]=value
    return pygame.image.fromstring(bytes(image_bytes),image.get_size(),'RGBA') 
