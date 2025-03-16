import sqlite3
import pandas as pd
import csv
import numpy as np

#1.1
with sqlite3.connect('chinook.db') as conn:
    df_customers = pd.read_sql_query("SELECT * FROM customers", conn)

df_customers.head(10)


#1.2
df_iris = pd.read_json('iris.json')
print(df_iris.shape)
print(df_iris.columns)


#1.3
df_titanic = pd.read_excel('titanic.xlsx')
df_titanic.head(5)


#1.4
df_parquet = pd.read_parquet('data')
df_parquet.info()

#1.5

df_csv = pd.read_csv('movie.csv')
df_csv.sample(10)


#2.1
df = pd.read_json('iris.json')
df.columns = df.columns.str.lower()
df_selected = df[['sepallength', 'sepalwidth']]
df_selected.head()


#2.2
df_titanic = pd.read_excel('titanic.xlsx')
over_thirty = df_titanic[df_titanic['Age'] >30]
gender_count = over_thirty['Sex'].value_counts()
gender_count

#2.3
df_parquet = pd.read_parquet('flights')
selected_columns = df_parquet[['origin', 'dest', 'carrier']]
print(selected_columns)
unique_dest = selected_columns['dest'].unique()
print(unique_dest)


#2.4

df_movie = pd.read_csv('movie.csv')
duration = df_movie[df_movie['duration'] > 120]
duration.sort_values(by=['director_facebook_likes'], ascending=False)
print(duration.head())

#3.1

#3.1
df_iris = pd.read_json('iris.json')
mean = df_iris.mean(numeric_only=True)
median = df_iris.median(numeric_only=True)
std = df_iris.std(numeric_only=True)
print(mean)
print(median)
print(std)


#3.2
df_titanic = pd.read_excel('titanic.xlsx')
max = df_titanic['Age'].max()
min = df_titanic['Age'].min()
sum = df_titanic['Age'].sum()
print(max)
print(min)
print(sum)


#3.3
df_movies = pd.read_csv('movie.csv')
director_likes = df_movies.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
longest_movies = df_movies.nlargest(5, "duration")[["movie_title", "director_name", "duration"]]

print(top_director)
print(longest_movies)

#3.4
df_flights = pd.read_parquet('flights')
print("Missing values per column:")
print(df.isnull().sum())

numerical_column = 'distance'

if numerical_column in df.columns:
    column_mean = df[numerical_column].mean()
    df[numerical_column].fillna(column_mean, inplace=True)
    print(f"\nFilled missing values in '{numerical_column}' with mean: {column_mean}")
else:
    print(f"\nColumn '{numerical_column}' not found in the dataset.")

print("\nMissing values after filling:")
print(df.isnull().sum())
