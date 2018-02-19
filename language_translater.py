import requests
from pprint import pprint

def main():
    text=input("Give your input here")
    res=requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170812T192952Z.f92c0c8f2455dc30.67ae87dc994b01e337afd446918baaef5aff3ab7&text="+text+"&lang=ru")
    trans=res.json()
    pprint(trans)
    pprint(trans['text'][0])
main()