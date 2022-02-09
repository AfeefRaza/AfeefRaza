rom selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

PATH = "C:\Program Files\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get('https://www.bevmo.com/my-store/store-locator')
# print(driver.title)
# search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# search.send_keys('python')
# search.send_keys(Keys.RETURN)
try:
    driver.implicitly_wait(20)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.findAll('a', {'class': 'fp-link-secondary'})

    for result in results:
        print(result.text)
        # _url = result.find('a')['href']
        # print(_url)
        # print()

except:
    # driver.quit()
    pass

# _next = driver.find_element_by_css_selector('#pnnext').click()
