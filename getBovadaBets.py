import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pos_american_to_ip(american):
    ip = 100 / (american + 100) * 100
    return ip

def neg_american_to_ip(american):
    ip = (-1) * american / ((-1) * american + 100) * 100
    return (ip)

def list_of_bets():
    url = 'https://www.bovada.lv/sports/esports/starcraft'
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path="/Users/Patrick/chromedriver", options=options)
    browser.get(url)
    time.sleep(3)
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
    chunked_list = [new_list[i:i + chunk_size] for i in range(0, len(new_list), chunk_size)]

    return chunked_list

if __name__ == '__main__':

    list_of_bets()



