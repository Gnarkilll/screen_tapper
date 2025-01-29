import pyautogui
import random
import time

def get_mouse_position():
    """
    Displays the current mouse coordinates every 2 seconds until interrupted.
    """
    print("Move the mouse to the desired location. Coordinates will be displayed every 2 seconds.")
    try:
        while True:
            x, y = pyautogui.position()  # Get current mouse coordinates
            print(f"Current coordinates: X={x}, Y={y}")
            time.sleep(2)  # Delay for update
    except KeyboardInterrupt:
        print("Exiting the program.")

def random_move_and_click(region, multi_clicks=False):
    """
    Performs a random movement and click within the specified area.
    :param region: Tuple (x, y, width, height) defining the click area.
    :param multi_clicks: If True, performs multiple clicks at the same point.
    """
    x_start, y_start, width, height = region

    # Generate a random point within the area
    x = random.randint(x_start, x_start + width)
    y = random.randint(y_start, y_start + height)

    # Move the mouse
    move_duration = random.uniform(0.1, 0.5)  # Faster movement
    pyautogui.moveTo(x, y, duration=move_duration)

    if multi_clicks:
        # Perform multiple clicks at the same point
        num_clicks = random.randint(2, 5)  # Number of clicks
        for i in range(num_clicks):
            pyautogui.click()
            print(f"Click #{i + 1} at: ({x}, {y})")
            time.sleep(random.uniform(0.05, 0.2))  # Minimal delay between clicks
    else:
        # Single click
        pyautogui.click()
        print(f"Click performed at: ({x}, {y})")

    # Reduced delay after action
    post_click_delay = random.uniform(0.1, 0.3)
    time.sleep(post_click_delay)


def random_scroll_chance():
    """
    Occasionally performs a random scroll up or down.
    """
    if random.random() < 0.1:  # 10% chance of scrolling
        scroll_amount = random.randint(-100, 100)  # Smaller scroll range
        pyautogui.scroll(scroll_amount)
        print(f"Scrolled by {scroll_amount} pixels")


def main():
    region = (383, 423, 937, 636)  # Click area
    num_clicks = 500  # Increased number of clicks per run

    print(f"Starting. Scheduled {num_clicks} clicks.")
    for i in range(num_clicks):
        print(f"Cycle {i + 1}/{num_clicks}")

        # Perform random movement and click
        multi_click_chance = random.random() < 0.3  # 30% chance for multiple clicks
        random_move_and_click(region, multi_clicks=multi_click_chance)

        # Possible scrolling
        random_scroll_chance()

        # Minimal delay between cycles
        delay = random.uniform(0.1, 0.5)  # Shortened pause
        print(f"Delay: {delay:.2f} seconds")
        time.sleep(delay)

    print("Automation complete.")


if __name__ == "__main__":
    main()
