# CECS343 Request for Proposal



John is a small-time landlord: He owns an apartment building with 20 units. He wants you to
write a program that will make it easier for him to record data and print reports regarding the
finances of the apartment building. If you and John can agree on payment, schedule, and the
overall purpose of the program, you've completed the inception part of the development process.
Currently John is recording all the information about his apartment building by hand, in old-
fashioned ledger books. He shows you the forms he's currently using. There are four of them:

* The Tenant List
* The Rental Income Record
* The Expense Record
* The Annual Summary

The Tenant List shows apartment numbers in one column and the corresponding tenant's names
in the adjacent columns.

The Rental Income Record records incoming rent payments. It contains 12 columns, one for
each month; and one row for each apartment number. Each time John receives a rental payment
from a tenant, he records it in the appropriate row and columns of the Rental Income Record.

The Expense Record records outgoing payments. It has columns for date, the payee (the
company or person to whom John writes the check), and the amount being paid. In addition ,
there's a column where John can specify the budget category to which the payment should be
charged. Budget categories include Mortgage, Repairs, Utilities, Taxes, Insurance, and so on.

The Annual Report uses data from the Rental Income Record and Expense Record to
summarize how much money came in and how much went out during the year. All the rents are
summed and the result is displayed. The expenses are summed and displayed by the budget
category, which makes it easy to see, for example, how much was spent on repairs during the
year. Finally, expenses are subtracted from income to show how much money John made (or
lost) during the year.

John tells you that he wants the program to pretty much duplicate what he's currently doing on
the paper forms. He wants to be able to enter data about tenants, rents, and expenses, and
display the various reports.

# How to run

### 1. Run main program

```
python app.py
```

### 2. Login with correct credentials:

```
Username: 343group6
Password: landlord
```

## Login Page

![Login Page](/examples/login_page.png "Snapshot of webapp when asking user to login.")

## Main Menu

![Main Menu](/examples/main_menu.png "Snapshot of webapp when displaying main menu.")

## Example of Tenant List

![Tenant List](/examples/tenant_list.png "Snapshot of webapp when displaying tenant list.")

## Example of Rental Income Record

![Rental Income Record](/examples/rental_income_record.png "Snapshot of webapp when displaying rental income record.")

## Example of Expense Record

![Expense Record](/examples/expense_record.png "Snapshot of webapp when displaying expense record.")


## Example of Annual Report

![Annual Report](/examples/annual_report.png "Snapshot of webapp when displaying annual report.")
