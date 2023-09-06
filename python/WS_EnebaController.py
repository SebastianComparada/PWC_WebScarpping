from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
from selenium.webdriver.common.by import By 

chromedriver_autoinstaller.install()


# Goes to the Eneba website trhough the link
def openEneba():

    he.go_to('https://www.eneba.com/latam/')

    time.sleep(3)

    return None


# Uses the given string to search for the game in the Eneba website. 
def searchInEneba(name):
    search_box = he.find_all(he.S("[aria-label='Buscar']"))[0]

    he.write(name, into=search_box)

    he.press(he.ENTER)

    time.sleep(3)
    
    return None


# This function checks that the game exists, if the Eneba website shows the text that means that the game doesnt exists 
# then the string "the game wasn't found in Eneba" will be added to the list,
# if the text doesnt show then it means that the game does exists and executes the following function (priceEneba(list)).
def gameExistsEneba(list):
    notFound = he.Text("No pudimos encontrar nada relacionado con:")
    if notFound.exists():
        return (list.append("The game wasn't found in Eneba"))
    else:
        priceEneba(list)
    return None


# This function recieves a list, the function copy the game's price and add it to the given list.
def priceEneba(list):
    time.sleep(3)
    game_price = (he.find_all(he.S("//html/body/div[1]/main/div/div/section/div[2]/div[2]/div[1]/div/div[3]/a/div[1]/span[2]")))[0].web_element.text
    return (list.append("Eneba: " + game_price))

