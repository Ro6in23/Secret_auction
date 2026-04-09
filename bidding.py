
print("Welcome to secret auction program")
records = {}
continue_bid = True
max_record = 0
winner = ""
while continue_bid:
    user_name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    records[user_name] = bid
    bidders = input("Are there any other bidders?: 'yes' or 'no'.").lower()
    if bidders == "no":
        continue_bid = False
        for key in records:
            if records[key]>max_record:
                max_record = records[key]
                winner = key
        print(f"The highest bid is from {winner} with a bid of ${max_record}")

    elif bidders == "yes":
        print("\n"*20)

