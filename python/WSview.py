from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
from helium import *
from selenium.webdriver.common.by import By 
import json
import WS_EnebaController
import WS_GreenManGamingController
import WS_SteamController

chromedriver_autoinstaller.install()

# Creates a json archive with the given list.
def jsonArchive(list):
    jsonString = json.dumps(list)
    jsonFile = open("prices.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

# Recieves a string trhough an input and returns it, the string represents the game's name.
def gameToSearch():

    print("welcome, when you enter the name of a game, i will search for it on three different websites and tell you how nuch it costs on each one. Then, you can decide where to buy it.")

    gameN = input("please enter a game name: ")

    return (gameN)


def main():

    # This is the list that will later be used to create the json file, this list will contain the prices of the game or a message saying that the game wasnt found.
    prices = []
    
    game = gameToSearch()

    he.start_chrome("https://www.google.com/")

# Eneba (WS_EnebaController.py)
    WS_EnebaController.openEneba()

    WS_EnebaController.searchInEneba(game)

    WS_EnebaController.gameExistsEneba(prices)

# Green Man Gaming (WS_GreenManGamingController.py)
    WS_GreenManGamingController.openGMG()

    WS_GreenManGamingController.searchInGMG(game)

    WS_GreenManGamingController.gameExistsGMG(prices)

# Steam (WS_SteamController.py)
    WS_SteamController.openSteam()

    WS_SteamController.searchInSteam(game)

    WS_SteamController.gameExistsSteam(prices)

    jsonArchive(prices)

    he.kill_browser()

main()