def vote(votes):
    print("Give your vote, the options are:")
    print("yay, nay, idk")
    choice = input("> ").lower()
    try:
        votes[choice] += 1
    except KeyError:
        votes["error"] += 1

def show_results(votes):
    print()
    for key, value in votes.items():
        print(f"{key.capitalize():<5}: {'#' * value}")
    print()

tax_renewal = {
    "yay": 0,
    "nay": 0,
    "idk": 0,
    "error": 0
}
pooh_for_president = {
    "yay": 12,
    "nay": 0,
    "idk": 5,
    "error": 4
}

print("Should we implement the tax renewal?")
vote(tax_renewal)
show_results(tax_renewal)

print("Vote Winnie the Pooh for president?")
vote(pooh_for_president)
show_results(pooh_for_president)
