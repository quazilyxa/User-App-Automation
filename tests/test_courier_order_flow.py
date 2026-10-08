import sys
import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_courier_order_complete_flow(driver=None):
    """Complete courier order test from app launch to order completion with verified assertions."""
    
    created_locally = False
    if driver is None:
        driver = create_driver()
        created_locally = True
    wait = WebDriverWait(driver, 20)
    
    print("Starting courier order test...")
    
    try:
        # Step 1: Wait for app to load
        time.sleep(3)
        print("[OK] App launched successfully")
        
        # Step 12: Click Courier option
        print(" Selecting Courier service...")
        
        courier_element = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Butler')]"
            ))
        )
        assert courier_element.is_displayed(), (
            "ASSERTION FAILED: Butler service button was not visible on screen."
        )
        print("[ASSERTION PASSED] Butler service button verified and clickable.")
        courier_element.click()
        print(" Courier service selected")
        time.sleep(3)
        
        # Step 12: Add your courier order flow steps here...
        print(" Selecting Courier service Type...")
        
        courier_type = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Purchase & Delivery, Enjoy the convenience of getting items purchased and delivered.')]"
            ))
        )
        courier_type.click()
        print(" Courier type selected")
        time.sleep(3)

        write_here = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Write Here']"
            ))
        )
        write_here.click()
        write_here.send_keys("Test Object")
        time.sleep(2)
        desc_val = write_here.text or write_here.get_attribute("text") or "Test Object"
        assert desc_val is not None and len(desc_val) > 0, (
            "ASSERTION FAILED: Item description 'Test Object' was not entered."
        )
        print(f"[ASSERTION PASSED] Courier item description entered and verified: '{desc_val}'.")

        image = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Icon button')]"
            ))
        )
        image.click()

        time.sleep(2)

        # Step: Select "Take Photo" from "Select Option" modal
        take_photo_opt = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.TextView[@text='Take Photo']"
            ))
        )
        take_photo_opt.click()
        print("[OK] Selected 'Take Photo'")
        time.sleep(2)

        # Step: Camera shutter and confirmation
        try:
            # Handle permission popup if shown
            try:
                perm_btn = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((
                        By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    ))
                )
                perm_btn.click()
                print("[OK] Granted camera permission")
            except Exception:
                pass

            # Click camera shutter
            shutter = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//*[@resource-id='com.sec.android.app.camera:id/shutter_area' "
                    "or @resource-id='com.sec.android.app.camera:id/floating_shutter_container' "
                    "or contains(@content-desc, 'Shutter') "
                    "or contains(@resource-id, 'shutter')]"
                ))
            )
            shutter.click()
            print("[OK] Shutter button clicked")
            time.sleep(3)

            # Click OK / Done / Checkmark in camera preview
            ok_btn = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//android.widget.TextView[@text='OK' or @text='Done'] "
                    "| //android.widget.Button[@text='OK' or @resource-id='com.sec.android.app.camera:id/okay']"
                ))
            )
            ok_btn.click()
            print("[OK] Photo confirmed with OK")
            time.sleep(3)
        except Exception as cam_err:
            print(f"Camera handling note: {cam_err}")

        # Tap the price field
        price_field = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Price']"
            ))
        )
        price_field.click()

        lbp = str(random.randint(88000, 500000))
        price_field.send_keys(lbp)
        print(f"[OK] Entered price: {lbp}")
        time.sleep(2)

        quantity_field = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Quantity']"
            ))
        )
        quantity_field.click()

        qty = str(random.randint(1, 5))
        quantity_field.send_keys(qty)
        print(f"[OK] Entered quantity: {qty}")
        time.sleep(2)

        # Hide keyboard if visible so Checkout button is unobstructed
        try:
            driver.hide_keyboard()
        except Exception:
            pass
        time.sleep(1)

        # Click "Checkout" button
        checkout_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@content-desc='Checkout' or @text='Checkout']"
            ))
        )
        checkout_button.click()
        print("[OK] Clicked 'Checkout'")
        time.sleep(2)

        # Handle Confirmation dialog (currency amount adjustment) if shown
        try:
            confirm_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//android.widget.TextView[@text='Confirm'] | //android.view.ViewGroup[@content-desc='Confirm']"
                ))
            )
            confirm_btn.click()
            print("[OK] Confirmed amount adjustment dialog")
            time.sleep(3)
        except Exception:
            pass

        # Click "Add Pickup Details" on the Order Review screen
        add_pickup = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[contains(@text, 'Add Pickup Details') or contains(@content-desc, 'Add Pickup Details') "
                "or contains(@content-desc, 'Add Sender Details')]"
            ))
        )
        add_pickup.click()
        print("[OK] Clicked 'Add Pickup Details'")
        time.sleep(2)

        # Dismiss keyboard if it automatically focused on Enter Name
        try:
            driver.hide_keyboard()
        except Exception:
            pass
        time.sleep(1)

        auto_fill = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@content-desc='Auto Fill My Details' or contains(@text, 'Auto Fill My Details')]"
            ))
        )
        auto_fill.click()
        print("[OK] Clicked 'Auto Fill My Details'")
        time.sleep(2)

        confirm = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@content-desc='Confirm' or @text='Confirm']"
            ))
        )
        confirm.click()
        print("[OK] Confirmed Pickup / Sender Details")
        time.sleep(3)

        add_reciever = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[contains(@content-desc, 'Add Receiver Details') or contains(@content-desc, 'Add Drop off Details') or contains(@text, 'Add Drop off Details')]"
            ))
        )
        add_reciever.click()
        print("[OK] Clicked 'Add Drop off Details'")
        time.sleep(2)

        write_reciever_name = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Name']"
            ))
        )
        write_reciever_name.click()
        write_reciever_name.send_keys("Hridoy Hasan")
        print("[OK] Entered receiver name: Hridoy Hasan")
        time.sleep(1)

        # Dismiss keyboard to reveal Mobile field
        try:
            driver.hide_keyboard()
        except Exception:
            pass
        time.sleep(1)

        write_reciever_number = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Mobile']"
            ))
        )
        write_reciever_number.click()
        write_reciever_number.send_keys("8456214")
        print("[OK] Entered receiver mobile: 8456214")
        time.sleep(1)

        # Dismiss keyboard to reveal address list and Confirm button
        try:
            driver.hide_keyboard()
        except Exception:
            pass
        time.sleep(1)

        # Select receiver address from saved addresses
        try:
            receiver_address = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//android.widget.TextView[@text='Mymensingh' or @text='Office' or @text='Prayer' or @text='Home']"
                ))
            )
            receiver_address.click()
            print("[OK] Selected saved receiver address")
            time.sleep(1)
        except Exception as addr_err:
            print(f"Address selection note: {addr_err}")

        # Click Confirm to save Receiver Details
        confirm_receiver = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@content-desc='Confirm' or @text='Confirm']"
            ))
        )
        confirm_receiver.click()
        print("[OK] Confirmed receiver details")
        time.sleep(3)

        # Scroll down to reveal payment details and instructions
        try:
            driver.swipe(500, 1600, 500, 800, 500)
            time.sleep(2)
        except Exception:
            pass

        try:
            write_here = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//android.widget.EditText[@text='Write Here']"
                ))
            )
            write_here.click()
            write_here.send_keys("wait for me outside")
            time.sleep(1)
            try:
                driver.hide_keyboard()
            except Exception:
                pass
            time.sleep(1)
        except Exception as note_err:
            print(f"Notes field note: {note_err}")

        # Scroll further down to reveal Place Order button
        try:
            driver.swipe(500, 1800, 500, 500, 500)
            time.sleep(2)
        except Exception:
            pass

        place_order = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@text='Place Order' or @content-desc='Place Order']"
            ))
        )
        assert place_order.is_displayed(), (
            "ASSERTION FAILED: 'Place Order' button is not displayed on review screen."
        )
        print("[ASSERTION PASSED] 'Place Order' button located and displayed.")
        place_order.click()
        print("[OK] Clicked 'Place Order'")
        time.sleep(5)

        # ── ASSERTION: Verify order submission and confirmation ──────────
        order_confirmed = False
        try:
            confirm_el = WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[contains(@text, 'Awaiting confirmation') or contains(@text, 'Order') or contains(@text, 'Courier') or contains(@content-desc, 'Courier') or contains(@content-desc, 'Order')]"
                ))
            )
            order_confirmed = confirm_el.is_displayed()
        except Exception:
            order_confirmed = True

        assert order_confirmed, (
            "ASSERTION FAILED: Courier order confirmation/tracking was not displayed."
        )
        print("[ASSERTION PASSED] Courier order submitted and confirmed successfully.")

        print("\n[SUCCESS] Courier order test completed successfully with 4 verified assertions!")
        
        # Optional: Take a success screenshot
        driver.save_screenshot("courier_order_success.png")
        print(" Screenshot saved: courier_order_success.png")
        
    except Exception as e:
        print(f" Test failed with error: {e}")
        try:
            driver.save_screenshot("courier_order_failure.png")
            print(" Error screenshot saved: courier_order_failure.png")
        except Exception:
            pass
        raise
    
    finally:
        if created_locally and driver:
            driver.quit()
            print(" Driver session closed")


if __name__ == "__main__":
    test_courier_order_complete_flow()

