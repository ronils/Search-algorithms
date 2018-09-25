

def readData(filename):
    inFile = open(filename,'r')
    years = []
    cities = []
    countries = []
    line = inFile.readline()
    while line !="":
        line = line.strip()
        year= line[0:4]
        line = line[4: ].strip()
        city,country=line.split(",")
        years = years+[year]
        cities = cities + [city]
        countries = countries+[country]
        line = inFile.readline()

    inFile.close()
    return years, cities, countries

def findYearLinear(yearList, year):
    counter =1
    
    for i in range (len(years)):
            if  years[i]== year:
                counter = counter+1
                index=[i]
    print('Linear search took: ', counter)
    print('Linear search took: ', counter)
    return index

def findYearBinary(yearList, year):
    
    print('Binary search took: ', counter)
    return index
        
    
def findCity(year, yearList, cityList, searchMode):
    if searchMode == 'linear':
        index = findYearLinear(yearList, year)
        if index != -1:
            return cityList[index]
        else:
            return 'Year Not Found'
    elif searchMode == 'binary':
        index = findYearBinary(yearList, year)
        if index != -1:
            return cityList[index]
        else:
            return 'Year Not Found'
    else:
        return 'illegal search mode'
    
def findCountry(year, yearList, countryList, searchMode):
    return findCity(year, yearList, countryList, searchMode)

def printMenu():
    print('Select one of the following choices:')
    print('\t1- Find City - Search Using Linear Search ')
    print('\t2- Find City - Search Using Binary Search ')
    print('\t3- Find Country - Search Using Linear Search ')
    print('\t4- Find Country - Search Using Binary Search ')
    print('\t5- Exit \n')

def main():
    filename = input('Enter name of file: ')
    years, cities, countries = readData(filename)

    choice = 1
    while choice != 5:
        printMenu()
        choice = int(input())
        if choice == 5:
            print('Good Bye')
            break
        else:
            year = input('Enter a year: ')
            if choice == 1:
                city = findCity(year, years, cities, 'linear')
                print('The Olympics in ', year, ' was held in : ', city, '\n')
            elif choice == 2:
                city = findCity(year, years, cities, 'binary')
                print('The Olympics in ', year, ' was held in : ', city, '\n')
            elif choice == 3:
                country = findCountry(year, years, countries, 'linear')
                print('The Olympics in ', year, ' was held in : ', country, '\n')
            elif choice == 4:
                country = findCountry(year, years, countries, 'binary')
                print('The Olympics in ', year, ' was held in : ', country, '\n')
            else:
                print('Wrong choice! Try again.\n')
