from time import sleep
from selenium import webdriver

# class POENode:

#     def __init__(self, ):


URL = "https://www.pathofexile.com/trade/search/Metamorph"
bulk_ex_button = "//div[@id='trade']/div[@class='navigation']/ul[1]//a[@href='/trade/exchange/Metamorph']"

chaos_orb_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[4]/img[@alt='Chaos Orb']"
exalted_orb_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[6]/img[@alt='Exalted Orb']"
orb_of_fusing_want = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[1]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[2]/img[@alt='Orb of Fusing']"

chaos_orb_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[4]/img[@alt='Chaos Orb']"
exalted_orb_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[6]/img[@alt='Exalted Orb']"
orb_of_fusing_have = "/html//div[@id='trade']/div[@class='top']/div[@class='search-panel']/div[2]/div/div[2]/div[@class='filter-group']/div[@class='filter-group-body']/div[1]/div[@class='filter-body']/div[2]/img[@alt='Orb of Fusing']"

send_button = "//div[@id='trade']/div[@class='top']//div[@class='controls-center']/button[@type='button']"


def getPrices(buy, sell):
    """ getPrices method returns the poe currency exchange using poe main website

    parameters:
        buy (str) : what currency do you want
        sell (str) : what currency do you have

    """

    driver = webdriver.Chrome()
    driver.get(URL)
    sleep(4)
    driver.find_element_by_xpath(bulk_ex_button).click()
    sleep(2)
    driver.find_element_by_xpath(buy).click()
    sleep(.5)
    driver.find_element_by_xpath(sell).click()
    sleep(.5)
    driver.find_element_by_xpath(send_button).click()
    sleep(3)
    price_pay = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) .price-right > .price-block > span:nth-of-type(1)").text
    price_get = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) .price-left > .price-block > span:nth-of-type(3)").text
    price_seller = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) a[target='_blank']").text
    price_stock = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(1) .pull-left.stock > span:nth-of-type(1)").text
    price_get2 = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(2) .price-left > .price-block > span:nth-of-type(3)").text
    price_pay2 = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(2) .price-right > .price-block > span:nth-of-type(1)").text
    price_seller2 = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(2) a[target='_blank']").text
    price_stock2 = driver.find_element_by_css_selector(
        ".exchange.resultset > div:nth-of-type(2) .pull-left.stock > span:nth-of-type(1)").text
    sleep(0.7)
    print(
        f"you pay {price_pay} exalted orbs and get {price_get} chaos orbs from vendor {price_seller} who has stock {price_stock}")
    print(
        f"you pay {price_pay2} exalted orbs and get {price_get2} chaos orbs from vendor {price_seller2} who has stock {price_stock2}")
    sleep(2)


getPrices(chaos_orb_want, exalted_orb_have)
