###############################Voting System#####################################
Aap=0
BJP=0 
Congress=0 
Samajwadi=0 
print("Welcome to Elections 2024")
print("Press 1 for casting your vote\nPress 2 for Knowing the parties standing for elections 2024\nPress 3 for knowing leading party")
choice=int(input("Choose your option from the above"))
match choice:
    case 1:
        print("Enter 1 for giving your vote to BJP\nEnter 2 for giving your vote to AAP\nEnter 3 for giving your vote to Congress\nEnter 4 for giving your vote to Samajwadi")
        choice=int(input("Enter the above key"))
        match choice:
            case 1:
                BJP++
            case 2:
                AAP++
            case 3:
                Congress++
            case 4:
                Samajwadi++
            case _:
                print("Invalid Choice")
    case 2:
        print("BJP\nCongress\nAap\nSamajwadi")
    case 3:
        if(BJP>AAP and BJP>Congress and BJP>Samajwadi):
            print("BJP is winning")
        elif(AAP>Congress and AAP>BJP and AAP>Samajwadi):
            print("AAP is winning")
        elif(Samajwadi>BJP and Samajwadi>Congress and Samajwadi>AAP):
            print("Samajwadi is winning")
        elif(Congress>AAP and Congress>BJP and Congress>Samajwadi):
            print("Congress is winning")
        else:
            print("None leading")
    case _:
        print("Invalid choice")
if(BJP>AAP and BJP>Congress and BJP>Samajwadi):
    print("BJP won")
elif(AAP>Congress and AAP>BJP and AAP>Samajwadi):
    print("AAP won")
elif(Samajwadi>BJP and Samajwadi>Congress and Samajwadi>AAP):
    print("Samajwadi won")
elif(Congress>AAP and Congress>BJP and Congress>Samajwadi):
    print("Congress won")
else:
    print("No one Won")

        
