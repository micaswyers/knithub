import csv

def reverse_chart():
    with open('reverse_me.csv', 'rb') as csvfile:
        chart_reader = csv.reader(csvfile)
        for row in chart_reader:
            print row[::-1]

reverse_chart()

