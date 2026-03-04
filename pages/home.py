
# import time
# import random
# from utils.driver import create_driver
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from appium.webdriver.extensions.android.nativekey import AndroidKey


# def get_available_system_port():
#     return random.randint(8200, 8300)


# def select_location(driver, wait):
#     """Select location from address list"""
#     print("Attempting to select location...")
    
#     try:
#         element = wait.until(
#             EC.presence_of_element_located(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Google Building 40, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"]')

#             )
#         )
#         element.click()
#         print("Location screen detected")
#         time.sleep(2)

#         select_address_in_scroll_view(driver, "Lyxa BD, Bd, Bd")
        
#     except Exception as e:
#         print(f"Error in select_location: {e}")
#         try:
#             driver.find_element(
#                 AppiumBy.ACCESSIBILITY_ID,
#                 "Lyxa BD, Bd, Bd"
#             ).click()
#         except:
#             print("Could not find address using any method")


# def select_address_in_scroll_view(driver, address_desc):
#     """Scroll to an address using content-desc and click it"""
#     print(f"Attempting to scroll to and click address: {address_desc}")
    
#     try:
#         element = driver.find_element(
#             AppiumBy.ANDROID_UIAUTOMATOR,
#             f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{address_desc}"))'
#         )
#         element.click()
#         print(f"Successfully clicked address: {address_desc}")
        
#     except Exception as e:
#         print(f"UiAutomator scroll failed: {e}")
#         try:
#             element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_desc)
#             element.click()
#             print(f"Found address by accessibility ID: {address_desc}")
#         except Exception as e2:
#             print(f"Accessibility ID approach also failed: {e2}")
#             try:
#                 element = driver.find_element(AppiumBy.XPATH, f"//*[@text='{address_desc}']")
#                 element.click()
#                 print(f"Found address by text: {address_desc}")
#             except Exception as e3:
#                 print(f"All methods failed: {e3}")
#                 raise
#     time.sleep(5)


# def userAutomation(driver, wait):
#     """Helper: Search for products and add items to cart"""
#     print("Starting search and add to cart flow...")
    

        
#         xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'

#         wait = WebDriverWait(driver, 20)
#         element = wait.until(
#             EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
#         )

#         element.click()
        
#         driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").click()
        
#         xpath = ('//android.widget.ScrollView/android.view.ViewGroup/'
#          'android.view.ViewGroup/android.view.ViewGroup[5]/'
#          'android.view.ViewGroup/com.horcrux.svg.SvgView/'
#          'com.horcrux.svg.GroupView/com.horcrux.svg.PathView')

#         element = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((AppiumBy.XPATH, xpath))
#         )
#         element.click()
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Female")
#             )
#         )
#         element.click()
        
        
#         element = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]')
#             )
#         )
#         element.click()
        
#         xpath = (
#     '//android.widget.ScrollView/android.view.ViewGroup/'
#     'android.view.ViewGroup/android.view.ViewGroup[4]/'
#     'android.view.ViewGroup/com.horcrux.svg.SvgView/'
#     'com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
#     )

#         element = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((AppiumBy.XPATH, xpath))
#         )
#         element.click()
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Orders")
#             )
#         )
#         element.click()
        
#         parent_xpath = (
#         '//android.widget.FrameLayout[@resource-id="android:id/content"]'
#         '/android.widget.FrameLayout/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup/'
#         'android.widget.ScrollView/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup[4]'
#         '/android.view.ViewGroup'
#     )
#         driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
#         coupons = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Coupons")
#             )
#         )
#         coupons.click()
        
#         element = WebDriverWait(driver, 20).until(
#          EC.element_to_be_clickable(
#         (
#             AppiumBy.ACCESSIBILITY_ID,
#             "Coupon: Save 10%, Save: , Expires on 30-06-2026, Code PJN0ZP"
#                 )
#             )
#         )
#         element.click()
        
#         edit_text = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#                 (AppiumBy.XPATH, '//android.widget.EditText[@text="Enter coupon code"]')
#             )
#         )

#         edit_text.click()
#         edit_text.clear()
#         edit_text.send_keys("3Z1Z2Y")
        
#         add_coupon = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#             (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Coupon"]')
#             )
#         )
#         add_coupon.click()
        
        
#         parent_xpath = (
#         '//android.widget.ScrollView/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup[4]/'
#         'android.view.ViewGroup'
#         )

#         driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        
#         lbp_balance = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="LBP Balance"]')
#             )
#         )
#         lbp_balance.click()
        


#         wait = WebDriverWait(driver, 20)

#         # 1️⃣ Click "Add Funds"
#         add_funds = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Funds"]')
#             )
#         )
#         add_funds.click()

#         # 2️⃣ Find the amount input field
#         amount_input = wait.until(
#             EC.presence_of_element_located(
#                 (AppiumBy.CLASS_NAME, 'android.widget.EditText')
#             )
#         )

#         # 3️⃣ Type amount
#         amount_input.click()
#         amount_input.clear()
#         amount_input.send_keys("180000")

#         # Optional: hide keyboard
#         driver.hide_keyboard()

#         tokyo = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#         (AppiumBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')
#             )
#         )
#         tokyo.click()
        
#         next_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]')
#             )
#         )
#         next_btn.click()
        
        
#         confirm_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#             (AppiumBy.ID, "android:id/button1")
#                 )
#             )
#         confirm_btn.click()
        
        
#         parent_xpath = (
#         '//android.widget.FrameLayout[@resource-id="android:id/content"]'
#         '/android.widget.FrameLayout/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup/'
#         'android.widget.ScrollView/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup[4]'
#         '/android.view.ViewGroup'
#         )

#         driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        
#         faq = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#             (AppiumBy.ACCESSIBILITY_ID, "FAQ")
#             )
#         )
#         faq.click()
        
#         oh_lala = WebDriverWait(driver, 20).until(
#          EC.element_to_be_clickable(
#         (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
#             )
#         )
#         oh_lala.click()
        
#         time.sleep(2)
        
#         oh_lala = WebDriverWait(driver, 20).until(
#          EC.element_to_be_clickable(
#         (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
#             )
#         )
#         oh_lala.click()
        
#         parent_xpath = (
#         '//android.widget.ScrollView/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup[4]/'
#         'android.view.ViewGroup'
#         )

#         driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        
#         get_support = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#             (AppiumBy.ACCESSIBILITY_ID, "Get Support")
#             )
#         )
#         get_support.click()
        
        
#         support_account = WebDriverWait(driver, 20).until(
#          EC.element_to_be_clickable(
#         (AppiumBy.XPATH, '//android.widget.TextView[@text="Support For account"]')
#         )
#         )
#         support_account.click()
        
        
#         faq_item = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable(
#         (
#                     AppiumBy.XPATH,
#                     '//android.widget.TextView[@text="How do I update my payment information"]'
#                 )
#             )
#         )
#         faq_item.click()
        
#         chat_with_us = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Chat with us"]')
#             )
#         )
#         chat_with_us.click()
                
        
        
#         parent_xpath = (
#         '//android.widget.FrameLayout[@resource-id="android:id/content"]'
#         '/android.widget.FrameLayout/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup/'
#         'android.widget.ScrollView/android.view.ViewGroup/'
#         'android.view.ViewGroup/android.view.ViewGroup[5]'
#         '/android.view.ViewGroup'
#     )

#         driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        
        
#     driver.find_element(
#         AppiumBy.XPATH,
#         '//com.horcrux.svg.PathView/parent::com.horcrux.svg.GroupView/parent::com.horcrux.svg.SvgView/parent::android.view.ViewGroup'
#     ).click()
   
     
 
import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey


def get_available_system_port():
    return random.randint(8200, 8300)


def select_location(driver, wait):
    """Select location from address list"""
    print("Attempting to select location...")
    
    try:
        element = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Google Building 40, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"]')
            )
        )
        element.click()
        print("Location screen detected")
        time.sleep(2)

        select_address_in_scroll_view(driver, "Lyxa BD, Bd, Bd")
        
    except Exception as e:
        print(f"Error in select_location: {e}")
        try:
            driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Lyxa BD, Bd, Bd"
            ).click()
        except:
            print("Could not find address using any method")


def select_address_in_scroll_view(driver, address_desc):
    """Scroll to an address using content-desc and click it"""
    print(f"Attempting to scroll to and click address: {address_desc}")
    
    try:
        element = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{address_desc}"))'
        )
        element.click()
        print(f"Successfully clicked address: {address_desc}")
        
    except Exception as e:
        print(f"UiAutomator scroll failed: {e}")
        try:
            element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_desc)
            element.click()
            print(f"Found address by accessibility ID: {address_desc}")
        except Exception as e2:
            print(f"Accessibility ID approach also failed: {e2}")
            try:
                element = driver.find_element(AppiumBy.XPATH, f"//*[@text='{address_desc}']")
                element.click()
                print(f"Found address by text: {address_desc}")
            except Exception as e3:
                print(f"All methods failed: {e3}")
                raise
    time.sleep(5)


def userAutomation(driver, wait):
    """Helper: Search for products and add items to cart"""
    print("Starting search and add to cart flow...")
    
    try:
        xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'

        wait = WebDriverWait(driver, 20)
        element = wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
        )
        element.click()
        
        driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").click()
        
        xpath = ('//android.widget.ScrollView/android.view.ViewGroup/'
                 'android.view.ViewGroup/android.view.ViewGroup[5]/'
                 'android.view.ViewGroup/com.horcrux.svg.SvgView/'
                 'com.horcrux.svg.GroupView/com.horcrux.svg.PathView')

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        element.click()
        
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Female")
            )
        )
        element.click()
        
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]')
            )
        )
        element.click()
        
        xpath = ('//android.widget.ScrollView/android.view.ViewGroup/'
                 'android.view.ViewGroup/android.view.ViewGroup[4]/'
                 'android.view.ViewGroup/com.horcrux.svg.SvgView/'
                 'com.horcrux.svg.GroupView/com.horcrux.svg.PathView')

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        element.click()
        
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Orders")
            )
        )
        element.click()
        
        parent_xpath = (
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/'
            'android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[4]'
            '/android.view.ViewGroup'
        )
        driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        coupons = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Coupons")
            )
        )
        coupons.click()
        
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Coupon: Save 10%, Save: , Expires on 30-06-2026, Code PJN0ZP"
                )
            )
        )
        element.click()
        
        edit_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Enter coupon code"]')
            )
        )
        edit_text.click()
        edit_text.clear()
        edit_text.send_keys("3Z1Z2Y")
        
        add_coupon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Coupon"]')
            )
        )
        add_coupon.click()
        
        parent_xpath = (
            '//android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[4]/'
            'android.view.ViewGroup'
        )
        driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        lbp_balance = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="LBP Balance"]')
            )
        )
        lbp_balance.click()

        wait = WebDriverWait(driver, 20)

        # Click "Add Funds"
        add_funds = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Funds"]')
            )
        )
        add_funds.click()

        # Find the amount input field
        amount_input = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, 'android.widget.EditText')
            )
        )

        # Type amount
        amount_input.click()
        amount_input.clear()
        amount_input.send_keys("180000")

        # Hide keyboard
        driver.hide_keyboard()

        tokyo = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')
            )
        )
        tokyo.click()
        
        next_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]')
            )
        )
        next_btn.click()
        
        confirm_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "android:id/button1")
            )
        )
        confirm_btn.click()
        
        parent_xpath = (
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/'
            'android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[4]'
            '/android.view.ViewGroup'
        )
        driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        faq = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "FAQ")
            )
        )
        faq.click()
        
        oh_lala = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
            )
        )
        oh_lala.click()
        
        time.sleep(2)
        
        oh_lala = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
            )
        )
        oh_lala.click()
        
        parent_xpath = (
            '//android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[4]/'
            'android.view.ViewGroup'
        )
        driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        get_support = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Get Support")
            )
        )
        get_support.click()
        
        support_account = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Support For account"]')
            )
        )
        support_account.click()
        
        faq_item = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="How do I update my payment information"]'
                )
            )
        )
        faq_item.click()
        
        chat_with_us = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Chat with us"]')
            )
        )
        chat_with_us.click()
        
        parent_xpath = (
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/'
            'android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[5]'
            '/android.view.ViewGroup'
        )
        driver.find_element(AppiumBy.XPATH, parent_xpath).click()
        
        # Final click
        driver.find_element(
            AppiumBy.XPATH,
            '//com.horcrux.svg.PathView/parent::com.horcrux.svg.GroupView/parent::com.horcrux.svg.SvgView/parent::android.view.ViewGroup'
        ).click()
     
    except Exception as e:
        print(f"Error in userAutomation flow: {e}")
        raise