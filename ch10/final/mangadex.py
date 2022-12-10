import requests
import os

class MangadexAPI():
  def __init__(self):
    self.link = "https://api.mangadex.org"
  def mangadexid(self, title):
    # link = "https://api.mangadex.org"
    r = requests.get(f"{self.link}/manga",params={"title": title})
    rjson = r.json()['data'][0]['id']
    return rjson
  def mangachapterid(self, mangaid, languages):
    # link = "https://api.mangadex.org"
    r = requests.get(f"{self.link}/manga/{mangaid}/feed",params={"translatedLanguage[]": languages},)
    rjson = r.json()['data'][0]
    chapter_id = rjson['id']
    print(chapter_id)
    return chapter_id
  def mangachapterfile(self, chapterid= "27cd0902-ad4c-490a-b752-ae032f0503c9"):
    # link = "https://api.mangadex.org"
    r = requests.get(f"{self.link}/at-home/server/{chapterid}")
    rjson = r.json()
    host = rjson["baseUrl"]
    chapter_hash = rjson["chapter"]["hash"]
    data = rjson["chapter"]["data"]
    folder_path = f"ch10/final/Mangadex/{chapterid}"
    os.makedirs(folder_path, exist_ok=True)
    for page in data:
      r = requests.get(f"{host}/data/{chapter_hash}/{page}")
      with open(f"{folder_path}/{page}", mode="wb") as f:
        f.write(r.content)
    print(f"Downloaded {len(data)} pages.")

  