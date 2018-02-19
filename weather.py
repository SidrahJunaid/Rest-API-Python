import requests
from pprint import pprint

def main():
    city = input('Enter city: ')
    print('Hello', city)
    res=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1f44424256fc87747b9c2e216b250803&units=metric")
    #fetch response in json
    weather=res.json()
    pprint(weather)
    pprint(weather['coord']['lat'])
    pprint(weather['weather'][0]['icon'])



if __name__=='__main__':
    main()
