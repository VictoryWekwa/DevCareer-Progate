import numpy as np
#### This class holds the data for each continent
def login():
	user_input=("Enter 1 to continue or 2 to close app")
	if user_input=="1":
		covid_details()
	elif user_input=="2":
		exit()
		

class Data:
    def __init__(self, n_america, europe, s_america, asia, africa):
        self.n_america = n_america
        self.europe = europe
        self.s_america = s_america
        self.asia = asia
        self.africa = africa
        
    def n_america(): #north america function
        n_america = {
            'countries' : ['USA', 'Canada', 'mexico'],
            'total_cases' : [1746311, 87519, 78023],
            'active cases' : [1153939, 34590, 15043],
            'discharged'   : [490256, 46164, 54383],
            'death' : [102116, 6765, 8597] 
        }
        return n_america
        
    def europe(): #europe function
        europe = {
            'countries' : ['Russia', 'Spain', 'Italy'],
            'total_cases' : [379051, 283849, 231139],
            'active cases' : [223916, 59773,50996 ],
            'discharged'  : [150993, 196958, 147101],
            'death' : [4142, 27118, 33072] 
        }
        return europe
        
    def s_america(): #south america function
        s_america = {
            'countries' : ['Brazil', 'Peru', 'Chile'],
            'total_cases' : [414661, 134905,82289 ],
            'active cases' : [222317, 75753, 47908],
            'discharged'   : [166647, 56169, 33540],
            'death' : [25697, 3983,841] 
        }
        return s_america
    def asia(): #asia function
        asia = {
            'countries' : ['China', 'India', 'Japan'],
            'total_cases' : [82995, 159054, 16651],
            'active cases' : [73,86584 , 1829],
            'discharged'   : [78288, 67929, 13973],
            'death' : [4634, 4541, 858] 
        }
        return asia
        
    def africa(): #africa function
        africa = {
            'countries' : ['Nigeria', 'Egypt', 'Ghana'],
            'total_cases' : [8733 , 19666, 7303],
            'active cases' : [5978, 13645, 4857],
            'discharged'   : [2501, 5205, 2412],
            'death' : [254, 816, 34] 
        }
        return africa
#### This class Covid hold the detailed statistics across continents
class Covid: 
    def __init__(self, n_america, europe, s_america, asia, africa):
        self.n_america = n_america
        self.europe = europe
        self.s_america = s_america
        self.asia = asia
        self.africa = africa
        
    def n_america_stats(n_america): #north america statistics
        print("Minimum : " + str(np.min(n_america['total_cases'])))
        print("Max : " + str(np.max(n_america['total_cases'])))
        print("Sum : " + str(np.sum(n_america['total_cases'])))
        print("Mean : " + str(np.mean(n_america['total_cases'])))
        
    def europe_stats(europe): #europe statistics
        print("Minimum : " + str(np.min(europe['total_cases'])))
        print("Max : " + str(np.max(europe['total_cases'])))
        print("Sum : " + str(np.sum(europe['total_cases'])))
        print("Mean : " + str(np.mean(europe['total_cases'])))
        
    def s_america_stats(s_america): #south america statistics
        print("Minimum : " + str(np.min(s_america['total_cases'])))
        print("Max : " + str(np.max(s_america['total_cases'])))
        print("Sum : " + str(np.sum(s_america['total_cases'])))
        print("Mean : " + str(np.mean(s_america['total_cases'])))
        
    def asia_stats(asia): #asia statistics
        print("Minimum : " + str(np.min(asia['total_cases'])))
        print("Max : " + str(np.max(asia['total_cases'])))
        print("Sum : " + str(np.sum(asia['total_cases'])))
        print("Mean : " + str(np.mean(asia['total_cases'])))
        
    def africa_stats(africa): #africa statistics
        print("Minimum : " + str(np.min(africa['total_cases'])))
        print("Max : " + str(np.max(africa['total_cases'])))
        print("Sum : " + str(np.sum(africa['total_cases'])))
        print("Mean : " + str(np.mean(africa['total_cases'])))
        

        
### fuunctions to get the total cases, active cases, death cases an the likes
def get_continent(continent):
    if continent == 'asia':
        total_cases = Data.asia()
    elif continent == 'africa':
        total_cases = Data.africa()
    elif continent == 's_america':
        total_cases = Data.s_america()
    elif continent == 'n_america':
        total_cases = Data.n_america()
    elif continent == 'europe':
        total_cases = Data.europe()
    return total_cases

### function to get the details statistics
def get_statistics(continent):
#     continent = get_continent(continent)
    if continent == 'asia':
        stats = Covid.asia_stats(Data.asia())
    elif continent == 'africa':
        stats = Covid.africa_stats(Data.africa())
    elif continent == 's_america':
        stats = Covid.s_america_stats(Data.s_america())
    elif continent == 'n_america':
        stats = Covid.n_america_stats(Data.n_america())
    elif continent == 'europe':
        stats = Covid.europe_stats(Data.europe())
    return stats

###################### Applying my functions#######################
def covid_details():
	continent = input('What continent would you like to check?:' ).lower() ###Collect user's desired continent
	print(get_continent(continent))
	see_details = input('Check statistics? Answer yes or no: ').lower() ###### Ask for details
	if see_details == 'no':
    login()
    elif see_details == 'yes':
    print(get_statistics(continent))
    login()
    

login()
#     def login():
#         logged_in = input('What continent will you like to see the corona virus cases statistics? '
#                       'Enter 1 to continue or 2 to exit: ')
#         if logged_in == '1':
#             new_user()
#         elif logged_in == '2':
#             exit()
#         else:
#             print("Invalid request")


#     def new_user():
#         user_name = input("Please enter your preferred name: ")
#         print("Hello", user_name, "Hope you're feeling good today")
#         continent = input("Enter the continent you will like to know their statistics: ")
#         details = input("Would you like to see the details? Enter yes or no to continue: ")

#     # Creating for Asia
#         if continent == "Asia":
#             print(asia.items())
#             if details == "yes":
#                 print(Covid.asia_stats(asia))
#             elif details == "no":
#                 login()
#             else:
#                 print("Wrong choice!Goodbye")
#                 exit()
#     # Creating for Africa
#         if continent == "Africa":
#             print(africa)
#             if details == "yes":
#                 print(Covid.africa_stats)
#             elif details == "no":
#                 login()
#         else:
#             print("Wrong choice!Goodbye")
#             exit()
#     # Creating for Europe
#         if continent == "Europe":
#             print(europe)
#             if details == "yes":
#                 print(Covid.europe_stats)
#             elif details == "no":
#                 login()
#         else:
#             print("Wrong choice!Goodbye")
#             exit()
#     # Creating for South America
#         if continent == "South America":
#             print(s_america)
#             if details == "yes":
#                 print(Covid.s_america_stats)
#             elif details == "no":
#                 login()
#         else:
#             print("Wrong choice!Goodbye")
#             exit()
    
#     # Creating for North America
#         if continent == "North America":
#             print(n_america)
#             if details == "yes":
#                 print(Covid.n_america_stats)
#             elif details == "no":
#                 login()
#         else:
#             print("Wrong choice!Goodbye")
#             exit()


#     new_user()
v