import re
import csv
from tabulate import tabulate
import requests

def main():
    print("CS50 final project \"Bank\", created by Antoni Wisniewski, August 2022")
    print("Welcome to the bank!")
    #before doing anything, sort the file by account number
    try:
        with open('accounts.csv') as file:
            reader = csv.DictReader(file)
            sortedlist = sorted(reader, key=lambda row: row['acc_no'], reverse=False)

        with open('accounts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=["acc_no", "pounds", "pennies"])
            writer.writeheader()
            for row in sortedlist:
                writer.writerow(row)
    #if file doesnt exist, create it
    except FileNotFoundError:
        with open("accounts.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["acc_no", "pounds", "pennies"])
            writer.writeheader()
    try:
        number = input("Would you like to add account (type 1), remove accounts (type 2), list accounts (type 3) or convert an existing account to any currency (type 4)?\n")
        match int(number):
            case 1:
                try:
                    add_account(input("How many pounds do you have (with two decimals)?\n"))
                except ValueError:
                    print("Incorrect format")
            case 2:
                try:
                    remove_account(input("What account number would you like to remove?\n"))
                except:
                    print("That account doesnt exist!")
            case 3:
                list_accounts()
            case 4:
                try:
                    number = input("Enter the number of the account that you want converted\n")
                    with open("accounts.csv") as file:
                        reader = csv.reader(file)
                        #count the number of rows
                        if sum(1 for _ in reader)-1 < int(number):
                            raise ValueError
                        #reset the reader
                        file.seek(0)
                        reader = csv.reader(file)
                        for row in reader:
                            if number == row[0]:
                                pounds = row[1]
                                pennies = row[2]
                    currency = input("To which currency would you like to convert?\n")
                    try:
                        print(f"Your account converted to {currency} would be {convert(pounds, pennies, currency)}")
                    except ValueError:
                        print("Wrong currency!")
                except ValueError:
                    print("That account doesnt exist!")
            case _:
                print("Wrong number")
    except EOFError:
        print("Goodbye")

def convert(pounds, pennies, currency):
    #list of currencies https://openexchangerates.org/api/currencies.json
    url = f"https://api.exchangerate.host/convert?from=GBP&to={currency}&amount={pounds}.{pennies}"
    response = requests.get(url)
    data = response.json()
    if data["result"] != None:
        return round(data['result'], 2)
    raise ValueError



def add_account(value):
    if re.search(r"^\d+\.\d\d$", value):
        account = 1
        pounds, pennies = value.split(".")
        with open("accounts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["acc_no"]) != account:
                    break
                account += 1
        with open("accounts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["acc_no", "pounds", "pennies"])
            writer.writerow({"acc_no": account, "pounds": pounds, "pennies": pennies})
    else:
        raise ValueError


def remove_account(number):
    flag = False
    with open("accounts.csv") as file:
        lines = file.readlines()
    with open("accounts.csv", "w") as file:
        for line in lines:
            if line.startswith(f"{number}") == False:
                file.write(line)
            else:
                #raise a flag if it founds the account number
                flag = True
    #if the account number is not found raise ValueError
    if flag == False:
        raise ValueError


def list_accounts():
    with open("accounts.csv") as file:
        table = csv.reader(file)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()