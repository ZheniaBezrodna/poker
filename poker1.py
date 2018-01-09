from collections import Counter

import re

field = set()

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['heart', 'diamond', 'club', 'spade']


print("Write the cards in your hand from the deck of cards in the following "
      "format:\n"
      "two - 2\n"
      "three - 3\n"
      "four - 4\n"
      "five - 5\n"
      "six - 6\n"
      "seven - 7\n"
      "eight - 8\n"
      "nine - 9\n"
      "ten - t\n"
      "jack - j\n"
      "queen - q\n"
      "king - k\n"
      "ace - a\n"
      "suits: \n"
      "spade - s\n"
      "heart - h\n"
      "diamond - d\n"
      "club -c\n"
      "for ex. 2c 3s jh qc ad, \n"
      "and now you must enter cards: ")


def check():
    # This function verifies the correctness of the cards entry
    """

    :board1: list, 2c 3s jh qc ad
    :return: list, [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]

    :board1: list, 2q 3s jh qc ad
    :return: string,
             Enter the correct list of carts, please. For ex. 2c 3s jh qc ad.

    """
    board1 = input()
    if not re.search(
            "^[2-9tjqka][shdc]\s+[2-9tjqka][shdc]\s+[2-9tjqka][shdc]\s+"
            "[2-9tjqka][shdc]\s+[2-9tjqka][shdc]$", board1):
        print("Enter the correct list of carts, please. For ex. 2c 3s jh "
              "qc ad.")
        return check()
    board1 = board1.split()
    board1 = [[i[0], i[1]] for i in board1]
    return board1


board = check()
print(board)


def value_checker(similar_cards, times, lst):
    """

    :param similar_cards: int, 2
    :param times: int, 1
    :param lst: list, [1, 7, 9, 3, 1, 2, 8]
    :return: 1
    """
    # Lst = [1, 7, 9, 3, 1, 2, 8] ->
    # counter = {1: 2, 2: 1, 3: 1, 7: 1, 8: 1, 9: 1}
    counter = Counter(lst[b][0] for b in range(len(lst)))
    if len([c for c, d in counter.items() if d >= similar_cards]) >= times:
        return 1


def suit_checker(lst, similar_cards):
    # This function checks for 4 cards of 1 suit.
    """

    :param lst: list, [1, 7, 9, 3, 1, 2, 8]
    :param similar_cards: int, 4
    :return: 1
    """
    # Lst = [1, 7, 9, 3, 1, 2, 8] ->
    # counter = {1: 2, 2: 1, 3: 1, 7: 1, 8: 1, 9: 1}
    counter = Counter(lst[e][1] for e in range(len(lst)))
    if len([f for f, j in counter.items() if j >= similar_cards]) >= 1:
        return 1


def set1(lst):
    # This function calculates the probability of a combination of the set.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0
    """
    if value_checker(3, 1, lst):
        return 1
    elif pair(lst) == 1:
        return 2 / (52 - len(lst))
    else:
        return 0


def pair(lst):
    # This function calculates the probability of pairing from cards.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: float, 0.3191489361702127


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 1


    """
    if value_checker(2, 1, lst) == 1:
        return 1
    return (3 / (52 - len(lst))) * 5


def two_pairs(lst):
    # This function calculates the probability of forming two pairs of cards.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 1

    """
    if pair(lst) == 1:
        if value_checker(2, 2, lst) == 1:
            return 1
        return (3 / (52 - len(lst))) * (len(lst) - 2)
    else:
        return 0


def flash(lst):
    # This function calculates the probability of a combination of the flash.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 0
    """

    if suit_checker(lst, 5) == 1:
        return 1
    elif suit_checker(lst, 4) == 1:
        return 9 / (52 - len(lst))
    else:
        return 0


def full_house(lst):
    # This function calculates the probability of a combination
    # of the full house.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 1
    """
    if value_checker(3, 1, lst) == 1 and value_checker(2, 2, lst):
        return 1
    elif set1(lst) == 1:
        return (3 / (52 - len(lst))) * (len(lst) - 3)
    elif two_pairs(lst) == 1:
        return 2 / (52 - len(lst)) * 2
    else:
        return 0


def kare(lst):
    # This function calculates the probability of a combination
    # of the kare.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: float, 0.02127659574468085
    """
    if value_checker(4, 1, lst) == 1:
        return 1
    elif set1(lst) == 1:
        return 1 / (52 - len(lst))
    else:
        return 0


def street(lst):
    # This function calculates the probability of a combination
    # of the street.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 0
    """

    combinations = []
    for h in range(len(lst)):
        field.add(lst[h][0])
    sequence = [{'a', '1', '2', '3', '4'}, {'1', '2', '3', '4', '5'},
                {'2', '3', '4', '5', '6'}, {'3', '4', '5', '6', '7'},
                {'4', '5', '6', '7', '8'}, {'5', '6', '7', '8', '9'},
                {'6', '7', '8', '9', 't'}, {'7', '8', '9', 't', 'j'},
                {'8', '9', 't', 'j', 'q'}, {'9', 't', 'j', 'q', 'k'},
                {'t', 'j', 'q', 'k', 'a'}]
    for g in sequence:
        if len(list(field.intersection(g))) == 5:
            return 1
        elif len(list(field.intersection(g))) == 4:
            combinations.append(list(field.intersection(g)))
    if len(combinations) == 0:
        return 0
    elif len(combinations) == 1 or combinations[0] != combinations[1]:
        return 4 / (52 - len(lst))
    elif combinations[0] == combinations[1]:
        return 8 / (52 - len(lst))


def street_flash(lst):
    # This function calculates the probability of a combination
    # of the street flash.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 0
    """
    combinations = []
    for k in lst:
        field.add(k[0] + k[1])
    sequence = [{'ac', '1c', '2c', '3c', '4c'}, {'1c', '2c', '3c', '4c', '5c'},
                {'2c', '3c', '4c', '5c', '6c'}, {'3c', '4c', '5c', '6c', '7c'},
                {'4c', '5c', '6c', '7c', '8c'}, {'5c', '6c', '7c', '8c', '9c'},
                {'6c', '7c', '8c', '9c', 'tc'}, {'7c', '8c', '9c', 'tc', 'jc'},
                {'8c', '9c', 'tc', 'jc', 'qc'}, {'9c', 'tc', 'jc', 'qc', 'kc'},
                {'tc', 'jc', 'qc', 'kc', 'ac'}, {'as', '1s', '2s', '3s', '4s'},
                {'1s', '2s', '3s', '4s', '5s'}, {'2s', '3s', '4s', '5s', '6s'},
                {'3s', '4s', '5s', '6s', '7s'}, {'4s', '5s', '6s', '7s', '8s'},
                {'5s', '6s', '7s', '8s', '9s'}, {'6s', '7s', '8s', '9s', 'ts'},
                {'7s', '8s', '9s', 'ts', 'js'}, {'8s', '9s', 'ts', 'js', 'qs'},
                {'9s', 'ts', 'js', 'qs', 'ks'}, {'ts', 'js', 'qs', 'ks', 'as'},

                {'ah', '1h', '2h', '3h', '4h'}, {'1h', '2h', '3h', '4h', '5h'},
                {'2h', '3h', '4h', '5h', '6h'}, {'3h', '4h', '5h', '6h', '7h'},
                {'4h', '5h', '6h', '7h', '8h'}, {'5h', '6h', '7h', '8h', '9h'},
                {'6h', '7h', '8h', '9h', 'th'}, {'7h', '8h', '9h', 'th', 'jh'},
                {'8h', '9h', 'th', 'jh', 'qh'}, {'9h', 'th', 'jh', 'qh', 'kh'},
                {'th', 'jh', 'qh', 'kh', 'ah'}, {'ad', '1d', '2d', '3d', '4d'},
                {'1d', '2d', '3d', '4d', '5d'}, {'2d', '3d', '4d', '5d', '6d'},
                {'3d', '4d', '5d', '6d', '7d'}, {'4d', '5d', '6d', '7d', '8d'},
                {'5d', '6d', '7d', '8d', '9d'}, {'6d', '7d', '8d', '9d', 'td'},
                {'7d', '8d', '9d', 'td', 'jd'}, {'8d', '9d', 'td', 'jd', 'qd'},
                {'9d', 'td', 'jd', 'qd', 'kd'}, {'td', 'jd', 'qd', 'kd', 'ad'}]
    for l in sequence:
        if len(list(field.intersection(l))) == 5:
            return 1
        elif len(list(field.intersection(l))) == 4:
            combinations.append(list(field.intersection(l)))
    if len(combinations) == 0:
        return 0
    elif len(combinations) == 1 or combinations[0] != combinations[1]:
        return 1 / (52 - len(lst))
    elif combinations[0] == combinations[1]:
        return 2 / (52 - len(lst))


def royal_flash(lst):
    # This function calculates the probability of a combination
    # of the royal flash.
    """

    :param lst: list,
                [['2', 'c'], ['3', 's'], ['j', 'h'], ['q', 'c'], ['a', 'd']]
    :return: int, 0


    :param lst: list,
                [['6', 's'], ['6', 'h'], ['6', 'd'], ['t', 's'], ['t', 'h']]
    :return: int, 0
    """
    sequence = [{'ts', 'js', 'qs', 'ks', 'as'}, {'tc', 'jc', 'qc', 'kc', 'ac'},
                {'td', 'jd', 'qd', 'kd', 'ad'}, {'th', 'jh', 'qh', 'kh', 'ah'}]
    for a in lst:
        field.add(a[0] + a[1])
    for q in sequence:
        if len(list(field.intersection(q))) == 4:
            return 1 / (52 - len(lst))
        elif len(list(field.intersection(q))) == 5:
            return 1

    return 0


def result():
    # This function displays the results of the calculations.
    # Combinations are based on growth
    # (from the weakest combination to the strongest).
    """

    :return: Probability of
             pair is  0.3191489361702127
             set is  0
             two pairs is  0
             flash is  0
             full house is  0
             ...

    """
    print("Probability of ")
    print("pair is ", pair(board))
    print("two pairs is ", two_pairs(board))
    print("set is ",  set1(board))
    print("street is ", street(board))
    print("flash is ", flash(board))
    print("full house is ", full_house(board))
    print("kare is ", kare(board))
    print("street flash is ", street_flash(board))
    print("royal flash is", royal_flash(board))
    return " "


print(result())


def one_more_card(list_of_cards):
    # This function asks you to enter one more card and validates
    # their input.
    """

    :param list_of_cards: list,
                          [['2', 'c'], ['3', 's'], ['j', 'h'],
                          ['q', 'c'], ['a', 'd']]
    | >>> Enter an only one next card, please.
    | >>> 3h
    :return: list,
             [['2', 'c'], ['3', 's'], ['j', 'h'],
             ['q', 'c'], ['a', 'd'], ['3', 'h']]


    :param list_of_cards: list,
                          [['2', 'c'], ['3', 's'], ['j', 'h'],
                          ['q', 'c'], ['a', 'd']]
    | >>> Enter an only one next card, please.
    | >>> 3e
    | >>> Your cart is wrong!
    | >>> Enter an only one next card, please.
    | >>> 3h
    :return: list,
             [['2', 'c'], ['3', 's'], ['j', 'h'],
             ['q', 'c'], ['a', 'd'], ['3', 'h']]
    """
    print("Enter an only one next card, please.")
    card = input()
    if not re.search("^[2-9tjqka][shdc]$", card):
        print("Your cart is wrong!")
        return one_more_card(list_of_cards)
    card = list(card)
    list_of_cards.append([card[0], card[1]])
    return list_of_cards


one_more_card(board)
print(result())
