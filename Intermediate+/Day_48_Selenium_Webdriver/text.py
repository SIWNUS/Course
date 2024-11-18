for i in range(1,5):
    x_path = f'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[{i}]/div[2]/h5/a'
    
    try:
        a_tag = driver.find_element(By.XPATH, x_path)
        link = a_tag.get_attribute('href')
        driver.execute_script(f"window.open('{link}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        wait_for_page_to_load()
        
        try:
            comments = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/span")))
            count = int(comments.text.split(" ")[0])
            if count < 100:
                driver.close()
            else:
                print(f"{comments} found in this tab.")
        except NoSuchElementException:
            print("Element not found")
            driver.close()
        except TimeoutException:
            print(f"Element not found within timeout for tab {i}")
            driver.close()     

        driver.switch_to.window(main_tab_hande)
    except NoSuchElementException as e:
        print(f"Link not found for item {i}: {e}")

    time.sleep(1)
    
    print(f"Switched back to main tab after processing link {i}")

