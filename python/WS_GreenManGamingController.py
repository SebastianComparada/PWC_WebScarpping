from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
from helium import *
from selenium.webdriver.common.by import By 

chromedriver_autoinstaller.install()


# Goes to the Green Man Gaming website trhough the link
def openGMG():
    he.go_to('https://www.greenmangaming.com/es/')

    time.sleep(3)

    return None


# Uses the given string to search for the game in the Green Man Gaming website. 
def searchInGMG(name):
    
    search_box = he.find_all(he.S("[placeholder='JUEGOS PARA PC, MAC Y CONSOLAS']"))[0]
    
    he.write(name, into=search_box)

    he.press(he.ENTER)

    time.sleep(3)
    
    return None


# This function checks that the game exists, if the Green Man Gaming website shows the text that means that the game doesnt exists 
# then the string "the game wasn't found in Green Man Gaming" will be added to the list,
# if the text doesnt show then it means that the game does exists and executes the following function (priceGMG(list)).
def gameExistsGMG(list):
    notFound = he.Text("WE COULDN'T FIND ANY GAMES MATCHING YOUR SEARCH TERM.")
    if notFound.exists():
        return (list.append("The game wasn't found in Green Man Gaming"))
    else:
        priceGMG(list)
    return None

# This function recieves a list, the function copy the game's price and add it to the given list.
def priceGMG(list):
    time.sleep(3)
    game_price = (he.find_all(he.S("//html/body/div[1]/div[4]/div[3]/div/div/div/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/ol/li[1]/div/div/div/div/div/div/div[1]/div[2]/div/span")))[0].web_element.text
    print (game_price)
    return (list.append("Green Man Gaming: " + game_price))

