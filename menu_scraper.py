import sys
import urllib2
import csv
from BeautifulSoup import BeautifulSoup


class MenuScraper():
	
	def __init__(self, dinning_hall_name, meal):
		self.dinning_hall_name = dinning_hall_name
		self.meal = meal
	
	def collect_data(self):
		url = urllib2.Request('http://umassdining.com/locations-menus/'+self.dinning_hall_name+'/menu')
		response = urllib2.urlopen(url)
		file = response.read()
		raw_html = BeautifulSoup(file)
		try:
			meal_html = raw_html.find('div', id = self.meal+'_menu').findAll("li", { "class" : "lightbox-nutrition" })
		except AttributeError:
			print "Could not find menu."
			sys.exit()
		data = {}
		for item in meal_html:
			dish_name = item.a.string
			data[dish_name] = {
				"name": str(dish_name),
				"calories": int(item.a["data-calories"]),
				"protein": str(item.a["data-protein"]),
				"sugars": str(item.a["data-sugars"]),
				"allergens": str(item.a["data-allergens"])
				}		
		return data

	def write_to_file(self):
		data = self.collect_data()
		with open(self.dinning_hall_name+" "+ self.meal +" menu.csv", "w") as toWrite:
			writer = csv.writer(toWrite, delimiter=",")
			writer.writerow(["Name", "Calories", "Protein", "Sugars", "Allergens"])
			for item in data.keys():
				writer.writerow([item, data[item]["calories"],
				data[item]["protein"], data[item]["sugars"], data[item]["allergens"]])


