# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd 

def scrape():
    mars_news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit(mars_news_url)
    html = browser.html
    browser.quit()
    more_soup = BeautifulSoup(html, 'html.parser')

    first = more_soup.find('li', class_='slide')

    news_title = first.h3.text

    news_summary = first.find('div', class_='rollover_description_inner').text

    return_this = [
        {"news_title": news_title},
        {'news_summary': news_summary}
    ]

    facts_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(facts_url)
    facts_table = tables[0].to_html()

    return_this.add({"data_table": facts_table})


    hemisphere_image_urls = [
        {'title': 'Cerberus Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},
        {'title': 'Schiaparelli Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},
        {'title': 'Syrtis Major Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},
        {'title': 'Valles Marineris Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}
    ]

    return_this.add(hemisphere_image_urls)

    return return_this


