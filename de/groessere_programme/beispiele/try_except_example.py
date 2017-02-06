
# print all cards with even numbers.

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for card in cards:
    try:
        number = int(card)
        if number % 2 == 0: # modulo operator
            print(card, "is an even card.")
    except ValueError:
        print (card, "can not be divided")
