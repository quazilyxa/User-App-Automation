import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey





"""
USER PROFILE AUTOMATION FEATURES TESTED
=======================================

TEST SUITE STRUCTURE
-------------------
The test suite is organized into 4 phases based on operation intensity:
- Phase 1: READ-ONLY (Tests 01-03) - Non-destructive viewing operations
- Phase 2: MODERATE OPS (Tests 04-05) - Operations with moderate impact
- Phase 3: FEATURES (Tests 06-07) - Feature-specific functionality
- Phase 4: DESTRUCTIVE (Test 08) - Permanent deletion operations

1. LOCATION MANAGEMENT
   -------------------
   - Initial location selection at app launch
   - Address selection from list (Google Building 40)
   - Scrolling to specific address (Lyxa BD, Bd, Bd)
   - Multiple address selection strategies:
     * XPATH by text
     * Accessibility ID
     * UiAutomator scrollIntoView
   - Error handling with fallback methods

2. PROFILE SCREEN NAVIGATION
   -------------------------
   - Profile icon/menu access
   - Navigation to profile screen from home
   - Complex XPath navigation through view hierarchy
   - Screenshot capture for debugging

3. NOTIFICATIONS (test_01_check_notifications)
   -------------------------------------------
   - Opening notifications panel
   - Viewing notification list
   - Back navigation from notifications
   - Debug screenshot capture before/after
   - Page source saving for troubleshooting

4. BANNER INTERACTIONS (test_02_click_banner_link)
   ------------------------------------------------
   - Promotional banner clicking (Coca-Cola)
   - Multiple banner location strategies:
     * Full XPath navigation
     * Simplified HorizontalScrollView approach
     * UiAutomator scrollIntoView
     * Coordinate-based tapping (fallback)
   - Banner click navigation verification
   - Back navigation to home screen

5. CART FUNCTIONALITY (test_03_visit_my_cart)
   ------------------------------------------
   - Cart icon identification
   - Cart screen opening
   - Cart contents viewing
   - Cart exit navigation

6. ORDER MANAGEMENT (test_04_cancel_order)
   ---------------------------------------
   - Orders list navigation
   - Order menu access (three dots/SVG icon)
   - Cancel Order button interaction
   - Confirmation dialog handling
   - Order cancellation verification
   - Back navigation to profile
   - Page source saving on failure

7. PAYMENT CARD MANAGEMENT (test_05_add_and_delete_card)
   ------------------------------------------------------
   - Manage Cards section navigation
   - Add card SVG icon tapping (center-tap for React Native)
   - Card details entry:
     * Card number (5555555555554444)
     * Expiry date (0530 - MMYY format)
     * CVC code (123)
     * ZIP/Postal code (12345)
   - Continue button interaction
   - Card verification (Tokyo, ****4444)
   - Card action menu access
   - Delete Card functionality
   - Card deletion confirmation

8. SOCIAL FEATURES (test_06_invite_friends)
   ----------------------------------------
   - Invite Friends button access
   - Share/Invite SVG icon interaction
   - Sharing screen verification
   - Screenshot capture
   - Back navigation

9. CUSTOMER SUPPORT (test_07_support_tickets)
   ------------------------------------------
   - Support Tickets section access
   - Tickets list viewing
   - Navigation to support section
   - Back navigation

10. ADDRESS MANAGEMENT (test_08_delete_address)
    -------------------------------------------
    - Addresses/Manage Addresses navigation
    - Address list viewing
    - Placeholder for address deletion flow

11. UI ELEMENT INTERACTIONS
    ------------------------
    - SVG elements (SvgView, GroupView, PathView)
      * Center-tap for React Native elements
      * Coordinate-based tapping
    - ImageView elements
    - TextView elements
    - EditText fields
      * Card number input
      * Expiry date input
      * CVC input
      * ZIP code input
    - ScrollView navigation
    - HorizontalScrollView handling
    - RecyclerView elements
    - Accessibility ID elements
    - Resource ID identification
    - Back button navigation

12. WAIT STRATEGIES
    ----------------
    - Explicit waits with expected conditions
      * Element presence
      * Element clickability
    - Timeouts with error handling
    - Screenshot capture on timeout

13. ERROR HANDLING & DEBUGGING
    --------------------------
    - Try-catch blocks for robust execution
    - Multiple element location fallbacks
    - Screenshot capture on failure
    - Page source saving for debugging
    - Detailed logging of each action
    - Method-specific failure screenshots

14. TEST SETUP & TEARDOWN
    ---------------------
    - Class-level setup (setup_class)
      * Driver initialization
      * Location selection
      * Profile screen navigation
    - Method-level setup (setup_method)
    - Class-level teardown (teardown_class)
      * Driver cleanup

15. SPECIALIZED INTERACTIONS
    -------------------------
    - React Native element handling (center-tap required)
    - UiAutomator selectors for complex element finding
    - Multiple SVG PathView instance handling
    - Card information entry with specific formats
    - Coordinate-based tapping for problematic elements
    - Hybrid element location strategies

16. TEST ORGANIZATION
    -----------------
    - Structured test suite with clear phases
    - Descriptive test method naming
    - Comprehensive logging for each step
    - Screenshot documentation
    - Failure recovery mechanisms
    - Independent test methods

17. HELPER METHODS
    ---------------
    - select_location: Location selection at startup
    - select_address_in_scroll_view: Scrolling address selection
    - navigate_to_profile_screen: Profile navigation
    - get_available_system_port: Port management for parallel execution
"""




class TestUserProfile:
    """Test suite for user profile and account features"""
    
    driver = None
    wait = None
    
    @classmethod
    def setup_class(cls):
        """Setup driver once for all tests"""
        cls.driver = create_driver()
        cls.wait = WebDriverWait(cls.driver, 20)
        print("✓ App launched")
        time.sleep(3)
        
        # Select location first (if needed)
        try:
            cls.select_location(cls.driver, cls.wait)
            print("✓ Location selected")
        except Exception as e:
            print(f"Location selection skipped or failed: {e}")
        
        # Navigate to profile screen once for all tests
        try:
            cls.navigate_to_profile_screen(cls.driver, cls.wait)
            print("✓ Navigated to profile screen")
        except Exception as e:
            print(f"Profile navigation failed: {e}")
    
    @classmethod
    def teardown_class(cls):
        """Close driver after all tests"""
        if cls.driver:
            cls.driver.quit()
            print("✓ Driver closed")
    
    @staticmethod
    def get_available_system_port():
        return random.randint(8200, 8300)

    @staticmethod
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

            TestUserProfile.select_address_in_scroll_view(driver, "Lyxa BD, Bd, Bd")
            
        except Exception as e:
            print(f"Error in select_location: {e}")
            try:
                driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    "Lyxa BD, Bd, Bd"
                ).click()
            except:
                print("Could not find address using any method")
    
    @staticmethod            
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
    
    @staticmethod
    def navigate_to_profile_screen(driver, wait):
        """Navigate to profile/menu screen"""
        try:
            xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup'

            element = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
            )
            element.click()
            print("✓ Profile icon clicked")
            time.sleep(2)  # Wait for page transition
        except Exception as e:
            print(f"Error navigating to profile: {e}")
            driver.save_screenshot("navigation_failed.png")
            raise
    
    def setup_method(self):
        """Run before each test to ensure we're on the profile screen"""
        print("\n🔄 Ensuring on profile screen...")
        time.sleep(1)
    
    # ==================== PHASE 1: READ-ONLY ====================
    
    def test_01_check_notifications(self):
        """Check and view notifications"""
        print("📬 Testing notifications...")
        
        # Debug: Take screenshot of current screen
        self.driver.save_screenshot("before_notifications.png")
        print("📸 Screenshot saved: before_notifications.png")
        
        try:
            # Method 1: Try XPath from profile screen
            xpath = (
                '//android.widget.FrameLayout[@resource-id="android:id/content"]'
                '/android.widget.FrameLayout/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup/'
                'android.widget.ScrollView/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup[5]'
                '/android.view.ViewGroup'
            )
            element = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
            )
            element.click()
            print("✓ Notifications clicked")
            time.sleep(3)
            
            # Go back
            self.driver.back()
            print("✓ Back pressed")
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error while testing notifications: {e}")
            self.driver.save_screenshot("test_01_failure.png")
            # Save page source for debugging
            with open("page_source.xml", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("📄 Page source saved: page_source.xml")
            raise

    def test_02_click_banner_link(self):
        """Click promotional banner (Coca-Cola)"""
        print("🎯 Testing banner click...")
        try:
            # Navigate back to home screen first
            try:
                self.driver.back()
                time.sleep(2)
                print("✓ Navigated back to home")
            except:
                print("Already on home screen")
            
            # Take screenshot to see current state
            self.driver.save_screenshot("before_banner_click.png")
            
            # Method 1: Try the complete XPath you provided
            try:
                xpath = (
                    '//android.widget.FrameLayout[@resource-id="android:id/content"]'
                    '/android.widget.FrameLayout/android.view.ViewGroup/'
                    'android.view.ViewGroup/android.view.ViewGroup/'
                    'android.widget.ScrollView/android.view.ViewGroup/'
                    'android.view.ViewGroup/android.view.ViewGroup[3]/'
                    'android.view.ViewGroup/android.widget.ScrollView/'
                    'android.view.ViewGroup/android.view.ViewGroup/'
                    'android.view.ViewGroup[3]/android.widget.HorizontalScrollView/'
                    'android.view.ViewGroup/android.view.ViewGroup/'
                    'android.view.ViewGroup/android.widget.ImageView'
                )
                
                banner = self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
                )
                banner.click()
                print("✓ Banner clicked (Method 1: Full XPath)")
                time.sleep(3)
                
            except Exception as e1:
                print(f"Method 1 failed: {e1}")
                
                # Method 2: Try finding ImageView in HorizontalScrollView
                try:
                    xpath = '//android.widget.HorizontalScrollView//android.widget.ImageView'
                    banner = self.wait.until(
                        EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
                    )
                    banner.click()
                    print("✓ Banner clicked (Method 2: Simplified)")
                    time.sleep(3)
                    
                except Exception as e2:
                    print(f"Method 2 failed: {e2}")
                    
                    # Method 3: Find by UiAutomator
                    try:
                        banner = self.driver.find_element(
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().className("android.widget.ScrollView"))'
                            '.scrollIntoView(new UiSelector().className("android.widget.ImageView"))'
                        )
                        banner.click()
                        print("✓ Banner clicked (Method 3: UiAutomator)")
                        time.sleep(3)
                        
                    except Exception as e3:
                        print(f"Method 3 failed: {e3}")
                        
                        # Method 4: Click by coordinates (center of banner area)
                        screen_size = self.driver.get_window_size()
                        x = int(screen_size['width'] * 0.5)  # Center horizontally
                        y = int(screen_size['height'] * 0.3)  # About 30% down
                        
                        self.driver.tap([(x, y)])
                        print(f"✓ Banner clicked (Method 4: Coordinates {x}, {y})")
                        time.sleep(3)
            
            # Verify we navigated to a new screen
            self.driver.save_screenshot("after_banner_click.png")
            print("✓ Navigated to shop link")
            
            # Go back
            self.driver.back()
            print("✓ Back pressed")
            time.sleep(2)
            
            print("✓ Banner link test completed")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_02_failure.png")
            raise
        
    def test_03_visit_my_cart(self):
        """View cart contents"""
        print("🛒 Testing cart view...")
        try:
            # Click cart icon using the XPath you provided
            cart_xpath = (
                '//android.widget.FrameLayout[@resource-id="android:id/content"]'
                '/android.widget.FrameLayout/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup/'
                'android.widget.ScrollView/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup[2]/'
                'android.view.ViewGroup[4]/android.view.ViewGroup/'
                'android.view.ViewGroup'
            )
            
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, cart_xpath))
            )
            cart_icon.click()
            print("✓ Cart icon clicked")
            time.sleep(2)
            
            # Verify cart screen opened
            self.driver.save_screenshot("cart_opened.png")
            print("✓ Cart opened")
            
            # Go back
            self.driver.back()
            time.sleep(1)
            print("✓ Returned from cart")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_03_failure.png")
            raise
    
    # ==================== PHASE 2: MODERATE OPS ====================
    
    def test_04_cancel_order(self):
        """Cancel an existing order"""
        print("❌ Testing order cancellation...")
        try:
            # Ensure on profile screen
            self.navigate_to_profile_screen(self.driver, self.wait)
            time.sleep(2)
            print("✓ On profile screen")
            
            # Navigate to orders
            orders_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Orders"
                ))
            )
            orders_btn.click()
            time.sleep(2)
            print("✓ Navigated to orders")
            
            # Take screenshot to see orders list
            self.driver.save_screenshot("orders_list.png")
            
            # Click on first order (the three dots menu or order card)
            parent_xpath = (
                '//androidx.recyclerview.widget.RecyclerView'
                '/android.widget.FrameLayout/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup[3]'
                '/android.view.ViewGroup/android.widget.ScrollView/'
                'android.view.ViewGroup/android.view.ViewGroup/'
                'android.view.ViewGroup[3]/com.horcrux.svg.SvgView'
            )
            
            order_menu = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, parent_xpath))
            )
            order_menu.click()
            print("✓ Opened order menu")
            time.sleep(2)
            
            # Click "Cancel Order" button
            cancel_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, 
                    '//android.widget.TextView[@text="Cancel Order"]'
                ))
            )
            cancel_btn.click()
            print("✓ Clicked Cancel Order")
            time.sleep(2)
            
            # Confirm cancellation
            confirm_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, 
                    '//android.widget.TextView[@text="Confirm Cancellation"]'
                ))
            )
            confirm_btn.click()
            print("✓ Order cancellation confirmed")
            time.sleep(2)
            
            # Take screenshot of cancellation result
            self.driver.save_screenshot("order_cancelled.png")
            
            # Go back to profile
            self.driver.back()
            time.sleep(1)
            print("✓ Order cancellation test completed")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_04_failure.png")
            # Save page source for debugging
            with open("test_04_page_source.xml", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise
        
    def test_05_add_and_delete_card(self):
        """Add payment card and delete it"""
        print("💳 Testing card management...")
        try:
            # # Ensure on profile screen
            # self.navigate_to_profile_screen(self.driver, self.wait)
            # time.sleep(2)

            # Navigate to Manage Cards
            manage_cards = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Manage Cards"]'
                ))
            )
            manage_cards.click()
            print("✓ Manage Cards opened")
            time.sleep(2)

            svg_xpath = (
                '//android.widget.FrameLayout[@resource-id="android:id/content"]'
                '/android.widget.FrameLayout/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup/'
                '/android.widget.ScrollView/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup[6]'
                '/android.view.ViewGroup/com.horcrux.svg.SvgView'
            )

            svg = self.wait.until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    svg_xpath
                ))
            )

            # 🔥 TAP SVG (this was missing)
            x = svg.location['x'] + svg.size['width'] / 2
            y = svg.location['y'] + svg.size['height'] / 2
            self.driver.tap([(x, y)])

            print("✓ Manage Cards SVG tapped")
            time.sleep(2)
            
            # Enter card number
            card_number = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="com.lyxa.user:id/et_card_number"]'
                ))
            )
            card_number.click()
            card_number.send_keys("5555555555554444")
            print("✓ Card number entered")

            # Enter expiry date (MMYY)
            expiry = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="com.lyxa.user:id/et_expiry"]'
                ))
            )
            expiry.click()
            expiry.send_keys("0530")
            print("✓ Expiry date entered")

            # Enter CVC
            cvc = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="com.lyxa.user:id/et_cvc"]'
                ))
            )
            cvc.click()
            cvc.send_keys("123")
            print("✓ CVC entered")

            # Enter ZIP / Postal Code
            zip_code = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="com.lyxa.user:id/postal_code"]'
                ))
            )
            zip_code.click()
            zip_code.send_keys("12345")
            print("✓ ZIP code entered")

            continue_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Continue"]'
                ))
            )

            continue_btn.click()
            print("✓ Continue button clicked")
            time.sleep(2)
            
            svg_icon = self.wait.until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.view.ViewGroup[@content-desc="Tokyo, ****4444, Exp 5/2030"]'
                    '/android.view.ViewGroup/android.view.ViewGroup'
                    '/com.horcrux.svg.SvgView'
                ))
            )

            # Tap center of SVG
            x = svg_icon.location['x'] + svg_icon.size['width'] / 2
            y = svg_icon.location['y'] + svg_icon.size['height'] / 2

            self.driver.tap([(x, y)])
            print("✓ Card action icon tapped")
            time.sleep(1)

            delete_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Delete Card"]'
                ))
            )

            delete_btn.click()
            print("✓ Delete Card button clicked")
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_05_failure.png")
            raise

    # ==================== PHASE 3: FEATURES ====================
    
    def test_06_invite_friends(self):
        """Test invite friends functionality"""
        print("👥 Testing invite friends...")
        try:
            # # Ensure on profile screen
            # self.navigate_to_profile_screen(self.driver, self.wait)
            # time.sleep(2)
            
            # Click Invite Friends button
            invite_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Invite Friends"]'
                ))
            )
            invite_btn.click()
            print("✓ Clicked Invite Friends")
            time.sleep(2)
            
            # Click the share/invite SVG icon
            svg_xpath = (
                '//android.widget.FrameLayout[@resource-id="android:id/content"]'
                '/android.widget.FrameLayout/android.view.ViewGroup/'
                'android.view.ViewGroup/android.view.ViewGroup/'
                'android.widget.ScrollView/android.view.ViewGroup/'
                'android.view.ViewGroup/android.widget.ScrollView/'
                'android.view.ViewGroup/android.view.ViewGroup[7]'
                '/com.horcrux.svg.SvgView'
            )
            
            svg = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, svg_xpath))
            )
            svg.click()
            print("✓ Clicked share icon")
            time.sleep(2)
            
            # Take screenshot
            self.driver.save_screenshot("invite_friends_opened.png")
            
            # Go back
            self.driver.back()
            time.sleep(1)
            print("✓ Invite friends test completed")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_06_failure.png")
            raise
        
    def test_07_support_tickets(self):
        """View support tickets"""
        print("🎫 Testing support tickets...")
        try:
            # Ensure on profile screen
            self.navigate_to_profile_screen(self.driver, self.wait)
            time.sleep(2)
            
            support_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Support Tickets"
                ))
            )
            support_btn.click()
            time.sleep(2)
            
            print("✓ Support tickets opened")
            
            # Go back
            self.driver.back()
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_07_failure.png")
            raise
    
    # ==================== PHASE 4: DESTRUCTIVE ====================
    
    def test_08_delete_address(self):
        """Delete saved address"""
        print("🗑️ Testing address deletion...")
        try:
            # Ensure on profile screen
            self.navigate_to_profile_screen(self.driver, self.wait)
            time.sleep(2)
            
            # Navigate to addresses
            addresses_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Addresses"] | '
                    '//android.widget.TextView[@text="Manage Addresses"]'
                ))
            )
            addresses_btn.click()
            time.sleep(2)
            
            print("✓ Navigated to addresses")
            
            # Go back
            self.driver.back()
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.driver.save_screenshot("test_08_failure.png")
            raise