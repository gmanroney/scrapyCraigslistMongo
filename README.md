This code written in python uses scrapy to read section of craigslist site and store results in a mongo database

This code is an amalgamation of code and concepts described in a number of webpages

- Extracting items with pagination using scrapy
http://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/

https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

- Storing results of scrap in Mongo
https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/

This code uses craigslist as the source and ammends records to the MongoDB collection each time it is run; in later versions the record will be checked to avoid occurence of duplicate records in the database

The code needs python to run; the specific requirements can be found in the file settings.txt

The code also needs the latest version of scrapy (1.4.0) and mongo (3.4.7) installed; for this implementation no username or password should be set in mongo. Again, something for improvement in the future

Once the above pre-requisites are met the scraper can be run using the command: scrapy crawl jobsIE
