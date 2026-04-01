from playwright.sync_api import sync_playwright
import json

def web_scrape(url: str):
    data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        data['title'] = page.title()
        
        return data

def main():
    page = str(input('Enter a page URL: '))
    data = web_scrape(page)
    with open('data.json', 'w') as f:
        json.dump(data)

if __name__ == '__main__':
    main()