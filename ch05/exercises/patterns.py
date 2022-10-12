def star_pyramid():
    rows = int(input("How many rows of stars do you want?"))
    for i in range(rows):
        i += 1
        star = "*"
        print(star * i)


star_pyramid()


def rstar_pyramid():
    row = int(input("How many rows of star do you want?"))
    for i in range(row):
        star = "*"
        print(star * row)
        row -= 1


rstar_pyramid()
