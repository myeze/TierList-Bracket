KnownList = [
    "Madvillainy",
    "FishScale",
    "Operation Doomsday",
    "The Melodic Blue",
    "Midnight Marauders",
    "IGOR",
    "Some Rap Songs",
    "Donuts",
    "UNLOCKED",
    "MMM...FOOD",
    "channel ORANGE",
    "ASTROWORLD",
    "Illmatic",
    "HEROES & VILLAINS",
    "My Beautiful Dark Twisted Fantasy",
    "Demon Days",
]

print(
    "Welcome to my Program! This will make either a music bracket or a tier list to choose a best album..."
)


def customEnter():
    AlbumList = []
    while True:
        try:
            print("\nChoose between 2, 4, 8, and 16")
            ListNum = int(input("\nHow Many Albums will you enter: "))
            if ListNum != 2:
                if ListNum != 4:
                    if ListNum != 8:
                        if ListNum != 16:
                            raise ValueError()
            break
        except ValueError:
            print("\nInvalid Number. Please Try Again.\n")
    for i in range(ListNum):
        print("Enter Album #" + str(i + 1))
        AlbumList.append(str(input()))
    return AlbumList


def runBracket(Songs):
    if len(Songs) == 2:
        while True:
            try:
                print("\n" + str(Songs[0]) + " vs " + str(Songs[1]))
                answer = int(
                    input(
                        "\nWhich is better? \n\n(Type 1 for "
                        + str(Songs[0])
                        + " or Type 2 for "
                        + str(Songs[1])
                        + "): "
                    )
                )
                if answer != 1:
                    if answer != 2:
                        raise ValueError()
                print(Songs[answer - 1] + " WINS!")
                break
            except ValueError:
                print("\nInvalid Number. Please Try Again.\n")
    elif len(Songs) == 4 or len(Songs) == 8 or len(Songs) == 16:
        WinList = []
        for i in range(0, len(Songs), 2):
            while True:
                try:
                    print("\n" + str(Songs[i]) + " vs " + str(Songs[i + 1]))
                    answer = int(
                        input(
                            "\nWhich is better? \n\n(Type "
                            + str(i)
                            + " for "
                            + str(Songs[i])
                            + " or Type "
                            + str(i + 1)
                            + ' for "'
                            + str(Songs[i + 1])
                            + '"):'
                        )
                    )
                    if answer == int(i):
                        WinList.append(Songs[answer])
                        break
                    elif answer == int(i + 1):
                        WinList.append(Songs[answer])
                        break
                    else:
                        raise ValueError()
                        break
                except ValueError:
                    print("\nInvalid Number. Please Try Again.\n")
        runBracket(WinList, len(WinList))


def tierList(Songs):
    SList = []
    AList = []
    BList = []
    CList = []
    DList = []
    FList = []
    for i in range(len(Songs)):
        while True:
            try:
                print("\nChoose a tier between S, A, B, C, D, and F")
                answer = str(input("\nWhat tier would " + str(Songs[i]) + " be: "))
                if answer == "S":
                    SList.append(Songs[i])
                    break
                elif answer == "A":
                    AList.append(Songs[i])
                    break
                elif answer == "B":
                    BList.append(Songs[i])
                    break
                elif answer == "C":
                    CList.append(Songs[i])
                    break
                elif answer == "D":
                    DList.append(Songs[i])
                    break
                elif answer == "F":
                    FList.append(Songs[i])
                    break
                else:
                    raise ValueError()
                    break
            except ValueError:
                print("\nInvalid Input. Please Try Again.\n")
    print("S-Tier: " + str(SList))
    print("A-Tier: " + str(AList))
    print("B-Tier: " + str(BList))
    print("C-Tier: " + str(CList))
    print("D-Tier: " + str(DList))
    print("F-Tier: " + str(FList))


def listChooser(List):
    while True:
        try:
            print("\nDo you want a Tournament Bracket or a Tierlist?")
            prefAnswer = int(
                input("\nType 1 for a Bracket and Type 2 for a Tierlist: ")
            )
            if prefAnswer == 1:
                runBracket(List)
                break
            elif prefAnswer == 2:
                tierList(List)
                break
            else:
                raise ValueError()
                break
        except ValueError:
            print("\nInvalid Number. Please Try Again.\n")


while True:
    try:
        print("\nDo you want a custom list or one already made?")
        prefList = int(input("\nType 1 for custom and 2 for pre made: "))
        if prefList == 1:
            AlbumList = customEnter()
            listChooser(AlbumList)
            break
        if prefList == 2:
            listChooser(KnownList)
            break
        else:
            raise ValueError()
            break
    except ValueError:
        print("\nInvalid Number. Please Try Again.\n")
