###############################Voting System#####################################
Aap=0
BJP=0 
Congress=0 
Samajwadi=0 
print("Please enter the password admin")
password=input("")
print("How many voters are there?")
number=int(input(""))
for i in range(1,number+1,1):
    print("Welcome to Elections 2024")
    print("Press 1 for casting your vote\nPress 2 for Knowing the parties standing for elections 2024\nPress 3 for knowing leading party")
    choice=int(input("Choose your option from the above\n"))
    match choice:
        case 1:
            print("Enter 1 for giving your vote to BJP\nEnter 2 for giving your vote to AAP\nEnter 3 for giving your vote to Congress\nEnter 4 for giving your vote to Samajwadi")
            choice=int(input("Enter the above key\n"))
            match choice:
                case 1:
                    BJP=BJP+1
                case 2:
                    Aap=Aap+1
                case 3:
                    Congress=Congress+1
                case 4:
                    Samajwadi=Samajwadi+1
                case _:
                    print("Invalid Choice")
        case 2:
            print("BJP\nCongress\nAap\nSamajwadi")
        case 3:
            if(BJP>Aap and BJP>Congress and BJP>Samajwadi):
                print("BJP is winning")
            elif(Aap>Congress and Aap>BJP and Aap>Samajwadi):
                print("AAP is winning")
            elif(Samajwadi>BJP and Samajwadi>Congress and Samajwadi>Aap):
                print("Samajwadi is winning")
            elif(Congress>Aap and Congress>BJP and Congress>Samajwadi):
                print("Congress is winning")
            else:
                print("None leading")
        case _:
            print("Invalid choice")
print("Please enter password for knowing the result")
pin=input("")
if(pin==password):
    if(BJP>Aap and BJP>Congress and BJP>Samajwadi):
        print("BJP won")
    elif(Aap>Congress and Aap>BJP and Aap>Samajwadi):
        print("AAP won")
    elif(Samajwadi>BJP and Samajwadi>Congress and Samajwadi>Aap):
        print("Samajwadi won")
    elif(Congress>Aap and Congress>BJP and Congress>Samajwadi):
        print("Congress won")
    else:
        print("No one Won")
else:
    print("Wrong password")
print("Elections 2024 Over")
