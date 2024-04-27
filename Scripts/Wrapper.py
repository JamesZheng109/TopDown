from Text import speech
click='..\\Audio\\SFX\\Click.wav'
def textwrapper(window,speaker,dialogue,image=[],background=None,sound=[],default_sfx=click):
    speech(window=window,name=speaker,namefontsize=50,text=dialogue,
                   textfontsize=50,text_color='black',box_color='yellow',box_x=100,box_y=700,width=1300,height=220,
                   name_x=1,name_y=7,text_x=10,text_y=78,image=image,background=background,sound=sound,default_sfx=default_sfx)
