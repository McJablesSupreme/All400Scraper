from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def getJobs(driver):
    i = 0
    j = 0
    jobs = {}

    # Just using the first page for now, but will eventually loop through all pages
    pages = [
        'https://www.all400s.com/every01.html'
    ]

    for page in pages:
        # Open company list
        driver.get(page)

        # Collect all href links with data-link-type='website'
        company_links = []
        link_elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-link-type="website"]')
        for href in link_elements:
            link = href.get_attribute('href')
            if link:
                company_links.append(link)
                i += 1

        print(f"Collected {len(company_links)} company links.")

        # Visit each company link and navigate to careers page
        for link in company_links:
            driver.get(link)
            time.sleep(2)  # Wait for the page to load

            # Try to find and click on the 'Careers' link
            try:
                careers_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Careers')
                careers_link.click()
                print(f"Visited careers page for {link}")
                j += 1
                time.sleep(2)  # Wait for the careers page to load
                
                # TODO: Scrape the careers page for job listings and store the data in the 'jobs' dictionary

                
            except Exception as e:
                print(f"Could not find careers page for {link}: {e}")

        print(f"Visited {j} careers pages out of {i} links scraped.") 

# Main 
driver_path = 'chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the WebDriver service
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Get jobs
getJobs(driver)

# Close the driver
driver.quit()
