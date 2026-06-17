highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print("\n")
print(highlighted_poems_list)  #makes a element for a list at each comma

highlighted_poems_stripped = []
for poem_info in highlighted_poems_list:
  highlighted_poems_stripped.append(poem_info.strip())
print("\n")
print(highlighted_poems_stripped)    #strips all the whitespace for each element

highlighted_poems_details = []
for info in highlighted_poems_stripped:
  highlighted_poems_details.append(info.split(":"))
print("\n")
print(highlighted_poems_details)  #splits at colon making them separate elements

titles = []
poets = []
dates = []
for item, item1, item2 in highlighted_poems_details:
  titles.append(item)
  poets.append(item1)
  dates.append(item2)
print("\n")
print(titles)
print("\n")                   #makes separate lists for each type of info as seen here
print(poets)
print("\n")
print(dates)
print("\n")      

for poem, poet, date in highlighted_poems_details:
  print("The poem {} was published by {} in {}.".format(poem, poet, date))   #this prints a string for every 1 poem, title and poet there is 