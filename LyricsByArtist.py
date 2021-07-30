'''
Lyrics generator



To push it further, have at least 3 songs by the same artist.

Next, ask the user to put the name of the artist so you can show them only options by that artist. Then the user can select a specific song from that list.

Top Ten Songs:
1. Bad Moon Rising by Credence Clearwater Revival
2. Fortunate Son by Credence Clearwater Revival
3. Proud Mary by Credence Clearwater Revival
4. Born In The USA by Bruce Springsteen
5. Hysteria by Def Leppard
6. Start Me Up by The Rolling Stones
7. Living On A Prayer by Bon Jovi
8. With Or Without You by U2
9. Jump by Van Halen
10. Hungry Like The Wolf by Duran Duran

Press * to choose again.


'''
import sys


def replay():
    play_again = input('Do you want to try again? If yes then press "*": ')
    if play_again.casefold() == '*':
        return True
    else:
        return False

print('Choose lyrics according to the artist')
print()

lyrics_by_artist = {
    "1.Credence Clearwater Revival" : {
        "Bad Moon Rising",
        "Fortunate Son",
        "Proud Mary"
    },
    "2.Bruce Springsteen" : {"Born In The USA"},
    "3.Def Leppard" : {"Hysteria"},
    "4.Rolling Stones" : {"Start Me Up"},
    "5.Bon Jovi" : {"Living On A Prayer"},
    "6.U2" : {"With Or Without You"},
    "7.Van Halen" : {"Jump"},
    "8.Duran Duran" : {"Hungry Like The Wolf"}
}

song_files = {
    "Bad Moon Rising" : "ccr_bad_moon_rising.txt",
    "Fortunate Son" : "ccr_fortunate_son.txt",
    "Proud Mary" : "ccr_proud_mary.txt",
    "Born In The USA": "bs_born_in_usa.txt",
    "Hysteria": "dl_hysteria.txt",
    "Start Me Up": "rs_start_me_up.txt",
    "Living On A Prayer": "bj_living_on_prayer.txt",
    "With Or Without You": "u2_with_without.txt",
    "Jump": "vh_jump.txt",
    "Hungry Like The Wolf": "dd_hungry_wolf.txt"
}

multiple_songs = {}
another_go = True
while another_go:
    print('Artists:')
    print()
    for item in lyrics_by_artist.keys():
        print(item)
    songs = []
    artist_choice = input('Please choose by number from the above list: ')
    if artist_choice in lyrics_by_artist.keys():
        print('List of songs:')
        print()
        for item in lyrics_by_artist[artist_choice]:
            songs.append(item)
        for item in songs:
            print(item)
        if len(songs) > 1:
            choose_one_song = input('Which song lyric would you like to see? ')
            print()
            print(choose_one_song)
            lyric_file = open(song_files[choose_one_song],"r")
            print(lyric_file.read())
        else:
            lyric_file = open(song_files[songs[0]],"r")
            print(lyric_file.read())
        if replay():
            another_go = True
        else:
            another_go = False
            print('Goodbye')
            sys.exit
    else:
        print('Your choice is not in the list')
        if replay():
            another_go = True
        else:
            print('Goodbye')
            another_go = False
            sys.exit
