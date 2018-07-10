import pytest
from selenium import webdriver

from RatingsPage import *

@pytest.fixture
def driver():
    d = webdriver.Firefox()
    yield d
    d.close()

@pytest.mark.parametrize("firstName, lastName, occupation, numOfCards, expectedRating", [
    ("Denise","Grant","Doctor", "3", "50"),
    ("Danny","Champ","Plumber", "1", "20"),
    ("Tammy","Kolmanksi","Lawyer", "9", "45"),
    ("Megan","Newton","Electrician", "9", "15")
])
def test_multipleUseCases(firstName, lastName, occupation, numOfCards, expectedRating, driver):
    driver.get("http://127.0.0.1:5000/")
    page = RatingsPage(driver)
    page.fillFormAndSubmit(firstName,lastName,occupation, numOfCards)

    resultString = "Your rating result is: " + expectedRating
    xPath = "//*[contains(.,'"+ resultString +"')]";
    resultElement = driver.find_element_by_xpath(xPath);

    assert resultElement  is not None

# # Title test
# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:5000/")
# assert "Credit Rate Checker" in driver.title
