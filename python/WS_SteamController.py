from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
from helium import *
from selenium.webdriver.common.by import By 

chromedriver_autoinstaller.install()


# Goes to the Steam website trhough the link
def openSteam():
    he.go_to('https://store.steampowered.com/?l=spanish')

    time.sleep(3)

    return None


# Uses the given string to search for the game in the Steam website. 
def searchInSteam(name):
    
    search_box = he.find_all(he.S("[placeholder='buscar']"))[0] 
    
    he.write(name, into=search_box)

    he.press(he.ENTER)

    time.sleep(3)
    
    return None


# This function checks that the game exists, if the Steam website shows the text that means that the game doesnt exists 
# then the string "the game wasn't found in Steam" will be added to the list,
# if th text doesnt show then it means that the game does exists and executes the following function (priceSteam(list)).
def gameExistsSteam(list):
    notFound = he.Text("0 resultados coinciden con la búsqueda.")
    if notFound.exists():
        return (list.append("The game wasn't found in Steam"))
    else:
        priceSteam(list)
    return None


# This function recieves a list, the function copy the game's price and add it to the given list.
def priceSteam(list):
    time.sleep(3)
    game_price = (he.find_all(he.S("//html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a[1]/div[2]/div[4]/div/div/div/div")))[0].web_element.text
    return (list.append("Steam: " + game_price))
