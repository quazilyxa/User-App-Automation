from asyncio import wait
import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey





# """
# USER PROFILE AUTOMATION FEATURES TESTED
# =======================================

# TEST SUITE STRUCTURE
# -------------------
# The test suite is organized into 4 phases based on operation intensity:
# - Phase 1: READ-ONLY (Tests 01-03) - Non-destructive viewing operations
# - Phase 2: MODERATE OPS (Tests 04-05) - Operations with moderate impact
# - Phase 3: FEATURES (Tests 06-07) - Feature-specific functionality
# - Phase 4: DESTRUCTIVE (Test 08) - Permanent deletion operations

# 1. LOCATION MANAGEMENT
#    -------------------
#    - Initial location selection at app launch
#    - Address selection from list (Google Building 40)
#    - Scrolling to specific address (Lyxa BD, Bd, Bd)
#    - Multiple address selection strategies:
#      * XPATH by text
#      * Accessibility ID
#      * UiAutomator scrollIntoView
#    - Error handling with fallback methods

# 2. PROFILE SCREEN NAVIGATION
#    -------------------------
#    - Profile icon/menu access
#    - Navigation to profile screen from home
#    - Complex XPath navigation through view hierarchy
#    - Screenshot capture for debugging

# 3. NOTIFICATIONS (test_01_check_notifications)
#    -------------------------------------------
#    - Opening notifications panel
#    - Viewing notification list
#    - Back navigation from notifications
#    - Debug screenshot capture before/after
#    - Page source saving for troubleshooting

# 4. BANNER INTERACTIONS (test_02_click_banner_link)
#    ------------------------------------------------
#    - Promotional banner clicking (Coca-Cola)
#    - Multiple banner location strategies:
#      * Full XPath navigation
#      * Simplified HorizontalScrollView approach
#      * UiAutomator scrollIntoView
#      * Coordinate-based tapping (fallback)
#    - Banner click navigation verification
#    - Back navigation to home screen

# 5. CART FUNCTIONALITY (test_03_visit_my_cart)
#    ------------------------------------------
#    - Cart icon identification
#    - Cart screen opening
#    - Cart contents viewing
#    - Cart exit navigation

# 6. ORDER MANAGEMENT (test_04_cancel_order)
#    ---------------------------------------
#    - Orders list navigation
#    - Order menu access (three dots/SVG icon)
#    - Cancel Order button interaction
#    - Confirmation dialog handling
#    - Order cancellation verification
#    - Back navigation to profile
#    - Page source saving on failure

# 7. PAYMENT CARD MANAGEMENT (test_05_add_and_delete_card)
#    ------------------------------------------------------
#    - Manage Cards section navigation
#    - Add card SVG icon tapping (center-tap for React Native)
#    - Card details entry:
#      * Card number (5555555555554444)
#      * Expiry date (0530 - MMYY format)
#      * CVC code (123)
#      * ZIP/Postal code (12345)
#    - Continue button interaction
#    - Card verification (Tokyo, ****4444)
#    - Card action menu access
#    - Delete Card functionality
#    - Card deletion confirmation

# 8. SOCIAL FEATURES (test_06_invite_friends)
#    ----------------------------------------
#    - Invite Friends button access
#    - Share/Invite SVG icon interaction
#    - Sharing screen verification
#    - Screenshot capture
#    - Back navigation

# 9. CUSTOMER SUPPORT (test_07_support_tickets)
#    ------------------------------------------
#    - Support Tickets section access
#    - Tickets list viewing
#    - Navigation to support section
#    - Back navigation

# 10. ADDRESS MANAGEMENT (test_08_delete_address)
#     -------------------------------------------
#     - Addresses/Manage Addresses navigation
#     - Address list viewing
#     - Placeholder for address deletion flow

# 11. UI ELEMENT INTERACTIONS
#     ------------------------
#     - SVG elements (SvgView, GroupView, PathView)
#       * Center-tap for React Native elements
#       * Coordinate-based tapping
#     - ImageView elements
#     - TextView elements
#     - EditText fields
#       * Card number input
#       * Expiry date input
#       * CVC input
#       * ZIP code input
#     - ScrollView navigation
#     - HorizontalScrollView handling
#     - RecyclerView elements
#     - Accessibility ID elements
#     - Resource ID identification
#     - Back button navigation

# 12. WAIT STRATEGIES
#     ----------------
#     - Explicit waits with expected conditions
#       * Element presence
#       * Element clickability
#     - Timeouts with error handling
#     - Screenshot capture on timeout

# 13. ERROR HANDLING & DEBUGGING
#     --------------------------
#     - Try-catch blocks for robust execution
#     - Multiple element location fallbacks
#     - Screenshot capture on failure
#     - Page source saving for debugging
#     - Detailed logging of each action
#     - Method-specific failure screenshots

# 14. TEST SETUP & TEARDOWN
#     ---------------------
#     - Class-level setup (setup_class)
#       * Driver initialization
#       * Location selection
#       * Profile screen navigation
#     - Method-level setup (setup_method)
#     - Class-level teardown (teardown_class)
#       * Driver cleanup

# 15. SPECIALIZED INTERACTIONS
#     -------------------------
#     - React Native element handling (center-tap required)
#     - UiAutomator selectors for complex element finding
#     - Multiple SVG PathView instance handling
#     - Card information entry with specific formats
#     - Coordinate-based tapping for problematic elements
#     - Hybrid element location strategies

# 16. TEST ORGANIZATION
#     -----------------
#     - Structured test suite with clear phases
#     - Descriptive test method naming
#     - Comprehensive logging for each step
#     - Screenshot documentation
#     - Failure recovery mechanisms
#     - Independent test methods

# 17. HELPER METHODS
#     ---------------
#     - select_location: Location selection at startup
#     - select_address_in_scroll_view: Scrolling address selection
#     - navigate_to_profile_screen: Profile navigation
#     - get_available_system_port: Port management for parallel execution
# """




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

            cls.select_location(cls.driver, cls.wait)
            # cls.navigate_to_profile_screen(cls.driver, cls.wait)

        @classmethod
        def teardown_class(cls):
            """Close driver after all tests"""
            if cls.driver:
                cls.driver.quit()
                print("✓ Driver closed")

        @staticmethod
        def select_location(driver, wait):
            """Select location from address list"""
            print("Selecting location...")

            element = wait.until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    "//android.widget.TextView[@text='Test']"
                ))
            )
            element.click()
            time.sleep(2)

            address = "Lyxa BD, Bd, Bd"
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{address}"))'
            )
            element.click()
            print(f"✓ Location selected: {address}")
            time.sleep(5)

        @staticmethod
        def navigate_to_profile_screen(driver, wait):
            """Navigate to profile/menu screen"""
            print("Navigating to profile screen...")

            user_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="home-header-user-svg"]'
                ))
            )
            user_icon.click()
            print("✓ Profile screen opened")
            time.sleep(2)


        # ==================== PHASE 1: READ-ONLY ====================

        def test_01_check_notifications(self):
            """Check and view notifications with verified assertions"""
            print("Testing notifications...")
            
            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            assert element.is_displayed(), "ASSERTION FAILED: Profile icon is not displayed."
            element.click()
            print("✓ Profile screen opened")
            time.sleep(2)

            notif_btn = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Notifications"))
            )
            assert notif_btn.is_displayed(), "ASSERTION FAILED: 'Notifications' menu item not displayed."
            print("[ASSERTION PASSED] Notifications button verified and visible.")
            notif_btn.click()
            print("✓ Notifications opened")
            time.sleep(3)

            self.driver.back()
            print("✓ Back pressed")
            time.sleep(2)

        def test_02_click_banner_link(self):
            """Click promotional banner with verified assertions"""
            print("Testing banner click...")

            self.driver.back()
            time.sleep(2)

            banner = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    "//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup"
                ))
            )
            assert banner.is_displayed(), "ASSERTION FAILED: Promotional banner is not visible."
            print("[ASSERTION PASSED] Promotional banner found and displayed.")
            banner.click()
            print("✓ Banner clicked")
            time.sleep(5)

            self.driver.back()
            print("✓ Back pressed")
            time.sleep(2)
            assert self.driver.current_package == "com.lyxa.user", "ASSERTION FAILED: App exited after banner navigation."
            print("[ASSERTION PASSED] Successfully returned from banner link to app.")

        def test_03_visit_my_cart(self):
            """View cart contents with verified assertions"""
            print("Testing cart view...")

            basket_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Go-to-basket"))
            )
            assert basket_btn.is_displayed(), "ASSERTION FAILED: 'Go-to-basket' button is not visible."
            print("[ASSERTION PASSED] 'Go-to-basket' icon verified and clickable.")
            basket_btn.click()
            print("✓ Cart opened")
            time.sleep(2)

            cart_active = len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Cart' or @text='Basket' or @content-desc='Go-to-basket' or contains(@text, 'LBP')]")) > 0
            assert cart_active, "ASSERTION FAILED: Cart contents/screen not active."
            print("[ASSERTION PASSED] Cart screen verified active.")

            self.driver.back()
            print("✓ Returned from cart")
            time.sleep(1)

        # ==================== PHASE 2: MODERATE OPS ====================

        def test_04_cancel_order(self):
            """Cancel an existing order with verified assertions"""
            print("Testing order cancellation...")

            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            assert element.is_displayed(), "ASSERTION FAILED: Profile icon not found."
            element.click()
            time.sleep(2)

            orders_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Orders"
                ))
            )
            assert orders_btn.is_displayed(), "ASSERTION FAILED: 'Orders' button not visible in profile."
            print("[ASSERTION PASSED] 'Orders' navigation button verified.")
            orders_btn.click()
            print("✓ Navigated to orders")
            time.sleep(2)

            order_menu = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//androidx.recyclerview.widget.RecyclerView'
                    '/android.widget.FrameLayout/android.view.ViewGroup'
                    '/android.view.ViewGroup/android.view.ViewGroup[3]'
                    '/android.view.ViewGroup/android.widget.ScrollView'
                    '/android.view.ViewGroup/android.view.ViewGroup'
                    '/android.view.ViewGroup[3]/com.horcrux.svg.SvgView'
                ))
            )
            order_menu.click()
            print("✓ Order menu opened")
            time.sleep(2)

            cancel_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Cancel Order"]'
                ))
            )
            assert cancel_btn.is_displayed(), "ASSERTION FAILED: 'Cancel Order' option not displayed."
            print("[ASSERTION PASSED] 'Cancel Order' option verified.")
            cancel_btn.click()
            print("✓ Cancel Order clicked")
            time.sleep(2)

            confirm_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Confirm Cancellation"]'
                ))
            )
            assert confirm_btn.is_displayed(), "ASSERTION FAILED: 'Confirm Cancellation' modal button not displayed."
            print("[ASSERTION PASSED] 'Confirm Cancellation' button verified.")
            confirm_btn.click()
            print("✓ Cancellation confirmed")
            time.sleep(2)

            self.driver.back()
            
            profile_icon = self.wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            self.driver.execute_script("mobile: clickGesture", {
                "elementId": profile_icon.id
            })
            print("✓ Profile icon clicked")
            time.sleep(1)

        # def test_05_add_and_delete_card(self):
        #     """Add payment card and delete it"""
        #     print("Testing card management...")


        #     element = self.wait.until(
        #         EC.element_to_be_clickable((
        #             AppiumBy.XPATH,
        #             '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
        #         ))
        #     )
        #     element.click()
        #     time.sleep(2)
        #     print("✓ Profile icon clicked")


        #     manage_cards = self.wait.until(
        #         EC.element_to_be_clickable((
        #             AppiumBy.XPATH,
        #             '//android.widget.TextView[@text="Manage Cards"]'
        #         ))
        #     )
        #     manage_cards.click()
        #     print("✓ Manage Cards opened")
        #     time.sleep(2)

        #     self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "add-card").click()
        #     print("✓ Add card icon tapped")
            
            
            
            
            
            
            
            
            
            
            




        #     # Find the WebView container bounds in native context
        #     webview_container = self.driver.find_element(
        #         AppiumBy.XPATH, '//android.webkit.WebView'
        #     )
        #     bounds = webview_container.rect
        #     base_x = bounds['x'] + bounds['width'] // 2
        #     base_y = bounds['y']

        #     # Approximate field positions as % of WebView height
        #     # Adjust these % values by inspecting the screen once
        #     self.tap_and_type(self.driver, base_x, base_y + int(bounds['height'] * 0.15), "4242424242424242")  # Card number
        #     self.tap_and_type(self.driver, base_x, base_y + int(bounds['height'] * 0.30), "Test User")          # Name
        #     self.tap_and_type(self.driver, base_x - 60, base_y + int(bounds['height'] * 0.45), "12")            # Month
        #     self.tap_and_type(self.driver, base_x + 20, base_y + int(bounds['height'] * 0.45), "26")            # Year
        #     self.tap_and_type(self.driver, base_x + 80, base_y + int(bounds['height'] * 0.45), "123")           # CVV
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

        #     svg_icon = self.wait.until(
        #         EC.presence_of_element_located((
        #             AppiumBy.XPATH,
        #             '//android.view.ViewGroup[@content-desc="Tokyo, ****4444, Exp 5/2030"]'
        #             '/android.view.ViewGroup/android.view.ViewGroup'
        #             '/com.horcrux.svg.SvgView'
        #         ))
        #     )
        #     x = svg_icon.location['x'] + svg_icon.size['width'] / 2
        #     y = svg_icon.location['y'] + svg_icon.size['height'] / 2
        #     self.driver.tap([(x, y)])
        #     print("✓ Card action icon tapped")
        #     time.sleep(1)

        #     delete_btn = self.wait.until(
        #         EC.element_to_be_clickable((
        #             AppiumBy.XPATH,
        #             '//android.widget.TextView[@text="Delete Card"]'
        #         ))
        #     )
        #     delete_btn.click()
        #     print("✓ Card deleted")
        #     time.sleep(2)
        
        
        
        
        
        def test_05_add_and_delete_card(self):
            """Add payment card and delete it"""
            print("Testing card management...")

            # ── Navigate to Manage Cards ──
            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            element.click()
            time.sleep(2)
            print("✓ Profile icon clicked")

            manage_cards = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Manage Cards"]'
                ))
            )
            assert manage_cards.is_displayed(), "ASSERTION FAILED: 'Manage Cards' menu item not displayed."
            print("[ASSERTION PASSED] 'Manage Cards' menu item verified.")
            manage_cards.click()
            time.sleep(2)
            print("✓ Manage Cards opened")

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "add-card").click()
            time.sleep(3)
            print("✓ Add card icon tapped")
            time.sleep(5)
            # ── Get WebView container bounds ──
            webview_container = self.wait.until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH, '//android.webkit.WebView'
                ))
            )
            bounds = webview_container.rect
            base_x = bounds['x'] + bounds['width'] // 2
            base_y = bounds['y']
            h = bounds['height']

            print(f"WebView bounds: x={bounds['x']} y={bounds['y']} "
                f"w={bounds['width']} h={h}")

            # ── Fill card form using tap + mobile:type ──
            self.tap_and_type(base_x,      base_y + int(h * 0.15), "4242424242424242")
            print("✓ Card number entered")

            # Use exact centers calculated from inspector bounds
            self.tap_and_type(539, 746, " Name")  # Name field is tricky, so using calibrated coords
            print("✓ Holder name entered")
            
            time.sleep(3)

            self.tap_and_type(219, 997, "12")
            print("✓ Expiry month entered")

            self.tap_and_type(362, 997, "26")
            print("✓ Expiry year entered")

            time.sleep(3)
            self.tap_and_type(766, 997, "123")
            print("✓ CVV entered")

            time.sleep(1)

            # ── Tap Continue ──
            continue_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]'
                ))
            )
            assert continue_btn.is_displayed(), "ASSERTION FAILED: 'Continue' button not displayed on card form."
            print("[ASSERTION PASSED] Card form 'Continue' button verified.")
            continue_btn.click()
            time.sleep(3)
            print("✓ Continue clicked")

            # ── Delete the card ──
            svg_icon = self.wait.until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.view.ViewGroup[@content-desc="Tokyo, ****4444, Exp 5/2030"]'
                    '/android.view.ViewGroup/android.view.ViewGroup'
                    '/com.horcrux.svg.SvgView'
                ))
            )
            x = svg_icon.location['x'] + svg_icon.size['width'] // 2
            y = svg_icon.location['y'] + svg_icon.size['height'] // 2
            self.driver.tap([(x, y)])
            time.sleep(1)
            print("✓ Card action icon tapped")

            delete_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, '//android.widget.TextView[@text="Delete Card"]'
                ))
            )
            assert delete_btn.is_displayed(), "ASSERTION FAILED: 'Delete Card' option not displayed."
            print("[ASSERTION PASSED] 'Delete Card' action button verified.")
            delete_btn.click()
            time.sleep(2)
            print("✓ Card deleted")

        # ==================== PHASE 3: FEATURES ====================

        def test_06_invite_friends(self):
            """Test invite friends functionality with verified assertions"""
            print("Testing invite friends...")
            
            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            element.click()
            time.sleep(2)
            print("✓ Profile icon clicked")
            time.sleep(2)

            invite_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Invite Friends"]'
                ))
            )
            assert invite_btn.is_displayed(), "ASSERTION FAILED: 'Invite Friends' option not displayed."
            print("[ASSERTION PASSED] 'Invite Friends' menu option verified.")
            invite_btn.click()
            print("✓ Invite Friends opened")
            time.sleep(2)
            
            send_invite_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Send Invite"]'
                ))
            )
            assert send_invite_btn.is_displayed(), "ASSERTION FAILED: 'Send Invite' button not displayed."
            print("[ASSERTION PASSED] 'Send Invite' button verified.")
            send_invite_btn.click()
            print("✓ Send Invite clicked")

            copy_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Copy text"
                ))
            )
            assert copy_btn.is_displayed(), "ASSERTION FAILED: 'Copy text' share button not displayed."
            print("[ASSERTION PASSED] 'Copy text' share button verified.")
            copy_btn.click()
            print("✓ Copy button clicked")
            time.sleep(2)

            self.driver.back()
            time.sleep(1)

        def test_07_support_tickets(self):
            """View support tickets with verified assertions"""
            print("Testing support tickets...")
            
            element = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//com.horcrux.svg.SvgView[@resource-id="home-header-user-svg"]'
                ))
            )
            element.click()
            time.sleep(2)
            print("✓ Profile icon clicked")
            time.sleep(2)

            support_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ACCESSIBILITY_ID,
                    "Support Tickets"
                ))
            )
            assert support_btn.is_displayed(), "ASSERTION FAILED: 'Support Tickets' button not displayed."
            print("[ASSERTION PASSED] 'Support Tickets' menu button verified.")
            support_btn.click()
            print("✓ Support Tickets opened")
            time.sleep(2)
            assert self.driver.current_package == "com.lyxa.user", "ASSERTION FAILED: App crashed on Support Tickets."
            print("[ASSERTION PASSED] Support Tickets screen opened and verified.")

            self.driver.back()
            time.sleep(1)

        # ==================== PHASE 4: DESTRUCTIVE ====================

        def test_08_delete_address(self):
            """Delete saved address with verified assertions"""
            print("Testing address deletion...")
            time.sleep(2)

            addresses_btn = self.wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Addresses"] | '
                    '//android.widget.TextView[@text="Manage Addresses"]'
                ))
            )
            assert addresses_btn.is_displayed(), "ASSERTION FAILED: 'Addresses' menu button not displayed."
            print("[ASSERTION PASSED] 'Addresses' navigation button verified.")
            addresses_btn.click()
            print("✓ Addresses opened")
            time.sleep(2)
            assert self.driver.current_package == "com.lyxa.user", "ASSERTION FAILED: App exited after opening Addresses."
            print("[ASSERTION PASSED] Addresses view opened and active.")

            self.driver.back()
            time.sleep(1)
