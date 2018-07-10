from Product.ratingService import RatingService

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Server says Hello!"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calc_rating', methods=['POST'])
def calc_rating():
    occupation = request.form['occupation']
    numberOfCreditCards = int(request.form['numberofcreditcards'])

    ratingService = RatingService()
    result = ratingService.calculateCreditRating(occupation, numberOfCreditCards)

    return render_template('result.html', rating=result)
    # return "Thank you, your rating is " + str(result)
