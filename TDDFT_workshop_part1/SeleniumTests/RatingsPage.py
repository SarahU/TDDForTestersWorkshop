from selenium import webdriver

class RatingsPage:

    def __init__(self, webdriver):
        self.driver = webdriver

    def fillFormAndSubmit(self, firstName, lastName, occupation, numberOfCreditCards):
        self.fillFirstName(firstName)
        self.fillLastName(lastName)
        self.fillOccupation(occupation)
        self.fillNumberOfCreditCards(numberOfCreditCards)
        self.clickSubmitButton()

    def fillFirstName(self, firstName):
        self.fillElement("firstname", firstName)

    def fillLastName(self, lastName):
        self.fillElement("lastname", lastName)

    def fillOccupation(self, occupation):
        self.fillElement("occupation", occupation)

    def fillNumberOfCreditCards(self, numberOfCreditCards):
        self.fillElement("numberofcreditcards", numberOfCreditCards)

    def fillElement(self, elementName, elementValue):
        elem = self.driver.find_element_by_name(elementName)
        elem.clear()
        elem.send_keys(elementValue)

    def clickSubmitButton(self):
        elem = self.driver.find_element_by_name("submit")
        elem.click()
