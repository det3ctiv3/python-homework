import pandas as pd
import sqlite3
import numpy as np

def chinook_inner_join():
    conn = sqlite3.connect('chinook.db')
    customers = pd.read_sql_query("SELECT * FROM customers", conn)
    invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
    merged = pd.merge(customers, invoices, on='CustomerId', how='inner')
    invoice_counts = merged.groupby('CustomerId').size().reset_index(name='Total_Invoices')
    print("Total invoices per customer:")
    print(invoice_counts)
    conn.close()
    return invoice_counts

def movie_outer_join():
    movies = pd.read_csv('movie.csv')
    df1 = movies[['director_name', 'color']]
    df2 = movies[['director_name', 'num_critic_for_reviews']]
    left_join = pd.merge(df1, df2, on='director_name', how='left')
    outer_join = pd.merge(df1, df2, on='director_name', how='outer')
    print(f"Left join row count: {len(left_join)}")
    print(f"Outer join row count: {len(outer_join)}")
    return left_join, outer_join

def titanic_grouping():
    titanic = pd.read_csv('titanic.csv')
    result = titanic.groupby('Pclass').agg({
        'Age': 'mean',
        'Fare': 'sum',
        'PassengerId': 'count'
    }).rename(columns={
        'Age': 'Average_Age',
        'Fare': 'Total_Fare',
        'PassengerId': 'Passenger_Count'
    })
    print("Titanic grouped results:")
    print(result)
    return result

def movie_multi_group():
    movies = pd.read_csv('movie.csv')
    result = movies.groupby(['color', 'director_name']).agg({
        'num_critic_for_reviews': 'sum',
        'duration': 'mean'
    }).rename(columns={
        'num_critic_for_reviews': 'Total_Reviews',
        'duration': 'Average_Duration'
    })
    print("Movie multi-level grouping:")
    print(result.head())
    return result

def flights_nested_group():
    flights = pd.read_csv('flights.csv')
    result = flights.groupby(['Year', 'Month']).agg({
        'FlightNum': 'count',
        'ArrDelay': 'mean',
        'DepDelay': 'max'
    }).rename(columns={
        'FlightNum': 'Total_Flights',
        'ArrDelay': 'Average_ArrDelay',
        'DepDelay': 'Max_DepDelay'
    })
    print("Flights nested grouping:")
    print(result.head())
    return result

def titanic_age_group():
    titanic = pd.read_csv('titanic.csv')
    def classify_age(age):
        if pd.isna(age):
            return 'Unknown'
        return 'Child' if age < 18 else 'Adult'
    titanic['Age_Group'] = titanic['Age'].apply(classify_age)
    print("Titanic with Age Groups:")
    print(titanic[['Age', 'Age_Group']].head())
    return titanic

def normalize_salaries():
    employees = pd.read_csv('employee.csv')
    employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() != x.min() else 0
    )
    print("Normalized salaries:")
    print(employees[['Department', 'Salary', 'Normalized_Salary']].head())
    return employees

def movie_duration_class():
    movies = pd.read_csv('movie.csv')
    def classify_duration(duration):
        if pd.isna(duration):
            return 'Unknown'
        if duration < 60:
            return 'Short'
        elif duration <= 120:
            return 'Medium'
        return 'Long'
    movies['Duration_Class'] = movies['duration'].apply(classify_duration)
    print("Movies with duration classification:")
    print(movies[['duration', 'Duration_Class']].head())
    return movies

def titanic_pipeline():
    titanic = pd.read_csv('titanic.csv')
    def filter_survived(df):
        return df[df['Survived'] == 1]
    def fill_age(df):
        mean_age = df['Age'].mean()
        return df.assign(Age=df['Age'].fillna(mean_age))
    def add_fare_per_age(df):
        return df.assign(Fare_Per_Age=df['Fare'] / df['Age'])
    result = (titanic
             .pipe(filter_survived)
             .pipe(fill_age)
             .pipe(add_fare_per_age))
    print("Titanic Pipeline Results:")
    print(result[['Age', 'Fare', 'Fare_Per_Age']].head())
    return result

def flights_pipeline():
    flights = pd.read_csv('flights.csv')
    def filter_delays(df):
        return df[df['DepDelay'] > 30]
    def add_delay_per_hour(df):
        return df.assign(Delay_Per_Hour=df['DepDelay'] / df['AirTime'])
    result = (flights
             .pipe(filter_delays)
             .pipe(add_delay_per_hour))
    print("Flights Pipeline Results:")
    print(result[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())
    return result

if __name__ == "__main__":
    chinook_inner_join()
    movie_outer_join()
    titanic_grouping()
    movie_multi_group()
    flights_nested_group()
    titanic_age_group()
    normalize_salaries()
    movie_duration_class()
    titanic_pipeline()
    flights_pipeline()