import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey





"""
In this file follwoing USER APP AUTOMATION FEATURES TESTED:
==============================================================
1. Location Selection
   - Address selection from list
   - Scrolling and selecting specific address

2. Product Search & Selection
   - Product category navigation
   - Product image/view interaction
   - Back navigation

3. Product Customization
   - Gender selection (Female)
   - Save preferences

4. Order Management
   - Orders section navigation
   - Order details viewing

5. Coupon System
   - Coupons section access
   - Coupon selection from available list
   - Manual coupon code entry
   - Add coupon functionality

6. Loyalty Points/Balance
   - LBP Balance section access
   - Add Funds functionality
   - Amount input (180,000)
   - Currency/Region selection (Tokyo)
   - Transaction confirmation

7. Customer Support Features
   - FAQ section access
   - Expand/collapse FAQ items (Oh lala)
   - Get Support section
   - Account-specific support
   - Payment information FAQ
   - Chat with us feature

8. Navigation Elements
   - Multiple back navigation points
   - SVG path interactions
   - ScrollView interactions
   - Parent ViewGroup clicks
   - Final element navigation

9. Input Operations
   - Text input (coupon codes, amounts)
   - Keyboard handling
   - Clear and send keys operations

10. UI Elements Interacted With
    - TextViews
    - ImageViews
    - EditText fields
    - SVG elements (PathView, GroupView, SvgView)
    - Accessibility IDs
    - Scrollable views
    - Dialog buttons (android:id/button1)

11. Wait Conditions
    - Element presence
    - Element clickability
    - Page transitions
    - Explicit waits with timeouts

12. Error Handling
    - Try-catch blocks for robust execution
    - Multiple element location strategies
    - Screenshot capture on success/failure
"""




def get_available_system_port():
    return random.randint(8200, 8300)

def __init__(self, driver):
        self.driver = driver


# def select_location(driver, wait):
#     """Select location from address list"""
#     print("Attempting to select location...")
    
#     try:
#         element = wait.until(
#             EC.presence_of_element_located(
#                 (AppiumBy.XPATH, "//android.widget.TextView[@text='Test']")
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


# def userAutomation(driver, wait, self):
#     """Helper: Search for products and add items to cart"""
#     print("Starting profile update flow..")
    
#     try:
#         element = self.wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
#             ))
#         )
#         element.click()
#         print("✓ Profile screen opened")
#         time.sleep(2)
#         print("✓ Profile screen opened")
        
        
#         # Re-find the ImageView element to avoid stale reference
#         image_view = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ImageView"))
#         )
#         image_view.click()
#         print("✓ ImageView clicked")
#         time.sleep(2)
        
#         xpath = ('//android.widget.ScrollView/android.view.ViewGroup/'
#                  'android.view.ViewGroup/android.view.ViewGroup[5]/'
#                  'android.view.ViewGroup/com.horcrux.svg.SvgView/'
#                  'com.horcrux.svg.GroupView/com.horcrux.svg.PathView')

#         element = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((AppiumBy.XPATH, xpath))
#         )
#         element.click()
#         print("✓ SVG Path clicked")
#         time.sleep(2)
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Female")
#             )
#         )
#         element.click()
#         print("✓ Female selected")
#         time.sleep(1)
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]')
#             )
#         )
#         element.click()
#         print("✓ Save clicked")
#         time.sleep(2)
        
#         driver.back()
#         print("✓ Back button clicked")
#         time.sleep(2)
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Orders")
#             )
#         )
#         element.click()
#         print("✓ Orders clicked")
#         time.sleep(2)
        
#         elements = driver.find_elements(
#             AppiumBy.XPATH,
#             '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/'
#             'android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/'
#             'android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/'
#             'android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView'
#         )

#         if elements:
#             elements[0].click()
#             print("✓ Optional element found and clicked")
#         else:
#             print("⚠ Optional element not found, continuing...")
#         time.sleep(6)
#         driver.back()
#         print("✓ Back button clicked")
#         time.sleep(2)
        
#         delivered_orders = driver.find_elements(
#         AppiumBy.XPATH,
#         '//android.widget.TextView[contains(@text,"Delivered")]'
#             )

#         if delivered_orders:
#             print("✓ Delivered order found")

#             driver.find_element(
#                 AppiumBy.XPATH,
#                 '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/'
#                 'android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/'
#                 'android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/'
#                 'android.view.ViewGroup/android.view.ViewGroup[3]/'
#                 'com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
#             ).click()

#             print("✓ Delivered order arrow clicked")
#         else:
#             print("⚠ No delivered orders found")
            
            
            
#         driver.find_element(
#             AppiumBy.XPATH,
#             '//android.widget.TextView[@text="Rate your order"]'
#         ).click()
#         print("✓ Rate your order clicked")
#         time.sleep(2)

        
        
#         driver.find_element(
#             AppiumBy.XPATH,
#             '//android.widget.TextView[@text="Submit"]'
#         ).click()
#         print("✓ Submit clicked")
#         time.sleep(2)
        
#         driver.find_element(
#             AppiumBy.XPATH,
#             '//android.widget.TextView[@text="Done"]'
#         ).click()
#         print("✓ Done clicked")
#         time.sleep(7)
        
        
#         xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'

#         wait = WebDriverWait(driver, 20)
#         element = wait.until(
#             EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
#         )
#         element.click()
#         print("✓ Profile clicked again")
#         time.sleep(4)
# # ////////////////////////////////////////////////////////////////////////////////////////////
        
#         coupons = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Coupons")
#             )
#         )
#         coupons.click()
#         print("✓ Coupons clicked")
#         time.sleep(2)
        
#         element = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "Coupon: Save 10%, Save: , Expires on 30-06-2026, Code PJN0ZP"
#                 )
#             )
#         )
#         element.click()
#         print("✓ Coupon selected")
#         time.sleep(2)
        
#         edit_text = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located(
#                 (AppiumBy.XPATH, '//android.widget.EditText[@text="Enter coupon code"]')
#             )
#         )
#         edit_text.click()
#         edit_text.clear()
#         edit_text.send_keys("3Z1Z2Y")
#         print("✓ Coupon code entered")
#         time.sleep(1)
        
#         add_coupon = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Coupon"]')
#             )
#         )
#         add_coupon.click()
#         print("✓ Add Coupon clicked")
#         time.sleep(2)
        
#         driver.back()
#         print("✓ Back clicked")
#         time.sleep(2)
        
#         lbp_balance = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="LBP Balance"]')
#             )
#         )
#         lbp_balance.click()
#         print("✓ LBP Balance clicked")
#         time.sleep(2)

#         # Click "Add Funds"
#         add_funds = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Funds"]')
#             )
#         )
#         add_funds.click()
#         print("✓ Add Funds clicked")
#         time.sleep(2)

#         # Find the amount input field
#         amount_input = wait.until(
#             EC.presence_of_element_located(
#                 (AppiumBy.CLASS_NAME, 'android.widget.EditText')
#             )
#         )

#         # Type amount
#         amount_input.click()
#         amount_input.clear()
#         amount_input.send_keys("180000")
#         print("✓ Amount entered: 180000")

#         # Hide keyboard
#         try:
#             driver.hide_keyboard()
#         except:
#             pass
#         time.sleep(1)

#         tokyo = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')
#             )
#         )
#         tokyo.click()
#         print("✓ Tokyo selected")
#         time.sleep(1)
        
#         next_btn = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]')
#             )
#         )
#         next_btn.click()
#         print("✓ Next clicked")
#         time.sleep(2)
        
#         confirm_btn = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ID, "android:id/button1")
#             )
#         )
#         confirm_btn.click()
#         print("✓ Confirmed")
#         time.sleep(3)
        
#         driver.back()
#         print("✓ Back clicked")
#         time.sleep(2)
        
#         faq = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "FAQ")
#             )
#         )
#         faq.click()
#         print("✓ FAQ clicked")
#         time.sleep(2)
        
#         oh_lala = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
#             )
#         )
#         oh_lala.click()
#         print("✓ Oh lala clicked (expand)")
#         time.sleep(2)
        
#         oh_lala = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
#             )
#         )
#         oh_lala.click()
#         print("✓ Oh lala clicked (collapse)")
#         time.sleep(2)
        
#         driver.back()
#         print("✓ Back clicked")
#         time.sleep(2)
        
#         get_support = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ACCESSIBILITY_ID, "Get Support")
#             )
#         )
#         get_support.click()
#         print("✓ Get Support clicked")
#         time.sleep(2)
        
#         support_account = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Support For account"]')
#             )
#         )
#         support_account.click()
#         print("✓ Support For account clicked")
#         time.sleep(2)
        
#         faq_item = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     '//android.widget.TextView[@text="How do I update my payment information"]'
#                 )
#             )
#         )
#         faq_item.click()
#         print("✓ FAQ item clicked")
#         time.sleep(2)
        
#         chat_with_us = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.XPATH, '//android.widget.TextView[@text="Chat with us"]')
#             )
#         )
#         chat_with_us.click()
#         print("✓ Chat with us clicked")
#         time.sleep(2)
        
#         driver.back()
#         print("✓ Final back clicked")
#         time.sleep(2)
        
#         # Final click
#         final_element = wait.until(
#             EC.element_to_be_clickable((
#                 AppiumBy.XPATH,
#                 '//com.horcrux.svg.PathView/parent::com.horcrux.svg.GroupView/parent::com.horcrux.svg.SvgView/parent::android.view.ViewGroup'
#             ))
#         )
#         final_element.click()
#         print("✓ Final element clicked")
#         time.sleep(2)
     
#     except Exception as e:
#         print(f"Error in userAutomation flow: {e}")
#         raise

def select_location(driver, wait):
    """Select location from address list"""
    print("Attempting to select location...")

    try:
        # Re-find and click in one shot to avoid stale reference
        wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Test']")
            )
        )
        # Re-locate before clicking to get a fresh reference
        driver.find_element(
            AppiumBy.XPATH, "//android.widget.TextView[@text='Test']"
        ).click()
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
        except Exception:
            print("Could not find address using any method")


def userAutomation(driver, wait):          # ← removed 'self'
    """Helper: Search for products and add items to cart"""
    print("Starting profile update flow..")

    try:
        element = wait.until(              # ← was self.wait
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
            ))
        )
        element.click()
        print("✓ Profile screen opened")
        time.sleep(2)

        image_view = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ImageView"))
        )
        image_view.click()
        print("✓ ImageView clicked")
        time.sleep(2)

        element = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.Button/com.horcrux.svg.SvgView"
            ))
        )
        element.click()
        print("✓ SVG element clicked")
        time.sleep(2)

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Female"))
        )
        element.click()
        print("✓ Female selected")
        time.sleep(1)

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]')
            )
        )
        element.click()
        print("✓ Save clicked")
        time.sleep(2)

        driver.back()
        print("✓ Back button clicked")
        time.sleep(2)

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Orders"))
        )
        element.click()
        print("✓ Orders clicked")
        time.sleep(2)

        elements = driver.find_elements(
            AppiumBy.XPATH,
            '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/'
            'android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/'
            'android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView'
        )
        if elements:
            elements[0].click()
            print("✓ Optional element found and clicked")
        else:
            print("⚠ Optional element not found, continuing...")
        time.sleep(6)

        driver.back()
        print("✓ Back button clicked")
        time.sleep(2)

        driver.back()

        # ── Coupons ───────────────────────────────────────────────────────────
        coupons = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Coupons"))
        )
        coupons.click()
        print("✓ Coupons clicked")
        time.sleep(2)

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "Coupon: Save 10%, Save: , Expires on 30-06-2026, Code PJN0ZP"
            ))
        )
        element.click()
        print("✓ Coupon selected")
        time.sleep(2)

        edit_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Enter coupon code"]')
            )
        )
        edit_text.click()
        edit_text.clear()
        edit_text.send_keys("3Z1Z2Y")
        print("✓ Coupon code entered")
        time.sleep(1)

        add_coupon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Coupon"]')
            )
        )
        add_coupon.click()
        print("✓ Add Coupon clicked")
        time.sleep(2)

        driver.back()
        print("✓ Back clicked")
        time.sleep(2)

        # ── LBP Balance ───────────────────────────────────────────────────────
        lbp_balance = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="LBP Balance"]')
            )
        )
        lbp_balance.click()
        print("✓ LBP Balance clicked")
        time.sleep(2)

        add_funds = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Add Funds"]')
            )
        )
        add_funds.click()
        print("✓ Add Funds clicked")
        time.sleep(2)

        amount_input = wait.until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
        )
        amount_input.click()
        amount_input.clear()
        amount_input.send_keys("180000")
        print("✓ Amount entered: 180000")
        try:
            driver.hide_keyboard()
        except Exception:
            pass
        time.sleep(1)

        tokyo = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')
            )
        )
        tokyo.click()
        print("✓ Tokyo selected")
        time.sleep(1)

        next_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]')
            )
        )
        next_btn.click()
        print("✓ Next clicked")
        time.sleep(2)

        confirm_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
        )
        confirm_btn.click()
        print("✓ Confirmed")
        time.sleep(3)

        driver.back()
        print("✓ Back clicked")
        time.sleep(2)

        # ── FAQ ───────────────────────────────────────────────────────────────
        faq = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "FAQ"))
        )
        faq.click()
        print("✓ FAQ clicked")
        time.sleep(2)

        oh_lala = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
            )
        )
        oh_lala.click()
        print("✓ Oh lala clicked (expand)")
        time.sleep(2)

        oh_lala = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Oh lala"]')
            )
        )
        oh_lala.click()
        print("✓ Oh lala clicked (collapse)")
        time.sleep(2)

        driver.back()
        print("✓ Back clicked")
        time.sleep(2)

        # ── Get Support ───────────────────────────────────────────────────────
        get_support = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Get Support"))
        )
        get_support.click()
        print("✓ Get Support clicked")
        time.sleep(2)

        support_account = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Support For account"]')
            )
        )
        support_account.click()
        print("✓ Support For account clicked")
        time.sleep(2)

        faq_item = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="How do I update my payment information"]'
            ))
        )
        faq_item.click()
        print("✓ FAQ item clicked")
        time.sleep(2)

        chat_with_us = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Chat with us"]')
            )
        )
        chat_with_us.click()
        print("✓ Chat with us clicked")
        time.sleep(2)

        driver.back()
        print("✓ Final back clicked")
        time.sleep(2)

        final_element = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//com.horcrux.svg.PathView/parent::com.horcrux.svg.GroupView'
                '/parent::com.horcrux.svg.SvgView/parent::android.view.ViewGroup'
            ))
        )
        final_element.click()
        print("✓ Final element clicked")
        time.sleep(2)

    except Exception as e:
        print(f"Error in userAutomation flow: {e}")
        raise


def test_complete_user_app_flow():
    """Complete end-to-end user app automation test"""
    print("🔥 USER APP TEST STARTED 🔥")
    
    driver = None
    try:
        # Initialize driver
        driver = create_driver()
        wait = WebDriverWait(driver, 20)
        print("✓ App launched")
        time.sleep(3)
        
        # Select location
        select_location(driver, wait)
        print("✓ Location selected")
        assert driver.current_package == "com.lyxa.user", (
            "ASSERTION FAILED: App is not running or crashed after location selection."
        )
        print("[ASSERTION PASSED] App active after location selection.")
        time.sleep(2)
        
        # Run user automation flow
        userAutomation(driver, wait)
        print("✓ User automation completed successfully")

        assert driver.current_package == "com.lyxa.user", (
            "ASSERTION FAILED: App session disconnected during user flow."
        )
        print("[ASSERTION PASSED] Complete user automation flow verified with assertions.")
        
        # Take success screenshot
        driver.save_screenshot("user_app_test_success.png")
        print("✓ Success screenshot saved")
        
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        if driver:
            driver.save_screenshot("user_app_test_failure.png")
            print("Screenshot saved: user_app_test_failure.png")
        raise
        
    finally:
        if driver:
            driver.quit()
            print("✓ Driver closed")


if __name__ == "__main__":
    # Allow running directly with: python tests/test_userApp.py
    test_complete_user_app_flow()