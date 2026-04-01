# from playwright.sync_api import sync_playwright
import json
import requests

# def web_scrape(url: str):
#     data = {}
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto(url)
        
#         data['title'] = page.title()
        
#         return data

# data = web_scrape('https://pokemondb.net/pokedex/bulbasaur')
data = requests.get('https://philoapi.vercel.app/search?keyword=diogenes').json()
with open('test/data.json', 'w') as f:
    json.dump(data, f)