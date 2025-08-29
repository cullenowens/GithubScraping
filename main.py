#make sure to check if using interpreter and running selenium
#python3 -m pip show selenium
#which python3

from selenium import webdriver #allows the browser to launch
from selenium.webdriver.common.by import By #allows search with params
from selenium.webdriver.support.ui import WebDriverWait #allows waiting for info to load
from selenium.webdriver.support import expected_conditions as EC #determine whether page has loaded
from selenium.common.exceptions import TimeoutException #handle timeout exception
from selenium.webdriver.chrome.service import Service #manage chromedriver service
import pandas as pd #for saving data data to pandas library


driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" - incognito") #open in incognito mode
#can use "--headless" to run in background (no visible window), better w autometion, but some sites detect headless
#driver_option.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0 Safari/537.36)") #make the bot seem like a user
chromedriver_path = '/Users/cullenowens/Desktop/WebScraping/chromedriver-mac-x64/chromedriver' #path to chromedriver

def create_webdriver():
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

#open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']") #extract all the things in the website

project_list = {} #list to hold each projects information
for proj in projects:
    proj_name = proj.text #name of proj
    proj_url = proj.find_elements(By.XPATH, "a")[0].get_attribute("href") #url of proj
    project_list[proj_name] = proj_url
    #explore the opportunities of looking through these links

input("Press Enter to close the browser...") #keep the browser open until user input

browser.quit() #close the browser when done

project_df = pd.DataFrame.from_dict(project_list, orient = 'index') #onverts the dictionary to a dataframe

print(project_df) #print the dataframe