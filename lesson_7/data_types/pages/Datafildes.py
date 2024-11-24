from selenium.webdriver.common.by import By

class DataFild:
    def __init__(self, browser):
        self.browser = browser

    def find_fields(self):
        self._first_name = (By.NAME, "first-name")
        self._last_name = (By.NAME, "last-name")
        self._address = (By.NAME, "address")
        self._email = (By.NAME, "e-mail")
        self._phone = (By.NAME, "phone")
        self._zip_code = (By.NAME, "zip_code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._job_position = (By.NAME, "job-position")
        self._company = (By.NAME, "company")

    def get_class_first_name(self):
        return self.browser.find_element(*self.class_first_name).get_attribute("class")
    
    def get_class_last_name(self):
        return self.browser.find_element(*self.class_last_name).get_attribute("class")
    
    def get_class_address(self):
        return self.browser.find_element(*self.class_address).get_attribute("class")
    
    def get_class_email(self):
        return self.browser.find_element(*self.class_email).get_attribute("class")
    
    def get_class_phone(self):
        return self.browser.find_element(*self.class_phone).get_attribute("class")
    
    def get_class_zipcode(self):
        return self.browser.find_element(*self.class_zip_code).get_attribute("class")
    
    def get_class_city(self):
        return self.browser.find_element(*self.class_city).get_attribute("class")
    
    def get_class_country(self):
        return self.browser.find_element(*self.class_country).get_attribute("class")
    
    def get_class_jobposition(self):
        return self.browser.find_element(*self.class_job_position).get_attribute("class")
    
    def get_class_company(self):
        return self.browser.find_element(*self.class_company).get_attribute("class")
