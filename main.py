
import sys


def get_num():
    try:
        num = int(input('Top _ albums '))
    except ValueError:
        print('Please enter an integer')
        get_num()
    else:
        return num


def get_info():
    return tuple(list(map(str.strip, input("Please type the name of the album and the artist in that order "
                                           "separated by a comma. ex: Amnesiac, Radiohead \n").title().split(','))))
    # improper input testing is in add(), the only place this is called.


def menu(alist, num):
    action = input('Type V to view your list, A to add an album, D to delete and album, Q to quit ')
    if action.lower() == 'q':
        print("You've quit the programme.")
        sys.exit()
    elif action.lower() == 'v':
        view(alist, num)
    elif action.lower() == 'a':
        add(alist, num)
    elif action.lower() == 'd':
        delete(alist, num)
    else:
        print("Sorry, didn't catch that.")


def add(alist, num):
    if len(alist) < num:
        try:
            info = get_info()
            print("{} by {} album was added".format(info[0], info[1]))
        except IndexError:
            print('You gotta put in an album and an artist separated by a comma.')
            add(alist, num)
        else:
            alist.append(info)
    else:
        del_q = input("You already have {} albums! Do you want to remove one to make "
                      "room for this one? y/n ".format(str(num)))
        if del_q.lower() == 'y':
            delete(alist, num)


def view(alist, num):
    print("Top {} Albums".format(str(num)))
    alist.sort()
    for tup in alist:
        print("{}) {} by {}".format((alist.index(tup)+1), tup[0], tup[1]))


def delete(alist, num):
    view(alist, num)
    to_delete = int(input('Please enter the number of the album you would like to remove. ')) - 1
    removed = alist.pop(to_delete)
    print("{} by {} has been removed.".format(removed[0], removed[1]))


def make_it_so():
    album_list = []
    print("Heya, we're going to build a list of your top albums. How many would you like to list?")
    num_albums = get_num()
    print("Gotcha, we'll make a list of your top {} albums.".format(str(num_albums)))
    print("Let's add an album. The list will be in alphabetical order, "
          "so don't worry about putting them in in any particular order.")
    add(album_list, num_albums)

    while True:
        menu(album_list, num_albums)

if __name__ == '__main__':
    make_it_so()
