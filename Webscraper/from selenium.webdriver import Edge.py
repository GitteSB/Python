from selenium.webdriver import Edge # first we import the webdriver from Selenium
driver = Edge(executable_path="C:\Program Files\msedgedriver.exe") #then we get the apropriot driver from our pc 

driver.get('https://oxylabs.io/blog') #Then we get the website we want to scrape

blog_titles = driver.get_elements_by_css_selector(' h2.blog-card__content-title') #What we want to scrape, here it's titles
for title in blog_titles:
    print(title.text) # We print the content we scraped for
driver.quit() # closing the browser
