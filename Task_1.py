# A program that provides the summary and details of corona virus cases as at 25th May 2020 by continent

# Dictionary that stores the continent details
# Using the values for all the countries in the continent
Africa_details = {"Total_cases": "120592", "Total Deaths": "3591", "Active cases": "67503",
                  "Total_discharged": " 49498"}
Oceania_details = {"Total_cases": "8741", "Total Deaths": "123", "Active cases": "503",
                   "total_discharged": " 8115"}
SouthAmerica_details = {"Total_cases": "661701", "Total Deaths": "32798", "Active cases": "363581",
                        "total_discharged": " 265322"}
Asia_details = {"Total_cases": "1002915", "Total Deaths": "28220", "Active cases": "385656",
                "Total_discharged": " 589039"}
NorthAmerica_details = {"Total_cases": "1920645", "Total Deaths": "116000", "Active cases": "1214687",
                        "Total_discharged": "589958 "}
Europe_details = {"Total_cases": "1934056", "Total Deaths": "169601", "Active cases": "851912",
                  "Total_discharged": " 912543"}
# Dictionary for the summary three countries in each continent.
# using the python function for min,max,mean and sum to generate for three countries
Africa_summary = {" min": " 8733", "max": "25937", "mean": "18112", "sum": "54336"}
Asia_summary = {" min": "141591 ", "max": "159797", "mean": "153333.6667", "sum": "460001"}
SouthAmerica_summary = {" min": "82289 ", "max": "414661", "mean": "210951.6667", "sum": "632855"}
NorthAmerica_summary = {" min": "78023 ", "max": "1745803", "mean": "637115", "sum": "1911345"}
Europe_summary = {" min": "267240 ", "max": "397051", "mean": "310046.6667", "sum": "930140"}
Oceania_summary = {" min": " 60", "max": "7150", "mean": "2904.6666", "sum": "8714"}


def login():
    logged_in = input('What continent will you like to see the corona virus cases statistics? '
                      'Enter 1 to continue or 2 to exit: ')
    if logged_in == '1':
        new_user()
    elif logged_in == '2':
        exit()
    else:
        print("Invalid request")
        login()


def new_user():
    user_name = input("Please enter your preferred name: ")
    print("Hello", user_name, "Hope you're feeling good today")
    continent = input("Enter the continent you will like to know their statistics: ")
    # Creating for Asia
    if continent == "Asia":
        print(Asia_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(Asia_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()
    # Creating for Africa
    if continent == "Africa":
        print(Africa_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(Africa_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()
    # Creating for Europe
    if continent == "Europe":
        print(Europe_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(Europe_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()
    # Creating for South America
    if continent == "South America":
        print(SouthAmerica_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(SouthAmerica_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()
    # Creating for Oceania
    if continent == "oceania":
        print(Oceania_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(Oceania_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()
    # Creating for North America
    if continent == "North America":
        print(NorthAmerica_summary)
    details = input("Would you like to see the details? Enter yes or no to continue: ")
    if details == "yes":
        print(NorthAmerica_details)
    elif details == "no":
        login()
    else:
        print("Wrong choice!Goodbye")
        exit()


new_user()


