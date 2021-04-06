# suadeanalytics
Suade Labs Python Challenge 2020

## Setting up a development environment (windows)

We assume that you have `git` and `virtualenv` installed.

    # Create a working directory in your local environment:
    e.g.
    mkdir Suade
    
    # Change to working directory:
    e.g 
    cd Suade
    
    # Clone this repo: 
    git clone https://github.com/sharmalondon16/suadeanalytics.git
    
    # Change to code directory:
    e.g 
    cd suadeanalytics
    
    # Create the virtual environment within your working directory (suggested)
    e.g
    .\Suade\suadeanalytics\Python -m venv env
        
        #Activate the virtual environment:
           e.g
           Suade\suadeanalytics\env\Scripts\activate.bat
    
    # Install dependencies with pip: 
    .\Suade\suadeanalytics\pip install -r requirements.txt
    
    # Create an environment variable to run main.py:
    e.g
    .\Suade\suadeanalytics\set FLASK_APP=main.py
    
            # Open code environment (optional)
            e.g (visual studio)
            .\Suade\suadeanalytics\code .
    
    # Start Web Server:
    e.g
    .\Suade\suadeanalytics\flask run
    
        # Test
        Open a browser and go to URL
        http://<IP>:5000                            => Welcome
        http://<IP>:5000/2019-08-01                 =>   example output
        {
         "customers": 877,
         "total_discount_amount": 23207660.62,
         "items": 291544,
         "order_total_avg": 14857290.47,
         "discount_rate_avg": 0.15,
         "commissions": {
            "promotions": {
                "1": 30789016.52,
                "3": 8054710.81,
                "2": 20082936.33,
                "5": 22946449.12,
                "4": 27573451.86
                },
            "total": 2532657169.95,
            "order_average": 2743940.59
         }
    }
    
    
    ## to unit test:
    
    Run test_analytics.py
    e.g .\Suade\suadeanalytics\Python test_analytics.py
 
