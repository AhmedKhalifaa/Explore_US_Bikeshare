import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city=input("Enter which City you want to Explore : chicago,new york city or washington")
    while True:
        city=input("Enter which City you want to Explore : chicago,new york city or washington\n")
        if city.lower() =='chicago' or city.lower()=='new york city' or city.lower()=='washington' :
            city=city.lower()
            print("You chose:",city.title())
            break
            

        else:
            print("That's not a valid city")
            print("Please Re-enter City Name")
            continue
    
    
    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("Enter a specific month(january,february,march,april,may,june),or type 'all' to see all months statistics\n")
        if month.lower()=="january" or month.lower()=="february" or month.lower()=="march" or month.lower()=="april" or month.lower()=="may" or month.lower()=="june" or month.lower()=="all":
            month=month.lower()
            print("You chose:",month.title())
            break
        
        else:
            print("That's not a valid month")
            print("Please Re-enter month Name")
            continue




    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter a specific day of the week(saturday,sunday,monday,tuesday,wednesday,thursday,friday),or type 'all' to see the whole month's statistics\n")
        if day.lower()=="saturday" or day.lower()=="sunday" or day.lower()=="monday" or day.lower()=="tuesday" or day.lower()=="wednesday" or day.lower()=="thursday" or day.lower()=="friday" or day.lower()=="all":
            day=day.lower()
            print("You chose:",day.title())
            break
        else:
            print("That's not a valid day")
            print("Please Re-enter day Name")
            continue


    print('-'*40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    print(df)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print(df)
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print(df)
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df=df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df=df[df['day_of_week'] == day.title()]
    print(df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df.head(5))
    # display the most common month
    most_common_month=df['month'].mode()[0]
    print("Most common month for travel is:",most_common_month)
    


    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("Most common day for travel is:",most_common_day)
    

    # display the most common start hour
    df["hour"]=df["Start Time"].dt.hour
    most_common_hour=df["hour"].mode()[0]
    print("Most common hour for travel is:",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=df["Start Station"].mode()
    print("most commonly used start station is:",most_common_start_station)


    # display most commonly used end station

    most_common_end_station=df["End Station"].mode()
    print("most commonly used end station is:",most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["Most_Common_Trip"]=df["Start Station"]+df["End Station"]
    most_frequent_combination=df["Most_Common_Trip"].mode()
    print("most frequent combination of start station and end station trip is:",most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("total travel time is",total_travel_time," Seconds")

    # display mean travel time
    average_travel_time=df["Trip Duration"].mean()
    print("average travel time is",average_travel_time," Seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count=df["User Type"].value_counts()
    print("User type count is:",user_type_count)

    # Display counts of gender
    try:
        gender_count=df["Gender"].value_counts()
        print("Gender count is:",gender_count)
    except:
        print("Gender data is unavailable for this city")
    

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year=df["Birth Year"].min()
        print("earliest year of birth is:",earliest_birth_year)

        most_recent_birth_year=df["Birth Year"].max()
        print("most recent year of birth is:",most_recent_birth_year)

        most_common_birth_year=df["Birth Year"].mode()
        print("most common year of birth is:",most_common_birth_year)
    except:
        print("Birth Year data is unavailable for this city")
       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_viewer(df):
    """Displays rows of of the raw data,5 new rows every time the user types 'yes'. Starts from the top 5 rows"""
    
    rows_counter=0

    while True:
        do_you_want_data=input("Do you want to see a portion of the raw data ? (yes/no)"+"\n")
        rows_counter=rows_counter+5
        if do_you_want_data=="yes".lower():
            print(df.head(rows_counter))
            continue
        elif do_you_want_data=="no".lower():
            print("")
            break
        else:
            print("Please answer with yes/no,"+"Do you want to see a portion of the raw data ? (yes/no)"+"\n")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_viewer(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



