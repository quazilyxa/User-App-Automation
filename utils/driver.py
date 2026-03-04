from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "uiautomator2")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("appPackage", "com.lyxa.user")
    options.set_capability("appActivity", "com.lyxa.user.MainActivity")
    options.set_capability("noReset", True)

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver
# def create_driver():
#     options = UiAutomator2Options()
#     options.platform_name = "Android"
#     options.automation_name = "UiAutomator2"

#     # Real device specifics
#     options.device_name = "Samsung Galaxy A35"
#     options.udid = "R5CX517EZJR"
#     options.platform_version = "16"

#     # App
#     options.app = r"C:\Users\quazi\Downloads\preprodlates.apk" 

#     # Stability options (VERY important)
#     options.no_reset = True
#     options.full_reset = False
#     options.new_command_timeout = 300
#     options.auto_grant_permissions = True
#     options.ignore_hidden_api_policy_error = True
#     options.disable_window_animation = True

#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4723",
#         options=options
#     )
#     return driver