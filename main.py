
import pandas as pd
import matplotlib.pyplot as plt

# laod data
df=pd.read_csv('D:/EDA internship/births.csv')
df["Decade"]=(df['year']//10)*10
print(df)
# Q.2: Show the descriptive statistics of the data.
print(df.describe())
# .3: Check if your data contains any missing values
null_counts=df.isnull().sum()
print(null_counts)
# Q.4: What is the trend of male & female births every decade?
births_by_decade_gender=df.groupby(['Decade','gender'])['births'].sum()
trend=births_by_decade_gender.unstack()
# Plot the trend
trend.plot(kind='bar', stacked=True, figsize=(10, 6), title='Trend of Male & Female Births Every Decade')
plt.xlabel('Decade')
plt.ylabel('Total Births')
plt.xticks(rotation=45)
plt.show()
# calcute the mean
mean=df['births'].mean()
std=df['births'].std()
# Define lower and upper bounds
lower_bounds=mean-5*std
upper_bound=mean+5*std

# original data
print(df)
# filtering data
filter_df = df[(df['births'] >= lower_bounds) & (df['births'] <= upper_bound)]
print(filter_df)
# Convert to datetime
df['date'] = pd.to_datetime(df['year'] * 10000 + df['month'] * 100 + df['day'], format='%Y%m%d', errors='coerce')

# Extract weekday
df['weekday'] = df['date'].dt.weekday

print(df[['date', 'weekday']])
# Group by weekday and sum the births for each weekday
births_by_weekday = df.groupby('weekday')['births'].sum()

# Plot births by weekday for each decade
births_by_weekday.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Weekday (0=Monday, 6=Sunday)')
plt.ylabel('Total Births')
plt.title('Births by Weekday for Several Decades')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Q.7: Group the data by month and day separately
group_by_month=df.groupby('month')['births'].sum()
# group by day
group_by_day=df.groupby('day')['births'].sum()

print(group_by_month)

print(group_by_day)


# Group the data by month and day, and calculate the average births for each date
daily_births_avg = df.groupby(['month', 'day'])['births'].mean()

# Reset the index to access month and day as columns
daily_births_avg = daily_births_avg.reset_index()

# Group the data by month and day, and calculate the average births for each date
daily_births_avg = df.groupby(['month', 'day'])['births'].mean()

# Reset the index to access month and day as columns
daily_births_avg = daily_births_avg.reset_index()

# Create a string column representing the date in 'YYYY-MM-DD' format
daily_births_avg['date_str'] = df['year'].astype(str) + '-' + daily_births_avg['month'].astype(str).str.zfill(2) + '-' + daily_births_avg['day'].astype(str).str.zfill(2)

# Convert the string column to datetime
daily_births_avg['date'] = pd.to_datetime(daily_births_avg['date_str'], errors='coerce')

# Drop rows where conversion failed
daily_births_avg.dropna(subset=['date'], inplace=True)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(daily_births_avg['date'], daily_births_avg['births'], marker='o', linestyle='-')
plt.title('Average Number of Births by Date of the Year')
plt.xlabel('Date')
plt.ylabel('Average Number of Births')
plt.grid(True)
plt.tight_layout()
plt.show()