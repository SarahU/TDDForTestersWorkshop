TDD For Testers Workshop
========================

This workshop looks at how to do TDD.
It also looks at code duplication redundancy

Part 1 - Has some completed selenium tests but unit tests need to be written
Part 2 - Part 1 completed (not all product rules are completed)
Part 3 - Place for continued development

## Requirements:
This code was developed on a Windows 10 OS. You may experience additional issues than those listed below. Please raise a pull request or issue to log changes to the README.

**Known issues**
At time of development, a few issues were encountered:

Known bug where Flask does not work with Python 3.6.
Issues in Windows with Chrome Webdriver - try Firefox instead

**Installation instructions**
Python 3.6 - not 3.7 - see issues above
Please select to 'add the PYTHONPATH to your environment variables' option

Also install:
pip install -U Flask
pip install -U pytest
pip install -U selenium
(pip comes with Python)

-> Windows users - run CMD as Administrator

**Running instructions**
On Windows:
  Product:
    set FLASK_APP = app.py
    flask run

  Unit Tests:
    pytest test_ratingService.py

  Selenium Tests:
    pytest selenium_acceptance_tests.py


## Product Rules:
Min rating = 0
Max rating = 100
Occupation of: Doctor, Lawyer, Accountant -> rating point of 50
                                otherwise -> 20
Number of current credit cards more than 7 -> minus 5 points
Current debt: 0  -> add 10 points
         0-2000  -> add 25 points
      2000-5000  -> add 15 points
      5000-7500  -> add 5 points
     7500-10000  -> minus 5 points
    10000-15000  -> minus 15 points
         >15000  -> minus 25 points    
