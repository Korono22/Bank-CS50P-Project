# Bank
### Video Demo: https://youtu.be/ZmssBQwm8X0
### Description:
The project is a console application that does basic bank functions such as adding account, removing account, listing all accounts and converting currecy with API.
### Libraries that i used:
* re
* requests
* tabulate
* csv
* pytest
___
### API that i used:
#### Main site: https://exchangerate.host
#### Documentation: https://exchangerate.host/#/#docs
___
## How it works:
When you run the file, before anything happens program sorts the accounts.csv file by account id, and if the file does not exist, it attempts to create it. Then user is asked what does he want to do and can leave at any time by pressing CTRL+D. The action that the program does depends on what number the user enters.
### Number 1 - Adding account:
The program asks you to enter the amount of money you have in pounds. Then function add_account executes. First it uses regex to check if the input is in correct format, otherwise the program ends informing the user that he inputted the currency with the wrong format. If the regex search returns True, using the csv.DictWriter, program saves the money in the accounts.csv file, and assigns it the first available number starting from 1.
### Number 2 - Removing account:
The program asks you to enter account number (account number can be checked with option 3 - List accounts) to remove. Then function remove_account executes. First it sets the flag variable to False. With the file readLines function it copies the file into a list.
The file is then rewritten, skipping the account with the account number that user entered. If the function finds the account that user wants removed it sets the Flag to True. At the end of the function it checks if the flag is False, if it is then it informs the user that the account that he wanted to remove does not exist.
### Number 3 - Listing accounts
The program executes list_accounts function, which is much simpler thanks to the tabulate function from tabulate library. It reads the accounts.csv file with csv.Reader, then prints a grid-like table with data from accounts.csv file.
### Number 4 - Converting the currency
The program asks the user to input number of account he wants to convert (account number can be checked with option 3 - List accounts). Then it tries to find the account in the account.csv file using csv.Reader and assigns pounds and pennies to variables. The user is asked to which currency he would like to convert his account to, and assigns input to variable. Then function convert is executed. This function takes the amount of money that the account and the currency that the user wants it converted to (List of currencies is on https://openexchangerates.org/api/currencies.json). Then it takes the data from API URL that got modified to match the amount of money and currency and reads the JSON response from API. If the value of the amount of money after conversion is None function raises ValueError and informs the user that account with such number does not exist. Also if the currency is wrong it informs the user that he inputted wrong currency.
If everything is right function returns the rounded value of currency that the user wanted to two decimals.
___
## Possible improvements
* Listing available currencies
* Accounts could save in which currency they are, as opposed to default (GBP).
* Account conversion could not be just theoretical, it could change the amount of money the account in the converted currency (addition to the first point)
* Adding more functionality such as adding the money to already existing account
* Improving the menu to be more visually appealing