from selenium.webdriver import Edge
driver =Edge(https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

driver.get('https://oxylabs.io/blog')

blog_title = driver.get_elements_by_css_selector(' h2.blog-card__content-title')
for title in blog_title:
    print(title.text)
 driver.quit()# closing the browser

