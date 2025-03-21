# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
continue_bidding = 'y'
bid_dict = {}
highestbid = 0
winner = ''
while continue_bidding == 'y':
    name = str(input('What is your name?:'))
    bid = int(input('What is your bid?:'))
    bid_dict[name] = bid
    continue_bidding = input('Are there more bids(Yes/No):')
    if continue_bidding.lower() != 'n':
        print("\n" * 100)

for name in bid_dict:
    if bid_dict[name] > highestbid:
        highestbid = bid_dict[name]
        winner = name       #Need more practice. Had to look at solution to find this simple answer to retrieving the key for the highest bid
    # ******************************************************
    # OR a super simple way is to use the max function
    # Example: winner = max(bid_dict, key=bid_dict.get)
    # ******************************************************


print(bid_dict)
print(f'The winner is {winner} with a winning bid of ${highestbid}')




