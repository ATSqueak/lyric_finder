'''
Lyrics generator
Ask a user to choose from a list of 10 songs. When the user does, you print out the lyrics to the song they selected.

Example:

Welcome, please select a select a song from this top 10 songs:

1. Baby by Bieber
2. Hotline Bling by Drake
3. Flawless by Beyonce
4. Fall by Eminem...
You chose Flawless by Beyonce. Here you go:

------- Flawless by Beyonce ------------
I'm out that H, town coming coming down
I'm coming down, drippin' candy on the ground
H, Town, Town, I'm coming down, coming down
Drippin' candy on the ground...

Press * to choose again.
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

'''

import sys

print('Welcome To Lyrics Generator')
print()

def song_list():

    print('Top Ten Songs:')
    print('1. Bad Moon Rising by Credence Clearwater Revival')
    print('2. Fortunate Son by Credence Clearwater Revival')
    print('3. Proud Mary by Credence Clearwater Revival')
    print('4. Born In The USA by Bruce Springsteen')
    print('5. Hysteria by Def Leppard')
    print('6. Start Me Up by The Rolling Stones')
    print('7. Living On A Prayer by Bon Jovi')
    print('8. With Or Without You by U2')
    print('9. Jump by Van Halen')
    print('10. Hungry Like The Wolf by Duran Duran')

    lyric_choice = input('Here is a list of 10 songs. Please choose from one and the lyrics will be provided to you: ')

    return lyric_choice

def replay():
    play_again = input('Do you want to try again? If yes then press "*": ')
    if play_again.casefold() == '*':
        return True
    else:
        return False

lyric_dictionary = {
    "1": "Bad Moon Rising by Credence Clearwater Revival",
    "2": "Fortunate Son by Credence Clearwater Revival",
    "3": "Proud Mary by Credence Clearwater Revival",
    "4": "Born In The USA by Bruce Springsteen",
    "5": "Hysteria by Def Leppard",
    "6": "Start Me Up by The Rolling Stones",
    "7": "Living On A Prayer by Bon Jovi",
    "8": "With Or Without You by U2",
    "9": "Jump by Van Halen",
    "10": "Hungry Like The Wolf by Duran Duran"
}

lyric_file_dictionary = {
    "1": "ccr_bad_moon_rising.txt",
    "2": "ccr_fortunate_son.txt",
    "3": "ccr_proud_mary.txt",
    "4": "bs_born_in_usa.txt",
    "5": "dl_hysteria.txt",
    "6": "rs_start_me_up.txt",
    "7": "bj_living_on_prayer.txt",
    "8": "u2_with_without.txt",
    "9": "vh_jump.txt",
    "10": "dd_hungry_wolf.txt"
}

another_go = True
while another_go:
    lyric_choice = song_list()
    if lyric_choice in lyric_dictionary:
        print('You selected ',lyric_dictionary[lyric_choice])
        print()
        print('Lyrics:')
        print()
        lyric_file = open(lyric_file_dictionary[lyric_choice],"r")
        print(lyric_file.read())
        if replay():
            another_go = True
        else:
            another_go = False
            print('Goodbye')
            sys.exit
    else:
        print('That is not in our list')
        if replay():
            another_go = True
        else:
            print('Goodbye')
            another_go = False
            sys.exit

