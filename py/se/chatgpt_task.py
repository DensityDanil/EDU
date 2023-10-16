from selenium import webdriver
#import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#geckodriver_autoinstaller.install()

profile = webdriver.FirefoxProfile(r"C:\Users\DanilAndNatasha\AppData\Roaming\Mozilla\Firefox\Profiles\re97x5y6.default")

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)

profile.update_preferences()
desired = DesiredCapabilities.FIREFOX


PATH0_geckdriver_x32 = r"C:\dev\python\geckodriver_v0.33.0-win64.exe"
PATH1_firefox_exe = r"C:\Program Files\Mozilla Firefox\firefox.exe" #https://stackoverflow.com/questions/66209119/automation-google-login-with-python-and-selenium-shows-this-browser-or-app-may

binary = FirefoxBinary(PATH1_firefox_exe)
options = webdriver.FirefoxOptions()

#options.headless = True

driver = webdriver.Firefox( options = options
                           ,executable_path = PATH0_geckdriver_x32
                           ,firefox_binary = binary
                           ,firefox_profile=profile
                           ,desired_capabilities=desired
                           )


# Відкриття веб-сайту
website_url = 'https://www.google.com'  # Замініть на URL вашого сайту
driver.get(website_url)

# Закриття браузера (необов'язково)
# driver.quit()
