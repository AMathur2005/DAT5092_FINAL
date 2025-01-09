import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Armed Forces Data.csv')

#---------------------------------------Line Graph ------------------------------------------------#

# List of countries for each level of development
lic_countries = ['Mozambique', 'Niger', 'Nigeria', 'Sierra Leone', 'Yemen']
mic_countries = ['Argentina', 'Brazil', 'China', 'India', 'South Africa']
hic_countries = ['Australia', 'Canada', 'Germany', 'Japan', 'United States']

COUNTRIES = data[data['Entity'].isin(lic_countries + mic_countries + hic_countries)]

#Average % of armed forces for each level of development
average_lic = COUNTRIES[COUNTRIES['Entity'].isin(lic_countries)].groupby('Year')['Armed forces personnel (% of total population) (World Bank (2017))'].mean() * 100
average_mic = COUNTRIES[COUNTRIES['Entity'].isin(mic_countries)].groupby('Year')['Armed forces personnel (% of total population) (World Bank (2017))'].mean() * 100
average_hic = COUNTRIES[COUNTRIES['Entity'].isin(hic_countries)].groupby('Year')['Armed forces personnel (% of total population) (World Bank (2017))'].mean() * 100
#multiply by 100 to show percentage from decimal 

plt.figure(figsize=(15, 10))
plt.plot(average_hic.index, average_hic.values, label='HIC', color='green')
plt.plot(average_mic.index, average_mic.values, label='MIC', color='orange')
plt.plot(average_lic.index, average_lic.values, label='LIC', color='red')
#colours for each level of development

plt.xlabel('Year')
plt.ylabel('Armed Forces Personnel as Percentage of Total Population (%)')
plt.title('Armed Forces Personnel as Percentage of Country Population by Income level')
plt.legend()
plt.grid(True)

plt.show()

#---------------------------------------Bar Graph ------------------------------------------------#

# Filter the dataset for the selected countries and the year 2015
filtered_data_2016 = data[(data['Entity'].isin(lic_countries + mic_countries + hic_countries)) & (data['Year'] == 2015)]

# Sort by armed forces in descending order to show ranking
filtered_data_2016 = filtered_data_2016.sort_values(by='Armed forces personnel (% of total population) (World Bank (2017))')

color_mapping = {
    'Mozambique': 'blue', 'Niger': 'blue', 'Nigeria': 'blue', 'Sierra Leone': 'blue', 'Yemen': 'blue',
    'Argentina': 'green', 'Brazil': 'green', 'China': 'green', 'India': 'green', 'South Africa': 'green',
    'Australia': 'red', 'Canada': 'red', 'Germany': 'red', 'Japan': 'red', 'United States': 'red'
}


