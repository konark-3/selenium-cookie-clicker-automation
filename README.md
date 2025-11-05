# Cookie Clicker Bot - Selenium Automation

This Python project automates the **Cookie Clicker** game using **Selenium**.  
It clicks the cookie continuously and buys upgrades automatically based on available in-game currency.

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `selenium`, `time`  
- **WebDriver:** ChromeDriver  

---

## Features

- Automatically clicks the main cookie repeatedly.  
- Tracks in-game currency in real-time.  
- Purchases upgrades automatically based on current money and item prices.  
- Handles multiple game upgrades: Cursor, Grandma, Factory, Mine, Shipment, Alchemy Lab, Portal, Time Machine.  

---

## Setup

1. Install dependencies:

pip install selenium

1.  Download and set up [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version.

2.  Update the script if needed with your browser options.

* * * * *

How It Works
------------

1.  Launches **Chrome** and opens the Cookie Clicker game.

2.  Continuously clicks the main cookie.

3.  Fetches prices for all available upgrades.

4.  Determines which upgrade can be purchased based on current money.

5.  Clicks the appropriate upgrade button.

6.  Repeats this process with a short delay (0.01s) to maximize efficiency.

* * * * *

Example Usage
-------------

Run the script:

`python cookie_clicker_bot.py`

Output example:

`Money: 123
Cursor price: 15
Clicked cursor
Grandma price: 100
...`

* * * * *

Notes
-----

-   Ensure ChromeDriver is installed and matches your Chrome version.

-   The script uses `detach=True` to keep the browser open after execution.

-   Adjust `time.sleep()` for performance and CPU usage.

-   Exceptions are caught to prevent script crashes during runtime.

