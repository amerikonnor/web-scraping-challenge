This project is an example of skills using splinter and BeautifulSoup to do web scraping, as well as establishing a connection to a Mongo database to store and retrieve data.

The app.py file creates a Flask app that runs using templates/index.html as a template.

The project scrapes the most recent news story from mars.nasa.gov/news and displays the title and sypnosis paragraph. Next it displays the most recent image from the Perseverance rover program (landing February 18th!, with more pictures coming!) from nasa.gov/perseverance/images. It also displays a table of Mars facts/data from space-facts.com/mars. Finally, it displays four high-res photos of the Martian hemispheres from the USGS Astrogeology website.

Also contained in the repository are the scraper that runs when the 'Scrape New Data' button in the app is clicked, the jupyter notebook used to develop the scraper code, and screenshots of the final app webpage.
