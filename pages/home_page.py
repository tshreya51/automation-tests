from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.name_input="//input[@id='name']"
        self.radioButtons="//input[contains(@class,'radioButton')]"
        self.checkboxes="//input[contains(@type,'checkbox')]"
        self.dyn_dropdowns="//input[contains(@class,'inputs ui-autocomplete-input')]"
        self.alerts="alertbtn"
        self.web_table="//div[contains(@class,'tableFixHead')]/table[@id='product']"

    #---------RADIO BUTTONS----------
    def select_radio(self,value):
        radios=self.driver.find_elements(By.XPATH,self.radioButtons)
        for radio in radios:
            if radio.get_attribute("value")==value:
                radio.click()
                assert radio.is_selected()
                return True
        return False

