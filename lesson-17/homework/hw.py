import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
merged = pd.merge(customers, invoices, on='CustomerId', how='inner')
invoice_counts = merged.groupby('CustomerId').size().reset_index(name='TotalInvoices')
print(invoice_counts)

movies = pd.read_csv('movie.csv')
df1 = movies[['director_name', 'color']]
df2 = movies[['director_name', 'num_critic_for_reviews']]
left_join = pd.merge(df1, df2, on='director_name', how='left')
left_rows = left_join.shape[0]
print(f"Left join rows: {left_rows}")
outer_join = pd.merge(df1, df2, on='director_name', how='outer')
outer_rows = outer_join.shape[0]
print(f"Full outer join rows: {outer_rows}")

titanic = pd.read_csv('titanic.csv')
result = titanic.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'sum', 'Pclass': 'count'}).rename(columns={'Pclass': 'PassengerCount'})
print(result)

movie_groups = movies.groupby(['color', 'director_name']).agg({'num_critic_for_reviews': 'sum', 'duration': 'mean'}).reset_index()
print(movie_groups)

flights = pd.read_csv('flights.csv')
flight_stats = flights.groupby(['Year', 'Month']).agg({'Year': 'count', 'ArrDelay': 'mean', 'DepDelay': 'max'}).rename(columns={'Year': 'TotalFlights'})
print(flight_stats)

def classify_age(age):
    if pd.isna(age):
        return 'Unknown'
    return 'Child' if age < 18 else 'Adult'
titanic['Age_Group'] = titanic['Age'].apply(classify_age)
print(titanic[['Age', 'Age_Group']].head())

employees = pd.read_csv('employee.csv')
employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
print(employees.head())

def classify_duration(duration):
    if pd.isna(duration):
        return 'Unknown'
    elif duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'
movies['Length_Category'] = movies['duration'].apply(classify_duration)
print(movies[['duration', 'Length_Category']].head())

def pipeline(df):
    return (df
            .query('Survived == 1')
            .assign(Age=lambda x: x['Age'].fillna(x['Age'].mean()))
            .assign(Fare_Per_Age=lambda x: x['Fare'] / x['Age']))
result = pipeline(titanic)
print(result[['Age', 'Fare', 'Fare_Per_Age']].head())

def flight_pipeline(df):
    return (df
            .query('DepDelay > 30')
            .assign(Delay_Per_Hour=lambda x: x['DepDelay'] / x['Duration']))
delayed_flights = flight_pipeline(flights)
print(delayed_flights.head())