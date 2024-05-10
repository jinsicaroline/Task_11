from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set up Chrome webdriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Find the draggable element
draggable_element = driver.find_element(By.ID, "draggable")

# Find the droppable element
droppable_element = driver.find_element(By.ID, "droppable")

# Perform the drag and drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Switch back to the default content
driver.switch_to.default_content()

# Close the browser
driver.quit()
