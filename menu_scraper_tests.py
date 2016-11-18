import sys
import urllib2
import csv
from BeautifulSoup import BeautifulSoup
from menu_scraper import MenuScraper

# Berkshire lunch menu
berk_lunch = MenuScraper("berkshire", "lunch")
berk_lunch.write_to_file()

# Hampshire dinner menu
hamp_dinner = MenuScraper("hampshire", "dinner")
hamp_dinner.write_to_file()

# Franklin breakfast menu
frank_breakfast = MenuScraper("franklin", "breakfast")
frank_breakfast.write_to_file() 

# Worcester latenight menu
worcester_latenight = MenuScraper("worcester", "late night")
worcester_latenight.write_to_file()
