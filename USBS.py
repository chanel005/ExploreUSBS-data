Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> print("chanel")
chanel
>>> 
=============================== RESTART: Shell ===============================
>>> ## TODO: import all necessary packages and functions


## 2018 US Bike Share Activity Snapshot
# My code

import csv
import datetime
import time
import file 


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    # My code down below


    if city == "Chicago":
        return(chicago)
    elif city == "New York":
        return(new_york_city)
    elif city == "Washington":
        return (washington)
    else:
        return("washington")
 
def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    # My code down below

     if time_period == 'month':
            month = get_month()
            result = ('month',month)
        elif time_period == 'day':
            month = get_month()
            day = get_day(month)
            result = ('day',month,day)
        elif time_period == 'none':
            result = ('none')

    	
    
def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    
    # My code down below

    
 month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    if month == "January" or month == "February" or month == "March"or month == "April" or month == "May"or month == "June":
        return month
    else:
        return "ERROR:

    month = [my_str.split("-")[0] for my_str in march]
	d["March"] = month
	get_month = [2]


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    # My code

    year=2017
    correctDate = None
    while not correctDate:

    day = input('\nWhich day? Please type your response as an integer.\n')
   
    if int(day) <= 7:
        return day
    else:
        return "one day"



def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    # My code down below
    """calculate the popular month of an area."""
						     
	month = self.month
        if month is None:
            try:
                month = popular_month ['month']
            except KeyError:
                try:
		 month = ( weeks/ days)
						     
    

    
def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?    '''
    # TODO: complete function
    """calculate the popular day of an area."""
    """Print the number of weeks and days in a number of days."""

    return "{} week(s) and {} day(s)".format(weeks, remainder)

	days = [0,]
    for row in city_file:
        days[row['startTime'].weekday()] += 1
    maxIx = 0 
    for i in range(0,9):
        if days[i] > days[maxI]:
            maxx = i



def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    """calculate the popular hour of an area."""
    """  This function reads in a file with the most popular hour data of day""" 
	hours = [,]
    for row in city_file:
        hours[row['startTime'].hour] += 1
    maxIx = 0 
    for i in range(0,25):
        if hours[i] > hours[maxx]:
            maxx = i
	

def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    """calculate the trip duration of an area."""
    """ Function reads in a file with trip data and reports the number of trips         made by customers"""

    with open (filename, 'r') as f_in:
	    #set up csv reader
	    reader = csv.Dictreader(f_in)
	    total_duration = 0
	    n_trips_over_30 = 0
	    n_trips_under_30 = 0
	    sub_total_duration = 0
	    
	    
def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    # My code below 
    """calculate the popular stations of an area."""

	data_files = ['./data/NYC-CitiBike-2017.csv',
              './data/Chicago-Divvy-2017.csv',
              './data/Washington-CapitalBikeshare-2017.csv',]

	
    starts = np.sum(trips, axis=1)  
    ends   = np.sum(trips, axis=0) 


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    # My code below 
    """calculate the popular trips of an area.""" 

	
    maxTrip = np.argmax(popular_trip) 
    maxStartIx = maxTrip // len(stnNames) 
    maxEndIx = maxTrip % len(stnNames) 


	for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip
    


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    # My Code below

	 for row in city_file:
        utype = row['utype']
        if type in userType:
            userType[type] += 1
print("Using the supplied filter, users:")
print("\tSubscriber: {}, Customer: {}, Unkonwn: {}")))
    

def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    # My code below

   genderType = {'M':0, 'F':0, 'U':0}
    for row in city_file:
        gtype = row['gender']
        if gtype in genderType:
            genderType[gtype] += 1

    print("Using the supplied filter,  per gender ")
    print("\tMale: {}, Female: {}, Unkonwn: {}".format(genderTypeAccum['M'],genderType['F'],genderType['U']))


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    # my code below

      pp = pprint.data(indent=4)
    print("data")
    cnt = 0
    for row in city_file:
        print()
        pp.pprint(row)
        cnt += 1
        if cnt % 5 == 0:
            if not promptToContinue('\nWould you like to view individual?'):
                return


      
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
     #TODO: call popular_month function and print the results
     #My code
       print("\nLoaded {} records from {} using filter".format(len(city_file))
       print("That took %s seconds." % (time.time() - start_time))

       popular_month(city_file, time_period)

	if len(city_file) == 0:
        print(" no trips.")
    else:
        firstOrNext = 'first'


        
# What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        # My code

        from datetime import date
	 import calendar
	 my_date = date.today()
	 calendar.day_name[my_date.weekday()]
'	Wednesday'

     print("That took %s seconds." % (time.time() - start_time))
        firstOrNext = 'next'


for i in range(7):
    tmp_date = sunday + datetime.timedelta(i)
    print tmp_date.toordinal()%7 + 1, '==', tmp_date.strftime('%A')
        
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    # My code

    print("\nCalculating the {} statistic...".format(firstOrNext))
    start_time = time.time()
    print("That took %s seconds." % (time.time() - start_time))
    firstOrNext = 'next'

    popular_hour(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results

   trip_duration(city_file, time_period)


    for row in reader:
            if float(row['duration']) <= 30:
                n_shortride += 1
                len_shortride += float(row['duration'])
            else:
                n_longride += 1
                len_longride +=float(row['duration'])

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

     popular_stations(stnNames, trips)

     print("That took %s seconds." % (time.time() - start_time))
     

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

	popular_trip(stnNames, trips)

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    users(city_file, time_period)
	     

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    gender(city_file, time_period)

	     

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    #My code

    birth_years(city_file, time_period)

    print("The average age is: " + str(age_sum / len(people)))
    print("The average birth year is: " + str(int(year_sum / len(people))) 

    

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
