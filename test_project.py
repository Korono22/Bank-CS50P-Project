from project import convert, add_account
import requests
import csv
import pytest


def test_convert_correct():
    url = f"https://api.exchangerate.host/convert?from=GBP&to=EUR&amount=123.12"
    response = requests.get(url)
    data = response.json()
    assert convert("123", "12", "EUR") == round(data['result'], 2)


def test_convert_incorrect():
    with pytest.raises(ValueError):
        assert convert("123", "12", "NonExistingCurrency")


def test_add_account():
    #test the add_account function and then remove the account that was the test
    add_account("123.12")
    with open("accounts.csv") as file:
        reader = csv.reader(file)
        last_acc = sum(1 for _ in reader)-1
        file.seek(0)
        reader = csv.reader(file)
        for row in reader:
            if last_acc == row[0]:
                assert row[1] == 123 and row[2] == 12
        file.seek(0)
        lines=file.readlines()
        lines.pop(len(lines)-1)
    with open("accounts.csv", "w") as file:
        for line in lines:
            file.write(line.strip() + "\n")


def test_add_account_incorrect():
    with pytest.raises(ValueError):
        add_account("123 12")
