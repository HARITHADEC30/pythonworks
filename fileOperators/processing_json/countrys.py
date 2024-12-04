from json import load

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\countrys.json",encoding="utf-8")

data=load(f)

#print numer of countries 
#print(len(data))

all_country_name=[country.get("name") for country in data]

#print(all_country_name)

#print all regions

all_regions=[country.get("region")for country in data]
#print(set(all_regions))

region_count={region:all_regions.count(region) for region in all_regions}
#print(region_count)

#maximum region count

max_region_count=max(region_count,key=lambda k:region_count.get(k))
#print(max_region_count,region_count.get(max_region_count))

#capital of a specific country
country_capital=[country.get("capital")for country in data if country.get("name")=="India"]
#print(country_capital)


#capital of a specific country
# country_cap=input("enter country")
# country_capital=[country.get("capital")for country in data if country.get("name")==country_cap]
#print(country_capital)

#countries with most numer of borders

country_boarder_count={country.get("name"):len(country.get("borders",[])) for country in data}
#print(country_boarder_count)
 
max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
#print(max_border_country)

#most population country

max_population_country=max(data,key=lambda country:country.get("population",0)).get("name")
#print(max_border_country)

alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="India"][0]
print(alpha_three_codes)
for code in alpha_three_codes:
    for country in data:
        if country.get("alpha3Code")==code:
            print(country.get("name"))


            