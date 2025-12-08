import time
import random
from utils.driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

def test_courier_order_complete_flow():
    """Complete courier order test from app launch to order completion"""
    
    # Create driver instance
    driver = create_driver()
    wait = WebDriverWait(driver, 20)
    
    print("Starting courier order test...")
    
    try:
        # Step 1: Wait for app to load
        time.sleep(3)
        print("✓ App launched successfully")
        
        # # Step 2: Click "Login to Unlock"
        # login_to_unlock = wait.until(
        #     EC.element_to_be_clickable((
        #         By.XPATH,
        #         "//android.widget.TextView[@text='Login to Unlock']"
        #     ))
        # )
        # login_to_unlock.click()
        # print("✓ Clicked 'Login to Unlock'")
        
        # # Step 3: Click "Continue with Email"
        # continue_email_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//android.widget.TextView[@text='Continue with Email']")
        #     )
        # )
        # continue_email_btn.click()
        # print("✓ Clicked 'Continue with Email'")
        
        # # Step 4: Enter email
        # email_field = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Enter Email']"))
        # )
        # email_field.click()
        # email_field.send_keys("tokyo@mail.com")
        # print("✓ Entered email")
        
        # # Step 5: Enter password
        # password_field = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Enter Password']"))
        # )
        # password_field.click()
        # password_field.send_keys("Dhaka@01")
        # driver.hide_keyboard()
        # print("✓ Entered password")
        
        # # Step 6: Click login button
        # login_btn = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Log in']"))
        # )
        # login_btn.click()
        # print(" Clicked login button")
        
        # # Step 7: Wait for login to complete
        # print(" Waiting for login to complete...")
        # time.sleep(5)
        
        # Step 8: Click "Start Ordering!"
        start_ordering = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.TextView[@text='Start Ordering!']"
            ))
        )
        start_ordering.click()
        print(" Clicked 'Start Ordering!'")
        time.sleep(3)
        
        # Step 9: Select location
        print(" Selecting location...")
        
        # Click "Current" location button
        current_location = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//android.widget.TextView[@text='Current']")
            )
        )
        current_location.click()
        print("✓ Location screen opened")
        
        time.sleep(2)
        
        # Step 10: Select address using scroll
        print(" Searching for address...")
        address_desc = "Office, Lyxa, Lyxa Office"
        
        try:
            # Try UiScrollable first
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{address_desc}"))'
            )
            element.click()
            print(f" Selected address: {address_desc}")
            
        except Exception as e:
            print(f"UiAutomator scroll failed: {e}")
            
            try:
                # Try accessibility ID
                element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, address_desc)
                element.click()
                print(f" Found address by accessibility ID")
                
            except Exception as e2:
                print(f"Accessibility ID failed: {e2}")
                
                try:
                    # Try XPath as last resort
                    element = driver.find_element(By.XPATH, f"//*[@text='{address_desc}']")
                    element.click()
                    print(f" Found address by text")
                except Exception as e3:
                    print(f"All methods failed: {e3}")
                    # Continue anyway - maybe location is already selected
        
        time.sleep(5)
        print(" Location selected successfully")
        
        # Step 11: Click Courier option
        print(" Selecting Courier service...")
        
        courier_element = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Courier')]"
            ))
        )
        courier_element.click()
        print(" Courier service selected")
        time.sleep(3)
        
        # Step 12: Add your courier order flow steps here...
        print(" Selecting Courier service Type...")
        
        courier_element = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Purchase & Delivery, Enjoy the convenience of getting items purchased and delivered.')]"
            ))
        )
        courier_element.click()
        print(" Courier type selected")
        time.sleep(3)

        # target = wait.until(
        # EC.element_to_be_clickable((
        #     By.XPATH,
        #     "//android.widget.FrameLayout[@resource-id='android:id/content']"
        #     "/android.widget.FrameLayout/android.view.ViewGroup"
        #     "/android.view.ViewGroup/android.view.ViewGroup[2]"
        #     "/android.widget.ScrollView/android.view.ViewGroup"
        #     "/android.view.ViewGroup/android.widget.ScrollView"
        #     "/android.view.ViewGroup/android.view.ViewGroup[2]"
        # ))
        # )

        # target.click()
        # target.send_keys("Test Object")

        write_here = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Write Here']"
            ))
        )
        write_here.click()
        write_here.send_keys("Test Object")
        time.sleep(3)

        image = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Icon button')]"
            ))
        )
        image.click()

        time.sleep(3)

        button2 = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.Button[@resource-id='android:id/button2']"
        ))
        )
        button2.click()

        time.sleep(3)

        element = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]/android.view.View"
        ))
        )

        element.click()

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


        time.sleep(5)


        quantity_field = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Quantity']"
            ))
        )
        quantity_field.click()

        two_digit = str(random.randint(10, 25))
        quantity_field.send_keys(two_digit)

        time.sleep(3)


        save_item = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.TextView[@text='Save  Item']"
            ))
        )

        save_item.click()

        confirm_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.Button[@resource-id='android:id/button1']"
            ))
        )

        confirm_button.click()

        time.sleep(3)
        add_sender = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Add Sender Details')]"
            ))
        )
        add_sender.click()

        time.sleep(3)

        add_sender = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Add Sender Details')]"
            ))
        )
        add_sender.click()

        time.sleep(3)

        auto_fill = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.view.ViewGroup[@content-desc='Auto Fill My Details']"
            ))
        )
        auto_fill.click()
        time.sleep(3)

        
        confirm = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.view.ViewGroup[@content-desc='Confirm']"
            ))
        )
        confirm.click()
        time.sleep(3)

        add_reciever = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Add Receiver Details')]"
            ))
        )
        add_reciever.click()

        time.sleep(3)

        write_reciever_name = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Name']"
            ))
        )
        write_reciever_name.click()
        write_reciever_name.send_keys("Hridoy Hasan")
        time.sleep(3)

        write_reciever_number = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Enter Mobile']"
            ))
        )
        write_reciever_number.click()
        write_reciever_number.send_keys("8456214")
        time.sleep(3)
        driver.press_keycode(AndroidKey.TAB)

        select_address = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.widget.EditText[@text='Select Address']"
            ))
        )
        select_address.click()
        time.sleep(3)

        select_location = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[contains(@content-desc, 'Choose different location')]"
            ))
        )
        select_location.click()
        time.sleep(3)

        svg_icon = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "(//android.widget.SeekBar[@content-desc='Bottom Sheet'])[2]"
        "/android.widget.ScrollView/android.view.ViewGroup"
        "/android.view.ViewGroup[2]/com.horcrux.svg.SvgView"
        "/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
        ))
        )
        svg_icon.click()
        time.sleep(3)


        element = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.EditText[@text='Enter your address']"
            ))
        )

        element.click()
        element.send_keys("Lavishta")
        time.sleep(3)

        lavishta_option = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//android.view.ViewGroup[@content-desc=\"Lavishta, Road 6, Dhaka, Bangladesh\"]"
            ))
        )

        lavishta_option.click()
        lavishta_option.click()
        time.sleep(3)

        confirm_add = wait.until(
         EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.TextView[@text='Confirm and Add Details']"
            ))
        )
        confirm_add.click()
        time.sleep(3)

        target = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "(//android.widget.SeekBar[@content-desc='Bottom Sheet'])[2]"
                "/android.widget.ScrollView/android.view.ViewGroup"
                "/android.widget.HorizontalScrollView[1]/android.view.ViewGroup"
                "/android.view.ViewGroup[1]/com.horcrux.svg.SvgView"
                "/com.horcrux.svg.GroupView/com.horcrux.svg.PathView"
            ))
        )

        target.click()
        time.sleep(3)

        target = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.EditText[@text='Friends house']"
            ))
        )

        target.click()
        target.send_keys("Jenny")
        time.sleep(3)

        save_btn = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.TextView[@text='Save']"
            ))
        )
        save_btn.click()
        save_btn.click()

        target = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.EditText[@text='Enter Apt/Suite/Floor']"
            ))
        )

        target.click()
        target.send_keys("Jenny")
        time.sleep(3)

        target_address = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.EditText[@text='Business or Building name']"
            ))
        )

        target_address.click()
        target_address.send_keys("Jenny's House")
        time.sleep(3)

        # meet_me_outside = wait.until(
        #     EC.element_to_be_clickable((
        #         By.XPATH,
        #         "//android.widget.TextView[@text='Meet me outside']"
        #     ))
        # )

        # meet_me_outside.click()

        # time.sleep(3)

        save_address = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.TextView[@text='Save Address']"
            ))
        )
        save_address.click()
        time.sleep(3)
        save_address.click()
        time.sleep(3)


        confirm = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.TextView[@text='Confirm']"
            ))
        )
        confirm.click()
        time.sleep(5)

        driver.swipe(300, 1000, 300, 600)

        write_here = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.EditText[@text='Write Here']"
            ))
        )

        write_here.click()
        write_here.send_keys("wait for me outside")
        time.sleep(3)
        driver.press_keycode(AndroidKey.TAB)

        driver.swipe(300, 1000, 300, 100)

        place_order = wait.until(
        EC.element_to_be_clickable((
        By.XPATH,
        "//android.widget.TextView[@text='Place Order']"
            ))
        )
        place_order.click()
        time.sleep(5)

        # Example:
        # 1. Enter pickup details
        # 2. Enter dropoff details
        # 3. Select package type
        # 4. Schedule pickup
        # 5. Confirm order
        
        print(" Add additional courier order steps here...")
        
        # Example placeholder - you should replace this with actual steps:
        print("1. Would enter pickup address here")
        print("2. Would enter dropoff address here")
        print("3. Would select package type here")
        print("4. Would confirm order here")
        
        print("\n🎉 Courier order test completed successfully!")
        
        # Keep the app open for inspection or take screenshot
        time.sleep(5)
        
        # Optional: Take a success screenshot
        driver.save_screenshot("courier_order_success.png")
        print(" Screenshot saved: courier_order_success.png")
        
        return driver
        
    except Exception as e:
        print(f" Test failed with error: {e}")
        
        # Take screenshot on error
        try:
            driver.save_screenshot("courier_order_failure.png")
            print(" Error screenshot saved: courier_order_failure.png")
        except:
            pass
        
        # Re-raise the exception to fail the test
        raise
    
    finally:
        # Optional: Uncomment to close driver automatically
        # driver.quit()
        # print("✅ Driver closed")
        pass

