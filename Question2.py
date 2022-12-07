import requests
from bs4 import BeautifulSoup
import  re

url = 'https://ful.io/'
regex_for_facebook = r"(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
regex_for_ln = r"(?:(?:http|https):\/\/)?(?:www.)?linkedin.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
regex_for_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_for_PNo = r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}"

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
        if re.match(regex_for_facebook,link.get("href")) is not None :
                print("Social links -")
                print(link.get("href"))

        if re.match(regex_for_ln,link.get("href")) is not None :
                print(link.get("href"))

        if re.findall(regex_for_PNo,link.get("href")) != []:
                print("Contact:\n" , link.get("href").split(":")[1])

        if re.findall(regex_for_mail,link.get("href")) != []:
                print("Email/s-\n",link.get("href").split(":")[1])


