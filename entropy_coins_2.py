def entropy():
    from random import randint
    ncoins = int(input('Input the number of coins to flip: '))
    nflips = int(input('Input how many times the coins shall flip: '))
    if ncoins <= 0 or nflips <= 0:
        raise ValueError('Input a value greater than zero!')
    # m=l=5
    return [[randint(0, 1) for coin in range(ncoins)] for flip in range(nflips)]


def conference(flippile):
    counter = 0
    indexes = []
    for index, flipset in enumerate(flippile):
        if sum(flipset) == len(flipset) or sum(flipset) == 0:
            counter += 1
            indexes.append(index)
    return counter, indexes


def pile_exhibition(flippile):
    c = 0
    for flipset in flippile:
        c += 1
        print(f'Flipping set #{c}: {flipset}')


def main(conf=False):
    print('-' * 50)
    game = entropy()
    analyzing = conference(game)
    if conf:
        pile_exhibition(game)
    counting = analyzing[0]
    drawn_indexes = analyzing[1]
    print('-' * 50)
    if counting == 0:
        print(f'The coins didn\'t fell on all equally.')
    else:
        print(f'The coins fell on all equally {counting} time'+('.' if counting == 1 else 's'), end=' ')
        if counting == 1:
            print(f'on the flipping set number {drawn_indexes[0]}')
        else:
            print(f'on the following flipping sets: ', end='')
            for c, value in enumerate(drawn_indexes):
                if c < len(drawn_indexes)-2:
                    print((value + 1), end=', ')
                elif c == len(drawn_indexes)-2:
                    print((value + 1), end=' and ')
                elif c == len(drawn_indexes)-1:
                    print((value + 1), end='.')


main()
