
import csv
import random
import matplotlib.pyplot as plt


filename1 = "world_bank_gdp.csv"
filename2 = "world_bank_tariff.csv"


gdps = []
tariffs = []


with open(filename1, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        gdps.append(row)

with open(filename2, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    for row in csvreader:
        tariffs.append(row)

all_datas = []

for row in gdps:
    idx = gdps.index(row)
    if (row[2] and tariffs[idx][2] and row[2]):
        all_datas.append([row[1], float(row[2]), float(tariffs[idx][2])])

country_to_display = []

for i in range(0, 10):
    country_to_display.append(all_datas[random.randint(0, len(all_datas))])

gdps_plot = []
tariffs_plot = []

for country in country_to_display:
    print(country)
    print('\n')
    gdps_plot.append(country[1])
    tariffs_plot.append(country[2])

plt.scatter(gdps_plot, tariffs_plot, label="stars", color="green",
            marker="*", s=30)


plt.xlabel('GDP')

plt.ylabel('Tariffs')

plt.title('GDP - Tariff / 10 random countries')

plt.legend()

plt.show()
