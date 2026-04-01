from playwright.sync_api import sync_playwright
from fastapi import FastAPI

app = FastAPI(
    title='Test API',
    summary='Pneumoultramicroscopicsilicovulcanoconiosis',
    description='Testing a hosted API on github!'
)

@app.get('/')
def home():
    return {'Message': 'The API is working!'}

def web_scrape(url: str):
    data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        data['title'] = page.title()
        
        return data
        
@app.get('/q')
def search(page: str):
    data = web_scrape(page)
    return data