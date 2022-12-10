from mangadex import MangadexAPI
from animenewsnetwork import Animenetwork
import requests
import os
# import mangadexapi

def main():
    api_two = Animenetwork()
    api_two.animelistxml()
    api_two.documenttreeparse()
    api_one = MangadexAPI()
    manga_name = input("Type the Name of a manga. Some may not work so I suggest  you to try a few.")
    manga_id = api_one.mangadexid(manga_name)
    manga_chapterid = api_one.mangachapterid(manga_id, ["en"])
    api_one.mangachapterfile(manga_chapterid)

main()

