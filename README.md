# PromoHub
Promo Code Hub


Installation Steps:


***
  Install Python and Anaconda
  
  Anaconda
  
    1. Install here https://docs.anaconda.com/anaconda/install/index.html
    
  ```
    2. After installation, open Anaconda command prompt, 
          type  
          >where conda
          Set each path to a User Variables path, (excluding the anaconda file names themselves)
                  i.e. C:\Users\guarinof\Anaconda3\Library\bin\conda.bat
                  should be C:\Users\guarinof\Anaconda3\Library\bin    in your path
  ```
          
          
    3. Create _new anaconda environment_ in the anaconda application UI
  
  
  
    4. Use VS Code
        Ctrl + Shift + P 
          Select Interpreter  Choose your _new anaconda env_
          
          
***

  Python
  
  Install here https://www.python.org/downloads/
  
  
***

Install necessary modules

Open CMD terminal 

pip install
    flask
    flask_restful
    flask_mysqldb
          
      
***

Start the server and run the source code


Open terminal

  CD into api folder
  
  ```
  CMD 
  > set FLASK_APP=main
  > flask run
   * Running on http://127.0.0.1:5000/
  ```
  ```
  Powershell
  > $env:FLASK_APP = "main"
  > flask run
    * Running on http://127.0.0.1:5000/
          
  ```
