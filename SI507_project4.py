import SCRAPING_SI507_project4
import csv

## confirmed import works
# print(SCRAPING_SI507_project4.topics_pages[0].prettify())
# print(SCRAPING_SI507_project4.soup.prettify())
# print(SCRAPING_SI507_project4.soup.find_all("a"))

# for i in SCRAPING_SI507_project4.topics_pages:
#     for e in i:
#         state = i.find('h1')
#         # location = i.find('h4')
#         print(state.string)
        # print(location.string)

    # for e in i.find('h1'):
    #     state = e.string
    #     print(e.string)
    # raw = i.find('h1')
    # print(raw.string)  ## prints out states

agg_park_data = []

for p in SCRAPING_SI507_project4.topics_pages:
    parks = p.find(id = 'list_parks')
    park_name = parks.find_all("li", class_ = "clearfix")

    for n in park_name:
        park_data = []
        ## name
        if n.find('h3') is None:
            new = e.replace_with('Not Applicable')
            park_data.append(new)
        else:
            park_data.append(n.find('h3').string)

        ## location
        if n.find('h4') is None:
            new = e.replace_with('Not Applicable')
            park_data.append(new)
        else:
            new = n.find('h4')
            park_data.append(new.string)

        ##type
        if n.find('h2') is None:
            new = e.replace_with('Not Applicable')
            park_data.append(new)
        else:
            new = n.find('h2')
            park_data.append(new.string)

        ##description
        if n.find('p') is None:
            new = e.replace_with('Not Applicable')
            park_data.append(new)
        else:
            # string = n.get_text('p')
            string = park_data.append(n.find('p').get_text(strip = True))
            park_data.append(string)


        agg_park_data.append(park_data)



# print(agg_park_data[5])



## export to csv

# newfile = open('nps_export.csv','w')
# newfile.write("'Park Name, 'Location, 'Park Type, 'Description")
# newfile.write('\n')
#
# for i in agg_park_data:
#     row_string = '"{}","{}","{}","{}"'.format(i[0],i[1],i[2],i[3])
#     newfile.write(row_string)
#     newfile.write('\n')
#
# newfile.close()


header = ['Park Name', 'Location', 'Park Type', 'Description']

with open('nps_export.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in agg_park_data:
        writer.writerow(i)


## states
# for i in SCRAPING_SI507_project4.topics_pages[0].find_all('h1'):
#     print(i.string)

# ## location
# location_list = []
# for i in SCRAPING_SI507_project4.topics_pages:
#     raw_loc = i.find_all('h4')[1:]
#     for e in raw_loc:
#         location_list.append(e.string)
# print(len(location_list))
#
# # for i in SCRAPING_SI507_project4.topics_pages[0].find_all('h4')[1:]:
# #     raw_loc = i.find('h4')[1:]
# #
# #     print(raw.string)
#
# ## name
# # for i in SCRAPING_SI507_project4.topics_pages[0].find_all('h3'):
# #     print(i.string)
#
# name_list = []
# for i in SCRAPING_SI507_project4.topics_pages:
#     raw_name = i.find_all('h3')
#     # for e in raw_name:
#     #     name_list.append(e.string)
#     for e in raw_name:
#         temp_list = []
#         temp = temp_list.append(e.string)
#         name_list.append(temp)
# print(len(name_list))
#
# ## type
# # for i in SCRAPING_SI507_project4.topics_pages[0].find_all('h2')[:-2]:
# #     print(i.string)
# # print('last one')
#
# type_list = []
# for i in SCRAPING_SI507_project4.topics_pages:
#     raw_type = i.find_all('h2')[:-2]
#     for e in raw_type:
#         if e is None:
#             new = e.replace_with('Not Applicable')
#             type_list.append(new)
#         else:
#             type_list.append(e.string)
# # print(type_list)
# print(len(type_list))
#
# ## description
# # for i in SCRAPING_SI507_project4.topics_pages[0].find_all('p'):
# #     print(i.string)
#
# des_list = []
# for i in SCRAPING_SI507_project4.topics_pages:
#     raw_des = i.find_all('p')
#     for e in raw_des:
#         if e is None:
#             new = e.replace_with('Not Applicable')
#             des_list.append(new)
#         else:
#             string = e.get_text(strip = True)
#             des_list.append(string)
# print(des_list)
# print(len(des_list))






# location = SCRAPING_SI507_project4.topics_pages[0].find_all('h4') ## has some front stuff
# name = SCRAPING_SI507_project4.topics_pages[0].find_all('h3') ## this needs to go deeper into the href
# type = SCRAPING_SI507_project4.topics_pages[0].find_all('h2') ## need to cut off front and end stuff
# description = SCRAPING_SI507_project4.topics_pages.find_all('p')

# print(location1)
# print(name)
# print(name0)
# print(name1)
# print(name2)
# print(name3)
# print(type)
# print(description)
