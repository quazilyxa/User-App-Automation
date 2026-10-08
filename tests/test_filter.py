import time
import random
from utils import driver
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestFilterAutomation:
    """Test suite for filter automation"""

    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        """Setup driver once for all tests"""
        cls.driver = create_driver()
        cls.wait = WebDriverWait(cls.driver, 20)

        print("✓ App launched")
        time.sleep(3)
        
        
        cls.wait.until(
        EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Filter")
            )
        )

        print("✓ Initial screen loaded")
        
        

    def test_user_automation_flow(self):
        print("🚀 Starting user automation flow...")

        driver = self.driver
        wait = self.wait

        try:
            # # ============================================================
            # # 1. Open Filter
            # # ============================================================
            

            
            
            

            filter_btn = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Filter")
                )
            )
            assert filter_btn.is_displayed(), "ASSERTION FAILED: 'Filter' button is not displayed on home screen."
            print("[ASSERTION PASSED] 'Filter' button verified and visible.")

            filter_btn.click()
            print("✓ Filter button clicked")
            time.sleep(2)

            # ============================================================
            # 2. Select Offers
            # ============================================================

            offers_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Offers"]'
                    )
                )
            )
            assert offers_btn.is_displayed(), "ASSERTION FAILED: 'Offers' filter section is not displayed."
            print("[ASSERTION PASSED] 'Offers' filter section verified.")

            offers_btn.click()
            print("✓ Clicked Offers")
            time.sleep(2)

            # ============================================================
            # 3. Select Buy 1 Get 1
            # ============================================================

            buy_one_get_one_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Buy 1 Get 1"]'
                    )
                )
            )

            buy_one_get_one_btn.click()
            print("✓ Clicked Buy 1 Get 1")
            time.sleep(2)

            # ============================================================
            # 4. Apply Offer Filter
            # ============================================================

            apply_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            time.sleep(2)

            # ============================================================
            # 5. Go Back
            # ============================================================

            driver.back()
            print("✓ Navigated back")
            time.sleep(1)

            # ============================================================
            # 6. Open Filter Again
            # ============================================================

            filter_btn = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Filter")
                )
            )

            filter_btn.click()
            print("✓ Filter button clicked again")
            time.sleep(2)

            # ============================================================
            # 7. Open Max Delivery Fee
            # ============================================================

            max_delivery_fee_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Max Delivery Fee"]'
                    )
                )
            )

            max_delivery_fee_btn.click()
            print("✓ Clicked Max Delivery Fee")
            time.sleep(1)

            # ============================================================
            # 8. Locate Left Slider Pointer
            # ============================================================

            left_pointer = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.ScrollView/'
                        'android.view.ViewGroup/'
                        'android.view.ViewGroup[5]/'
                        'android.view.ViewGroup/'
                        'android.view.ViewGroup[1]'
                    )
                )
            )

            print("✓ Left slider pointer found")

            # ============================================================
            # 9. Drag Left Pointer to Middle
            #
            # Slider bounds:
            # [122,722][969,733]
            #
            # Middle X:
            # (122 + 969) / 2 = 545
            #
            # Y:
            # 727
            # ============================================================

            start_x = 122
            start_y = 727

            end_x = 545
            end_y = 727

            print(
                f"Dragging slider from "
                f"({start_x}, {start_y}) "
                f"to "
                f"({end_x}, {end_y})"
            )

            finger = PointerInput("touch", "finger")

            actions = ActionBuilder(
                driver,
                mouse=finger
            )

            # Move to left pointer
            actions.pointer_action.move_to_location(
                start_x,
                start_y
            )

            # Press finger down
            actions.pointer_action.pointer_down()

            # Drag horizontally to middle
            actions.pointer_action.move_to_location(
                end_x,
                end_y,
            )

            # Release finger
            actions.pointer_action.pointer_up()

            # Execute gesture
            actions.perform()

            print("✓ Dragged Max Delivery Fee slider to middle")
            time.sleep(2)

            # ============================================================
            # 10. Apply Max Delivery Fee Filter
            # ============================================================

            apply_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            time.sleep(2)

          

            driver.back()
            print("✓ Navigated back")
            time.sleep(1)

            # ============================================================
            # 8. Open Cuisines Filter
            # ============================================================

            filter_btn = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Filter")
                )
            )

            filter_btn.click()
            print("✓ Filter button clicked")
            time.sleep(2)

            dessert_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Dessert"]'
                    )
                )
            )

            dessert_btn.click()
            print("✓ Clicked Dessert")

            apply_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            time.sleep(2)

            driver.back()
            print("✓ Navigated back")
            time.sleep(1)

            filter_btn = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Filter")
                )
            )

            filter_btn.click()
            print("✓ Filter button clicked")
            time.sleep(2)

            falafel_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Falafel"]'
                    )
                )
            )

            falafel_btn.click()
            print("✓ Clicked Falafel")

            apply_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            time.sleep(2)

            driver.back()
            print("✓ Navigated back")
            time.sleep(1)

            filter_btn = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Filter")
                )
            )

            filter_btn.click()
            print("✓ Filter button clicked")
            time.sleep(2)

            cuisines_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Cuisines"]'
                    )
                )
            )

            cuisines_btn.click()
            print("✓ Minimise Cuisines")

            sort_by_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Sort By"]'
                    )
                )
            )

            sort_by_btn.click()
            print("✓ Clicked Sort By")

            price_high_to_low_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Price high to low"]'
                    )
                )
            )

            price_high_to_low_btn.click()
            print("✓ Clicked Price high to low")

            apply_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            time.sleep(3)

            driver.back()
            print("✓ Navigated back")
            time.sleep(2)
            
            
            top_rated_btn = wait.until(
           EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Top Rated"]'
                    )
                )
            )

            top_rated_btn.click()
            print("✓ Clicked Top Rated")
            
            time.sleep(1)
            
             # Dynamic screen dimensions & scrolling logic
            screen_size = driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']

            start_x = int(width * 0.5)
            start_y = int(height * 0.85)  # Start near bottom
            end_x = start_x
            end_y = int(height * 0.15)    # End near top

            scroll_count = 2  # Adjust how many times to swipe

            for i in range(scroll_count):
                driver.swipe(
                    start_x,
                    start_y,
                    end_x,
                    end_y,
                    duration=random.randint(700, 1100)
                )
                # Brief pause between swipes allows content to settle/load
                time.sleep(random.uniform(0.5, 1.2))

            print(f"✓ Scrolled lower ({scroll_count} times)")
            
            back_to_top_btn = wait.until(
            EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Back to top"]'
                    )
                )
            )

            back_to_top_btn.click()
            print("✓ Clicked Back to top")
            
            time.sleep(2)
            
            
            top_rated_btn = wait.until(
           EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Top Rated"]'
                    )
                )
            )

            top_rated_btn.click()
            print("✓ Clear Top Rated Filter")
            
            time.sleep(2)
            
            offers_btn = wait.until(
             EC.element_to_be_clickable(
           (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Offers"]'
                    )
                )
            )

            offers_btn.click()
            print("✓ Clicked Offers")
            
            time.sleep(2)
            
            
                         # Dynamic screen dimensions & scrolling logic
            screen_size = driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']

            start_x = int(width * 0.5)
            start_y = int(height * 0.85)  # Start near bottom
            end_x = start_x
            end_y = int(height * 0.15)    # End near top

            scroll_count = 2  # Adjust how many times to swipe

            for i in range(scroll_count):
                driver.swipe(
                    start_x,
                    start_y,
                    end_x,
                    end_y,
                    duration=random.randint(700, 1100)
                )
                # Brief pause between swipes allows content to settle/load
                time.sleep(random.uniform(0.5, 1.2))

            print(f"✓ Scrolled lower ({scroll_count} times)")
            
            back_to_top_btn = wait.until(
            EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Back to top"]'
                    )
                )
            )

            back_to_top_btn.click()
            print("✓ Clicked Back to top")
            
            time.sleep(2)
            
            
            offers_btn = wait.until(
             EC.element_to_be_clickable(
           (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Offers"]'
                    )
                )
            )

            offers_btn.click()
            print("✓ Clear Offers Filter")
            
            time.sleep(2)
            
            free_delivery_btn = wait.until(
            EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Free Delivery"]'
                    )
                )
            )

            free_delivery_btn.click()
            print("✓ Clicked Free Delivery")
            
            time.sleep(2)
            
            
            # Dynamic screen dimensions & scrolling logic
            screen_size = driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']

            start_x = int(width * 0.5)
            start_y = int(height * 0.85)  # Start near bottom
            end_x = start_x
            end_y = int(height * 0.15)    # End near top

            scroll_count = 2  # Adjust how many times to swipe

            for i in range(scroll_count):
                driver.swipe(
                    start_x,
                    start_y,
                    end_x,
                    end_y,
                    duration=random.randint(700, 1100)
                )
                # Brief pause between swipes allows content to settle/load
                time.sleep(random.uniform(0.5, 1.2))

            print(f"✓ Scrolled lower ({scroll_count} times)")
            
            time.sleep(2)
            
            free_delivery_btn = wait.until(
            EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Free Delivery"]'
                    )
                )
            )

            free_delivery_btn.click()
            print("✓ Clear Free Delivery")
            
            
            
            
            free_delivery_btn = wait.until(
            EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Free Delivery"]'
                    )
                )
            )

            free_delivery_btn.click()
            print("✓ Clicked Free Delivery")

            time.sleep(1)

            # Get Free Delivery element position and size
            location = free_delivery_btn.location
            size = free_delivery_btn.size

            start_x = location["x"] + size["width"] // 2
            start_y = location["y"] + size["height"] // 2

            # Drag 300 pixels to the left
            end_x = start_x - 300
            end_y = start_y

            print(
                f"Dragging Free Delivery from "
                f"({start_x}, {start_y}) to ({end_x}, {end_y})"
            )

            finger = PointerInput("touch", "finger")
            actions = ActionBuilder(driver, mouse=finger)

            actions.pointer_action.move_to_location(
                start_x,
                start_y
            )

            actions.pointer_action.pointer_down()

            actions.pointer_action.pause(0.5)

            actions.pointer_action.move_to_location(
                end_x,
                end_y
            )

            actions.pointer_action.pause(0.5)

            actions.pointer_action.pointer_up()

            actions.perform()

            print("✓ Dragged Free Delivery to the left")
            
            time.sleep(2)
            
            cuisines_btn = wait.until(
            EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Cuisines"]'
                    )
                )
            )

            cuisines_btn.click()
            print("✓ Clicked Cuisines")
            
            time.sleep(2)
            
            
            ice_cream_btn = wait.until(
             EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Ice cream"]'
                    )
                )
            )

            ice_cream_btn.click()
            print("✓ Clicked Ice cream")
            
            time.sleep(2)
            
            apply_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Apply"]'
                    )
                )
            )

            apply_btn.click()
            print("✓ Clicked Apply")
            
            time.sleep(2)
            
            driver.back()
            print("✓ Navigated back")
            
            
            
            free_delivery_btn = wait.until(
            EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Free Delivery"]'
                    )
                )
            )

            free_delivery_btn.click()
            print("✓ Clear Quick Filter")
            
            
            screen_size = driver.get_window_size()

            width = screen_size["width"]
            height = screen_size["height"]

            driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 20,
                    "top": 300,
                    "width": width - 40,
                    "height": height - 600,
                    "direction": "up",
                    "percent": 0.9
                }
            )

            print("✓ Scrolled toward top")

           
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2)
            
            
            jasmine_bloom_btn = wait.until(
            EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '(//android.widget.TextView[@text="Jasmine & Bloom"])[2]'
                    )
                )
            )

            jasmine_bloom_btn.click()
            print("✓ Clicked Jasmine & Bloom")
            
            
            time.sleep(2)
            
            add_to_cart_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="add-to-cart-699d3c28d632b581f7da9583"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            
            time.sleep(2)
            
            view_basket_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="View Basket"]'
                    )
                )
            )

            view_basket_btn.click()
            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            
            checkout_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                    )
                )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)
            
            
            place_order_btn = wait.until(
             EC.element_to_be_clickable(
           (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            time.sleep(2)
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(3)
            
            driver.back()
            print("✓ Navigated back")
            
            
            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2)
            
            pets_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Pets"]'
            )
                )
            )

            pets_btn.click()
            print("✓ Clicked Pets")
            time.sleep(2)
            
            
            pet_heaven_btn = wait.until(
            EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Pet Heaven"]'
                    )
                )
            )

            pet_heaven_btn.click()
            print("✓ Clicked Pet Heaven")
            
            time.sleep(2)
            
            dogs_food_btn = wait.until(
             EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Dog\'s Food"]'
                    )
                )
            )

            dogs_food_btn.click()
            print("✓ Clicked Dog's Food")
            time.sleep(2)
            
            add_to_cart_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.Button[@content-desc="add-to-cart-6a2a89f0b7d9fba171e08aa4"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            
            time.sleep(2)
            
            driver.tap([(820, 2100)])

            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            checkout_btn = wait.until(
             EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                )
            )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)

            
            place_order_btn = wait.until(
             EC.element_to_be_clickable(
           (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            time.sleep(4)
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(3)
            
            
            driver.back()
            print("✓ Navigated back")
            time.sleep(1)
            
            
            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2) 
            
            beauty_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Beauty"]'
                    )
                )
            )

            beauty_btn.click()
            print("✓ Clicked Beauty")
            
            time.sleep(2) 
            urban_grooming_btn = wait.until(
            EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Urban Grooming"]'
                    )
                )
            )

            urban_grooming_btn.click()
            print("✓ Clicked Urban Grooming")
            
            
            time.sleep(2)     
            
            
            beauty_section_btn = wait.until(
              EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="beauty section"]'
                    )
                )
            )

            beauty_section_btn.click()
            print("✓ Clicked beauty section")
            
            time.sleep(2)
            
            add_to_cart_btn = wait.until(
             EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="add-to-cart-6a673b433e5a3eab5fd6f64d"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            
            time.sleep(2)
            
            driver.tap([(820, 2100)])

            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            checkout_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                )
            )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)
            
            
            
            place_order_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            time.sleep(4)
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(3)
            
            
            driver.back()
            print("✓ Navigated back")
            time.sleep(1)
            
            
            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2)
            
            electronics_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Electronics"]'
                    )
                )
            )

            electronics_btn.click()
            print("✓ Clicked Electronics")
            time.sleep(2)
            
            electro_hub_btn = wait.until(
              EC.element_to_be_clickable(
          (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Electro Hub"]'
                    )
                )
            )

            electro_hub_btn.click()
            print("✓ Clicked Electro Hub")
            time.sleep(3)
            
            personal_electronics_btn = wait.until(
           EC.element_to_be_clickable(
              (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Personal Electronics"]'
                    )
                )
            )

            personal_electronics_btn.click()
            print("✓ Clicked Personal Electronics")
            time.sleep(2)
            
            
            add_to_cart_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.Button[@content-desc="add-to-cart-6a6995ddd3884a9a693bb9bb"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            print("✓ Clicked DJI Mini 4K Standard")
            time.sleep(2)
            
            
            driver.tap([(820, 2100)])
            
            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            
            checkout_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                )
            )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)
            
            
            
            place_order_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            time.sleep(4)
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(4)
            
            
            driver.back()
            print("✓ Navigated back")
            time.sleep(1)
            
            
            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2)
            
            # Locate Electronics icon
            electronics_icon = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Electronics"]/android.view.ViewGroup/android.widget.ImageView'
                    )
                )
            )

            print("✓ Electronics icon found")
            
            
            # Get the icon's center position
            location = electronics_icon.location
            size = electronics_icon.size

            start_x = location["x"] + size["width"] // 2
            start_y = location["y"] + size["height"] // 2

            # Drag 300 pixels to the left
            end_x = start_x - 600
            end_y = start_y

            print(
                f"Dragging Electronics icon from "
                f"({start_x}, {start_y}) to ({end_x}, {end_y})"
            )

            finger = PointerInput("touch", "finger")
            actions = ActionBuilder(driver, mouse=finger)

            actions.pointer_action.move_to_location(
                start_x,
                start_y
            )

            actions.pointer_action.pointer_down()

            actions.pointer_action.pause(0.5)

            actions.pointer_action.move_to_location(
                end_x,
                end_y
            )

            actions.pointer_action.pause(0.5)

            actions.pointer_action.pointer_up()

            actions.perform()

            print("✓ Dragged Electronics icon to the left")  
            
            time.sleep(2)
            
            
            
            
            
            
            
            
            coffee_btn = wait.until(
             EC.element_to_be_clickable(
              (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="Coffee"]'
                    )
                )
            )

            coffee_btn.click()
            print("✓ Clicked Coffee")
            
            time.sleep(2)
            
            coffee_prince_btn = wait.until(
            EC.element_to_be_clickable(
              (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Coffee Prince"]'
                    )
                )
            )

            coffee_prince_btn.click()
            print("✓ Clicked Coffee Prince")
            
            time.sleep(2)
            
            add_to_cart_btn = wait.until(
           EC.element_to_be_clickable(
              (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="add-to-cart-6a33958e861fbd5affc72164"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            
            time.sleep(2)
            
            view_basket_btn = wait.until(
            EC.element_to_be_clickable(
           (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="View Basket"]'
                )
            )
            )

            view_basket_btn.click()
            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            checkout_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                )
            )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)
            
            
        #     complete_address_btn = wait.until(
        #         EC.element_to_be_clickable(
        #     (
        #     AppiumBy.XPATH,
        #     '(//android.widget.TextView[@text="Complete Address"])[1]'
        #             )
        #         )
        #     )

        #     complete_address_btn.click()
        #     print("✓ Clicked Complete Address")
        #     time.sleep(2)
            
        #     saved_address = wait.until(
        #         EC.element_to_be_clickable(
        # (
        #                 AppiumBy.XPATH,
        #                 '//android.widget.TextView[@text="Office"]'
        #             )
        #         )
        #     )

        #     saved_address.click()
        #     print("✓ Selected saved address")

        #     print("✓ Clicked Office Address")
            
            place_order_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            time.sleep(4)
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(3)
            
            
            driver.back()
            print("✓ Navigated back")
            time.sleep(1)
            
            
            stores_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Stores"]'
                    )
                )
            )

            stores_btn.click()
            print("✓ Clicked Stores")

            time.sleep(2)
            
            
            electronics_icon = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="Electronics"]/android.view.ViewGroup/android.widget.ImageView'
                    )
                )
            )

            # Get the icon's center position
            location = electronics_icon.location
            size = electronics_icon.size

            start_x = location["x"] + size["width"] // 2
            start_y = location["y"] + size["height"] // 2

            # Drag 600 pixels to the left
            end_x = start_x - 650
            end_y = start_y

            print(
                f"Dragging Electronics icon from "
                f"({start_x}, {start_y}) to ({end_x}, {end_y})"
            )

            finger = PointerInput("touch", "finger")
            actions = ActionBuilder(driver, mouse=finger)

            actions.pointer_action.move_to_location(
                start_x,
                start_y
            )

            actions.pointer_action.pointer_down()

            actions.pointer_action.pause(0.5)

            actions.pointer_action.move_to_location(
                end_x,
                end_y
            )

            actions.pointer_action.pause(0.5)

            actions.pointer_action.pointer_up()

            actions.perform()

            print("✓ Dragged Electronics icon to the left")  
            
            time.sleep(2)
            
            wellness_btn = wait.until(
              EC.element_to_be_clickable(
             (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="Wellness"]'
                    )
                )
            )

            wellness_btn.click()
            print("✓ Clicked Wellness")
            
            time.sleep(2)
            
            vitality_hub_btn = wait.until(
             EC.element_to_be_clickable(
          (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Vitality Hub"]'
                    )
                )
            )

            vitality_hub_btn.click()
            print("✓ Clicked Vitality Hub")
            
            time.sleep(2)
            
            supplement_btn = wait.until(
           EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Supplement"]'
                    )
                )
            )

            supplement_btn.click()
            print("✓ Clicked Supplement")
            
            time.sleep(2)
            
            add_to_cart_btn = wait.until(
            EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="add-to-cart-6a69a180d3884a9a693bba9d"]'
                    )
                )
            )

            add_to_cart_btn.click()
            print("✓ Clicked Add to Cart")
            
            time.sleep(2)
            
            
            driver.tap([(820, 2100)])
                        
            print("✓ Clicked View Basket")
            
            time.sleep(2)
            
            
            checkout_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Checkout"]'
                )
            )
            )

            checkout_btn.click()
            print("✓ Clicked Checkout")
            
            time.sleep(2)
            

            place_order_btn = wait.until(
                EC.element_to_be_clickable(
            (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Place Order"]'
                )
            )
            )

            place_order_btn.click()
            print("✓ Clicked Place Order")
            
            driver.tap([(820, 1900)])
            print("✓ Clicked Looks Good")
            time.sleep(3)
            
            driver.back()
            print("✓ Navigated back")
            time.sleep(3)

            
            
            
            
            
            
            
            
            
            
            
            
            
            

            # # Dynamic screen dimensions & scrolling logic
            # screen_size = driver.get_window_size()
            # width = screen_size['width']
            # height = screen_size['height']

            # start_x = int(width * 0.5)
            # start_y = int(height * 0.85)  # Start near bottom
            # end_x = start_x
            # end_y = int(height * 0.15)    # End near top

            # scroll_count = 3  # Adjust how many times to swipe

            # for i in range(scroll_count):
            #     driver.swipe(
            #         start_x,
            #         start_y,
            #         end_x,
            #         end_y,
            #         duration=random.randint(300, 500)
            #     )
            #     # Brief pause between swipes allows content to settle/load
            #     time.sleep(random.uniform(0.5, 1.2))

            # print(f"✓ Scrolled lower ({scroll_count} times)")

        except Exception as e:
            print(f"❌ User automation flow failed: {e}")
            raise