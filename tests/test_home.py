import sys
import time
import pytest

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


@pytest.mark.usefixtures("driver")
class TestUserAutomation:
    """Production-grade user automation test suite using Page Object Model"""

    def test_user_automation_flow(self, home_page, booking_page, profile_page):
        """
        End-to-end user automation test covering:
        1. Search & store discovery (with assertion)
        2. Store sub-items exploration
        3. Stores tab verification
        4. Top Rated toggle & Filter flow (with assertion)
        5. Cleaning Services booking & confirmation (with assertion)
        6. Profile subpages & nested tab navigation (with assertion)
        7. Logout & session termination (with assertion)
        """
        print("\n[START] Starting Page Object Model user automation flow...")

        # ── Step 0: Ensure starting on Home screen ────────────────────────
        home_page.ensure_home_screen()
        assert home_page.is_home_displayed(), (
            "ASSERTION FAILED: Home screen is not visible or search bar could not be found."
        )
        print("[ASSERTION PASSED] Home screen is active and verified.")

        # ── Step 1: Search & Select Store ─────────────────────────────────
        print("\n[STEP 1] Search interaction & store discovery...")
        store_selected = home_page.search_and_select_store("Test Shop")
        assert store_selected, (
            "ASSERTION FAILED: 'Test Shop' was not found or store card could not be clicked."
        )
        print("[ASSERTION PASSED] Store 'Test Shop' was found and opened successfully.")

        # ── Step 2: Explore Store Items ───────────────────────────────────
        print("\n[STEP 2] Exploring inside store...")
        home_page.explore_store_items()

        # ── Step 3: Stores Tab ────────────────────────────────────────────
        print("\n[STEP 3] Testing Stores tab...")
        home_page.test_stores_tab()

        # ── Step 4: Top Rated & Filter Flow ───────────────────────────────
        print("\n[STEP 4] Testing Top Rated toggle & Filters...")
        home_page.toggle_top_rated()
        home_page.open_filter_modal()
        assert home_page.is_filter_modal_open(), (
            "ASSERTION FAILED: Filter modal failed to open when clicking the Filter button."
        )
        print("[ASSERTION PASSED] Filter modal opened successfully.")

        home_page.select_discounts_and_apply()
        home_page.reopen_filter_and_reset()

        # ── Step 5: Cleaning Services & Booking Flow ──────────────────────
        print("\n[STEP 5] Cleaning Services & Booking flow...")
        home_page.open_cleaning_services()
        booking_page.select_deep_cleaning_service()
        booking_page.select_available_time_slot()
        booking_page.checkout_and_confirm()

        booking_confirmed = booking_page.is_booking_confirmed()
        assert booking_confirmed, (
            "ASSERTION FAILED: Booking confirmation 'Looks good' was not displayed or failed to click."
        )
        print("[ASSERTION PASSED] Cleaning service booking confirmed successfully with 'Looks good' modal.")

        home_page.ensure_home_screen()

        # ── Step 6: Profile & Account Navigation ──────────────────────────
        print("\n[STEP 6] Testing Profile menu and subpages...")
        home_page.open_profile()
        assert profile_page.is_on_profile_menu(), (
            "ASSERTION FAILED: Failed to open or detect the Profile menu."
        )
        print("[ASSERTION PASSED] Profile menu is active and verified.")

        profile_page.test_favorites()
        profile_page.test_bookings()
        profile_page.test_orders()
        profile_page.test_lyxa_pay()
        profile_page.test_coupons()
        profile_page.test_get_support()
        profile_page.test_manage_cards()
        profile_page.test_support_tickets()
        profile_page.test_faq()
        profile_page.test_invite_friends()

        # ── Step 7: Logout & Session Verification ─────────────────────────
        profile_page.logout()
        home_page.ensure_home_screen()
        assert home_page.is_logged_out(), (
            "ASSERTION FAILED: User account was not successfully logged out (login prompt missing)."
        )
        print("[ASSERTION PASSED] User successfully logged out; login banner is displayed.")

        print("\n[SUCCESS] Entire Page Object Model automation suite passed with 5 verified assertions!")