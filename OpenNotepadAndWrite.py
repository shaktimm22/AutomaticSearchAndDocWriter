import pyautogui as pg
import time
import wikipedia as wk
import requests


def text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 138)) -> None:
    """Convert the given str to handwriting"""
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()


def getTopic():
    '''This function asks for the topic to the user'''
    return pg.prompt('Enter the topic to be searched and written.')

    

def openNotepad():
    '''This function opens the notepad'''
    time.sleep(2)
    pg.hotkey('win','r')
    time.sleep(2)
    pg.write('notepad',interval=0.25)
    pg.press('enter')
    time.sleep(10)
    maximizeWindow()


def openMsWord():
    '''This function opens MS Word'''
    time.sleep(2)
    pg.hotkey('win','r')
    time.sleep(2)
    pg.write('WinWord.exe',interval=0.25)
    pg.press('enter')
    time.sleep(30)
    maximizeWindow()
    time.sleep(4)
    pg.press('enter')

def maximizeWindow():
    '''This function simply maximizes the window'''
    pg.hotkey('alt','space')
    pg.press('x')



def startWriting(s,topic):
    '''This function starts writing on the notepad'''

    #checking if there is something is write of not and if not alert the user
    if(s):
        pg.write(topic,interval=0.25)
        pg.press('enter')
        underline(topic)
        pg.press('enter')
        pg.write(s,interval=0.25)
        pg.press('enter')
    else:
        arg = pg.alert('No text given to write')
        if arg:
            searchAboutTheTopic(topic)

def underline(topic):
    '''This function gives underline to the topic'''
    for i in range(0,len(topic)):
        pg.write('-')

def searchAboutTheTopic(topic):
    '''This function searches and finds information from the internet'''
    return wk.summary(topic, sentences=3)  #if more sentences are required then change the value assigned to sentences in the argument



topic = getTopic()
if pg.confirm("Would you prefer to write in MS Word? \nPress 'OK' if yes otherwise 'Cancel'")=='OK':
    openMsWord()
    time.sleep(5)
    info = searchAboutTheTopic(topic)
    time.sleep(2)
    startWriting(info, topic)
elif pg.confirm("Would you want it in handwritten?\nPress 'OK' if yes\n\nNote that it will be in png format.")=='OK':
    text_to_handwriting((topic+'\n\n'+searchAboutTheTopic(topic)), 'C://Users/shakt/Desktop/assignment.png')
    pg.confirm("Assignment Successfully saved!")
    print("Successfull")
else:
    openNotepad()
    time.sleep(5)
    info = searchAboutTheTopic(topic)
    time.sleep(2)
    startWriting(info, topic)

