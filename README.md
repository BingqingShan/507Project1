#Instructions
## What this program can do
This program consists of 3 other files other than this Readme.md file. They are working together to help you build a functional mini bank app.


The lab3_code.py has written all the classes you need to run this program. Inside this file, there are 3 currency class (Dollar, Yuan and Pound), 1 currency class which can convert one currency to another, and a bank class which can deposit money and show the name, values of its hold currency.


The SI507_project1.py can tie the code in lab3_code.py into a Flask application. It will allow you to go to the routes at the specific paths and show the relevent result on the HTML page. Remember, if you are going to a route which is not defined in the program, you may run into error. So limit your routes in the following options, unless you want to add more routes yourself:

1. / (home page)
2. /bank/<name>
3. /dollar/<amt>
4. /yuan/<amt>
5. /pound/<amt>
6. /bank/<name>/<currency>/<value>


## Dependencies the project relies on
Thus, to guarantee everyone can run this program properly, you may install all the required packages which is written in requirements.txt.

How to install it:

once you set up your virtual environment, you can type in $ pip install -r requirements.txt to install all the required packages all at once.

## How to run this app
Once you download the folder, in your terminal, set up your virtual environment and install packages as said above. Once you are done with that, you can cd to the file SI507_project1.py, type in python SI507_project_1.py runserver in your terminal and then let it run. You will see a builtin server (eg. http://127.0.0.1:5000). copy paste it in your web browser and then you will see the homepage with "Welcome to the banking application!" on it. Now you can go ahead and start to try different routes now.
