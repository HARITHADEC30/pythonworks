years_path=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\years.txt","r")
century_path=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\century_year.txt","w")
leap_path=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\leap_year.txt","w")

def is_century_year(years):

    return True if year%100==00 else false

def is_leap_year(years):
    if year%100==0 and  year%4==0 or year%100!=0 and year%4==0:
        return true 
    else:
        return False
    
for year in years_path:
    year=int(year)
    
    if year%100==0:
        
        century_path.write(str(year)+"\n")

    if year%100==0 and  year%4==0 or year%100!=0 and year%4==0:
        leap_path.write(str(year)+"\n")



years_path.close()
century_path.close()
leap_path.close()



