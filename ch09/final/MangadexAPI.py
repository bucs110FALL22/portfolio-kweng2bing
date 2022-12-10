import requests
import os

class MangadexAPI():
  def __init__(self):
    '''
    Just the api url.
    args: None
    return: None
    '''
    self.link = "https://api.mangadex.org"
  def getmangadexid(self, title):
    '''
    Retrieves the id of the manga from the api  
    args: title(name of the manga)
    return: id (id for the manga)
    '''
    r = requests.get(f"{self.link}/manga",params={"title": title})
    rjson = r.json()['data'][0]['id']
    return rjson
  def getmangachapterid(self, mangaid, languages):
    '''
    Using the mangaid, this will retireve the chapter id from the api, which is just which chapter from the manga.
    args: mangaid(the id from getmangadexid), languages(just the language the chapter will be in)
    return: chapter_id(just the id fpr the chapter)
    '''
    r = requests.get(f"{self.link}/manga/{mangaid}/feed",params={"translatedLanguage[]": languages},)
    rjson = r.json()['data'][0]
    chapter_id = rjson['id']
    print(f"Chapter id:{chapter_id}. Look for chapter id in Mangadex")
    return chapter_id
  def getmangachapterfile(self, chapterid):
    '''
    Using the chapter id, this will retireve each png from the api for the chapter and add it to Mangadex with the title of the folder being the chapter id.
    args: chapterid(just the id from getmangachapterid)
    return: none
    '''
    r = requests.get(f"{self.link}/at-home/server/{chapterid}")
    rjson = r.json()
    host = rjson["baseUrl"]
    chapter_hash = rjson["chapter"]["hash"]
    data = rjson["chapter"]["data"]
    folder_path = f"ch09/final/Mangadex/{chapterid}"
    os.makedirs(folder_path, exist_ok=True)
    for page in data:
      r = requests.get(f"{host}/data/{chapter_hash}/{page}")
      with open(f"{folder_path}/{page}", mode="wb") as f:
        f.write(r.content)
    print(f"Downloaded {len(data)} pages.")

  