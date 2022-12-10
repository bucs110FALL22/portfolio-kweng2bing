import requests
import xml.etree.ElementTree as ET
import random
class AnimenetworkAPI():
  def __init__(self):
    '''
    Api url and location to files for reading and writing files.
    args: None
    return: None
    '''
    self.url =  "https://animenewsnetwork.p.rapidapi.com/reports.xml"
    self.file_path = f"ch09/final/animenewsnetwork.xml"
    # self.randomnum = str(random.randint(150,160))
  def getanimelistxml(self, id=155, nlist=80, nskip=1):
    '''
    Uses api url and apikey to import data from the api and writes it in the file.
    args: id, nlist, nskip(just specific info for headers and api)
    return: None
    '''
    querystring = {"id":f"{str(id)}","nlist":f"{str(nlist)}","nskip":f"{str(nskip)}"}
    apikey= "c6e6f7cadbmsh918827e2a563bbap1c89dajsnd8b44c661784"
    apihost = "animenewsnetwork.p.rapidapi.com"
    headers = {"X-RapidAPI-Key": apikey,"X-RapidAPI-Host": apihost}
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
