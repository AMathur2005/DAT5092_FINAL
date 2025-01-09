import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Armed Forces Data.csv')



# List of countries for each level of development
lic_countries = ['Mozambique', 'Niger', 'Nigeria', 'Sierra Leone', 'Yemen']
mic_countries = ['Argentina', 'Brazil', 'China', 'India', 'South Africa']
hic_countries = ['Australia', 'Canada', 'Germany', 'Japan', 'United States']

#---------------------------------------Line Graph ------------------------------------------------#
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
Countries_2015 = data[(data['Entity'].isin(lic_countries + mic_countries + hic_countries)) & (data['Year'] == 2015)]

# Sort by armed forces in descending order to show ranking
Countries_2015 = Countries_2015.sort_values(by='Armed forces personnel (% of total population) (World Bank (2017))')

color_mapping = { #assigning colours to designate countries income
    'Mozambique': 'Red', 'Niger': 'Red', 'Nigeria': 'Red', 'Sierra Leone': 'Red', 'Yemen': 'Red',
    'Argentina': 'Orange', 'Brazil': 'Orange', 'China': 'Orange', 'India': 'Orange', 'South Africa': 'Orange',
    'Australia': 'Green', 'Canada': 'Green', 'Germany': 'Green', 'Japan': 'Green', 'United States': 'Green'
}

colors = Countries_2015['Entity'].map(color_mapping) 

#the bar chart
plt.figure(figsize=(15, 8))
plt.barh(Countries_2015['Entity'], Countries_2015['Armed forces personnel (% of total population) (World Bank (2017))'] * 100, color=colors)  #show as percentage

# Adding labels and title
plt.xlabel('Armed Forces Personnel (% of Total Population)')
plt.ylabel('Country')
plt.title('Proportion of Armed Personnel from Total Population by Country in 2015')
plt.grid(True, linestyle='--', linewidth=0.5)

#custom legend to show bars and colour
plt.legend(handles=[plt.Rectangle((0,0),1,1, color='Green', label='HIC'),
                    plt.Rectangle((0,0),1,1, color='Orange', label='MIC'),
                    plt.Rectangle((0,0),1,1, color='Red', label='LIC')],
           title='Level of Economic development')

plt.show()

#---------------------------------------Box Plot ------------------------------------------------#
# Categorise countriies by development
def categorise(entity):
    if entity in lic_countries:
        return 'LIC'
    elif entity in mic_countries:
        return 'MIC'
    elif entity in hic_countries:
        return 'HIC'

#  function to create a new column for income categories
COUNTRIES['Income Category'] = COUNTRIES['Entity'].apply(categorise)

# Plotting the box plots
plt.figure(figsize=(12, 8))
COUNTRIES.boxplot(
    column='Armed forces personnel (% of total population) (World Bank (2017))',
    by='Income Category',
    grid=True
)

plt.xlabel('Income Category')
plt.ylabel('Armed Forces Personnel (% of Total Population)')
plt.title('Armed Forces Personnel by Income Category (1960 - 2015)')
plt.grid(True)
plt.suptitle('')  # remove unwanted title addition

plt.show()



