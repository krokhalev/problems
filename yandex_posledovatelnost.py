# array = [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
# array2 = [0, 0, 0, 0]
# array3 = []
#
# count = 0
# counts_array = []
# for element in array:
#     if element == 1:
#         count += 1
#     else:
#         if count != 0:
#             counts_array.append(count)
#             count = 0
#
# if len(counts_array) == 0:
#     print("0")
# else:
#     counts_array.sort()
#     print(counts_array[-1])

def card_game():
    count = int(input())
    cards = input().split(" ")
    if len(cards) != count:
        return "input correct sequence"

    petya = 0
    vasia = 0

    for index in range(0, count-1):
        petya += int(cards[index])
        vasia += int(cards[index+1])



    print(petya)
    print(vasia)


print(card_game())

# [1,2,3]
# [1,2]
# [1]
