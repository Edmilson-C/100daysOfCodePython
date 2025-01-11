print("#############################################")
print("#      Welcome to Secret Auction Program    #")
print("#############################################\n")

auction_bidders = {}

can_continue = "y"
max_bid = 0.0
max_bidder = ""

while can_continue == "y" or can_continue == "yes":
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: "))
    auction_bidders[name] = bid

    can_continue = input("Any other bidders? y-yes or n-no\n")

for bidder in auction_bidders:
    if max_bid < auction_bidders[bidder]:
        max_bid = auction_bidders[bidder]
        max_bidder = bidder

print(f"{max_bidder} won the auction with {auction_bidders[max_bidder]}MZN")