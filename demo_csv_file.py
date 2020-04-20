import csv      #imporrting the class csv

#reading csv files
"""with open("demo_csv_file.csv") as file:
    contents_of_file = csv.reader(file)
    for content in contents_of_file:
        print(content)"""

#writing csv files/ "w" flag will write , "a" flag will append
with open("demo_csv_file2.csv", "a", newline="") as file:
    file_writer = csv.writer(file)
    file_writer.writerow(["Year", "Event", "Winner"])
    file_writer.writerow(["1999", "world cup", "Abbas"])