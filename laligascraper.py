import requests
from bs4 import BeautifulSoup

standings_url = "https://fbref.com/en/comps/12/La-Liga-Stats"
url_data = requests.get(standings_url)
soup = BeautifulSoup(url_data.text)
standings_table = soup.select('table.stats_table')[0]
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if "/squads/" in l]

team_urls = [f"httos://fbref.com{l}" for l in links]
