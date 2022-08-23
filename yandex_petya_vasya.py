def cards():
    cards_capacity = int(input())
    cards_array = input().split(" ")
    petya_results = []
    vasya_results = []

    while cards_capacity > 0:
        vasya = 0
        petya = 0

        if len(cards_array) > 0:
            petya += int(cards_array.pop(0))

        if len(cards_array) > 0:
            vasya += int(cards_array.pop(0))

        if petya > vasya and len(cards_array) > 0:
            vasya += int(cards_array.pop(0))
            cards_capacity -= 1
        elif petya < vasya and len(cards_array) > 0:
            petya += int(cards_array.pop(0))
            cards_capacity -= 1

        cards_capacity -= 2
        petya_results.append(petya)
        vasya_results.append(vasya)

    if sum(petya_results) > sum(vasya_results):
        return "Petya"
    elif sum(petya_results) < sum(vasya_results):
        return "Vasya"
    else:
        return "draw"


print(cards())