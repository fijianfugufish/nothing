from pygame import *
import pyautogui

from modules.gui import textLabel

#* initialise window
WINDOWX = WINDOWY = 800
window: object = display.set_mode(size=(WINDOWX,WINDOWY))
display.set_caption(title='')
window.fill(color=(100,100,100))

font.init()

#* variables
clock: object = time.Clock()
FPS: int = 10

MIDDLE: tuple[float,float] = (WINDOWX/2,WINDOWY/2)

doing: bool | None = False
grace: int = 0
running: bool = True
secondsOfNothingness: int = 0
counter: int = 0

#* objects
objects: set[object] = set()

label: object = textLabel(x=MIDDLE[0],y=MIDDLE[1],
                          text=f'do something to start doing nothing',
                          textcol=(50,50,50),trans=0,textsize=50)
objects.add(label)

#* main game loop
def main() -> None:
    global running,window,doing,counter,secondsOfNothingness,grace
    
    events: list = event.get()
    pyautogui.moveTo(MIDDLE*2)
    event.wait()

    while running:
        events = event.get()
        
        counter += 1
        
        display.update()
        
        window.fill(color=(100,100,100))
        
        for obj in objects: obj.draw(surf=window)
        
        if events == list() and doing:
            label.updateText(text=f'you have been doing nothing for {secondsOfNothingness} seconds')
            grace += 1
            
        for e in events:
            if e.type == QUIT:
                running = False
            elif e.type and (doing or doing == None) and grace > 10:
                label.updateText(text=f'you did something; you lose')
                doing = None
            elif e.type and not doing == None and grace < 1:
                label.updateText(text=f'you have been doing nothing for {secondsOfNothingness} seconds')
                doing = True
                display.update()
                event.wait()
                break
        
        clock.tick(FPS)
        
        if counter >= FPS:
            counter = 0
            if doing:
                secondsOfNothingness += 1
            
if __name__ == '__main__':
    main()

quit()