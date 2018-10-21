import time
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
   
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*50)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*50)
    
    while True:
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            city = str(input('Select the city you want to analyze: \nChicago?\nNew York City?\nWashington?\n--> ')).lower()
            if city in CITY_DATA.keys():
                break
            else:
                print('\nError! "' + city.title() + '" is not available!\n')
        # Does the user want to filter for month /day / both /none?
        filter_ask = str(input('Do you want to filter "Month", "Day", "Both", or "None"?\n')).lower()
        while filter_ask not in ('month', 'day', 'both', 'none'):
            filter_ask = input('\nSorry, "' + filter_ask.title() + '" is not a valid answer, please input "Month", "Day", "Both" or "None".\n').lower()
        if filter_ask == "both":
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month = str(input('Select the month you want to analyze: \nJanuary, February, March, April, May, June \nor you choose "all": ')).lower()
                if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                    break
                else:
                    print('\nError! "' + month.title() + '" is not available!\n')
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day = str(input('Select the day of week you want to analyze. \n "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" \nor select "all": ')).lower()
                if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                    break
                else:
                    print('\nError! ' + day.title() + ' is not available!\n')
        elif filter_ask == 'month':
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month = str(input('Select the month you want to analyze: \nJanuary, February, March, April, May, June \nor you choose "all": ')).lower()
                if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                    day = 'all'
                    break
                else:
                    print('\nError! "' + month.title() + '" is not available!\n')
        elif filter_ask == 'day':
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day = str(input('Select the day of week you want to analyze. \n "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" \nor select "all": ')).lower()
                if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                    month = 'all'
                    break
                else:
                    print('\nError! ' + day.title() + ' is not available!\n')
        elif filter_ask == 'none':    
            day = 'all'
            month = 'all'
        # Check if the inputs are correct      
        input_control = input('You selected data to analyse the city: "' + city.title() + '" for the month: "' + month.title() + '" and the day: "' + day.title() + '".\nIs this correct? \n(If you choose "No" the data input will restart)\nYes/No: ').lower()
        while input_control not in ('yes', 'no'):
            input_control = input('\nSorry, ' + input_control + ' is not a valid answer, please input "Yes" if the selection is correct or "No" if you want to restart.\n').lower()
        if input_control == ('yes'):
            break
        else:
            continue    

    print('-'*50)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Import csv file for selected city
    df = pd.read_csv(CITY_DATA[city])
    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Convert End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])    
    # Extract month from Start Time column to create a month column
    df['Month'] = df['Start Time'].dt.month
    # Convert integer month into month name --> if there are Problems: Create a Dict with month integers and month names
    df['Month'] = df['Month'].apply(lambda x: calendar.month_name[x])
    # Filter Month by name of selected month or use all and overwrite the Data Frame
    if month != "all":
        df = df[df['Month'] == month.title()]
    # Extract day from Start Time column to create a day of week column
    df['Weekday'] = df['Start Time'].dt.weekday_name
    # Filter Weekday by name of selected Day or use all and overwrite the Data Frame
    if day != "all":
        df = df[df['Weekday'] == day.title()]   
    
    return df

def time_stats(df, city, month, day):
    
    """Displays statistics on the most frequent times of travel."""

    #print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == "all" and day == "all":
        popular_month = df['Month'].mode()[0]
        print('\nMost common month for data in ' + city.title() + ' is: ' + popular_month + '\n')
    elif month == "all" and day != "all":
        popular_month = df['Month'].mode()[0]
        print('Most common month for data in ' + city.title() + ' if only ' + day.title() + "'s are selected is: " + popular_month + '\n')
    elif month != "all":
        print('There is only one "most common" month, because you only selected: ' + month.title() + '\n')
    
    # TO DO: display the most common day of week
    if day == "all" and month == "all":
        popular_day = df['Weekday'].mode()[0]
        print('Most common day for data in ' + city.title() + ' is: ' + popular_day + '\n')
    elif day == "all" and month != "all":
        popular_day = df['Weekday'].mode()[0]
        print('Most common day for data in ' + city.title() + ' if you only selected ' + month.title() + ' is: ' + popular_day + '\n')
    else:
        print('There is only one "most common" day, because you only selected: ' + day.title() + '\n')

    # TO DO: display the most common start hour
    # Extract hour from Start Time column to create a hour column
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['Start Hour'].mode()[0]
    #print(popular_start_hour)
    print('Most common start hour for your selection in ' + city.title() + ' is: ' + str(popular_start_hour) + " o'clock\n")
    
    # TO DO: display the most common End hour
    # Extract hour from Start Time column to create a hour column
    df['End Hour'] = df['End Time'].dt.hour
    popular_end_hour = df['End Hour'].mode()[0]
    #print(popular_end_hour)
    print('Most common end hour for your selection in ' + city.title() + ' is: ' + str(popular_end_hour) + " o'clock\n") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip... \n(for your selection: City: ' + city.title() + ', Month: ' + month.title() + ', Day: ' + day.title() + ')\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station    
    start_station_counts = df['Start Station'].value_counts().tolist()
    start_station_names = df['Start Station'].value_counts().index.tolist()
    start_station_popular = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ' + start_station_popular + ', which was used: ' + str(start_station_counts[0]) + ' times. This is ' + str(start_station_counts[0] - start_station_counts[1]) + ' times more than the second most popular start station: ' + start_station_names[1] +'.\n')

    
    # TO DO: display most commonly used end station
    end_station_counts = df['End Station'].value_counts().tolist()
    end_station_names = df['End Station'].value_counts().index.tolist()
    print('The most commonly used end station is: ' + end_station_names[0] + ', which was used: ' + str(end_station_counts[0]) + ' times. This is ' + str(end_station_counts[0] - end_station_counts[1]) + ' times more than the second most popular end station: ' + end_station_names[1] +'.\n')
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = 'start station: ' + df['Start Station'] + '; end station: ' + df['End Station']
    start_end_counts = df['Start End'].value_counts().tolist()
    start_end_names = df['Start End'].value_counts().index.tolist()
    print('The most frequent combination of start station an end station trip is: ' + start_end_names[0] + ' with ' + str(start_end_counts[0]) + ' combinations.')   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)   

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # calculate total travel time in seconds
    travel_time = df['Trip Duration'].sum()
    
    # if-statements for the different possibilities of time display
    if travel_time < 60:
        print('The total travel time is: ' + str(travel_time) + ' seconds.')
        return
    elif travel_time >= 60 and travel_time < 3600:
        travel_minutes = travel_time // 60
        travel_seconds = travel_time - travel_minutes * 60
        print('The total travel time for your selection is: ' + str(travel_time) + ' seconds. \nThat is ' + str(travel_minutes) + ' minute(s) and ' + str(travel_seconds) + ' second(s).\n')
        return
    elif travel_time >= 3600 and travel_time < 86400:
        travel_hours = travel_time // 3600
        travel_minutes = (travel_time - travel_hours * 3600) // 60
        travel_seconds = (travel_time - travel_hours *3600) - travel_minutes * 60
        print('The total travel time for your selection is: ' + str(travel_time) + ' seconds. \nThat is ' + str(travel_hours) + ' hour(s), ' + str(travel_minutes) + ' minute(s) and '  + str(travel_seconds) + ' second(s).\n')
        return
    elif travel_time >= 86400 and travel_time < 31536000:
        travel_days = travel_time // 86400
        travel_hours = (travel_time - travel_days * 86400) // 3600
        travel_minutes = ((travel_time - travel_days * 86400) - travel_hours * 3600) // 60
        travel_seconds = ((travel_time - travel_days * 86400) - travel_hours * 3600) - travel_minutes * 60
        print('The total travel time for your selection is: ' + str(travel_time) + ' seconds. \nThat is ' + str(travel_days) + ' day(s), ' + str(travel_hours) + ' hour(s), ' + str(travel_minutes) + ' minute(s) and '  + str(travel_seconds) + ' second(s).\n')
    else: 
        travel_years = travel_time // 31536000
        travel_days = (travel_time - travel_years*31536000) // 86400
        travel_hours = ((travel_time - travel_years*31536000) - travel_days * 86400) // 3600
        travel_minutes = (((travel_time - travel_years*31536000) - travel_days * 86400) - travel_hours * 3600) // 60
        travel_seconds = ((((travel_time - travel_years*31536000) - travel_days * 86400) - travel_hours * 3600) - travel_minutes * 60)
        print('The total travel time for your selection is: ' + str(travel_time) + ' seconds. \nThat is ' + str(travel_years) + ' year(s), ' + str(travel_days) + ' day(s), ' + str(travel_hours) + ' hour(s), ' + str(travel_minutes) + ' minute(s) and '  + str(travel_seconds) + ' second(s).\n')

    # TO DO: display mean travel time
    # calculate mean travel time in seconds
    travel_mean_long = df['Trip Duration'].mean()
    travel_mean = round(travel_mean_long, 3)
    # if-statements for the different possibilities of time display
    if travel_mean < 60:
        print('The mean travel time is: ' + str(travel_mean) + ' seconds (to three decimal places).\n')
    else:
        travel_mean_minutes = travel_mean // 60
        travel_mean_seconds_long = travel_mean - travel_mean_minutes * 60
        travel_mean_seconds = round(travel_mean_seconds_long, 3)
        print('The mean travel time is: ' + str(travel_mean) + ' seconds (to three decimal places).\nThat is ' + str(travel_mean_minutes) + ' minute(s) and ' + str(travel_mean_seconds) + ' second(s).')
   
    print('\nIn the following table you can see an overview of the statistical characteristics of the column "Trip Duration": \n')
    print(df['Trip Duration'].describe())
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('What is the breakdown of users? \n' + str(user_counts))

    # TO DO: Display counts of gender and print a massage if "gender" is not available for the selected city
    print('\nWhat is the breakdown of gender?')
    try:
        gender_values = df['Gender'].value_counts().index.tolist()
        gender_counts = df['Gender'].value_counts().tolist()
        print('There are ' +  str(len(gender_values)) + ' types of gender:')
        for n in range(0, len(gender_values)):
            print(f' - There are {gender_counts[n]} {gender_values[n].lower()}s.')
    except:
        print('Sorry, gender is not available for ' + city.title() + '.')


    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nWhat is the oldest, youngest, and most common year of birth, respectively?')
    try:
        year_oldest = df['Birth Year'].min()
        year_youngest = df['Birth Year'].max()
        year_popular = df['Birth Year'].mode()[0]
        print(f' - The oldest year of birth is {int(year_oldest)}.')
        print(f' - The youngest year of birth is {int(year_youngest)}.')
        print(f' - The most common year of birth is {int(year_popular)}.')
    except:
        print('Sorry, year of birth is not available for ' + city.title() + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def display_data(df_raw):
    """Displays Raw data upon request by the user.""" 
    while True:
        raw_request = input('Do you want to see raw data?\nYes/No: ').lower()
        while raw_request not in ('yes', 'no'):
            raw_request = input('Sorry, ' + raw_request + ' is not a valid answer, please input "Yes" or "No" .\n').lower()
        if raw_request == ('yes'):            
            print(df_raw[0:5])
            start_number=5
            while True:
                end_number=start_number+5
                input_request = input('\nDo you want to see more raw data?\nYes/No: ').lower()
                while input_request not in ('yes', 'no'):
                    input_request = input('\nSorry, ' + input_request + ' is not a valid answer, please input "Yes" or "No".\n').lower()
                if input_request == ('yes'):            
                    print(df_raw[start_number:end_number])
                    start_number+=5
                    continue
                else:
                    print('\nYour run is finished!\n' )
                    break  
        else:
            print('\nYour run is finished!\n' )
        break    

def main():
    while True:
        # calculate time of the programm
        start_time = time.time()
        # "import" the functions
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df)
        user_stats(df, city)
        df_raw = load_data(city, month, day)
        display_data(df_raw)    
        print("\nThe entire programm took %s seconds." % (time.time() - start_time))
        print('-'*50)
        # Possible restart of the programm
        restart = input('\nWould you like to restart? Enter "Yes" or "No".\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
