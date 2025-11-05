import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

flag = True

while flag:
    try:
        cookie.click()

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        money = int(money)
        print(f"Money: {money}")

        cursor_button = driver.find_element(By.ID, "buyCursor")
        cursor_text = driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text
        cursor_price = int(cursor_text.split()[2].replace(",", ""))
        print(f"Cursor price: {cursor_price}")

        grandma_button = driver.find_element(By.ID, "buyGrandma")
        grandma_text = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text
        grandma_price = int(grandma_text.split()[2].replace(",", ""))
        print(f"Grandma price: {grandma_price}")

        factory_button = driver.find_element(By.ID, "buyFactory")
        factory_text = driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text
        factory_price = int(factory_text.split()[2].replace(",", ""))
        print(f"Factory price: {factory_price}")

        mine_button = driver.find_element(By.ID, "buyMine")
        mine_text = driver.find_element(By.CSS_SELECTOR, "#buyMine b").text
        mine_price_str = mine_text.split()[2].replace(",", "")
        mine_price = int(mine_price_str)
        print(f"Mine price: {mine_price}")

        shipment_button = driver.find_element(By.ID, "buyShipment")
        shipment_text = driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text
        shipment_price_str = shipment_text.split()[2].replace(",", "")
        shipment_price = int(shipment_price_str)
        print(f"Shipment price: {shipment_price}")

        alchemy_lab_button = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy_lab_text = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]').text
        alchemy_lab_price_str = alchemy_lab_text.split()[3].replace(",", "")
        alchemy_lab_price = int(alchemy_lab_price_str)
        print(f"Alchemy lab price: {alchemy_lab_price}")

        portal_button = driver.find_element(By.ID, "buyPortal")
        portal_text = driver.find_element(By.CSS_SELECTOR, '#buyPortal b').text
        portal_price_str = portal_text.split()[2].replace(",", "")
        portal_price = int(portal_price_str)
        print(f"Portal price: {portal_price}")

        time_machine_button = driver.find_element(By.ID, "buyTime machine")
        time_machine_text = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]').text
        time_machine_price_str = time_machine_text.split()[3].replace(",", "")
        time_machine_price = int(time_machine_price_str)
        print(f"Time machine price: {time_machine_price}")

        if cursor_price <= money < grandma_price:
            cursor_button.click()
            print("Clicked cursor")
        elif grandma_price <= money < factory_price:
            grandma_button.click()
            print("Clicked grandma")
        elif factory_price <= money < mine_price:
            factory_button.click()
            print("Clicked factory")
        elif mine_price <= money < shipment_price:
            mine_button.click()
            print("Clicked mine")
        elif shipment_price <= money < alchemy_lab_price:
            shipment_button.click()
            print("Clicked shipment")
        elif alchemy_lab_price <= money < portal_price:
            alchemy_lab_button.click()
            print("Clicked alchemy lab")
        elif portal_price <= money < time_machine_price:
            portal_button.click()
            print("Clicked portal")
        elif money >= time_machine_price:
            time_machine_button.click()
            print("Clicked time machine")
    except Exception as e:
        print(f"Exception: {e}")
        pass

    time.sleep(0.01)
