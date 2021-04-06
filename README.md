# suadeanalytics
Suade Labs Python Challenge 2020

## Setting up a development environment (windows)

We assume that you have `git` and `virtualenv` installed.

    # Create a working directory in your local environment:
    e.g.
    mkdir Suade\Analytics 
    
    # Clone this repo: 
    git clone https://github.com/sharmalondon16/suadeanalytics.git
    
    # Create the virtual environment within your working directory (suggested)
    e.g
    .\Suade\Analytics\Python -m venv env
        
        #Activate the virtual environment:
           e.g
           Suade\Analytics\env\Scripts\activate.bat
    
    # Install dependencies with pip: 
    .\Suade\Analytics\pip install -r requirements.txt
    
    # Create an environment variable to run main.py:
    e.g
    .\Suade\Analytics\set FLASK_APP=main.py
    
    # Open code environment
    e.g (visual studio)
    .\Suade\Analytics\code .
    
    
    # Start Web Server:
    e.g
    .\Suade\Analytics\flas krun
    
        # Test
        Open a browser and go to URL
        http://<IP>:5000                            => Welcome
        http://<IP>:5000/2019-08-01                 => I am good, how about you?
    
 
