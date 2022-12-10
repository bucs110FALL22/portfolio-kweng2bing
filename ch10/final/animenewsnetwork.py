import requests
import xml.etree.ElementTree as ET
import random
class Animenetwork():
  def __init__(self):
    '''
    Api url and location to files for reading and writing files.
    args: None
    return: None
    '''
    self.url =  "https://animenewsnetwork.p.rapidapi.com/reports.xml"
    self.file_path = f"ch10/final/animenewsnetwork.xml"
    # self.randomnum = str(random.randint(150,160))
  def getanimelistxml(self):
    '''
    Uses api url and apikey to import data from the api and writes it in the file. Apikey is  fixed so hardcoded.
    args: None
    return: None
    '''
    querystring = {"id":f"155","nlist":"80","nskip":"1"}
    headers = {
      "X-RapidAPI-Key": "c6e6f7cadbmsh918827e2a563bbap1c89dajsnd8b44c661784",
      "X-RapidAPI-Host": "animenewsnetwork.p.rapidapi.com"
      }
    response = requests.request("GET", self.url, headers=headers, params=querystring)
    r = requests.get(response.url)
    with open( self.file_path, 'wb') as f:
      f.write(r.content)
  def documenttreeparse(self):
    '''
    Parse through the file created from the previous api and only prints those that have the type 'manga'
    args: None
    return: None
    '''
    mytree = ET.parse(self.file_path)
    myroot = mytree.getroot()
    for x in myroot:
      test = myroot.findall('item')
      if x.find('type').text == 'manga':
        name  = x.find('name').text
        print(name)
