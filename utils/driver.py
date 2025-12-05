from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "uiautomator2")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("appPackage", "com.lyxauserapp")
    options.set_capability("appActivity", "com.lyxauserapp.MainActivity")
    options.set_capability("noReset", True)

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver
