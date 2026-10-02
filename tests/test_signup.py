import random
import string
import time
from utils.driver import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By



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
        
        driver.find_element(
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button"
        ).click()
        time.sleep(2)
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
        
        login_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Login"]'))
        )
        login_button.click()
        time.sleep(3)
        # ── Step 5: Click Sign up ─────────────────────────────────────────


        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionContains("Sign up")'
        ).click()

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
        time.sleep(2)

        # # ── Step 8: Select Male radio button ─────────────────────────────
        # male_radio = wait.until(
        #     EC.presence_of_element_located((
        #         AppiumBy.XPATH,
        #         '//android.view.ViewGroup[@content-desc="Male"]'
        #     ))
        # )
        # driver.execute_script("mobile: clickGesture", {
        #     "elementId": male_radio.id
        # })
        # print("✓ Male radio selected")

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

        
        first_digit = random.choice("13456789")

        remaining_digits = ''.join(random.choices("0123456789", k=6))
        random_number = first_digit + remaining_digits
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

        # Locate OTP container / first box
        first_box = wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.ScrollView/android.view.ViewGroup"
                "/android.view.ViewGroup/android.view.ViewGroup[4]"
            ))
        )

        # Click to focus
        driver.execute_script("mobile: clickGesture", {
            "elementId": first_box.id
        })
        time.sleep(1)

        # Check if keyboard is shown
        if not driver.is_keyboard_shown():
            raise Exception("❌ Keyboard did not appear. OTP cannot be entered.")

        # Enter OTP digit by digit
        for digit in otp_code:
            driver.press_keycode(keycode_map[digit])
            time.sleep(0.3)
            print(f"Entered digit: {digit}")

        time.sleep(2)

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

        # ── Step 16: Validate OTP success + Click Done ────────────────────
        try:
            done_btn = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    "//android.widget.TextView[contains(@text,'Done')]"
                ))
            )
            print("✅ OTP accepted — Done button appeared")
        except TimeoutException:
            raise Exception("❌ OTP entry failed — Done button never appeared")

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

    # Click search bar
    search_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="Search-bar"]/android.view.ViewGroup[2]'
        ))
    )
    search_btn.click()
    print("✓ Clicked Search bar")

    # Search for location
    search_input = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//android.widget.EditText[@text='Search']"
        ))
    )
    search_input.click()
    search_input.send_keys("Test shop")
    time.sleep(3)
    driver.press_keycode(66)
    time.sleep(2)
    driver.press_keycode(AndroidKey.TAB)


    # Select shop
    select_shop = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Test Shop']"
        ))
    )
    select_shop.click()
    time.sleep(2)
    add_to_cart_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '(//android.widget.Button[@content-desc="add-to-cart-692978d097bfef4ad9de79a0"])[2]'
        ))
    )
    add_to_cart_btn.click()


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
        time.sleep(10)
        print("✓ Order placed successfully!")
        
        driver.back()
        time.sleep(3)
        pets_element = driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Pets"
        )
        
        driver.execute_script("mobile: swipeGesture", {
            "elementId": pets_element.id,
            "direction": "left",
            "percent": 0.6
        })
        
        time.sleep(3)
    

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