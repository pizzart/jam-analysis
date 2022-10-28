import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
driver = Firefox(options=options)


def req_main_page(username: str):
    source = ''
    # print(f'https://ldjam.com/users/{username}/games')
    driver.get(f'https://ldjam.com/users/{username}/games')
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, '-cover'))
        )
        source = driver.page_source
    except selenium.common.exceptions.TimeoutException:
        print('timed out.')
    # finally:
        # driver.quit()
    return source


def req_game_pages(links: list):
    source_list = []
    event_nums = []
    for link in links:
        # print(f'https://ldjam.com{link}')
        # source = ''
        # try:
        driver.get(f'https://ldjam.com{link}')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, '-grade'))
            )
            source_list.append(driver.page_source)
            event_nums.append(link.split('/')[3])
        except selenium.common.exceptions.TimeoutException:
            print('timed out.')
        # except:
            # print('FAILED TO LOAD GAME PAGE.')
    # driver.quit()
    return (source_list, event_nums)


def req_stat_pages(nums: list):
    event_stat_pages = []
    for num in nums:
        # print(f'https://ldjam.com{link}')
        # source = ''
        # try:
        driver.get(f'https://ldjam.com/events/ludum-dare/{num}/stats')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'content-common-body'))
            )
            event_stat_pages.append(driver.page_source)
        except selenium.common.exceptions.TimeoutException:
            print('timed out.')
        # except:
            # print('FAILED TO LOAD GAME PAGE.')
    driver.quit()
    return event_stat_pages
