# Imports
from typing import List

import bs4
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Feilds


# FUNCTIONS
# Get player_one and player_two from Aligulac
def player_id(player_name):
    url = "http://www.google.com/search?q={}+alligulac.com".format(player_name)
    id_and_name = ""
    html = requests.get(url).text
    gsoup = bs4.BeautifulSoup(html, 'lxml')

    split = gsoup.text.split()
    n = 0
    for i in split:
        n += 1
        if i == 'players':
            id_and_name = (split[n + 1])
            break

    pID = ''
    for i in id_and_name:
        if i != '-':
            pID += i
        else:
            break

    id_and_name = pID + '-' + player_name
    return id_and_name
# percent chance of winning bo3
def aligulac_percent_bo3(player_one, player_two):
    content = requests.get(
        "http://aligulac.com/misc/compare/{},{}/".format(player_id(player_one), player_id(player_two)))
    soup = BeautifulSoup(content.text, 'lxml')
    try:
        stats = soup.select('tr')[7].getText()
        percent_first_player = stats[26:37].replace("%\n", "").strip()
        percent_second_player = stats[74:84].replace("%\n", "").strip()
    except:
        percent_first_player = 0
        percent_second_player = 1
    # return(player_one + percent_first_player + " " + player_two + " " + percent_second_player)
    returnList = [player_one, percent_first_player, player_two, percent_second_player]

    return returnList
# decimal odds to implied probability
def decimal_to_percent(decimal_odds):
    implied_probability = (1 / decimal_odds) * 100
    return implied_probability
# implied probability to decimal odds
def ip_to_decimal(ip):
    ip = float(ip)
    decimal_odds = 100 / ip
    decimal_odds = round(decimal_odds, 2)
    return decimal_odds
# American odds to implied probability
def neg_american_to_ip(american):
    ip = (-1) * american / ((-1) * american + 100) * 100
    return (ip)

def pos_american_to_ip(american):
    ip = 100 / (american + 100) * 100
    return ip

# american to decimal
def american_to_decimal(american):
    if american > 0:
        decimal = (american / 100) + 1
    else:
        decimal = 1 + (100 / ((-1) * american))
    return decimal

def main():
    url = 'https://www.bovada.lv/sports/esports/starcraft'
    options = Options()
    options.add_argument('--headless')
    # path to chromedriver
    browser = webdriver.Chrome(executable_path="/Users/Patrick/chromedriver", options=options)
    browser.get(url)
    time.sleep(4)
    html = browser.page_source
    browser.quit()
    soup = bs4.BeautifulSoup(html, 'lxml')

    # Data to a list with odds

    playercount = 0
    players_list = []
    odds_list = []

    # Gets all players names
    for item in soup.select('.name'):
        playercount += 1
        players_list.append(item.text)

    # grouped_events count = gec
    gec = len(soup.select('.grouped-events'))

    for event in range(0, gec):
        # amout of series  = aos
        a = soup.select('.grouped-events')[event]
        aos = len(soup.select('.grouped-events')[event].select('.markets-container'))

        for game in range(0, aos):
            b = soup.select('.grouped-events')[event].select('.markets-container')[game].select('.market-type')[
                1].select(
                '.bet-price')
            # makes odds list in terms of american odds
            for odd in b:
                odd = odd.text.replace(" ", "")
                odd = odd.replace("(", "")
                odd = odd.replace(")", "")
                odd = odd.replace(" ", "")
                odds_list.append(odd)

    # makes odds into ip
    odds_int_list = []

    for i in odds_list:
        if i == "EVEN":
            i = 50
        i = int(i)
        odds_int_list.append(i)
    odds_im_prob_list = []
    for i in odds_int_list:
        if i > 0:
            i = pos_american_to_ip(i)
        else:
            i = neg_american_to_ip(i)
        odds_im_prob_list.append(round(i, 2))

    # Sorts data
    new_list = []
    for i in range(0, len(players_list)):
        new_list.append(players_list[i])
        # make string for now
        new_list.append(str(odds_im_prob_list[i]))

    chunk_size = 4
    chunked_list: list[list[str]] = [new_list[i:i + chunk_size] for i in range(0, len(new_list), chunk_size)]

    # print Bovada data in same format
    print("Bovada Data : ")
    j = -1

    for i in chunked_list:
        print(i)
        # print(" ".join(i))

    # takes bovada and makes into aligulac data
    print("")
    print("")
    print("Aligulac Data : ")
    AligulacList = []
    j = -1
    for i in chunked_list:
        j += 1
        player_one = str(chunked_list[j][0])
        player_two = str(chunked_list[j][2])
        AligulacList.append(aligulac_percent_bo3(player_one, player_two))



    for i in AligulacList:
        # print(" ".join(i))
        print(i)

if __name__ == '__main__':

   main()
