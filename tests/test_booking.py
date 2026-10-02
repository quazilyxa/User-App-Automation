import time
import random
import re
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

"""
BOOKING AUTOMATION TEST
=======================
Feature: Complete Service Booking Flow (Cleaning Services)
- Launch app without login
- Select "Cleaning Services"
- Select "Deep Cleaning"
- Select "Industrial Compliance"
- Click "Book Service"
- Click "Next"
- Pick a random available Time Slot (e.g., "19:00 - 19:30" or any available slot)
- Click "Next"
- Click "Checkout"
- Click "Confirm Booking"
"""


def click_element_with_fallback(driver, wait, text=None, accessibility_id=None, timeout=15):
    """Helper to find and click an element with explicit wait and multiple locator fallbacks."""
    custom_wait = WebDriverWait(driver, timeout)
    element = None

    if accessibility_id:
        try:
            element = custom_wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            )
            element.click()
            return element
        except Exception:
            pass

    if text:
        # Try UiAutomator text exact match
        try:
            element = custom_wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{text}")'
                ))
            )
            element.click()
            return element
        except Exception:
            pass

        # Try XPath text match
        try:
            element = custom_wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    f'//*[@text="{text}"]'
                ))
            )
            element.click()
            return element
        except Exception:
            pass

        # Try UiScrollable scroll into view
        try:
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
            )
            element.click()
            return element
        except Exception as e:
            raise NoSuchElementException(f"Could not locate or click element with text '{text}': {e}")

    raise NoSuchElementException(f"No valid locator provided (text={text}, accessibility_id={accessibility_id})")


def select_random_time_slot(driver, wait):
    """Find all visible time slots and select one at random."""
    print("Searching for available time slots...")
    time.sleep(2)

    # Strategy 1: Look for TextViews matching time slot pattern (e.g. "19:00 - 19:30")
    slot_elements = driver.find_elements(
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, ":") and contains(@text, "-")]'
    )

    # Strategy 2: If XPath didn't find any, try UiAutomator regex
    if not slot_elements:
        try:
            slot_elements = driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textMatches(".*\\d{1,2}:\\d{2}\\s*-\\s*\\d{1,2}:\\d{2}.*")'
            )
        except Exception:
            pass

    if slot_elements:
        chosen_element = random.choice(slot_elements)
        slot_text = chosen_element.text
        print(f"✓ Found {len(slot_elements)} time slot(s). Randomly selecting: '{slot_text}'")
        chosen_element.click()
        return slot_text

    # Strategy 3: Fallback to default specific slot "19:00 - 19:30"
    print("⚠ No dynamic slot list found, attempting fallback to '19:00 - 19:30'...")
    fallback_slot = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("19:00 - 19:30")'
        ))
    )
    fallback_slot.click()
    print("✓ Selected fallback slot: '19:00 - 19:30'")
    return "19:00 - 19:30"


def test_booking_cleaning_service_flow():
    """Complete booking flow for cleaning services without logging in."""
    print("\n" + "=" * 55)
    print("🚀 STARTING SERVICE BOOKING TEST FLOW")
    print("=" * 55)

    driver = None
    try:
        # Step 0: Initialize driver and launch app
        driver = create_driver()
        wait = WebDriverWait(driver, 20)
        print("✓ App launched successfully")
        time.sleep(3)

        # Step 1: Click "Cleaning Services"
        print("\n[Step 1] Selecting 'Cleaning Services'...")
        click_element_with_fallback(driver, wait, text="Cleaning Services")
        print("✓ Clicked 'Cleaning Services'")
        time.sleep(2)

        # Step 2: Click "Deep Cleaning"
        print("\n[Step 2] Selecting 'Deep Cleaning'...")
        click_element_with_fallback(driver, wait, text="Deep Cleaning")
        print("✓ Clicked 'Deep Cleaning'")
        time.sleep(2)

        # Step 3: Click "Industrial Compliance"
        print("\n[Step 3] Selecting 'Industrial Compliance'...")
        click_element_with_fallback(driver, wait, text="Industrial Compliance")
        print("✓ Clicked 'Industrial Compliance'")
        time.sleep(2)

        # Step 4: Click "Book Service"
        print("\n[Step 4] Clicking 'Book Service'...")
        click_element_with_fallback(driver, wait, text="Book Service")
        print("✓ Clicked 'Book Service'")
        time.sleep(2)

        # Step 5: Click "Next" (Accessibility ID / Text)
        print("\n[Step 5] Clicking 'Next'...")
        click_element_with_fallback(driver, wait, text="Next", accessibility_id="Next")
        print("✓ Clicked 'Next'")
        time.sleep(2)

        # Step 6: Select Random Time Slot
        print("\n[Step 6] Selecting Time Slot...")
        selected_slot = select_random_time_slot(driver, wait)
        print(f"✓ Time slot selected: {selected_slot}")
        time.sleep(2)

        # Step 7: Click "Next"
        print("\n[Step 7] Clicking 'Next' after slot selection...")
        click_element_with_fallback(driver, wait, text="Next", accessibility_id="Next")
        print("✓ Clicked 'Next'")
        time.sleep(2)

        # Step 8: Click "Checkout"
        print("\n[Step 8] Clicking 'Checkout'...")
        click_element_with_fallback(driver, wait, text="Checkout")
        print("✓ Clicked 'Checkout'")
        time.sleep(2)

        # Step 9: Click "Confirm Booking"
        print("\n[Step 9] Clicking 'Confirm Booking'...")
        click_element_with_fallback(driver, wait, text="Confirm Booking")
        print("✓ Clicked 'Confirm Booking'")
        time.sleep(3)

        print("\n" + "=" * 55)
        print("🎉 BOOKING TEST COMPLETED SUCCESSFULLY!")
        print("=" * 55)

        # Save success screenshot
        driver.save_screenshot("booking_success.png")
        print("✓ Success screenshot saved: booking_success.png")

    except Exception as e:
        print(f"\n❌ [ERROR] Booking test failed: {e}")
        if driver:
            screenshot_file = "booking_failure.png"
            driver.save_screenshot(screenshot_file)
            print(f"✓ Error screenshot saved: {screenshot_file}")
        raise

    finally:
        if driver:
            driver.quit()
            print("✓ Driver session closed")


if __name__ == "__main__":
    # Allow running directly: python tests/test_booking.py
    test_booking_cleaning_service_flow()
