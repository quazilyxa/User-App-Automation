import time
import random

from attrs import fields
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction






# """
# In this file follwoing USER APP AUTOMATION FEATURES TESTED:
# ===========================================================

# 1. LOCATION MANAGEMENT
#    -------------------
#    - Initial location selection from address list
#    - Scrolling and selecting specific address (Lyxa BD, Bd, Bd)
#    - Multiple address selection strategies (XPATH, accessibility ID, UiAutomator)

# 2. HOME SCREEN & NAVIGATION
#    -------------------------
#    - Shopping List SVG interaction (center-tap for React Native elements)
#    - Offers section navigation
#    - Category browsing (Food, Grocery)
#    - Fresh category SVG interaction

# 3. OFFERS & PROMOTIONS
#    --------------------
#    - Offers tab access
#    - 10% Off offer selection
#    - Apply button interactions

# 4. SEARCH FUNCTIONALITY
#    ---------------------
#    - Search trigger clicks ("Search food", "Search groceries")
#    - EditText interactions (click, clear, send_keys)
#    - Search execution with ENTER key
#    - Search result selection (Test Location, Grocery Point)
#    - Store/product search within categories

# 5. CATEGORY BROWSING
#    -------------------
#    - Food category navigation
#    - Grocery category navigation
#    - Vegetables tab selection
#    - Product filtering and sorting

# 6. SORTING & FILTERING
#    --------------------
#    - Sort By option selection
#    - Price low to high sorting
#    - Apply button confirmations

# 7. PRODUCT INTERACTIONS
#    ---------------------
#    - Product selection
#    - Vegetable search (turnip)
#    - SVG PathView interactions (multiple instances)
#    - Copy text functionality
#    - Share SVG interactions

# 8. USER ACCOUNT FEATURES
#    ----------------------
#    - Profile menu access
#    - Favorites section
#    - Items tab navigation
#    - Support Tickets access
#    - Account Chat feature
#    - Legal section navigation
#    - Terms and Conditions viewing
#    - Logout functionality

# 9. DISCOVERY FEATURES
#    -------------------
#    - Hidden gems discovery
#    - Near Shops exploration
#    - Groceries tab in explore view
#    - Pinch zoom gesture (zoom_out method)
#    - Swipe gestures for scrolling

# 10. ORDER MANAGEMENT
#     -----------------
#     - Order Again feature
#     - Previous order interactions

# 11. CUSTOMER SUPPORT
#     -----------------
#     - Support Tickets section
#     - Account Chat access
#     - Legal documentation (Terms and Conditions)

# 12. UI ELEMENT INTERACTIONS
#     ------------------------
#     - SVG elements (SvgView, GroupView, PathView)
#     - ImageView elements
#     - TextView elements
#     - EditText fields
#     - ScrollView navigation
#     - Back button navigation
#     - Accessibility ID elements
#     - Content-desc attributes

# 13. GESTURE AUTOMATIONS
#     --------------------
#     - Tap at coordinates (center-tap for React Native)
#     - Swipe gestures (vertical scrolling)
#     - Pinch zoom (pinchOpenGesture)
#     - Back navigation

# 14. WAIT STRATEGIES
#     ----------------
#     - Explicit waits with expected conditions
#     - Presence of element
#     - Element clickability
#     - Visibility of element

# 15. ERROR HANDLING
#     ---------------
#     - Try-catch blocks for robust execution
#     - Multiple element location fallbacks
#     - Screenshot capture on failure

# 16. SPECIALIZED INTERACTIONS
#     -------------------------
#     - React Native element handling (center-tap required)
#     - UiAutomator selectors for complex element finding
#     - Multiple SVG PathView instance selection
#     - Copy text functionality testing

# 17. SEARCH VARIATIONS
#     ------------------
#     - Location search: "Test Location"
#     - Store search: "grocery point"
#     - Product search: "turnip" within Vegetables category

# 18. PROFILE & SETTINGS
#     -------------------
#     - Profile menu navigation
#     - Favorites management
#     - Support tickets
#     - Account chat
#     - Legal documents
#     - Logout process
# """





class TestUserAutomation:
    """Test suite for user automation"""
    
    driver = None
    wait = None
    
    @classmethod
    def setup_class(cls):
        """Setup driver once for all tests"""
        cls.driver = create_driver()
        cls.wait = WebDriverWait(cls.driver, 20)
        print("✓ App launched")
        time.sleep(3)
        
        # Select location
        try:
            select_location(cls.driver, cls.wait)
            print("✓ Location selected")
        except Exception as e:
            print(f"Location selection failed: {e}")

    
    def test_user_automation_flow(self):
        print("🚀 Starting user automation flow...")

        driver = self.driver
        wait = self.wait

        try:
            # filter_btn = wait.until(
            #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Filter"))
            # )
            # filter_btn.click()
            # print("✓ Filter button clicked")
            # time.sleep(2)

            
            # offers_btn = self.wait.until(
            #     EC.element_to_be_clickable((
            #         AppiumBy.XPATH,
            #         '//android.widget.TextView[@text="Offers"]'
            #     ))
            # )

            # offers_btn.click()
            # print("✓ Clicked Offers")
            # time.sleep(2)

            
            # offer_10_percent = self.wait.until(
            #     EC.element_to_be_clickable((
            #         AppiumBy.XPATH,
            #         '//android.widget.TextView[@text="10% Off"]'
            #     ))
            # )

            # offer_10_percent.click()
            # print("✓ Clicked 10% Off offer")
            # time.sleep(2)
            
            # apply_btn = self.wait.until(
            #     EC.element_to_be_clickable((
            #         AppiumBy.XPATH,
            #         '//android.widget.TextView[@text="Apply"]'
            #     ))
            # )

            # apply_btn.click()
            # print("✓ Clicked Apply")
            # time.sleep(2)
            # self.driver.back()
            
            
            
            
            
            
            

            # time.sleep(3)
            category_row = driver.find_element(
                AppiumBy.XPATH,
                "//android.widget.FrameLayout[@resource-id='android:id/content']"
                "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                "/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView"
                "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"
                "/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup"
                "/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup"
            )

            driver.execute_script("mobile: swipeGesture", {
                "elementId": category_row.id,
                "direction": "left",
                "percent": 0.7
            })
            
            time.sleep(3)
            
            courier_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Courier"]'))
            )
            courier_btn.click()
            time.sleep(3)
            
            
            purchase_delivery = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Purchase & Delivery"]'))
            )
            purchase_delivery.click()
            
            time.sleep(3)
            
            icon_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Icon button"))
            )
            icon_btn.click()
            
            time.sleep(3)
            
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, "android:id/button3"))
            )
            btn.click()
            
            time.sleep(3)
            
            
            shutter_btn = wait.until(
            EC.element_to_be_clickable((
            AppiumBy.ID,
            "com.sec.android.app.camera:id/shutter_area"
                ))
            )
            shutter_btn.click()
            print("✓ Photo captured")
                
            time.sleep(2)
                
            ok_btn = wait.until(
            EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/navigation_bar_item_small_label_view" and @text="OK"]'
                ))
            )
            ok_btn.click()
            print("✓ Photo confirmed")    
                
            time.sleep(2)    
            
            input_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.FrameLayout[@resource-id='android:id/content']"
                "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                "/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView"
                "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                "/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]"
                ))
            )

            input_field.click()
            edit_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.CLASS_NAME,
                    "android.widget.EditText"
                ))
            )
            edit_text.send_keys("Test Product")
            time.sleep(2)    
            
            price_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.EditText[@text="Enter Price"]'
                ))
            )
            price_field.click()
            price_field.send_keys("450000")
            time.sleep(1)   
            
            quantity_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.EditText[@text="Enter Quantity"]'
                ))
            )
            quantity_field.click()
            quantity_field.clear()
            quantity_field.send_keys("2")
            time.sleep(1)  
            
            
            checkout_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Checkout"]'
                ))
            )
            checkout_btn.click()
            
            time.sleep(3)
            
            pickup_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Add Pickup Details"]'
                ))
            )
            pickup_btn.click()
            time.sleep(2)
            
            autofill_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Auto Fill My Details"]'
                ))
            )
            autofill_btn.click()
            time.sleep(1)
            
            confirm_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//*[@content-desc="Confirm"]'
                ))
            )
            confirm_btn.click()
            time.sleep(3)
            
            
            drop_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Add Drop off Details"]'
                ))
            )
            drop_btn.click()
            time.sleep(2)
            
            fields = WebDriverWait(driver, 10).until(
                lambda d: d.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            )
            
            fields[0].click()
            fields[0].clear()
            fields[0].send_keys("Test User")
            time.sleep(2)
            
            random_number = str(random.randint(1000000, 9999999))

            fields[1].click()
            fields[1].clear()
            fields[1].send_keys(random_number)

            print(f"✓ Mobile entered: {random_number}")
            
            time.sleep(2)
            
            def tap(driver, x, y):
                actions = ActionChains(driver)
                actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(x, y)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.pause(0.1)
                actions.w3c_actions.pointer_action.release()
                actions.perform()

            # Use exact coordinates from Appium Inspector
            tap(driver, 385, 1547)
            print("✓ Clicked Home / Test, Gulshan")
            print("✓ Clicked via coordinates")
            
            time.sleep(2)
            confirm_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//*[@content-desc="Confirm"]'
                ))
            )
            confirm_btn.click()
            time.sleep(1)
            
            
            
            
            
            food_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Food"))
            )
            food_btn.click()

            print("✓ Clicked Food image")
            time.sleep(4)

            
            search_trigger = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Search food"]')
                )
            )
            search_trigger.click()

            # Wait for ANY EditText to appear
            search_input = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, 'android.widget.EditText')
                )
            )

            search_input.click()
            search_input.clear()
            search_input.send_keys("Test Shop")
            

            # Trigger search
            self.driver.press_keycode(AndroidKey.ENTER)


            print("✓ Typed search text and pressed Enter")
            time.sleep(2)
        
            test_location_title = self.wait.until(
            EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Test Shop"]'
                ))
            )

            test_location_title.click()
            print("✓ Clicked Test Shop title")
            time.sleep(5)
            
            self.driver.swipe(300, 1200, 300, 700)
            time.sleep(5)
            self.driver.back()
            self.driver.back()
            self.driver.back()
            time.sleep(2)
            
            # //////////////////////////////////////////////
  
        
        
            image_xpath = (
                '//android.view.ViewGroup[@content-desc="Grocery"]'
                '/android.view.ViewGroup/android.widget.ImageView'
            )

            image = self.wait.until(
                    EC.presence_of_element_located((
                        AppiumBy.XPATH,
                        image_xpath
                    ))
                )

            # Tap center of the image
            x = image.location['x'] + image.size['width'] / 2
            y = image.location['y'] + image.size['height'] / 2
            self.driver.tap([(x, y)])

            print("✓ Clicked Grocery image")
            time.sleep(2)        
        
            search_trigger = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Search groceries"]')
                )
            )
            search_trigger.click()

            # Wait for ANY EditText to appear
            search_input = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, 'android.widget.EditText')
                )
            )

            search_input.click()
            search_input.clear()
            search_input.send_keys("grocery point")
            

            # Trigger search
            self.driver.press_keycode(AndroidKey.ENTER)


            print("✓ Typed search text and pressed Enter")
            time.sleep(2)
        
            grocery_point_title = self.wait.until(
            EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Grocery Point"]'
                ))
            )

            grocery_point_title.click()
            print("✓ Clicked Grocery Point title")
            time.sleep(2)
        
        
            vegetables_tab = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Vegetables"]'
                ))
            )

            vegetables_tab.click()
            print("✓ Clicked Vegetables")
            time.sleep(2)
            
            search_title = self.wait.until(
            EC.presence_of_element_located(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "vegetable")]/..'
                    )
                )
            )
            search_title.click()

            # Wait for the search input (top search bar)
            search_input = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, 'android.widget.EditText')
                )
            )

            search_input.click()
            search_input.clear()
            search_input.send_keys("turnip")

            # Trigger search
            self.driver.press_keycode(AndroidKey.ENTER)

            print("✓ Searched for turnip")
            
            grocery_point = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Turnip"]'
                ))
            )
            grocery_point.click()
            
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("com.horcrux.svg.PathView").instance(2)'
            ).click()
            
            copy_text = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.FrameLayout[@content-desc="Copy text"]'
                ))
            )
            copy_text.click()

            
            self.driver.back()
            self.driver.back()
            self.driver.back()
            
        
            time.sleep(5)


            time.sleep(2)
            
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("com.horcrux.svg.PathView").instance(2)'
            ).click()

            print("✓ Clicked share SVG")
            
            copy_text = self.wait.until(
            EC.element_to_be_clickable((
            AppiumBy.XPATH,
                    '//android.widget.FrameLayout[@content-desc="Copy text"]'
                ))
            )

            copy_text.click()
            print("✓ Clicked Copy text")
            time.sleep(1)
            self.driver.back()
            self.driver.back()
            self.driver.back()
            time.sleep(2)

            
            
            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            element.click()
            print("✓ Profile screen opened")
                
            favorites = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Favorites"]'
                ))
            )
            favorites.click()    
                        
            items_tab = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Items"]'
                ))
            )
            items_tab.click()
            time.sleep(4)
                
            self.driver.back()
            self.driver.back()
            
            support_tickets = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Support Tickets"]'
            ))
            )
            support_tickets.click()
            
            time.sleep(2)
            
            account_chat = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Account Chat"]'
                ))
            )
            account_chat.click()
            
            time.sleep(4)
            self.driver.back()
            self.driver.back()
            
            legal = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Legal"]'
                ))
            )
            legal.click()
            
            terms = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Terms and Conditions"]'
                ))
            )
            terms.click()
                        
            time.sleep(6)
            self.driver.back()
            self.driver.back()
            self.driver.back()
            
            
            
            self.driver.swipe(300, 1200, 300, 700)
            


            # self.zoom_out()
        

            self.driver.back()

            near_shops = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Near Shops"
                ))
            )
            near_shops.click()
            print("✓ Clicked Near Shops")
            time.sleep(5)
            self.driver.swipe(300, 1500, 300, 500)
            time.sleep(7)
            self.driver.back()
            
            self.driver.swipe(300, 1800, 300, 400)
            
            order_again = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Order Again")
                )
            )
            order_again.click()
            print("✓ Clicked Order Again")
            time.sleep(4)
            # self.driver.swipe(300, 1500, 300, 500)
            # time.sleep(7)
            self.driver.back()
            
            
            xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'

            element = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
            )
            element.click() 
            print("✓ Opened profile menu")
            time.sleep(3)
            

            logout = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.view.ViewGroup[@content-desc="Log out"]'
                ))
            )
            logout.click()
            time.sleep(2)
            print("✓ Clicked Log out")

            print("✓ User automation flow completed successfully")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_automation_failure.png")
            raise


def select_location(driver, wait):
    """Select location from address list"""
    print("Attempting to select location...")
    
    try:
        element = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Test']")
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


def zoom_out(self):
            size = self.driver.get_window_size()
            center_x = size["width"] // 2
            center_y = size["height"] // 2

            self.driver.execute_script("mobile: pinchOpenGesture", {
                "left": center_x - 200,
                "top": center_y - 200,
                "width": 400,
                "height": 400,
                "percent": 0.5
            })




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