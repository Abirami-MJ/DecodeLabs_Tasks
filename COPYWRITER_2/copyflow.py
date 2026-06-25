# ============================================================
#  copyflow.py — CopyFlow Main Program
#  Entry point of the application. Handles user interaction,
#  menu display, and coordinates all modules together.
# ============================================================

from config    import PLATFORMS, TONES, APP_NAME, APP_VERSION, APP_TAGLINE
from generator import generate_copy, generate_all_platforms

# ── BANNER ───────────────────────────────────────────────────
def show_banner():
    print("\n" + "═" * 54)
    print(f"   ✦  {APP_NAME} v{APP_VERSION}")
    print(f"   {APP_TAGLINE}")
    print("═" * 54)

# ── NUMBERED MENU ────────────────────────────────────────────
def show_menu(title, options):
    """
    Displays a numbered menu and returns the user's choice.

    Args:
        title   (str)  : Menu heading
        options (list) : List of options to display

    Returns:
        str: The selected option
    """
    print(f"\n  ── {title} ──")
    for i, option in enumerate(options, 1):
        print(f"    {i}. {option}")

    while True:
        try:
            choice = int(input(f"\n  Enter number (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"  ⚠️  Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.")

# ── DISPLAY RESULTS ──────────────────────────────────────────
def display_result(platform, copy):
    """
    Displays generated copy in a clean formatted box.

    Args:
        platform (str) : Platform name
        copy     (str) : Generated marketing copy
    """
    print("\n" + "═" * 54)
    print(f"  ✦ {platform} Copy")
    print("═" * 54)
    print(f"\n{copy}\n")
    print("═" * 54)

# ── GENERATION MODE MENU ─────────────────────────────────────
def select_mode():
    """
    Asks user whether to generate for one platform or all.

    Returns:
        str: 'single' or 'all'
    """
    print("\n  ── Generation Mode ──")
    print("    1. Single Platform")
    print("    2. All Platforms (LinkedIn + Instagram + Email)")

    while True:
        try:
            choice = int(input("\n  Enter number (1-2): "))
            if choice == 1:
                return "single"
            elif choice == 2:
                return "all"
            else:
                print("  ⚠️  Please enter 1 or 2")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.")

# ── MAIN PROGRAM ─────────────────────────────────────────────
def main():
    show_banner()

    while True:
        # ── STEP 1: Product Details ───────────────────────
        print("\n  ── Product Details ──")
        product_name = input("  Product Name  : ").strip()
        description  = input("  Description   : ").strip()

        # Basic validation
        if not product_name or not description:
            print("\n  ⚠️  Product name and description cannot be empty.")
            continue

        # ── STEP 2: Select Tone ───────────────────────────
        tone = show_menu("Select Tone", TONES)

        # ── STEP 3: Select Mode ───────────────────────────
        mode = select_mode()

        # ── STEP 4: Generate ──────────────────────────────
        print(f"\n  ⚙️  Generating copy using {tone} tone...\n")

        if mode == "single":
            platform = show_menu("Select Platform", PLATFORMS)
            copy     = generate_copy(product_name, description, platform, tone)
            display_result(platform, copy)

        elif mode == "all":
            results = generate_all_platforms(
                product_name, description, tone, PLATFORMS
            )
            for platform, copy in results.items():
                display_result(platform, copy)

        # ── STEP 5: Continue or Exit ──────────────────────
        print("\n  ── What's Next? ──")
        print("    1. Generate copy for another product")
        print("    2. Exit CopyFlow")

        while True:
            try:
                next_choice = int(input("\n  Enter number (1-2): "))
                if next_choice == 1:
                    break
                elif next_choice == 2:
                    print("\n  ✦ Thank you for using CopyFlow. Goodbye!\n")
                    print("═" * 54 + "\n")
                    exit()
                else:
                    print("  ⚠️  Please enter 1 or 2")
            except ValueError:
                print("  ⚠️  Invalid input. Please enter a number.")

# ── ENTRY POINT ───────────────────────────────────────────────
if __name__ == "__main__":
    main()