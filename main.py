#make sure to check if using interpreter and running selenium
#python3 -m pip show selenium
#which python3

from selenium import webdriver #allows the browser to launch
from selenium.webdriver.common.by import By #allows search with params
from selenium.webdriver.support.ui import WebDriverWait #allows waiting for info to load
from selenium.webdriver.support import expected_conditions as EC #determine whether page has loaded
from selenium.common.exceptions import TimeoutException #handle timeout exception
from selenium.webdriver.chrome.service import Service #manage chromedriver service


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

input("Press Enter to close the browser...") #keep the browser open until user input