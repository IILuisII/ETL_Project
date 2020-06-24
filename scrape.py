from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import datetime


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":  r"C:\Users\Maxi\Desktop\chromedriver_83\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://cnbc.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    lists = soup.find_all(class_="LatestNews-newsFeed")
    href = []
    for headline in lists:
        href.append(headline.a.get("href"))

    # create lists
    headlines = []
    datetimes = []
    links = []

    for article in news:
    headline = article.find(class_="LatestNews-headline").text      
    datePub = article.find(class_="LatestNews-timestamp").text
    
    headlines.append(headline)
    datetimes.append(datePub)

    cnbc = soup.find('a',attrs={'class':'branding-menu-logo'})['href']
    cnbc = cnbc.replace("/","")


    # Store data in a dictionary
    cnbc_news = {
        "header": headlines,
        "article_url": href,
        "date_published": datePub,
        "main_url": cnbc
    }

    # Return results
    return cnbc_news
