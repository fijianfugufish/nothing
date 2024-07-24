from pygame import *

font.init()

class gui(sprite.Sprite):
    """
    basic graphical user interface class
    """
    def __init__(self,*,x:float,y:float,w:float,h:float,col:Color,trans:float=255) -> None:
        """kwargs only
        
        Args:
            X (float): x position.
            Y (float): y position.
            w (float): width.
            h (float): height.
            col (Color): color.
            trans (float, optional): transparency. Defaults to 255.
        """
        self.w = w
        self.h = h
        self.rect = Rect(0,0,w,h)
        self.ox = x
        self.oy = y
        self.x = x - self.rect.w/2
        self.y = y - self.rect.h/2
        self.colour = col
        self.transparency = trans
        self.surface = Surface((w,h))
        self.surface.set_alpha(trans)
        self.font = font.SysFont('Comic Sans',25)
        self.display = ''
        self.textcol = (0,0,0)
        self.texttrans = 0
    def draw(self,surf:surface) -> None:
        """draw the object to the display
        """
        global window
        draw.rect(self.surface,self.colour,self.rect)
        text = self.font.render(self.display,False,self.textcol)
        text.set_alpha(self.texttrans)
        self.surface.set_alpha(self.transparency)
        surf.blit(self.surface,(self.x,self.y))
        surf.blit(text,(self.x,self.y))

class textLabel(gui):
    """label to display text
    """
    def __init__(self,*,x:float,y:float,text:str,textsize:int=25,texttrans:float=255,trans=255,col:Color=(255,255,255),textcol:Color=(0,0,0),textfont:str='Ariel') -> None:
        """kwargs only
        
        Args:
            x (float): x position.
            y (float): y position.
            col (Color, optional): color. Defaults to (255,255,255).
            text (str): display text.
            textcol (Color, optional): display text color. Defaults to (0,0,0).
            textsize (int, optional): display text size. Defaults to 25.
            texttrans (float, optional): display text transparency. Defaults to 255.
            trans (float, optional): transparency. Defaults to 255.
            textfont (str,optional): display text font. Defaults to 'Ariel'
        """
        super().__init__(x=x,y=y,w=0,h=0,col=col,trans=trans)
        self.display = text
        self.textcol = textcol
        self.font = font.SysFont(textfont,textsize)
        self.rect = self.font.render(self.display,False,self.textcol).get_rect()
        self.x = x - self.rect.w/2
        self.y = y - self.rect.h/2
        self.surface = Surface((self.rect.w,self.rect.h))
        self.texttrans = texttrans
    def updateText(self,*,text:str) -> None:
        """update display text

        kwargs only
        
        Args:
            text (str): display text.
        """
        self.display = text
        self.rect = self.font.render(self.display,False,self.textcol).get_rect()
        self.x = self.ox - self.rect.w/2
        self.y = self.oy - self.rect.h/2
        