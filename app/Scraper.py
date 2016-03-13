import requests
from app.models import HTML
import lxml.html
import requests
from unidecode import unidecode
from app import db

class Scraper:
    def __init__(self,place=None):
        if type(place) == type(str()):
            place = place.replace(",","").replace(".","").replace("-","")
        if place:
            self.place = place
            self.base_urls = self.map_place(place)
        else:
            #consider getting rid of this
            self.base_urls = [
                "http://newyork.backpage.com/FemaleEscorts/",
                "http://newyork.backpage.com/BodyRubs/",
                "http://newyork.backpage.com/Strippers/",
                "http://newyork.backpage.com/Domination/",
                "http://newyork.backpage.com/TranssexualEscorts/",
                "http://newyork.backpage.com/MaleEscorts/",
                "http://newyork.backpage.com/Datelines/",
                "http://newyork.backpage.com/AdultJobs/"
            ]
            self.place = place

    def update_place(self,place):
        if type(place) == type(str()):
            place = place.replace(",","").replace(".","").replace("-","")
        self.base_urls = self.map_place(place)

    def update_investigation(self,urls):
        self.scraping_ads(links=urls)

    def generate_pages(self,url):
        urls = []
        endings = [
            "FemaleEscorts/",
            "BodyRubs/",
            "Strippers/",
            "Domination/",
            "TranssexualEscorts/",
            "MaleEscorts/",
            "Datelines/",
            "AdultJobs/"
        ]
        init_urls = []
        for ending in endings:
            init_urls.append(url+ending)
        for i in xrange(1,6):
            for url in init_urls:
                urls.append(url+"?page="+str(i))
        urls = init_urls + urls
        return urls
    
    def map_place(self,place):
        #I believe this is lazy evaluation, otherwise, I'm kinda dumb...
        place = place.lower()
        places = {
            "alabama":self.generate_pages("http://alabama.backpage.com/"),
            "manhattan":self.generate_pages("http://manhattan.backpage.com/"),
            "new york":self.generate_pages("http://newyork.backpage.com/"),
            "new york city":self.generate_pages("http://manhattan.backpage.com/")+self.generate_pages("http://statenisland.backpage.com/")+self.generate_pages("http://queens.backpage.com/")+self.generate_pages("http://brooklyn.backpage.com/")+self.generate_pages("http://bronx.backpage.com/"),
            "buffalo":self.generate_pages("http://buffalo.backpage.com/"),
            "albany new york":self.generate_pages("http://albany.backpage.com/"),
            "binghamton":self.generate_pages("http://binghamton.backpage.com/"),
            "catskills":self.generate_pages("http://catskills.backpage.com/"),
            "chautauqua":self.generate_pages("http://chautauqua.backpage.com/"),
            "elmira":self.generate_pages("http://elmira.backpage.com/"),
            "fairfield":self.generate_pages("http://fairfield.backpage.com/"),
            "fingerlakes":self.generate_pages("http://fingerlakes.backpage.com/"),
            "glens falls":self.generate_pages("http://glensfalls.backpage.com/"),
            "hudson valley":self.generate_pages("http://hudsonvalley.backpage.com/"),
            "ithaca":self.generate_pages("http://ithaca.backpage.com/"),
            "long island":self.generate_pages("http://longisland.backpage.com/"),
            "oneonta":self.generate_pages("http://oneonta.backpage.com/"),
            "plattsburgh":self.generate_pages("http://plattsburgh.backpage.com/"),
            "potsdam":self.generate_pages("http://plattsburgh.backpage.com/"),
            "rochester":self.generate_pages("http://plattsburgh.backpage.com/"),
            "syracuse":self.generate_pages("http://plattsburgh.backpage.com/"),
            "twintiers":self.generate_pages("http://twintiers.backpage.com/"),
            "utica":self.generate_pages("http://utica.backpage.com/"),
            "watertown":self.generate_pages("http://watertown.backpage.com/"),
            "westchester":self.generate_pages("http://watertown.backpage.com/")
        }
        return places[place]
        
    def scraping_ads(self,links):
        responses = []
        for link in links:
            r = requests.get(link)
            responses.append(r)
        return responses
    
    def scraping_links(self,links):
        responses = []
        for link in links:
            r = requests.get(link)
            text = unidecode(r.text)
            html = lxml.html.fromstring(text)
            ads = html.xpath("//div[contains(@class,'cat')]/a/@href")
            for ad in ads:
                try:
                    responses.append(requests.get(ad))
                except requests.exceptions.ConnectionError:
                    print "hitting connection error"
                    continue
        return responses

    def scrape(self,links=[]):
        data = []
        responses = self.scraping_links(links)
        for response in responses:
            tmp = {}
            tmp["text"] = response.text
            tmp["html"] = lxml.html.fromstring(response.text)
            data.append(tmp)
            print "saving",response.url
            self.save(response.text,response.url)
        return data
    
    def investigate(self,case_number):
        data = self.scrape(links=self.base_urls,scraping_ads=True)
        self.investigate(case_number) #this is an infinite loop, which I am okay with.

    def save(self,text,url):
        html = HTML(text,url)
        db.session.add(html)
        db.session.commit()
        
if __name__ == '__main__':
    scraper = Scraper(place="New York City")
    print scraper.scrape(links=["http://newyork.backpage.com/FemaleEscorts/"])
