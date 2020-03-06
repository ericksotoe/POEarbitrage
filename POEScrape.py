from time import sleep
from selenium import webdriver
from typing import List, TypeVar
from BellmanFordPOE import BellmanFordPOE as bf
import math

num2curr = {0: "chaos", 1: "exalted", 2: "fusing"}

URL = "https://www.pathofexile.com/trade/search/Metamorph"

bulk_ex_button = "//div[@id='trade']/div[@class='navigation']/ul[1]//a[@href='/trade/exchange/Metamorph']"

chaos_orb_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[4]/img[@alt='Chaos Orb']"
exalted_orb_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[6]/img[@alt='Exalted Orb']"
orb_of_fusing_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[2]/img[@alt='Orb of Fusing']"

chaos_orb_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[4]/img[@alt='Chaos Orb']"
exalted_orb_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[6]/img[@alt='Exalted Orb']"
orb_of_fusing_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[2]/img[@alt='Orb of Fusing']"

send_button = "//div[@id='trade']/div[@class='top']//div[@class='controls-center']/button[@type='button']"


def getPrices(sell, buy, u, v):
    """ getPrices method returns the poe currency exchange using poe main website

    parameters:
        buy (str) : what currency do you want
        sell (str) : what currency do you have

    """

    # if 'chaos' in sell:

    driver = webdriver.Chrome()
    driver.get(URL)
    sleep(4)
    driver.find_element_by_xpath(bulk_ex_button).click()
    sleep(2)
    driver.find_element_by_xpath(sell).click()
    sleep(.5)
    driver.find_element_by_xpath(buy).click()
    sleep(.5)
    driver.find_element_by_xpath(send_button).click()
    sleep(3)
    price_pay = int(driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) .price-right > .price-block > span:nth-of-type(1)").text)
    price_get = int(driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) .price-left > .price-block > span:nth-of-type(3)").text)
    # price_seller = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(1) a[target='_blank']").text
    # price_stock = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(1) .pull-left.stock > span:nth-of-type(1)").text
    # price_pay2 = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(2) .price-left > .price-block > span:nth-of-type(3)").text
    # price_get2 = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(2) .price-right > .price-block > span:nth-of-type(1)").text
    # price_seller2 = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(2) a[target='_blank']").text
    # price_stock2 = driver.find_element_by_css_selector(
    #     ".exchange.resultset > div:nth-of-type(2) .pull-left.stock > span:nth-of-type(1)").text
    # print(f"your {price_pay} exalted orbs for their {price_get} chaos orbs")
    # print(f"so 1 chaos is worth {price_pay/price_get} exalted")
    w = price_pay/price_get
    return bf.POEEdge(u, v, w)


edges = []
edges.append(getPrices(exalted_orb_have, chaos_orb_want, 1, 0))
edges.append(getPrices(exalted_orb_have, orb_of_fusing_want, 1, 2))
edges.append(getPrices(chaos_orb_have, orb_of_fusing_want, 0, 2))
edges.append(getPrices(chaos_orb_have, exalted_orb_want, 0, 1))
for edge in edges:
    print(num2curr[edge.u])
    print(num2curr[edge.v])
    print(edge.w)
