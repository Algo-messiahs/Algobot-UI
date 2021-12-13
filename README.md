# Algobot-UI 
* Algobot-UI Is an algorithmic trading application that introduces user to the concept of algorithmic trading. The web based application comes with a plethora of data visualization tools. The command line based tool helps with portfolio manipulation.

## Installation (How to)

### Prerequisites
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all necessary libraries. This file contains required libraries to make the application work.
```bash
pip install -r requirements.txt
```
* Use of either of these applications requires the use of the Alpaca API, https://app.alpaca.markets/signup
After creating an account the api Keys must be generated.
* Navigate to the path "Algobot-UI\Algobot_Backend" there us a file named config.py edit it with your alpaca account information as seen below. 
```python
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
APCA_API_KEY_ID = "Your Key Id Here"
APCA_API_SECRET_KEY = "Your Secret Key Here"
```

#### Web Application Installation
There is currently a wroking web based implementation that requires a local database.
* Clone repository and perform prerequisite steps outlines above.
* Create a local DB called Algobot
* Update .env file with your perspective credentials 
* Run migration  
```python
python manage.py makemigrations && python manage.py migrate 
```
* Start development server 
``` python
python manage.py runserver  
```
* Navigate to 127.0.0.1:8000 on your browser to view your current portfolio.

#### Command Line Application Installation
The command line implementation of the algorithmic trading bot demonstrates the more practical features of portfolio management.
* Clone repository and perform prerequisite steps outlines above.
* Navigate to "Algobot-UI\Algobot_Backend" 
* Find file "portfolio_manager.py"
* Run file using 
``` python
python -m portfolio_manager.py 
```

## Authors
* Alejandro Rojas
* Eesha Patel
* Kevin Morales-Folgar
* Kyle Weidner
* Selamawit Abdo

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


