import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
driver = Firefox(options=options)


def req_main_page():
    source = ''
    driver.get('https://ldjam.com/users/pizzart64/games')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, '-cover'))
        )
        source = driver.page_source
    except selenium.common.exceptions.TimeoutException:
        print('timed out.')
    finally:
        driver.quit()
    return source


def req_game_pages(links: list):
    source_list = []
    for link in links:
        print(link)
        # source = ''
        try:
            driver.get(link)
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, '-grade'))
                )
                source_list.append(driver.page_source)
            except selenium.common.exceptions.TimeoutException:
                print('timed out.')
        except:
            print('FAILED TO LOAD GAME PAGE.')
    driver.quit()
    return source_list
