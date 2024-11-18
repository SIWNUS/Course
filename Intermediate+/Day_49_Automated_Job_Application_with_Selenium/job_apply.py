from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Function to log in to LinkedIn
def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    # Find the email and password input fields
    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    # Enter credentials
    email_field.send_keys(username)
    password_field.send_keys(password)
    
    # Submit the login form
    password_field.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "global-nav")))

# Function to apply to a job with "Easy Apply"
def apply_to_job(driver, job_url):
    driver.get(job_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Easy Apply")]')))
    
    try:
        # Wait for the "Easy Apply" button to be clickable and click it
        easy_apply_button = driver.find_element(By.XPATH, '//button[contains(text(), "Easy Apply")]')
        easy_apply_button.click()
        time.sleep(2)
        
        # Handle the "Next" button and proceed with filling any required fields
        while True:
            try:
                # Click "Next" buttons
                next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
                next_button.click()
                time.sleep(2)
            except:
                break
        
        # Look for "Submit application" button and click it to submit
        submit_button = driver.find_element(By.XPATH, '//button[@aria-label="Submit application"]')
        submit_button.click()
        print("Applied to job:", job_url)
    except Exception as e:
        print(f"Error applying to {job_url}: {e}")

# Function to search for jobs and apply to all available positions
def search_and_apply(driver, search_query, username, password):
    # Log in to LinkedIn
    login_to_linkedin(driver, username, password)
    
    # Navigate to LinkedIn Jobs
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(5)
    all_search = driver.find_element(By.ID, "global-nav-search")
    search_job = all_search.find_element(By.CLASS_NAME, "jobs-search-box__keyboard-text-input")
    search_job.send_keys(search_query)
    job_location = all_search.find_element(By.CLASS_NAME, "jobs-search-box__text-input--with-clear")
    job_location.send_keys("Chennai, Tamil Nadu, India", Keys.ENTER)

    time.sleep(2)

    # Loop to navigate through multiple pages of job listings
    page_number = 1
    while True:
        print(f"Processing page {page_number}...")
        # Wait for job listings to load
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="jobs-search-results__list list-style-none"]/li')))
        
        # Get all job listings on the current page
        job_cards = driver.find_elements(By.XPATH, '//ul[@class="jobs-search-results__list list-style-none"]/li')

        # Loop through each job card and apply if "Easy Apply" button is available
        for job in job_cards:
            try:
                job_link = job.find_element(By.XPATH, './/a[@class="result-card__full-card-link"]')
                job_url = job_link.get_attribute("href")
                
                # Check if "Easy Apply" button exists for this job
                easy_apply_button = job.find_element(By.XPATH, './/button[contains(text(), "Easy Apply")]')
                if easy_apply_button.is_displayed():
                    print(f"Applying to job: {job_url}")
                    apply_to_job(driver, job_url)
            except Exception as e:
                print(f"Could not apply to job: {e}")
        
        # Check for the "Next" button to go to the next page
        try:
            next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
            next_button.click()
            page_number += 1
            time.sleep(3)
        except:
            print("No more pages found.")
            break

# Main function to run the automation
def main():
    # Your LinkedIn login credentials
    linkedin_username = "udemy3296@gmail.com"
    linkedin_password = "Su$i0410"
    
    # Set up the browser and WebDriver
    options = Options()
    options.binary_location = os.getenv("FIREFOX_EXEC_PATH")
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(service=Service(executable_path=os.getenv("GECKO_PATH")), options=options)
    
    # Job search query
    search_query = "Web Developer Intern"
    
    # Start the automation
    search_and_apply(driver, search_query, linkedin_username, linkedin_password)
    
    # Close the browser
    driver.quit()

# Run the script
if __name__ == "__main__":
    main()
