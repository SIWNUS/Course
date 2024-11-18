from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

# Set up Firefox options and driver
options = Options()
options.binary_location = os.getenv("FIREFOX_EXEC_PATH")
gecko_path = os.getenv("GECKO_PATH")
service = Service(executable_path=gecko_path)
driver = webdriver.Firefox(service=service, options=options)

try:
    # Navigate to the desired URL
    driver.get("https://arunagiritemples.wordpress.com/2019/10/20/%E0%AE%B5%E0%AF%87%E0%AE%B2%E0%AF%8D-%E0%AE%AE%E0%AE%BE%E0%AE%B1%E0%AE%B2%E0%AF%8D-%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AE%BE%E0%AE%AF%E0%AE%A3%E0%AE%AE%E0%AF%8D/")

    # Find all <p> elements on the page
    p_tags = driver.find_elements(By.TAG_NAME, "p")
    if not p_tags:
        print("No <p> tags found!")
        exit()

    # Write the text from <p> tags to VelMaral.txt
    with open("VelMaral.txt", 'a') as fp:
        for p in p_tags[15:98]:
            fp.write(f"\n{p.text}\n")

    # Read and process the lyrics
    with open("VelMaral.txt", 'r') as fp:
        lyrics = [lyric.strip() for lyric in fp.readlines() if lyric.strip()]

    # Find specific text for replacement
    ch_text = ''
    for idx, lyric in enumerate(lyrics):
        if idx == 10:
            ch_text = lyric.replace("( … இந்த அடியை முதலில் 20 முறை ஓதவும் … )", "")

    # Replace text for specific indices
    modified_lyrics = []
    for idx, lyric in enumerate(lyrics):
        if 11 < idx < 78:
            lyric = lyric.replace("( … திரு … )", f"\n{ch_text}\n")
        modified_lyrics.append(lyric)

    # Write final content to Final.txt
    with open("Final.txt", 'a') as fp:
        fp.writelines(f"\n{elem}\n" for elem in modified_lyrics)

finally:
    driver.quit()
