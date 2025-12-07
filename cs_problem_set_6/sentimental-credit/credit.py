card = input("Number: ")

total = 0
rev = card[::-1]

for i in range(len(rev)):
    n = int(rev[i])

    if i % 2 == 1:
        n = n * 2
        if n > 9:
            n = n - 9
    total += n


if total % 10 != 0:
    print("INVALID")
else:
    if card[0] == '4' and len(card) in [13, 16]:
        print("VISA")
    elif len(card) == 15 and ((card[0] + card[1]) == "34" or (card[0] + card[1]) == "37"):
        print("AMEX")
    elif len(card) == 16 and (card[0] + card[1]) in ["51", "52", "53", "54", "55"]:
        print("MASTERCARD")
    else:
        print("INVALID")
