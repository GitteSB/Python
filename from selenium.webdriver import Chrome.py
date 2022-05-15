from selenium.webdriver import Chrome
from selenium.webdriver import Edge

driver = Chrome(executable_path='/path/to/driver')
driver.get('https://oxylabs.io/blog')
driver = Edge(executable_path='/path/to/driver' )
driver.get('https://job.jobnet.dk/CV/FindWork?SearchString=datamatiker&Offset=0&SortValue=BestMatch')


blog_titles = driver.get_elements_by_css_selector(' h2.blog-card__content-title')
for title in blog_titles:
    print(title.text)
driver.quit() # closing the browser