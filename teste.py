from selenium.webdriver import Remote, ChromeOptions

browser_option = ChromeOptions()

#Selenium Grid
browser_option.page_load_strategy = 'eager'
browser_option.set_capability('browserName','chrome')
browser_option.set_capability('platformName','LINUX')

brw = Remote(
    command_executor='http://localhost:4444',
    options=browser_option
)

brw.get('https://google.com.br')
print(brw.title)
brw.quit()