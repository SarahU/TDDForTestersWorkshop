import pytest

from Product.ratingService import RatingService

def test_returnMinRatingOfZero():  # check for min rating
    service = RatingService()
    assert service.calculateCreditRating("Nurse", 1) >= 0
