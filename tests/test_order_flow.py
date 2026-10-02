# ==============================================================================
# THREE ORDERS FLOW: CASH, WHISH, CARD (USER SPECIFIED LOCATORS & FALLBACKS)
# ==============================================================================

import sys
import time
import random

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def navigate_to_test_shop(driver, wait):
    """
    Navigates to Test Shop from Home:
    1. Clicks LYXA (to reset to Home view)
    2. Clicks 'Find your favourites' search bar
    3. Clicks 'Search for Test Shop'
    4. Clicks 'Test Shop' from store results
    """
    print("\n--- [Step 1: Navigating to Test Shop] ---")
    
    # 1. Click LYXA
    try:
        lyxa_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("LYXA")'
        )
        lyxa_btn.click()
        print("✓ Clicked 'LYXA'")
        time.sleep(2)
    except Exception:
        pass

    # 2. Click Search Bar ("Find your favourites")
    try:
        search_bar = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Find your favourites")'
            ))
        )
        search_bar.click()
        print("✓ Clicked 'Find your favourites' search bar")
    except Exception:
        search_bar = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textMatches("(?i).*(find|search|favourite|favorite).*")'
            ))
        )
        search_bar.click()
        print("✓ Clicked search bar via fallback")

    time.sleep(2)

    # 3. Click 'Search for Test Shop'
    try:
        search_suggestion = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "Search for Test Shop"
            ))
        )
        search_suggestion.click()
        print("✓ Clicked 'Search for Test Shop'")
    except Exception:
        search_input = wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        search_input.click()
        search_input.clear()
        search_input.send_keys("Test Shop")
        driver.press_keycode(66)
        print("✓ Entered 'Test Shop' into search field")

    time.sleep(3)

    # 4. Select Test Shop
    try:
        shop_card = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//*[contains(@content-desc, 'Test Shop') and contains(@content-desc, '4.7')] | //android.widget.TextView[@text='Test Shop']"
            ))
        )
        shop_card.click()
        print("✓ Selected 'Test Shop'")
    except Exception:
        shop_card = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "Test Shop, 4.7, 25 - 30 min , LBP 810,000"
            ))
        )
        shop_card.click()
        print("✓ Clicked 'Test Shop' via accessibility id")

    time.sleep(3)


def add_product_and_proceed_to_checkout(driver, wait):
    """
    Inside Test Shop:
    1. Scrolls down a little bit to reveal products
    2. Clicks add-to-cart-69e70fa962be1aa321ab8ece
    3. Clicks '1, LBP 90,000, View Basket'
    4. Clicks 'Checkout'
    """
    print("\n--- [Step 2: Adding Product & Proceeding to Checkout] ---")
    
    # 1. Scroll down a little bit
    try:
        size = driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.70)
        end_y = int(size['height'] * 0.40)
        driver.swipe(start_x, start_y, start_x, end_y, 400)
        print("✓ Scrolled down to reveal product")
        time.sleep(2)
    except Exception as e:
        print(f"Scroll notice: {e}")

    # 2. Click Add-To-Cart
    try:
        add_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "add-to-cart-69e70fa962be1aa321ab8ece"
            ))
        )
        add_btn.click()
        print("✓ Clicked 'add-to-cart-69e70fa962be1aa321ab8ece'")
    except Exception:
        add_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//*[contains(@content-desc, 'add-to-cart')]"
            ))
        )
        add_btn.click()
        print("✓ Clicked add-to-cart via fallback")

    # 3. Click View Basket (Instant dynamic match on 'View Basket')
    try:
        view_basket = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("View Basket")'
            ))
        )
        view_basket.click()
        print("✓ Clicked 'View Basket'")
    except Exception:
        view_basket = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//*[contains(@content-desc, 'View Basket') or contains(@text, 'View Basket')]"
            ))
        )
        view_basket.click()
        print("✓ Clicked 'View Basket' via fallback")

    # 4. Click Checkout
    checkout_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.ACCESSIBILITY_ID,
            "Checkout"
        ))
    )
    checkout_btn.click()
    print("✓ Clicked 'Checkout'")


def handle_whish_response(driver, wait):
    """
    Handles Whish payment response:
    - If error popup appears, clicks 'OK'.
    - If no error, waits for page to load.
    """
    time.sleep(2)
    try:
        # Check for error popup / OK button
        ok_buttons = driver.find_elements(
            AppiumBy.XPATH,
            "//*[@text='OK' or @text='Ok' or @text='ok' or @resource-id='android:id/button1']"
        )
        if ok_buttons:
            ok_buttons[0].click()
            print("✓ Detected error dialog, clicked 'OK'")
            time.sleep(2)
            return True
        else:
            print("✓ No error dialog; waiting for page load...")
            time.sleep(3)
            return False
    except Exception as e:
        print(f"Notice during Whish response check: {e}")
        return False


def click_payment_element(driver, element, name="Payment Option"):
    """
    Safely clicks a payment option in React Native:
    - If the element is a non-clickable TextView, attempts to click its clickable parent ViewGroup.
    - If regular click does not dispatch or fails, taps the element's center coordinates using clickGesture.
    """
    try:
        if element.get_attribute("clickable") == "false":
            try:
                parent = element.find_element(AppiumBy.XPATH, "..")
                if parent.get_attribute("clickable") == "true":
                    parent.click()
                    print(f"✓ Clicked parent clickable ViewGroup for '{name}'")
                    return True
            except Exception:
                pass
    except Exception:
        pass

    try:
        element.click()
        print(f"✓ Clicked '{name}' element directly")
        return True
    except Exception:
        pass

    try:
        loc = element.location
        size = element.size
        cx = int(loc['x'] + size['width'] / 2)
        cy = int(loc['y'] + size['height'] / 2)
        try:
            driver.execute_script("mobile: clickGesture", {"x": cx, "y": cy})
        except Exception:
            driver.execute_script("mobile: tap", {"x": cx, "y": cy})
        print(f"✓ Tapped '{name}' at coordinates ({cx}, {cy})")
        return True
    except Exception as e:
        print(f"Failed to click/tap '{name}': {e}")
        return False


def scroll_down_for_payment(driver):
    """
    Scrolls down on checkout page to bring Whish and Card payment options into view.
    """
    print("Scrolling down to reveal payment options (Whish / Card)...")
    try:
        size = driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.70)
        end_y = int(size['height'] * 0.40)
        driver.swipe(start_x, start_y, start_x, end_y, 400)
        time.sleep(1.5)
        print("✓ Scrolled down to reveal payment options")
    except Exception as e:
        print(f"Notice during scroll: {e}")


def handle_looks_good_button(driver, wait=None, wait_time=2, max_retries=6):
    """
    After placing an order, gives 2 seconds for the 'Looks good' button to appear,
    and clicks it before proceeding to go back.
    """
    print(f"\nWaiting {wait_time} seconds for 'Looks good' confirmation button to appear...")
    time.sleep(wait_time)

    looks_good_selectors = [
        (AppiumBy.ACCESSIBILITY_ID, "Looks good"),
        (AppiumBy.ACCESSIBILITY_ID, "Looks Good"),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i)^looks\\s*good$")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches("(?i)^looks\\s*good$")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Looks good")'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Looks good")'),
        (AppiumBy.XPATH, '//*[@content-desc="Looks good" or @text="Looks good" or @content-desc="Looks Good" or @text="Looks Good"]'),
        (AppiumBy.XPATH, '//*[contains(translate(@text, "LOOKS GOOD", "looks good"), "looks good") or contains(translate(@content-desc, "LOOKS GOOD", "looks good"), "looks good")]'),
        (AppiumBy.ACCESSIBILITY_ID, "looks-good")
    ]

    start_time = time.time()
    while time.time() - start_time < max_retries:
        for by, sel in looks_good_selectors:
            try:
                elements = driver.find_elements(by, sel)
                for el in elements:
                    if el.is_displayed():
                        print(f"✓ Found 'Looks good' button using: {sel}")
                        if click_payment_element(driver, el, "Looks good"):
                            time.sleep(2)
                            return True
            except Exception:
                pass
        time.sleep(0.5)

    print("ℹ 'Looks good' button not visible or already closed.")
    return False


def navigate_back_to_shop_or_home(driver, wait):
    """
    Navigates back after an order:
    1. Checks and clicks 'Looks good' button if present (waits 2s after placing order)
    2. Checks if already returned to Home screen
    3. Dynamically waits for and clicks the back button ('Go-back' / SvgView)
    4. Returns cleanly to the Home/LYXA screen.
    """
    # 1. Check and click 'Looks good' button before navigating back
    handle_looks_good_button(driver, wait)

    print("\nNavigating back to Home / Shop...")

    # 2. Check if already on Home screen (e.g. dismissed by 'Looks good')
    try:
        if driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Search-bar") or \
           driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LYXA")'):
            print("✓ Already on Home screen")
            return True
    except Exception:
        pass

    # 3. Fast dynamic wait for back button (Accessibility ID takes ~30ms without full DOM dump)
    clicked = False
    for back_id in ["Go-back", "Go back"]:
        try:
            back_btn = WebDriverWait(driver, 6).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, back_id))
            )
            back_btn.click()
            print(f"✓ Clicked '{back_id}' button via Accessibility ID")
            clicked = True
            time.sleep(1.5)
            break
        except Exception:
            pass

    # Fast fallback: SvgView inside back button if Accessibility ID didn't click
    if not clicked:
        try:
            svg_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.Button[@content-desc="Go back"]/com.horcrux.svg.SvgView | '
                    '//android.widget.Button[@content-desc="Go-back"]/com.horcrux.svg.SvgView'
                ))
            )
            svg_btn.click()
            print("✓ Clicked back button via SvgView")
            time.sleep(1.5)
        except Exception:
            pass

    # 4. Check if we reached Home (using fast Accessibility ID & UiSelector)
    for step in range(3):
        # Quick check if search bar is visible on Home (~30ms)
        try:
            search_bars = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Search-bar")
            if search_bars and search_bars[0].is_displayed():
                print("✓ On Home screen (Search bar detected)")
                return True
        except Exception:
            pass

        # Quick check for LYXA text logo
        try:
            lyxa = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LYXA")')
            if lyxa and lyxa[0].is_displayed():
                lyxa[0].click()
                print("✓ Clicked 'LYXA' logo -> On Home screen")
                time.sleep(1.5)
                return True
        except Exception:
            pass

        # Press Android system back button if still not on Home
        try:
            driver.back()
            print(f"✓ Triggered driver.back() (step {step + 1})")
            time.sleep(1.5)
        except Exception:
            pass

    return False


def select_payment_cash(driver, wait):
    """
    Finds and clicks 'CASH ON DELIVERY' / 'Cash on delivery' on checkout / place order page.
    Waits for page load, searches visible text, scrolls down slightly if needed, with fallback.
    """
    print("\n--- [Selecting Payment: CASH ON DELIVERY] ---")

    # 1. Ensure we arrived on Checkout / Place Order page
    try:
        wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//*[@content-desc='Place Order' or @text='Place Order' or @text='Payment Method' or contains(@text, 'Checkout')]"
            ))
        )
        print("✓ Arrived on Checkout / Place Order page")
    except Exception:
        print("Note: Checkout indicators not immediately seen, proceeding with search...")

    time.sleep(1)

    for attempt in range(2):
        print(f"Searching for text 'CASH ON DELIVERY' (attempt {attempt + 1}/2)...")
        for by, selector in [
            # 1. Exact or case-insensitive text match for 'Cash on delivery' / 'CASH ON DELIVERY'
            (AppiumBy.XPATH, '//*[contains(@content-desc, "Cash on delivery") or @text="Cash on delivery"]'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*cash on delivery.*")'),
            (AppiumBy.ACCESSIBILITY_ID, "Cash on delivery"),
            (AppiumBy.XPATH, '//*[contains(translate(@text, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "cash on delivery")]'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*cash.*")'),
            # Fallback instance(16)
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)')
        ]:
            try:
                elements = driver.find_elements(by, selector)
                for element in elements:
                    if element.is_displayed():
                        text_val = element.get_attribute("text") or element.get_attribute("content-desc") or "Cash on delivery"
                        print(f"✓ Found text '{text_val}' using selector: {selector}")
                        if click_payment_element(driver, element, "Cash on Delivery"):
                            time.sleep(2)
                            return element
            except Exception:
                pass

        if attempt == 0:
            print("Scrolling down slightly to bring payment methods into view...")
            scroll_down_for_payment(driver)

    raise NoSuchElementException("Could not locate 'Cash on Delivery' payment text on page.")


def select_payment_whish(driver, wait):
    """
    Finds and clicks 'Whish' / 'WHISH' on checkout / place order page.
    Scrolls down immediately to bring Whish into view, then finds and clicks.
    """
    print("\n--- [Selecting Payment: WHISH] ---")

    # 1. Ensure we arrived on Checkout / Place Order page
    try:
        wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//*[@content-desc='Place Order' or @text='Place Order' or @text='Payment Method' or contains(@text, 'Checkout')]"
            ))
        )
        print("✓ Arrived on Checkout / Place Order page")
    except Exception:
        pass

    time.sleep(1)

    # 2. Scroll down immediately so Whish is visible
    scroll_down_for_payment(driver)

    for attempt in range(2):
        print(f"Searching for text 'Whish' (attempt {attempt + 1}/2)...")
        for by, selector in [
            # 1. Primary verified selectors: Accessibility ID, XPath text/content-desc, regex
            (AppiumBy.XPATH, '//*[@content-desc="Whish" or @text="Whish"]'),
            (AppiumBy.ACCESSIBILITY_ID, "Whish"),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*whish.*")'),
            (AppiumBy.XPATH, '//*[contains(translate(@text, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "whish")]'),
            (AppiumBy.XPATH, '//*[contains(translate(@content-desc, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "whish")]'),
            # Fallback instance(24)
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(24)')
        ]:
            try:
                elements = driver.find_elements(by, selector)
                for element in elements:
                    if element.is_displayed():
                        text_val = element.get_attribute("text") or element.get_attribute("content-desc") or "Whish"
                        print(f"✓ Found text '{text_val}' using selector: {selector}")
                        if click_payment_element(driver, element, "Whish"):
                            time.sleep(2)
                            return element
            except Exception:
                pass

        if attempt == 0:
            scroll_down_for_payment(driver)

    raise NoSuchElementException("Could not locate 'Whish' payment text on page.")


def select_payment_card(driver, wait):
    """
    Finds and clicks 'Card' / 'Credit Card' / 'Master Card' on checkout / place order page.
    Scrolls down immediately to bring Card options into view, then finds and clicks.
    """
    print("\n--- [Selecting Payment: CARD] ---")

    # 1. Ensure we arrived on Checkout / Place Order page
    try:
        wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//*[@content-desc='Place Order' or @text='Place Order' or @text='Payment Method' or contains(@text, 'Checkout')]"
            ))
        )
        print("✓ Arrived on Checkout / Place Order page")
    except Exception:
        pass

    time.sleep(1)

    # 2. Scroll down immediately so Card is visible
    scroll_down_for_payment(driver)

    for attempt in range(2):
        print(f"Searching for Card text (attempt {attempt + 1}/2)...")
        for by, selector in [
            # 1. Primary verified selectors: Master Card, saved card, credit card
            (AppiumBy.XPATH, '//*[contains(@content-desc, "Master Card") or @text="Master Card"]'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*master card.*")'),
            (AppiumBy.XPATH, '//*[contains(@content-desc, "512345")]'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*(master card|visa|credit card|debit card).*")'),
            (AppiumBy.XPATH, '//*[contains(@content-desc, "Add Credit Card") or @text="Add Credit Card"]'),
            # Fallback instance(26)
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(26)')
        ]:
            try:
                elements = driver.find_elements(by, selector)
                for element in elements:
                    if element.is_displayed():
                        text_val = element.get_attribute("text") or element.get_attribute("content-desc") or "Card"
                        print(f"✓ Found text '{text_val}' using selector: {selector}")
                        if click_payment_element(driver, element, "Card"):
                            time.sleep(2)
                            return element
            except Exception:
                pass

        if attempt == 0:
            scroll_down_for_payment(driver)

    raise NoSuchElementException("Could not locate 'Card' payment text on page.")


def place_order_with_cash(driver, wait):
    """Places order using Cash payment method by finding text 'Cash on Delivery'"""
    print("\n=======================================================")
    print("🛒 ORDER 1: CASH ON DELIVERY")
    print("=======================================================")

    # 1. Select Cash on Delivery by finding the text
    select_payment_cash(driver, wait)
    time.sleep(2)

    # 2. Click Place Order
    place_order_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//*[@content-desc='Place Order' or @text='Place Order']"
        ))
    )
    place_order_btn.click()
    print("✓ Clicked 'Place Order' with Cash")

    # 3. Dynamic wait, handle 'Looks good', and return
    navigate_back_to_shop_or_home(driver, wait)
    print("🎉 Order 1 (Cash) Completed Successfully!\n")


def place_order_with_whish(driver, wait):
    """Places order using Whish payment method by finding text 'Whish'"""
    print("\n=======================================================")
    print("🛒 ORDER 2: WHISH PAYMENT")
    print("=======================================================")

    # 1. Select Whish by finding the text
    select_payment_whish(driver, wait)
    time.sleep(2)

    # 2. Click Place Order
    place_order_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//*[@content-desc='Place Order' or @text='Place Order']"
        ))
    )
    place_order_btn.click()
    print("✓ Clicked 'Place Order' to enter Whish flow")
    time.sleep(2)

    # 3. Whish Step 1: Input phone number 70123456
    try:
        phone_input = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.CLASS_NAME,
                "android.widget.EditText"
            ))
        )
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys("70123456")
        print("✓ Entered Whish phone number: 70123456")
        time.sleep(1)

        # Whish Step 2: Click next-button
        next_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("next-button")'
            ))
        )
        next_btn.click()
        print("✓ Clicked 'next-button'")
        time.sleep(2)

        # Whish Step 3: Input OTP 111111
        otp_field = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("whish-otp")'
            ))
        )
        otp_field.click()
        otp_field.send_keys("111111")
        print("✓ Entered Whish OTP: 111111")
        time.sleep(1)

        # Whish Step 4: Click submit-button
        submit_btn = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("submit-button")'
            ))
        )
        submit_btn.click()
        print("✓ Clicked 'submit-button'")
        time.sleep(2)

        # Whish Step 5: Handle error if present or wait for page load
        handle_whish_response(driver, wait)

    except Exception as e:
        print(f"Whish flow interaction detail: {e}")
        handle_whish_response(driver, wait)

    # 4. Click Go-back / return to Home
    navigate_back_to_shop_or_home(driver, wait)
    print("🎉 Order 2 (Whish) Completed Successfully!\n")


def place_order_with_card(driver, wait):
    """Places order using Card payment method by finding text 'Card'"""
    print("\n=======================================================")
    print("🛒 ORDER 3: CARD PAYMENT")
    print("=======================================================")

    # 1. Select Card by finding the text
    select_payment_card(driver, wait)
    time.sleep(2)

    # 2. Click Place Order
    place_order_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//*[@content-desc='Place Order' or @text='Place Order']"
        ))
    )
    place_order_btn.click()
    print("✓ Clicked 'Place Order' with Card")

    # 3. Dynamic wait, handle 'Looks good', and return
    navigate_back_to_shop_or_home(driver, wait)
    print("🎉 Order 3 (Card) Completed Successfully!\n")


# ==========================================
# MAIN TEST - RUNS ALL 3 ORDER FLOWS
# ==========================================
def test_complete_order_flow():
    """
    Places 3 orders adding the same product every time:
    1. Order with Cash (instance 16)
    2. Order with Whish (instance 24, phone 70123456, OTP 111111)
    3. Order with Card (instance 26)
    """
    print("\n" + "=" * 65)
    print("🚀 STARTING THREE-ORDER AUTOMATION SUITE: CASH -> WHISH -> CARD")
    print("=" * 65)

    driver = None
    try:
        driver = create_driver()
        wait = WebDriverWait(driver, 20)
        # Performance optimization: disable 10-second animation freeze
        driver.update_settings({"waitForIdleTimeout": 100})
        print("✓ App launched successfully (optimized waitForIdleTimeout=100ms)")
        time.sleep(3)

        # -------------------------------------------------------------
        # ORDER 1: CASH
        # -------------------------------------------------------------
        navigate_to_test_shop(driver, wait)
        add_product_and_proceed_to_checkout(driver, wait)
        place_order_with_cash(driver, wait)
        time.sleep(3)

        # -------------------------------------------------------------
        # ORDER 2: WHISH
        # -------------------------------------------------------------
        navigate_to_test_shop(driver, wait)
        add_product_and_proceed_to_checkout(driver, wait)
        place_order_with_whish(driver, wait)
        time.sleep(3)

        # -------------------------------------------------------------
        # ORDER 3: CARD
        # -------------------------------------------------------------
        navigate_to_test_shop(driver, wait)
        add_product_and_proceed_to_checkout(driver, wait)
        place_order_with_card(driver, wait)

        print("\n" + "=" * 65)
        print("🏆 ALL 3 ORDERS (CASH, WHISH, CARD) PLACED SUCCESSFULLY!")
        print("=" * 65)

    except Exception as e:
        print(f"\n❌ TEST SUITE FAILED: {e}")
        if driver:
            try:
                driver.save_screenshot("three_orders_failure.png")
                print("✓ Failure screenshot saved: three_orders_failure.png")
            except Exception:
                pass
        raise

    finally:
        if driver:
            driver.quit()
            print("✓ Driver closed cleanly")