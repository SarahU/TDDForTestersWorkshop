import pytest

from Product.ratingService import RatingService

def test_returnMinRatingOfZero():  # check for min rating
    service = RatingService()
    assert service.calculateCreditRating("Nurse", 1) >= 0

def test_doctorScores():           # check for Doctor - experiment, number of cards = 1 - control
    service = RatingService()
    assert service.calculateCreditRating("Doctor", 1) == 50

def test_moreThanSevenCreditCardsMinusFivePoints():  # check for number of cards - experiment, Doctor - control
    service = RatingService()
    assert service.calculateCreditRating("Doctor", 8) == 45

def test_LawyerWithMoreThanSevenCreditCardsMinusFivePoints(): # check for number of cards - experiment, Lawyer - control
    service = RatingService()
    assert service.calculateCreditRating("Lawyer", 8) == 45

def test_NonProfessionalMoreThanSevenCreditCardsMinusFivePoints(): # check not prof job - experiment, number of cards = 2 - control
    service = RatingService()
    assert service.calculateCreditRating("Not a Doctor", 2) == 20

def test_NonProfessionalMoreThanSevenCreditCardsMinusFivePoints(): # number of cards = 2 - experiment, check not prof job - control
    service = RatingService()
    assert service.calculateCreditRating("Not a Doctor", 9) == 15

# Above tests can also we written as below:

@pytest.mark.parametrize("firstName, lastName, occupation, numOfCards, expectedRating", [
    ("Denise","Grant","Doctor", 3, 50),
    ("Danny","Champ","Plumber", 1, 0),
    ("Tammy","Kolmanksi","Lawyer", 9, 45),
    ("Megan","Newton","Electrician", 9, 15)
])
def multipleScenarios(firstName, lastName, occupation, numOfCards, expectedRating):
    service = RatingService()
    assert int(service.calculateCreditRating(occupation,numOfCards)) == expectedRating
