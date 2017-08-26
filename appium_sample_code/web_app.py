from appium import webdriver

# python
# setup the web driver and launch the webview app.
capabilities = { 
                'browserName': 'Chrome', 
                'platformName': 'Android',
                'deviceName': 'H6D5T15606000272'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)



# Navigate to the page and interact with the elements on the guinea-pig page using id.
driver.get('http://saucelabs.com/test/guinea-pig')
div = driver.find_element_by_id('i_am_an_id')
# check the text retrieved matches expected value
assert 'I am a div' == div.text

# populate the comments field by id
driver.find_element_by_id('comments').send_keys('My comment')

# close the driver
#driver.quit()