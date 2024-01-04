driver=webdriver.chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
username_input=driver.find_element_by_id("username")
username_input=driver.find_element_by_id("password")
login_button.click()

expected_title="orangehrm"
actual_title=driver.title

if actual_title==expected_title:
    print("The title of admin page is orangehrm.")
else:
    print("the tirle of admin page is not orangehrm.") 

#expected options
    
expected_options=["user management", "jobs", "organisation", "qualifications", "nationalities", "corporate banking", "confguration"]   
actual_options=[option.text for option in driver.find_element_by_xpath("//div[@class='menu']/ul/li/a/span")] 

if actual_options==expected_options:

    print{"All the expected options are displayed on the admin page."}
else:
    print("expected options are not displayed")

    driver.quit()    

