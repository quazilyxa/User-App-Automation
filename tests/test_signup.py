# import random
# import string
# import time
# from utils.driver import create_driver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.common.exceptions import TimeoutException


# # ================================
# # RANDOM DATA GENERATORS
# # ================================

# def generate_random_name():
#     length = random.randint(6, 7)
#     return ''.join(random.choices(string.ascii_letters, k=length))


# def generate_random_email():
#     random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
#     return f"{random_part}@testmail.com"

# def tap_element(driver, element):
#     """
#     Taps the center of an element using clickGesture.
#     Works for SVG, ViewGroup, and React Native elements.
#     """
#     driver.execute_script("mobile: clickGesture", {
#         "elementId": element.id
#     })

# # ================================
# # HELPER: TAP ELEMENT BY COORDINATES
# # ================================

# def tap_element(driver, element):
#     """
#     Taps the center of an element using screen coordinates.
#     Reliable for SVG, ViewGroup, and React Native elements
#     that block standard .click() interactions.
#     """
#     location = element.location
#     size = element.size
#     x = int(location['x'] + size['width'] / 2)
#     y = int(location['y'] + size['height'] / 2)
#     driver.execute_script("mobile: tap", {"x": x, "y": y})


# # ================================
# # SIGNUP FUNCTION
# # ================================

# def signup_user(driver, wait, name, email, password):
#     """Helper: Perform user signup"""

#     print("Starting signup flow...")

#     try:
#         # ── Step 1: Continue ──────────────────────────────────────────────
#         continue_btn = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[@text='Continue']"
#             ))
#         )
#         continue_btn.click()
#         time.sleep(2)

#         # ── Step 2: Allow location permission ────────────────────────────
#         try:
#             driver.find_element(
#                 AppiumBy.XPATH,
#                 '//android.widget.Button[@text="While using the app"]'
#             ).click()
#             time.sleep(2)
#         except Exception:
#             print("⚠ Location permission dialog not shown, continuing...")

#         # ── Step 3: Skip ──────────────────────────────────────────────────
#         skip_btn = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[@text='Skip']"
#             ))
#         )
#         skip_btn.click()
#         time.sleep(5)


#         profile_icon = wait.until(
#             EC.presence_of_element_located((
#                 AppiumBy.XPATH,
#                 '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
#             ))
#         )

#         driver.execute_script("mobile: clickGesture", {
#             "elementId": profile_icon.id
#         })

#         print("✓ Profile icon clicked")

#         # ── Step 5: Click Sign up ─────────────────────────────────────────
#         signup_btn = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[@text='Sign up']"
#             ))
#         )
#         signup_btn.click()
#         time.sleep(2)

#         # ── Step 6: Enter Name ────────────────────────────────────────────
#         name_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.EditText[contains(@text,'Enter Name')]"
#             ))
#         )
#         name_field.click()
#         name_field.clear()
#         random_name = generate_random_name()
#         name_field.send_keys(random_name)
#         print(f"✓ Entered name: {random_name}")
#         time.sleep(1)

#         # ── Step 7: Enter Email ───────────────────────────────────────────
#         email_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.EditText[contains(@text,'Enter Email')]"
#             ))
#         )
#         email_field.click()
#         email_field.clear()
#         random_email = generate_random_email()
#         email_field.send_keys(random_email)
#         print(f"✓ Entered email: {random_email}")
#         time.sleep(3)

#         # ── Step 8: Select Male radio button ─────────────────────────────
#         # content-desc="Male" ViewGroup also has SVG inside — tap by coords
#         male_radio = wait.until(
#             EC.presence_of_element_located((
#                 AppiumBy.XPATH,
#                 '//android.view.ViewGroup[@content-desc="Male"]'
#             ))
#         )

#         driver.execute_script("mobile: clickGesture", {
#             "elementId": male_radio.id
#         })

#         print("✓ Male radio selected")

#         # ── Step 9: Enter Password ────────────────────────────────────────
#         password_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.EditText[contains(@text,'Enter Password')]"
#             ))
#         )
#         password_field.click()
#         password_field.clear()
#         password_field.send_keys("Dhaka@01")
#         print("✓ Password entered")
#         time.sleep(1)
#         try:
#             driver.hide_keyboard()
#         except Exception:
#             pass

#         # ── Step 10: Confirm Password ─────────────────────────────────────
#         confirm_password_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.EditText[contains(@text,'Confirm Password')]"
#             ))
#         )
#         confirm_password_field.click()
#         confirm_password_field.clear()
#         confirm_password_field.send_keys("Dhaka@01")
#         print("✓ Confirm password entered")
#         time.sleep(1)
#         try:
#             driver.hide_keyboard()
#         except Exception:
#             pass

#         # ── Step 11: Accept Terms checkbox (SVG) ─────────────────────────
#         terms_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]' \
#                         '/android.widget.FrameLayout' \
#                         '/android.view.ViewGroup' \
#                         '/android.view.ViewGroup' \
#                         '/android.view.ViewGroup' \
#                         '/android.view.ViewGroup' \
#                         '/android.widget.ScrollView' \
#                         '/android.view.ViewGroup' \
#                         '/android.view.ViewGroup' \
#                         '/android.widget.ScrollView' \
#                         '/android.view.ViewGroup' \
#                         '/android.view.ViewGroup[11]' \
#                         '/com.horcrux.svg.SvgView' \
#                         '/com.horcrux.svg.GroupView' \
#                         '/com.horcrux.svg.PathView'

#         terms_checkbox = wait.until(
#             EC.element_to_be_clickable((AppiumBy.XPATH, terms_xpath))
#         )
#         terms_checkbox.click()
#         time.sleep(2)

#         # ── Step 12: Final Sign Up button ─────────────────────────────────
#         final_signup = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[@text='Sign Up']"
#             ))
#         )
#         final_signup.click()
#         time.sleep(3)

#         # ── Step 13: Enter Phone Number ───────────────────────────────────
#         random_number = ''.join(random.choices("0123456789", k=7))
#         full_number = "961" + random_number
#         print(f"Final phone number: {full_number}")

#         phone_input = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.CLASS_NAME,
#                 "android.widget.EditText"
#             ))
#         )
#         phone_input.click()
#         phone_input.clear()
#         phone_input.send_keys(full_number)
#         print("✓ Phone number entered successfully")

#         cont_btn = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[contains(@text,'Continue')]"
#             ))
#         )
#         cont_btn.click()
#         time.sleep(6)

#         # ── Step 14: Enter OTP (Digit by Digit with 3s delay) ─────────────

# # ── Step 14: Enter OTP Digit by Digit (Fixed) ─────────────

#         otp_code = "231220"

#         # Android keycode mapping
#         keycode_map = {
#             "0": 7,
#             "1": 8,
#             "2": 9,
#             "3": 10,
#             "4": 11,
#             "5": 12,
#             "6": 13,
#             "7": 14,
#             "8": 15,
#             "9": 16
#         }

#         # Click first OTP box
#         first_box = wait.until(
#             EC.presence_of_element_located((
#                 AppiumBy.XPATH,
#                 "//android.widget.ScrollView/android.view.ViewGroup"
#                 "/android.view.ViewGroup/android.view.ViewGroup[4]"
#             ))
#         )

#         driver.execute_script("mobile: clickGesture", {
#             "elementId": first_box.id
#         })

#         time.sleep(0.5)

#         # Enter digits one by one
#         for digit in otp_code:
#             driver.press_keycode(keycode_map[digit])
#             print(f"Entered digit: {digit}")
#             time.sleep(3)

#         print("✓ OTP entered digit by digit")

#         # ── Step 15: Handle optional permission popup ─────────────────────
#         try:
#             allow_btn = WebDriverWait(driver, 2).until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_button"
#                 ))
#             )
#             allow_btn.click()
#             print("✓ Permission allowed")
#         except TimeoutException:
#             print("✓ Permission popup not shown, continuing...")

#         # ── Step 16: Done ─────────────────────────────────────────────────
#         done_btn = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 "//android.widget.TextView[contains(@text,'Done')]"
#             ))
#         )
#         done_btn.click()
#         print("✓ Account created successfully")
        

#         current_btn = wait.until(
#         EC.element_to_be_clickable((
#         AppiumBy.XPATH,
#                 '//android.widget.TextView[@text="Current"]'
#             ))
#         )

#         current_btn.click()
#         print("✓ Clicked on Current")
                
#         time.sleep(3)
        
#         add_location_btn = wait.until(
#         EC.element_to_be_clickable((
#         AppiumBy.ACCESSIBILITY_ID,
#         "Add new location"
#             ))
#         )

#         add_location_btn.click()
#         print("✓ Clicked on Add new location")
        
#         time.sleep(3)
        
#         confirm_btn = wait.until(
#          EC.element_to_be_clickable((
#         AppiumBy.XPATH,
#         '//android.widget.TextView[@text="Confirm and Add Details"]'
#             ))
#         )

#         confirm_btn.click()
#         print("✓ Clicked on Confirm and Add Details")
#         time.sleep(3)
        
#         home_btn = wait.until(
#          EC.element_to_be_clickable((
#         AppiumBy.XPATH,
#         '//android.widget.TextView[@text="Home"]'
#             ))
#         )

#         home_btn.click()
#         print("✓ Clicked on Home")
        
        
#         # ── Enter Apt/Suite/Floor ─────────────────────────────

#         apt_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 '//android.widget.EditText[@text="Enter Apt/Suite/Floor"]'
#             ))
#         )

#         apt_field.click()
#         apt_field.clear()
#         apt_field.send_keys("Dhaka")
#         print("✓ Entered Dhaka in Apt/Suite/Floor")


#         # ── Enter Business or Building name ───────────────────

#         building_field = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 '//android.widget.EditText[@text="Business or Building name"]'
#             ))
#         )

#         building_field.click()
#         building_field.clear()
#         building_field.send_keys("Rampura")
#         print("✓ Entered Rampura in Business/Building name")


#         # ── Click Save Address ────────────────────────────────

#         save_btn = wait.until(
#             EC.presence_of_element_located((
#                 AppiumBy.XPATH,
#                 '//android.widget.TextView[@text="Save Address"]/parent::*'
#             ))
#         )

#         driver.execute_script("mobile: clickGesture", {
#             "elementId": save_btn.id
#         })

#         print("✓ Clicked Save Address")
        
        
#         # ----------------------------------------------------------------
        
#         time.sleep(3)
#         def search_and_add_to_cart(driver, wait):
#             """Helper: Search for product and add to cart"""
#         print("Starting search and add to cart flow...")
        
#         try:
#             # Click search icon
#             search_btn = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "S, e, a, r, c, h,  , f, o, r,  , p, i, z, z, a"
#                 ))
#             )

#             search_btn.click()
#             print("✓ Clicked Search for pizza")


    
#             # Search for location
#             search_input = wait.until(
#                 EC.element_to_be_clickable(
#                     (AppiumBy.XPATH, "//android.widget.EditText[@text='Search']")
#                 )
#             )
#             search_input.click()
#             search_input.send_keys("Test Location")
#             time.sleep(3)
#             driver.press_keycode(66)
#             time.sleep(2)
#             driver.press_keycode(AndroidKey.TAB)

#             # Select shop
#             select_shop = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.widget.TextView[@text='Test Location']"
#                 ))
#             )
#             select_shop.click()
#             time.sleep(2)

#             # Select test product
#             test_product = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.widget.TextView[@text='Test Product']"
#                 ))
#             )
#             test_product.click()
#             time.sleep(2)

#             # Click product again
#             test_product = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.widget.TextView[@text='Test Product']"
#                 ))
#             )
#             test_product.click()
#             time.sleep(2)

#             # Click circle
#             circle = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.widget.TextView[@text='Test Product']/ancestor::android.view.ViewGroup//com.horcrux.svg.CircleView"
#                 ))
#             ).click()

#             time.sleep(2)

#             price_element = wait.until(
#                 EC.presence_of_element_located((
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup[contains(@content-desc,'LBP')]"
#                 ))
#             )

#             driver.execute_script("mobile: clickGesture", {
#                 "elementId": price_element.id
#             })

#             time.sleep(3)
            
            
#             print("✓ Items added to cart successfully!")
            
#         except Exception as e:
#             print(f"✗ Error in search_and_add_to_cart: {e}")
#             raise


#     def checkout_and_place_order(driver, wait):
#         """Helper: Checkout and place order"""
#         print("Starting checkout and place order flow...")
        
#         try:
#             # View basket
#             view_basket = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup[contains(@content-desc, 'View Basket')]"
#                 ))
#             )
#             view_basket.click()
#             time.sleep(2)

#             # Click checkout button
#             checkout = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup[contains(@content-desc, 'Checkout')]"
#                 ))
#             )
#             checkout.click()

#             # Place order
#             placeOrder = wait.until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup[contains(@content-desc, 'Place Order')]"
#                 ))
#             )
#             placeOrder.click()
            
#             print("✓ Order placed successfully!")
            
#         except Exception as e:
#             print(f"✗ Error in checkout_and_place_order: {e}")
#             raise


#         except Exception as e:
#             print(f"✗ Error in signup flow: {e}")
#             raise


# # ================================
# # MAIN TEST
# # ================================

# def test_signup_flow():
#     """Test: User Signup Flow"""

#     print("SIGNUP TEST STARTED")

#     driver = None

#     try:
#         driver = create_driver()
#         wait = WebDriverWait(driver, 20)

#         print("✓ App launched")
#         time.sleep(3)

#         signup_user(
#             driver,
#             wait,
#             name="Test User",
#             email="testuser123@example.com",
#             password="Test@1234"
#         )

#         print("SIGNUP TEST PASSED")

#     except Exception as e:
#         print(f"SIGNUP TEST FAILED: {e}")
#         if driver:
#             driver.save_screenshot("signup_error.png")
#         raise

#     finally:
#         if driver:
#             driver.quit()
#             print("✓ Driver closed")

# tests/test_signup.py

import random
import string
import time
from utils.driver import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import TimeoutException


# ================================
# RANDOM DATA GENERATORS
# ================================

def generate_random_name():
    length = random.randint(6, 7)
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    return f"{random_part}@testmail.com"


# ================================
# HELPER: TAP ELEMENT BY COORDINATES
# ================================

def tap_element(driver, element):
    """
    Taps the center of an element using screen coordinates.
    Reliable for SVG, ViewGroup, and React Native elements
    that block standard .click() interactions.
    """
    location = element.location
    size = element.size
    x = int(location['x'] + size['width'] / 2)
    y = int(location['y'] + size['height'] / 2)
    driver.execute_script("mobile: tap", {"x": x, "y": y})


# ================================
# SIGNUP FUNCTION
# ================================

def signup_user(driver, wait, name, email, password):
    """Helper: Perform user signup"""

    print("Starting signup flow...")

    try:
        # ── Step 1: Continue ──────────────────────────────────────────────
        continue_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Continue']"
            ))
        )
        continue_btn.click()
        time.sleep(2)

        # ── Step 2: Allow location permission ────────────────────────────
        try:
            driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.Button[@text="While using the app"]'
            ).click()
            time.sleep(2)
        except Exception:
            print("⚠ Location permission dialog not shown, continuing...")

        # ── Step 3: Skip ──────────────────────────────────────────────────
        skip_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Skip']"
            ))
        )
        skip_btn.click()
        time.sleep(5)

        # ── Step 4: Click Profile Icon ────────────────────────────────────
        profile_icon = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
            ))
        )
        driver.execute_script("mobile: clickGesture", {
            "elementId": profile_icon.id
        })
        print("✓ Profile icon clicked")

        # ── Step 5: Click Sign up ─────────────────────────────────────────
        signup_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Sign up']"
            ))
        )
        signup_btn.click()
        time.sleep(2)

        # ── Step 6: Enter Name ────────────────────────────────────────────
        name_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.EditText[contains(@text,'Enter Name')]"
            ))
        )
        name_field.click()
        name_field.clear()
        random_name = generate_random_name()
        name_field.send_keys(random_name)
        print(f"✓ Entered name: {random_name}")
        time.sleep(1)

        # ── Step 7: Enter Email ───────────────────────────────────────────
        email_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.EditText[contains(@text,'Enter Email')]"
            ))
        )
        email_field.click()
        email_field.clear()
        random_email = generate_random_email()
        email_field.send_keys(random_email)
        print(f"✓ Entered email: {random_email}")
        time.sleep(3)

        # ── Step 8: Select Male radio button ─────────────────────────────
        male_radio = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@content-desc="Male"]'
            ))
        )
        driver.execute_script("mobile: clickGesture", {
            "elementId": male_radio.id
        })
        print("✓ Male radio selected")

        # ── Step 9: Enter Password ────────────────────────────────────────
        password_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.EditText[contains(@text,'Enter Password')]"
            ))
        )
        password_field.click()
        password_field.clear()
        password_field.send_keys("Dhaka@01")
        print("✓ Password entered")
        time.sleep(1)
        try:
            driver.hide_keyboard()
        except Exception:
            pass

        # ── Step 10: Confirm Password ─────────────────────────────────────
        confirm_password_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.EditText[contains(@text,'Confirm Password')]"
            ))
        )
        confirm_password_field.click()
        confirm_password_field.clear()
        confirm_password_field.send_keys("Dhaka@01")
        print("✓ Confirm password entered")
        time.sleep(1)
        try:
            driver.hide_keyboard()
        except Exception:
            pass

        # ── Step 11: Accept Terms checkbox (SVG) ─────────────────────────
        terms_xpath = (
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[11]'
            '/com.horcrux.svg.SvgView'
            '/com.horcrux.svg.GroupView'
            '/com.horcrux.svg.PathView'
        )
        terms_checkbox = wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, terms_xpath))
        )
        terms_checkbox.click()
        time.sleep(2)

        # ── Step 12: Final Sign Up button ─────────────────────────────────
        final_signup = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Sign Up']"
            ))
        )
        final_signup.click()
        time.sleep(3)

        # ── Step 13: Enter Phone Number ───────────────────────────────────
        random_number = ''.join(random.choices("0123456789", k=7))
        full_number = "961" + random_number
        print(f"Final phone number: {full_number}")

        phone_input = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.CLASS_NAME,
                "android.widget.EditText"
            ))
        )
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys(full_number)
        print("✓ Phone number entered successfully")

        cont_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[contains(@text,'Continue')]"
            ))
        )
        cont_btn.click()
        time.sleep(3)

        # ── Step 14: Enter OTP Digit by Digit ────────────────────────────
        otp_code = "231220"

        keycode_map = {
            "0": 7, "1": 8, "2": 9, "3": 10,
            "4": 11, "5": 12, "6": 13, "7": 14,
            "8": 15, "9": 16
        }

        first_box = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.ScrollView/android.view.ViewGroup"
                "/android.view.ViewGroup/android.view.ViewGroup[4]"
            ))
        )
        driver.execute_script("mobile: clickGesture", {
            "elementId": first_box.id
        })
        time.sleep(0.5)

        for digit in otp_code:
            driver.press_keycode(keycode_map[digit])
            print(f"Entered digit: {digit}")
            time.sleep(1)

        print("✓ OTP entered digit by digit")

        # ── Step 15: Handle optional permission popup ─────────────────────
        try:
            allow_btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_button"
                ))
            )
            allow_btn.click()
            print("✓ Permission allowed")
        except TimeoutException:
            print("✓ Permission popup not shown, continuing...")

        # ── Step 16: Done ─────────────────────────────────────────────────
        done_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[contains(@text,'Done')]"
            ))
        )
        done_btn.click()
        print("✓ Account created successfully")
        
        time.sleep(4)

        # ── Step 17: Select Current location tab ─────────────────────────
        current_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Current"]'
            ))
        )
        current_btn.click()
        print("✓ Clicked on Current")
        time.sleep(3)

        # ── Step 18: Add new location ─────────────────────────────────────
        add_location_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "Add new location"
            ))
        )
        add_location_btn.click()
        print("✓ Clicked on Add new location")
        time.sleep(3)

        # ── Step 19: Confirm and Add Details ─────────────────────────────
        confirm_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Confirm and Add Details"]'
            ))
        )
        confirm_btn.click()
        print("✓ Clicked on Confirm and Add Details")
        time.sleep(3)

        # ── Step 20: Select Home ──────────────────────────────────────────
        home_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Home"]'
            ))
        )
        home_btn.click()
        print("✓ Clicked on Home")

        # ── Step 21: Enter Apt/Suite/Floor ────────────────────────────────
        apt_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.EditText[@text="Enter Apt/Suite/Floor"]'
            ))
        )
        apt_field.click()
        apt_field.clear()
        apt_field.send_keys("Dhaka")
        print("✓ Entered Dhaka in Apt/Suite/Floor")

        # ── Step 22: Enter Business or Building name ──────────────────────
        building_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.EditText[@text="Business or Building name"]'
            ))
        )
        building_field.click()
        building_field.clear()
        building_field.send_keys("Rampura")
        print("✓ Entered Rampura in Business/Building name")
        
        try:
            driver.hide_keyboard()
        except Exception:
            pass

        # ── Step 23: Save Address ─────────────────────────────────────────
        save_btn = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Save Address"]/parent::*'
            ))
        )
        driver.execute_script("mobile: clickGesture", {
            "elementId": save_btn.id
        })
        print("✓ Clicked Save Address")
        time.sleep(3)

    except Exception as e:
        print(f"✗ Error in signup flow: {e}")
        raise


# ================================
# SEARCH AND ADD TO CART
# ================================

def search_and_add_to_cart(driver, wait):
    """Helper: Search for product and add to cart"""

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
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.EditText[@text='Search']"
            ))
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
        wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Test Product']"
                "/ancestor::android.view.ViewGroup//com.horcrux.svg.CircleView"
            ))
        ).click()
        time.sleep(2)

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

        print("Items added to cart successfully!")

    except Exception as e:
        print(f"✗ Error in search_and_add_to_cart: {e}")
        raise


# ================================
# CHECKOUT AND PLACE ORDER
# ================================

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
        place_order = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Place Order')]"
            ))
        )
        place_order.click()

        print("✓ Order placed successfully!")

    except Exception as e:
        print(f"✗ Error in checkout_and_place_order: {e}")
        raise


# ================================
# MAIN TEST
# ================================

def test_signup_flow():
    """Test: User Signup Flow"""

    print("SIGNUP TEST STARTED")

    driver = None

    try:
        driver = create_driver()
        wait = WebDriverWait(driver, 20)

        print("App launched")
        time.sleep(3)

        signup_user(
            driver,
            wait,
            name="Test User",
            email="testuser123@example.com",
            password="Test@1234"
        )

        search_and_add_to_cart(driver, wait)

        checkout_and_place_order(driver, wait)

        print("SIGNUP TEST PASSED")

    except Exception as e:
        print(f"SIGNUP TEST FAILED: {e}")
        if driver:
            driver.save_screenshot("signup_error.png")
        raise

    finally:
        if driver:
            driver.quit()
            print("Driver closed")