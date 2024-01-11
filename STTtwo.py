from time import sleep # Inbuilt
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options # pip install selenium
from selenium.webdriver.common.by import By # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Link = "https://www.textfromtospeech.com/en/voice-to-text/"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--headless-new")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(Link)

sleep(5)
histrytext=""
ChatNumber=0
start='toggle-dictation'
clear='clear-content'
changelang='//*[@id="select2-reader-voice-container"]'
textbox='text-box'

driver.find_element(by=By.ID,value=start).click()

def textscrapper():
    while True:
        text=driver.find_element(by=By.ID,value=textbox).text
        if len(str(text))==0:
            pass

        elif histrytext==text:
            ChatNumber=+1
        else:
            histrytext=text
            return text


while True:
    print(textscrapper())
