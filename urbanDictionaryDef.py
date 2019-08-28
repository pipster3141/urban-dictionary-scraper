#Urban Dictionary Web Scraping Project - Trevor J Dalton - 9/13/2018
#Intended to practice my web scraping skills.

import bs4, urllib3, requests, lxml
from bs4 import BeautifulSoup
urllib3.disable_warnings()

"""
    initialPhrase = soup.find('div', class_='def-header')
    phrase = initialPhrase.find('a', class_='word').text
    meaning = soup.find('div', class_='meaning').text
    print('Phrase: '+phrase)
    print('Meaning: '+meaning)
"""

def main():
    print('This program finds the last few words of the day for urban dictionary gives them to you in a quick and easy fashion!')
    print()
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print()
    soup = getHTML('https://www.urbandictionary.com/')
    dates = getDates(soup)
    phrases = getPhrases(soup)
    meanings = getMeanings(soup)
    for i in range(len(dates)):
        print('Date: '+dates[i])
        print('Phrase: '+phrases[i])
        print('Meaning: '+meanings[i])
        print()
    k = input('Press enter to exit')
    return

def getDates(soup):
    dates = []
    initialDate = soup.find('div', id='content')
    for child in initialDate:
        type_ = type(child.div)
        if 'None' not in str(type_):
            try:
                twoStep = child.find('div', class_='small-6 columns')
                date = twoStep.div.text
                dates.append(date)
            except:
                pass
    return dates

def getPhrases(soup):
    phrases = []
    initialPhrase = soup.find('div', id='content')
    for child in initialPhrase:
        type_ = type(child.div)
        if 'None' not in str(type_):
            try:
                twoStep = child.find('div', class_='def-header')
                phrase = twoStep.find('a', class_='word').text
                phrases.append(phrase)
            except:
                pass
    return phrases

def getMeanings(soup):
    meanings = []
    initialMeaning = soup.find('div', id='content')
    for child in initialMeaning:
        type_ = type(child.div)
        if 'None' not in str(type_):
            try:
                meaning = child.find('div', class_='meaning').text
                meanings.append(meaning)
            except:
                pass
    return meanings
        
def getHTML(url):
    http = urllib3.PoolManager()
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'lxml')
    return soup
    

if __name__ == "__main__":
    main()
