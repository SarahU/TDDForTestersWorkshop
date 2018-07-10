class RatingService:
    def calculateCreditRating(self, occupation, numberOfCreditCards):
        total = 0
        if(occupation == "Doctor" or occupation == "Lawyer"):
            total += 50
        else: total += 20

        if(numberOfCreditCards > 5):
            total -= 5

        if(total < 0):
            return 0
        return total
