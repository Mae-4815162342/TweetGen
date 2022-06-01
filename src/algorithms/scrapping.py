import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pandas as pd

Nonotext = ['Les utilisateurs de Twitter sont les premiers à savoir.',
            "Affichez plus d'informations sur vos choix",
            'Inscrivez-vous pour profiter de votre propre fil personnalisé !',
            "S'inscrire avec un numéro de téléphone ou une adresse email",
            'Les utilisateurs de Twitter sont les premiers à savoir.'
            "Connectez-vous pour découvrir des Tweets sur les sujets que vous suivez dans votre fil d'actualités.",
            "Refuser les cookies non nécessaires",
            "Ne manquez pas ce qui se passe.",
            'Informations sur les publicités',
            'Tendance dans la catégorie France'
            ]


def valid_tweet(link):
    return link not in Nonotext


def clean_text(tweets):
    return [elem.strip().replace('\n', '') for elem in list(dict.fromkeys(tweets)) if (len(elem) > 0) and valid_tweet(elem)]

class TwitterBot:
    def __init__(self):
        options = Options()
        options.headless = True
        self.bot = webdriver.Firefox(options=options)

    def get_tweet(self, name):
        bot = self.bot
        url = "https://twitter.com/"
        bot.get(url + name)
        URL = bot.current_url
        if URL != url + name :
            print("Error page")
            return "error= user doesnt exist"

        links = []
        bot.refresh()
        for i in range(110):
            print(i)
            try:
                bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(3)
                tweets = bot.find_elements(By.XPATH,
                                          "//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")

                links = links + [elem.text for elem in tweets if (len(elem.text) > 30) and valid_tweet(elem.text)]
            except Exception:
                print("exception")
                continue
        valid_links = [link for link in links if link is not None]
        valid_links = clean_text(valid_links)
        bot.quit()
        print("nb of elements: ", len(valid_links))
        df = pd.DataFrame(valid_links)
        df.to_csv('../data/tweets.csv', index=False)
        print("nb of elements: ", len(valid_links))
        print(valid_links)
        return "name=" + name

if __name__ == '__main__':

    print("Please enter your account name : ")
    name = str(input())
    print(name)
    ias = TwitterBot()
    ias.get_tweet(name)
