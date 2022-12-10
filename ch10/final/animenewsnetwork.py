import requests
import xml.etree.ElementTree as ET
import random
class Animenetwork():
  def __init__(self):
    self.url =  "https://animenewsnetwork.p.rapidapi.com/reports.xml"
    self.folder_path = f"ch10/final/animenewsnetwork.xml"
    # self.randomnum = str(random.randint(150,160))
  def animelistxml(self):
    url = "https://animenewsnetwork.p.rapidapi.com/reports.xml"
    querystring = {"id":f"155","nlist":"80","nskip":"1"}
    headers = {
      "X-RapidAPI-Key": "c6e6f7cadbmsh918827e2a563bbap1c89dajsnd8b44c661784",
      "X-RapidAPI-Host": "animenewsnetwork.p.rapidapi.com"
      }
    response = requests.request("GET", self.url, headers=headers, params=querystring)
    r = requests.get(response.url)
    with open( self.folder_path, 'wb') as f:
      f.write(r.content)
  def documenttreeparse(self):
    mytree = ET.parse(self.folder_path)
    myroot = mytree.getroot()
    for x in myroot:
      test = myroot.findall('item')
      if x.find('type').text == 'manga':
        name  = x.find('name').text
        print(name)


# url = "https://animenewsnetwork.p.rapidapi.com/reports.xml"

# querystring = {"id":"155","nlist":"50","nskip":"1"}

# headers = {
# 	"X-RapidAPI-Key": "c6e6f7cadbmsh918827e2a563bbap1c89dajsnd8b44c661784",
# 	"X-RapidAPI-Host": "animenewsnetwork.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)
# r = requests.get(response.url)
# folder_path = f"ch10/final/animenewsnetwork.xml"

# with open('topnewsfeed.xml', 'wb') as f:
#   f.write(r.content)
  
# mytree = ET.parse('topnewsfeed.xml')
# myroot = mytree.getroot()
# for x in myroot:
#   test = myroot.findall('item')
  
#   if x.find('type').text == 'manga':
#     name  = x.find('name').text
#     # print(test)
#     print(name)

#   if myroot.findall('type') == 'manga':
#     name  = x.find('name').text
#     print("===")
#     print(name)