import csv
import sqlite3

con = sqlite3.connect('myapi.db')
cursor = con.cursor()

with open('data/User_profile.csv', 'r', encoding="utf-8-sig") as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        cursor.execute('INSERT INTO User_Profile (User_id, name, sex, age) VALUES (?, ?, ?, ?)', (int(row[0]), row[1], row[2], int(row[3])))


con.commit()
con.close()
