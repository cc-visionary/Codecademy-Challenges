import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
#print(wood.info())
#print(steel.info())

lowercase = lambda x: x.lower()

# write function to plot rankings over time for 1 roller coaster here:
def rank_1(data, roller_coaster, park_name):
    to_plot = data[(data['Name'].apply(lowercase) == lowercase(roller_coaster)) & (data['Park'].apply(lowercase) == lowercase(park_name))]
    rankPlot = plt.subplot()
    rankPlot.set_yticks(range(50))
    plt.plot(to_plot['Year of Rank'], to_plot['Rank'])
    plt.xlabel('Year of Ranking')
    plt.ylabel('Rank')
    plt.title('Rank of ' + roller_coaster + ' from the ' + park_name)
    plt.gca().invert_yaxis()
    plt.show()
#roller_coaster = wood.loc[2, 'Name']
#park_name = wood.loc[2, 'Park']
#rank_1(wood, roller_coaster, park_name)

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def rank_2(data, n1, p1, n2, p2):
    to_plot_1 = data[(data['Name'].apply(lowercase) == lowercase(n1)) & (data['Park'].apply(lowercase) == lowercase(p1))]
    to_plot_2 =data[(data['Name'].apply(lowercase) == lowercase(n2)) & (data['Park'].apply(lowercase) == lowercase(p2))]
    rankPlot = plt.subplot()
    rankPlot.set_yticks(range(50))
    plt.plot(to_plot_1['Year of Rank'], to_plot_1['Rank'])
    plt.plot(to_plot_2['Year of Rank'], to_plot_2['Rank'])
    plt.xlabel('Year of Ranking')
    plt.ylabel('Rank')
    plt.legend([n1 + ' from ' + p1, n2 + ' from ' + p2])
    plt.title('Ranking of Roller Coasters vs Year')
    plt.gca().invert_yaxis()
    plt.show()
#r1 = steel.loc[0, 'Name']
#p1 = steel.loc[0, 'Park']
#r2 = steel.loc[3, 'Name']
#p2 = steel.loc[3, 'Park']
#rank_2(steel, r1, p1, r2, p2)

plt.clf()

# write function to plot top n rankings over time here:
def rank_top_n(data, n):
    legends = []
    fig = plt.figure(figsize=(25, 10))
    for i in range(0, n):
        name = data.loc[i, 'Name']
        park = data.loc[i, 'Park']
        legends.append(name + ' from ' + park)
        to_plot = data[(data['Name'].apply(lowercase) == lowercase(name)) & (data['Park'].apply(lowercase) == lowercase(park))]
        plt.plot(to_plot['Year of Rank'], to_plot['Rank'])
    plt.legend(legends)
    plt.title('Top ' + str(n) + ' Ranking of Roller Coasters vs Year')
    plt.xlabel('Year of Ranking')
    plt.ylabel('Rank')
    plt.gca().invert_yaxis()
    plt.savefig('top_' + str(n) + '_rankings.png')
    plt.show()

#rank_top_n(steel, 10)
#rank_top_n(wood, 5)
plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv('roller_coasters.csv')

# write function to plot histogram of column values here:
def hist_numeric(data, column):
    fig = plt.figure(figsize=(10, 5))
    plt.hist(data[column].dropna(), bins = 50)
    plt.title(column.capitalize() + ' Histogram')
    plt.ylabel(column.capitalize())
    plt.xlabel('Roller Coaster')
    plt.savefig(column + '_histogram.png')
    plt.show()
#hist_numeric(roller_coasters, 'speed')
#hist_numeric(roller_coasters, 'height')
#hist_numeric(roller_coasters, 'length')

plt.clf()

# write function to plot inversions by coaster at a park here:
def num_inversion(data, park):
    fig = plt.figure(figsize=(10, 5))
    ax = plt.subplot()
    inversion = data[data['park'] == park]
    inversion = inversion.sort_values(by='num_inversions', ascending=False)
    names = inversion['name']
    plt.bar(range(len(inversion)), inversion['num_inversions'])
    plt.title('Number of Inversions per Roller Coaster at ' + park)
    ax.set_xticks(range(len(inversion)))
    ax.set_xticklabels(names, rotation=-90)
    plt.ylabel('Num of Inversions')
    plt.xlabel('Roller Coaster')
    plt.savefig('inversion_at_' + '_'.join(park.lower().split(' ')) + '.png')
    plt.show()
    
num_inversion(roller_coasters, 'Parc Asterix')
num_inversion(roller_coasters, 'Bobbejaanland')
num_inversion(roller_coasters, 'Six Flags Great Adventure')
plt.clf()

# write function to plot pie chart of operating status here:
def pie_operating_status(data):
    fig = plt.figure(figsize=(20, 10))
    statuses = roller_coasters.groupby('status').name.count().reset_index()
    plt.pie(statuses['name'], autopct='%.1f%%')
    plt.legend(statuses['status'].unique())
    plt.axis('equal')
    plt.title('Status Percentage of All Roller Coasters')
    plt.savefig('status_percentage.png')
    plt.show()

#pie_operating_status(roller_coasters)

#)
plt.clf()

# write function to create scatter plot of any two numeric columns here:
def scatter_two(data, col1, col2):
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(data[col1], data[col2])
    plt.xlabel(col1.capitalize())
    plt.ylabel(col2.capitalize())
    plt.title(col1.capitalize() + ' vs. ' + col2.capitalize())
    plt.savefig(col1 + '_vs_' + col2 + '.png')
    plt.show()
    
#scatter_two(roller_coasters, 'height', 'speed')
#scatter_two(roller_coasters, 'speed', 'num_inversions')
#scatter_two(roller_coasters,  'num_inversions', 'speed')
#scatter_two(roller_coasters,  'num_inversions', 'length')
    
plt.clf()
