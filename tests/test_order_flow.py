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


def search_and_add_to_cart(driver, wait):
    """Helper: Search for products and add items to cart"""
    print("Starting search and add to cart flow...")
    
    try:
        # Click search icon
        search_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "S, e, a, r, c, h,  , f, o, r,  , p, i, z, z, a"
            ))
        )

        search_btn.click()
        print("✓ Clicked Search for pizza")


  
        # Search for location
        search_input = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.EditText[@text='Search']")
            )
        )
        search_input.click()
        search_input.send_keys("Test Location")
        time.sleep(3)
        driver.press_keycode(66)
        time.sleep(2)
        driver.press_keycode(AndroidKey.TAB)

        # Select shop
        select_shop = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Location']"
            ))
        )
        select_shop.click()
        time.sleep(2)

        # Select test product
        test_product = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Product']"
            ))
        )
        test_product.click()
        time.sleep(2)

        # Click product again
        test_product = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Product']"
            ))
        )
        test_product.click()
        time.sleep(2)

        # Click circle
        circle = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Product']/ancestor::android.view.ViewGroup//com.horcrux.svg.CircleView"
            ))
        ).click()

        time.sleep(2)

        # # Click path element
        # path_el = wait.until(
        #     EC.presence_of_element_located((
        #         AppiumBy.XPATH,
        #         "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
        #     ))
        # )
        # path_el.click()

        # # Enter special instructions
        # special_input = wait.until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         "//android.widget.EditText[@hint='Enter Special Instructions']"
        #     ))
        # )

        # special_input.click()
        # special_input.send_keys("please wait outside")

        
        # target = wait.until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         "//android.widget.FrameLayout[@resource-id='android:id/content']"
        #         "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
        #         "/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup"
        #         "/android.view.ViewGroup/android.view.ViewGroup[5]"
        #         "/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
        #     ))
        # )
        # target.click()
        # time.sleep(2)

        # Click price element
        price_element = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[contains(@content-desc,'LBP')]"
            ))
        )

        driver.execute_script("mobile: clickGesture", {
            "elementId": price_element.id
        })

        time.sleep(3)
        
        
# Find the yellow button container
        # target = wait.until(
        #     EC.presence_of_element_located((
        #         AppiumBy.XPATH,
        #         '//android.view.ViewGroup[@content-desc="LBP 180,000"]'
        #     ))
        # )
        
        # # Use mobile gesture to click
        # driver.execute_script('mobile: clickGesture', {'elementId': target.id})
        # print("✓ Clicked using mobile gesture")
        # time.sleep(2)
        # # Swipe to scroll
        # driver.swipe(300, 1200, 300, 700)

        # Add Mug to cart
        # target = wait.until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         "//android.view.ViewGroup[contains(@content-desc, 'Mug')]/android.view.ViewGroup[3]"
        #     ))
        # )
        # target.click()
        
        # target = wait.until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         "//android.view.ViewGroup[@content-desc='Mug, test, LBP 207,000']/android.view.ViewGroup[2]/android.view.ViewGroup"
        #     ))
        # )
        # target.click()
        # time.sleep(3)
        
        # driver.swipe(300, 700, 300, 50)

        # Click Final Check
    #     target = wait.until(
    #         EC.element_to_be_clickable((
    #             AppiumBy.XPATH,
    #             "//android.view.ViewGroup[contains(@content-desc, 'Final Check')]"
    #             "/android.view.ViewGroup[3]/android.view.ViewGroup"
    #         ))
    #     )
    #     driver.execute_script("mobile: clickGesture", {
    #     "elementId": el.id
    # })
    #     target.click()
        
        print("✓ Items added to cart successfully!")
        
    except Exception as e:
        print(f"✗ Error in search_and_add_to_cart: {e}")
        raise


def checkout_and_place_order(driver, wait):
    """Helper: Checkout and place order"""
    print("Starting checkout and place order flow...")
    
    try:
        # View basket
        view_basket = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'View Basket')]"
            ))
        )
        view_basket.click()
        time.sleep(2)

        # Click checkout button
        checkout = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Checkout')]"
            ))
        )
        checkout.click()

        # Place order
        placeOrder = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Place Order')]"
            ))
        )
        placeOrder.click()
        
        print("✓ Order placed successfully!")
        
    except Exception as e:
        print(f"✗ Error in checkout_and_place_order: {e}")
        raise


# ==========================================
# MAIN TEST - This is what pytest will run
# ==========================================
def test_complete_order_flow():
    """Complete end-to-end order flow test"""
    print("TEST STARTED")
    
    driver = None
    try:
        # Initialize driver
        driver = create_driver()
        wait = WebDriverWait(driver, 20)
        
        print("✓ App launched")
        time.sleep(3)

        # # Start ordering
        # start_ordering = wait.until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         "//android.widget.TextView[@text='Start Ordering!']"
        #     ))
        # )
        # start_ordering.click()
        # time.sleep(3)
        # print("✓ Clicked 'Start Ordering'")

        # Select location
        select_location(driver, wait)
        print("✓ Location selected")

        # Search and add to cart
        search_and_add_to_cart(driver, wait)
        print("✓ Items added to cart")

        # Checkout and place order
        checkout_and_place_order(driver, wait)
        print("✓ Order placed")

        print("🎉 COMPLETE ORDER FLOW TEST PASSED 🎉")
        
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        if driver:
            driver.save_screenshot("error_screenshot.png")
        raise
        
    finally:
        if driver:
            driver.quit()
            print("✓ Driver closed")