from time import sleep # Inbuilt
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options # pip install selenium
from selenium.webdriver.common.by import By # pip install selenium
import warnings # Inbuilt
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



Link = "https://readloud.net/english/british/1-male-voice-brian.html"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--headless-new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(Link)



def WaitForWeb():
    sleep(2)
    while True:
        try:                        
            driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea')
            break
            
        except:
            pass


def speak(Text):
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').send_keys(Text)
    
    except:
        pass

    sleep(0.8)
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/span/input').click()
    
    except:
        pass
    
    sleep(0.8)

    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').clear()
    
    except:
        pass




