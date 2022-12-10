from MangadexAPI import MangadexAPI
from AnimenewsnetworkAPI import AnimenetworkAPI

def main():
    api_two = AnimenetworkAPI()
    api_two.getanimelistxml()
    api_two.documenttreeparse()
    api_one = MangadexAPI()
    manga_name = input("Type the Name of a manga. Some may not work so I suggest  you to try a few.")
    manga_id = api_one.getmangadexid(manga_name)
    manga_chapterid = api_one.getmangachapterid(manga_id, ["en"])
    api_one.getmangachapterfile(manga_chapterid)

main()

