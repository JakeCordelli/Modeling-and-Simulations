import os, win32api
import pygame as pg
from math import *

topBar = 25
WIDTH = win32api.GetSystemMetrics(0)
HEIGHT = win32api.GetSystemMetrics(1)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,topBar)
pg.display.init()
pg.font.init()
scrInfo = pg.display.Info()
first = pg.display.set_mode((40,40))
pg.display.iconify()

FPS = 300
clock = pg.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)

first.fill(BLACK)

circleG = pg.image.load("img\circleGreen.png")
circleR = pg.image.load("img\circleRed.png")
circleY = pg.image.load("img\circleYellow.png")

nameNo = 0

myFontLarge = pg.font.SysFont("Arial", 18)
myFont = pg.font.SysFont("Arial", 14)
myFontSmall = pg.font.SysFont("Arial", 11)
versionRunning = myFontSmall.render("v.0.1.3.1 (Copyright BenTech(TM) September 2017)", False, (255,255,255))

mouseL = 0
mouseR = 0
mouseM = 0

lClicks = 0
rClicks = 0
mClicks = 0

partSecond = 0
seconds = 0
minutes = 0
hours = 0
timeInSeconds = 0
timeInMinutes = 0

lineLocations = []
colors = []
gCircles = []
rCircles = []
yCircles = []

def span(value,low,high):
    if value >= high:
        value = high
    if value <= low:
        value = low
    return value

def lineCoordinates(x2,y2,x1,y1):
    newLine = ((x1,y1),(x2,y2))
    return newLine
    #lineLocations.append(newLine)
    #print(lineLocations)

def color(first1,first2,second1,second2):
    mult = 7
    num = span(int(sqrt((first1-second1)**2+(first2-second2)**2))*mult,0,255)
    colorG = 255-num
    colorR = num
    color = (colorR,colorG,255)
    return color

def drawLines(lines,scr):
    j = 0
    for i in lineLocations:
        pg.draw.line(scr, colors[j],i[0],i[1])
        j += 1

def drawCircles(rc,gc,yc,scr):
    for i in rc:
        scr.blit(circleR,i)
    for i in gc:
        scr.blit(circleG,i)
    for i in yc:
        scr.blit(circleY,i)

def run():
    global partSecond,seconds,minutes,hours,timeInSeconds,timeInMinutes,lineLocations,colors,gCircles,rCircles,yCircles

    lClicks = 0
    rClicks = 0
    mClicks = 0

    running = True
    alt = False
                    
    mouse = win32api.GetCursorPos()
    x1 = mouse[0]
    y1 = mouse[1]
    x2 = x1
    y2 = y1

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                end(nameNo)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LALT or event.key == pg.K_RALT:
                    alt = True
                if event.key == pg.K_F4:
                    end(name_no)
                
        mouse = win32api.GetCursorPos()
        lineLocations.append(lineCoordinates(x2,y2,x1,y1))
        colors.append(color(x1,y1,x2,y2))
        x2 = x1
        y2 = y1
        x1 = mouse[0]
        y1 = mouse[1]

        mouse_left = win32api.GetKeyState(0x01)             
        mouse_right = win32api.GetKeyState(0x02)            
        mouse_middle = win32api.GetKeyState(0x04)           

        if mouse_left >= 0:
            held_l = True

        if mouse_right >= 0:
            held_r = True

        if mouse_middle >= 0:
            held_m = True

        if mouse_left < 0 and held_l:
            gCircles.append((x1 - 4,y1 - 4))
            held_l = False
            lClicks += 1

        if mouse_right < 0 and held_r:
            rCircles.append((x1 - 4,y1 - 4))
            held_r = False
            rClicks += 1

        if mouse_middle < 0 and held_m:
            yCircles.append((x1 - 4,y1 - 4))
            held_m = False
            mClicks += 1

        partSecond += 1                                         
    
        if partSecond >= 300:                                   
            partSecond = 0
            seconds += 1
            timeInSeconds += 1

        if seconds >= 60:                                       
            seconds = 0
            minutes += 1

        if minutes >= 60:                                       
            minutes = 0
            hours += 1

        ##print("(("+str(x1)+","+str(y1)+"),("+str(x2)+","+str(y2)+"))")
		
def end(x):
    global partSecond,seconds,minutes,hours,timeInSeconds,timeInMinutes, lineLocations, colors, gCircles, rCircles, yCircles

    screen = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.iconify()
    screen.fill(BLACK)
    
    timeInMinutes = float(timeInSeconds/60)
    avgLeftClicks = (len(gCircles)/(timeInMinutes))
    avgRightClicks = (len(rCircles)/(timeInMinutes))
    avgMiddleClicks = (len(yCircles)/(timeInMinutes))

    drawLines(lineLocations,screen)
    drawCircles(gCircles,rCircles,yCircles,screen)

    show_def_s = myFont.render("Slow =", False, (255,255,255))                                                                      
    show_def_f = myFont.render("Fast =", False, (255,255,255))                                                                      
    show_def_l = myFont.render("Left-click =", False, (255,255,255))                                                                
    show_def_r = myFont.render("Right-click =", False, (255,255,255))                                                               
    show_def_m = myFont.render("Middle-click =", False, (255,255,255))                                                              
    lclicks_no = myFont.render("Number of left-clicks: " + str(lClicks), False, (255,255,255))                                      
    rclicks_no = myFont.render("Number of right-clicks: " + str(rClicks), False, (255,255,255))                                     
    mclicks_no = myFont.render("Number of middle-clicks: " + str(mClicks), False, (255,255,255))                                    
    sessionTime = myFont.render("Length of session: " + str(hours) + ":" + str(minutes) + ":" + str(seconds), False, (255,255,255)) 
    avgLeftClicksNo = myFont.render("Avg left-clicks per minute: " + str(round(avgLeftClicks,1)), False, (255,255,255))             
    avgRightClicksNo = myFont.render("Avg right-clicks per minute: " + str(round(avgRightClicks,1)), False, (255,255,255))          
    avgMiddleClicksNo = myFont.render("Avg middle-clicks per minute: " + str(round(avgMiddleClicks,1)), False, (255,255,255))
    keyLineSlow = show_def_s.get_size()[0] + 8
    keyLineFast = show_def_f.get_size()[0] + 8
    keyCircleGreen = show_def_l.get_size()[0] + 8
    keyCircleRed = show_def_r.get_size()[0] + 8
    keyCircleYellow =  show_def_m.get_size()[0] + 8
    width = avgMiddleClicksNo.get_size()[0]

    s = pg.Surface((width + 10,230), pg.SRCALPHA)   
    s.fill((0,0,0,200))                         
    screen.blit(s, (0,0))

    screen.blit(show_def_s,       (  0,  0))                                                ##########
    screen.blit(show_def_f,       (  0, 15))                                                #
    screen.blit(sessionTime,      (  0, 30))                                                #
    screen.blit(show_def_l,       (  0, 60))                                                #
    screen.blit(show_def_r,       (  0, 75))                                                #Prints
    screen.blit(show_def_m,       (  0, 90))                                                #session
    screen.blit(lclicks_no,       (  0,120))                                                #stats
    screen.blit(avgLeftClicksNo,  (  0,135))                                                #to
    screen.blit(rclicks_no,       (  0,155))                                                #image
    screen.blit(avgRightClicksNo, (  0,170))                                                #
    screen.blit(mclicks_no,       (  0,190))                                                #
    screen.blit(avgMiddleClicksNo,(  0,200))                                                #
    pg.draw.line(screen, ( 0 ,255,255), (keyLineSlow, 9), (keyLineSlow + 50, 9))            #
    pg.draw.line(screen, (255, 0 ,255), (keyLineFast, 24), (keyLineFast + 50, 24))          #
    screen.blit(circleG, (keyCircleGreen, 67))                                              #
    screen.blit(circleR, (keyCircleRed, 82))                                                #
    screen.blit(circleY, (keyCircleYellow, 97))                                             ##########

    screen.blit(versionRunning, (5, HEIGHT - 15))
            
    save = False
    while not save:
        try:
            pg.image.load('Saved Images\screenshot(' + str(x) + ').png')
            x += 1
        except:
            fileName = 'Saved Images\screenshot(' + str(x) + ').png'
            pg.image.save(screen, fileName)
            save = True

    running = False        
    pg.quit()
    #quit()

run()
