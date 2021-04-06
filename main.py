from analytics import Analytics
from flask import Flask, jsonify, render_template
from datetime import datetime
import re
app = Flask(__name__)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # very pretty output to screen
app.config['JSON_SORT_KEYS'] = False              # to maintain dictionary key order

# function to validate input into our analytics server 
def isValidDate(inputDate):
    # check the format of the date supplied
    r = re.compile('....-.*-.*')
    if r.match(inputDate) is  None:
        return False
    
    year,month,day = inputDate.split('-')
    try :
        datetime(int(year),int(month),int(day))
        isValidDate = True
    except ValueError :
        isValidDate = False

    return isValidDate

# create route for a home page
@app.route("/")
def index():
    return render_template('index.html')

        
# create route to serve the analytics data for a given date (YYYY-MM-DD)     
@app.route("/<analytics_date>")
def request_analytics_by_date(analytics_date):

    #redirect to date_error page is invalid date format
    if not isValidDate(analytics_date):
        return render_template('date_error.html')
    
    # create Analytics object and populate with analytics data.
    data = Analytics(analytics_date)
    data.get_analytics()
    
    # return the output dictionary in json format to the browser
    return jsonify (data.output)



if __name__ =="__main__":
    app.run()