import re
import psycopg2
from collections import Counter
from functools import reduce
import statistics


# Get content of HMTL file
with open("python_class_question.html") as f:
    html_content = f.read()

# Extract colors from HTML
matches = re.findall(r'<td>([A-Z,\s]+)</td>', html_content)
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
for item in matches:
    if item in weekdays:
        matches.remove(item)

all_colors = sorted(', '.join(matches).split(', '))

# Get median color
total = len(all_colors)
median_color = all_colors[total//2]

# Store colors by frequency in dictionary
colors = {}
for color in all_colors:
    if color not in colors:
        colors[color] = 0
    colors[color] += 1

# sort colors by frequency in descending order
sorted_colors = dict(sorted(colors.items(), key=lambda x:x[1]))

# Most worn color
most_worn = list(sorted_colors.keys())[-1]


# Probability of randomly choosing 'RED'
probability = sorted_colors.get('RED')/total


# Mean color and color statistics variance
color_data = list(sorted_colors.values())

mean = sum(color_data) / len(color_data)

mean_color = list(sorted_colors.keys())[int(mean)]
variance = sum((x - mean) ** 2 for x in color_data) / len(color_data)

# Connecting to database
conn = psycopg2.connect(
    database='bincom',
    user='bincom_dev',
    password='dev_1234',
    host='localhost'
)
cursor = conn.cursor()

# Save colors and their frequencies in postgres data base
# Create table to store data
cursor.execute("CREATE TABLE IF NOT EXISTS color_frequency (color VARCHAR(255) PRIMARY KEY,frequency INT)")

# Insert color and frequencies for sorted dict
# for key, val in sorted_colors.items():
#     cursor.execute("""INSERT INTO color_frequency (color, frequency) VALUES (%s, %s)""", (key, val))


# Commit changes and close connection
conn.commit()
cursor.close()
conn.close


print(f"Mean color: {mean_color}")
print(f"Most worn color: {most_worn}")
print(f"Median color: {median_color}")
print(f"Variance of color statistice: {variance}")
print(f"Probability of RED choosen at random: {probability} of {probability*100}%")
print("Colors and frequencies saved in database.")
