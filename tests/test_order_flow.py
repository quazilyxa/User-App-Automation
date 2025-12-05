import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.appiumby import AppiumBy



def get_available_system_port():
    return random.randint(8200, 8300)

def test_launch_app():
    driver = create_driver()
    wait = WebDriverWait(driver, 20) 
    

    time.sleep(3)

#     login_to_unlock = wait.until(
#         EC.element_to_be_clickable((
#             By.XPATH,
#             "//android.widget.TextView[@text='Login to Unlock']"
#         ))
#     )
#     login_to_unlock.click()


# def test_login_and_location():
#     driver = create_driver()
#     wait = WebDriverWait(driver, 20)
    
#     # Continue with Email
#     continue_email_btn = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//android.widget.TextView[@text='Continue with Email']")
#         )
#     )
#     continue_email_btn.click()
    

#     email_field = wait.until(
#         EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Enter Email']"))
#     )
#     email_field.click()
#     email_field.send_keys("tokyo@mail.com")
    
    
#     password_field = wait.until(
#         EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Enter Password']"))
#     )
#     password_field.click()
#     password_field.send_keys("Dhaka@01")
    
#     driver.hide_keyboard()
    
  
#     login_btn = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Log in']"))
#     )
#     login_btn.click()
    
#     print("Waiting for login to complete...")
#     time.sleep(5) 
    
   
    start_ordering = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//android.widget.TextView[@text='Start Ordering!']"
        ))
    )
    start_ordering.click()
    time.sleep(3) 

  
    select_location(driver, wait)

    
    print("Login and location selection successful!")
    return driver


def select_location(driver, wait=None):
    """Select location from address list"""
    if wait is None:
        wait = WebDriverWait(driver, 20)
    
    print("Attempting to select location...")
    
    try:
        element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//android.widget.TextView[@text='Current']")
            )
        )
        element.click()
        print("Location screen detected")
        
        time.sleep(2)     

        select_address_in_scroll_view(driver, "Office, Lyxa, Lyxa Office")
        
    except Exception as e:
        print(f"Error in select_location: {e}")
        try:
            driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Office, Lyxa, Lyxa Office"
            ).click()
        except:
            print("Could not find address using any method")


def select_address_in_scroll_view(driver, address_desc):
    """Scroll to an address using content-desc and click it"""
    print(f"Attempting to scroll to and click address: {address_desc}")
    
    try:
        # Try UiScrollable first
        element = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{address_desc}"))'
        )
        element.click()
        print(f"Successfully clicked address: {address_desc}")
        
    except Exception as e:
        print(f"UiAutomator scroll failed: {e}")

        try:
            # Try accessibility ID
            element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_desc)
            element.click()
            print(f"Found address by accessibility ID: {address_desc}")
            
        except Exception as e2:
            print(f"Accessibility ID approach also failed: {e2}")
            
            try:
                # Try XPath as last resort
                element = driver.find_element(By.XPATH, f"//*[@text='{address_desc}']")
                element.click()
                print(f"Found address by text: {address_desc}")
            except Exception as e3:
                print(f"All methods failed: {e3}")
                raise
    time.sleep(5) 


def test_search_and_add_to_cart(driver=None, wait=None):
    """Test case 1: Search for products and add items to cart"""
    
    # Create driver if not provided
    if driver is None:
        driver = create_driver()
    
    if wait is None:
        wait = WebDriverWait(driver, 20)
    
    print("Starting search and add to cart flow...")
    
    try:
       
        wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[@content-desc=\"What’s on Your Shopping List?\"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]"
            ))
        ).click()


        time.sleep(3)
  
        search_input = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//android.widget.EditText[@text='Search']")
            )
        )
        search_input.click()
        search_input.send_keys("Test Location")
        time.sleep(3)
        driver.press_keycode(66)
        time.sleep(2)
        # driver.press_keycode(4)
        driver.press_keycode(AndroidKey.TAB)

        select_shop = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Location']"
            ))
        )
        select_shop.click()

        time.sleep(2)

        #adding product in details mood

        test_product = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.TextView[@text='Test Product']"
            ))
        )
        test_product.click()

        time.sleep(2)

        test_product = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.TextView[@text='Test Product']"
            ))
        )
        test_product.click()

        time.sleep(2)

        circle = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//com.horcrux.svg.CircleView"
            ))
        )
        circle.click()


        time.sleep(2)

        path_el = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
            ))
        )

        path_el.click()


        # time.sleep(2)

        special_input = wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//android.widget.EditText[@text='Enter Special Instructions']"
            ))
        )

        time.sleep(2)

        special_input.click()
        special_input.send_keys("please wait outside")

        target = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.FrameLayout[@resource-id='android:id/content']"
                "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                "/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup"
                "/android.view.ViewGroup/android.view.ViewGroup[5]"
                "/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
            ))
        )
        target.click()

        time.sleep(2)


        price_element = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'LBP')]"
            ))
        )
        price_element.click()

        time.sleep(3)

        driver.implicitly_wait(3)
        driver.swipe(300, 1200, 300, 700)

        # Add item to cart (Mug)
        target = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Mug, Buy 1 Get 1')]/android.view.ViewGroup[3]"
            ))
        )

        target.click()

        time.sleep(3)
        
        driver.swipe(300, 700, 300, 50)

        # Click on Final Check item
        target = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Final Check')]"
                "/android.view.ViewGroup[3]/android.view.ViewGroup"
            ))
        )

        target.click()

        
        print("✓ Items added to cart successfully!")
        return driver
        
    except Exception as e:
        print(f"✗ Error in search_and_add_to_cart: {e}")
        raise


def test_checkout_and_place_order(driver=None, wait=None):
    """Test case 2: Checkout and place order"""
    
    # Create driver if not provided
    if driver is None:
        driver = create_driver()
    
    if wait is None:
        wait = WebDriverWait(driver, 20)
    
    print("Starting checkout and place order flow...")
    
    try:
        # View basket
        view_basket = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'View Basket')]"
            ))
        )
        view_basket.click()
        time.sleep(2)
        wait = WebDriverWait(driver, 20)
        # Click checkout button
        checkout = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Checkout')]"
            ))
        )
        checkout.click()

        wait = WebDriverWait(driver, 20)
        placeOrder = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Place Order')]"
            ))
        )
        placeOrder.click()
        
        print("✓ Order placed successfully!")
        return driver
        
    except Exception as e:
        print(f" Error in checkout_and_place_order: {e}")
        raise


