# Algobot-UI 
* Algobot-UI Is an algorithmic trading platform that introduces user to the concept of algorithmic trading.

## Installation (How to)

### Prerequisites
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all necessary libraries.
```bash
pip install -r requirements.txt
```
Use of either of these applications requires the use of the Alpaca API, https://app.alpaca.markets/signup
After creating account api Keys must be generated.

#### Web Application Installation
There is currently a wroking web based implementation that requires a local database.
* Create a local DB called Algobot
* Update .env file with your perspective credentials 
* Install Packages -  ``` pip install -r requirements.txt``` from the terminal 
* Run migration -  ```python manage.py makemigrations``` && ```python manage.py migrate ```
* Start development server -  ``` python manage.py runserver  ```

### Command Line Application Installation
The command line implementation of the algorithmic trading bot demonstrates the more practical features of portfolio management.
* Clone repository
*  

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


