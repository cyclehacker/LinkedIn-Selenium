import csv
import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector

writer = csv.writer(open(parameters.result_file, 'w'))
writer.writerow(['name', 'job_title', 'location', 'schools', 'ln_url'])

driver = webdriver.Chrome('/home/cyrpto-cypher/Programming/chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://www.linkedin.com/')
sleep(4)

driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

username_input = driver.find_element_by_name('session_key')
username_input.send_keys(parameters.username)
sleep(0.5)

password_input = driver.find_element_by_name('session_password')
password_input.send_keys(parameters.password)
sleep(0.5)

# click on the sign in button
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(3)

# skip adding phone number if asked
skip = driver.find_elements_by_xpath('//button[text()="Skip"]')
if skip:
    skip.click()
    sleep(4)
else:
    pass

# use google.com to list linked in profiles
driver.get('https://google.com')
sleep(3)

# input search details into search field and return results
search_input = driver.find_element_by_name("q")
search_input.send_keys(parameters.search_query)
search_input.send_keys(Keys.RETURN)

# gather profiles
profiles = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
profiles = [profile.get_attribute('href') for profile in profiles]
for profile in profiles:
    driver.get(profile)
    sleep(5)
    sel = Selector(text=driver.page_source)
    name = sel.xpath('//title/text()').extract_first().split(' | ')[0].split('(20) ')[1]
    job_title = sel.xpath('//h2/text()').extract()[1].strip()
    location = sel.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first().strip()
    schools = sel.xpath('//*[contains(@class, "pv-entity__school-name")]/text()').extract()
    ln_url = driver.current_url

    print('\n')
    print(name)
    print(job_title)
    print(location)
    print(schools)
    print(ln_url)
    print('\n')

    writer.writerow([name, job_title, location, schools, ln_url])

driver.quit()