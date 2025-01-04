from secret_auction.art import logo


def show_logo():
    print(logo)
    print("Welcome to the secret auction program.")


def get_highest_bid(bids):
    highest_bid = ("", 0)

    for name in bids:
        if bids[name] > highest_bid[1]:
            highest_bid = (name, bids[name])
    return highest_bid


def main():
    show_logo()
    end_of_auction = False

    bids = {}
    while not end_of_auction:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        bids[name] = bid

        another_bid = input("Are there any other bidders?  Type 'yes' or 'no'.\n")
        if another_bid == "no":
            end_of_auction = True
        else:
            print("\n" * 100)

    highest_bid = get_highest_bid(bids)
    print(f"The winner is {highest_bid[0]} with a bid of ${highest_bid[1]}.")


if __name__ == "__main__":
    main()
