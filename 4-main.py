import donkeydefs
import donkeylogic
import donkeyinterface

def main():
    """
    Creates a new donkey and implements the main menu logic of donkeygotchi.
    """

    donkeydata = donkeylogic.init()
    
    while True:
        donkeyinterface.show_state(donkeydata)
        choice = donkeyinterface.prompt_choice(donkeydata)
        
        if choice == donkeydefs.QUIT:
            break

        if choice == donkeydefs.FEED:
            donkeylogic.feed(donkeydata)
        elif choice ==  donkeydefs.TICKLE:
            donkeylogic.tickle(donkeydata)
        elif choice == donkeydefs.WORK:
            donkeylogic.work(donkeydata)
        elif choice == donkeydefs.RESET:
            donkeydata = donkeylogic.init()

if __name__ == "__main__":
    main()
