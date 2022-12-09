import requests
import os

def main():
    # mangadexapi("One Piece")
    manga_id = mangadexid("One Piece")
    manga_chapterid = mangachapterid(manga_id, ["en"])
    print("+++++++++++")
    print(manga_chapterid)
    # mangachapterfile(manga_chapterid)
    mangachapterfile()

# def mangadexapi(title):
#     link = "https://api.mangadex.org"
#     r = requests.get(f"{link}/manga",params={"title": title})
#     rjson = r.json()['data'][0]
#     manga_id = rjson['id']
#     manga_description = rjson['attributes']['description']['en']
#     manga =0 
def mangadexid(title):
    link = "https://api.mangadex.org"
    r = requests.get(f"{link}/manga",params={"title": title})
    rjson = r.json()['data'][0]['id']
    # print(rjson)
    return rjson
def mangachapterid(mangaid, languages):
    link = "https://api.mangadex.org"
    r = requests.get(f"{link}/manga/{mangaid}/feed",params={"translatedLanguage[]": languages},)
    rjson = r.json()['data'][0]
    chapter_id = rjson['id']
    print(chapter_id)
    return chapter_id
    # print(rjson)
    # print([chapter["id"] for chapter in r.json()["data"]])/
def mangachapterfile(chapterid= "27cd0902-ad4c-490a-b752-ae032f0503c9"):
    link = "https://api.mangadex.org"
    r = requests.get(f"{link}/at-home/server/{chapterid}")
    rjson = r.json()
    # print(rjson)
    host = rjson["baseUrl"]
    chapter_hash = rjson["chapter"]["hash"]
    data = rjson["chapter"]["data"]
    # data_saver = rjson["chapter"]["dataSaver"]
    host = rjson
    folder_path = f"Mangadex/{chapterid}"
    os.makedirs(folder_path, exist_ok=True)
    for page in data:
        r = requests.get(f"{host}/data/{chapter_hash}/{page}")
        with open(f"{folder_path}/{page}", mode="wb") as f:
            f.write(r.content)
    print(f"Downloaded {len(data)} pages.")


main()

