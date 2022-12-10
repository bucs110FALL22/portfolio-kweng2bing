# CS110 Final Exam

## SHORT DESCRIPTION *(1 or 2 sentences describing your program)*
One of the api generates a list of possible mangas to read. Thsi gives user some perferance in what to read. The other api downloads the images of a specific chapter of the manga into the folder called 'Mangadex'. Note: The chapter downloaded is a little random.
## KNOWN BUGS AND INCOMPLETE PARTS *(list any known bugs or non-working parts)*
<p>I notice that that api_one doesn't work super well with popular mangas. You can try a few but there should be some that work. I know it doesn't work for: One Piece, Naruto, Bleach, Jujutsu Kaisen, Spy X Family.</p>
If it doesn't work it will say something like
"
File "ch10/final/main.py", line 17, in <module>
    main()
  File "ch10/final/main.py", line 15, in main
    api_one.mangachapterfile(manga_chapterid)
  File "/home/runner/portfolio-kweng2bing/ch10/final/mangadexAPI.py", line 23, in mangachapterfile
    host = rjson["baseUrl"]
KeyError: 'baseUrl'
"
The best option is just to run it again and type something else. I don't have the time to make it so that it let's you type again.
  
<p>Listing a few that I tested and it worked( Death Note, Code Geass, Boruto) I am not confident that all the manga from api_two works for api_one. There are some that does work (ex. Darwin Incidient, Origin)</p>

## REFERENCES *(any resources you use outside of class materials)*
https://docs.python.org/3/library/xml.etree.elementtree.html

https://www.edureka.co/blog/python-xml-parser-tutorial/#:~:text=Python%20allows%20parsing%20these%20XML,of%20that%20particular%20XML%20file.

https://www.cleancss.com/python-beautify/

https://api.mangadex.org/docs/guide/find-manga/

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)*
<p>Sorry about the fact that some of the manga doesn't work. I just don't have time to investigate why it doesn't work and fix it.</p>
<p>I added a few extra words after get just to help distingusih which api is which. Hope that is fine.</p>
