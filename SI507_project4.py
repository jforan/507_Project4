import SCRAPING_SI507_project4
import csv

## confirmed import works
# print(SCRAPING_SI507_project4.topics_pages[0].prettify())
# print(SCRAPING_SI507_project4.soup.prettify())
# print(SCRAPING_SI507_project4.soup.find_all("a"))

agg_park_data = []

for p in SCRAPING_SI507_project4.topics_pages:
    parks = p.find(id = 'list_parks')
    park_name = parks.find_all("li", class_ = "clearfix")

    for n in park_name:
        park_data = []
        ## name
        if n.find('h3') is None:
            new = n.replace_with('Not Applicable')
            park_data.append(new)
        else:
            park_data.append(n.find('h3').string)

        ## location
        if n.find('h4') is None:
            new = n.replace_with('Not Applicable')
            park_data.append(new)
        else:
            new = n.find('h4')
            park_data.append(new.string)

        ##type
        if n.find('h2') is None:
            new = 'Not Applicable'
            park_data.append(new)
        else:
            new = n.find('h2')
            park_data.append(new.string)

        ##description
        if n.find('p') is None:
            new = n.replace_with('Not Applicable')
            park_data.append(new)
        else:
            # string = n.get_text('p')
            string = park_data.append(n.find('p').get_text(strip = True))
            park_data.append(string)


        agg_park_data.append(park_data)

# print(agg_park_data[5])



## export to csv

header = ['Park Name', 'Location', 'Park Type', 'Description']

with open('nps_export.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in agg_park_data:
        writer.writerow(i)
