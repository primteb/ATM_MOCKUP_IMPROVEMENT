


#Rgister
#- first name, last name, email, password
#- generate user account number


#Login
# - account number and password


#Bank Operations

# Initializing the system

database = {}  #dictionary

def init():
    isValidOptionSelected = False
    print("Welcome to BankPython")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option")

    def login():
        print("@@@@@@@@@login@@@@@@@")

        isloginSucessful = False
        
        while isloginSucessful == False:

            accountNumberFromUser = int(input("What is your account number? \n"))
            password = input("What is your passwaord \n")

            for accountNumber, userDetails in database.items():
                if(accountNumber == accountNumberFromUser):
                    if(userDetails[3]== password):
                        isloginSucessful = True

            print("invalid account or password")
        bankOperation(userDetails)
    
    def register():

        print('@@@@@@@@@Register@@@@@@@@@@')

        email = input("What is your email address? \n")
        first_name = input("What is yourrr first name? \n")
        last_name = input("What is your last name? \n")
        passwaord = input("Create a password for yourself \n")

        accountNumber = generateAccountNumber()

        database[accountNumber] = [first_name, last_name, emai, passwaord]

        print("What account has been created")
        print("== === ==== === ==")
        print("Your account numberrr is: %d" % accountNumber)
        print("Make dure you keepit safe")
        print("== === ==== === ==")

        login()

    def bankOperation(User):
       
        print("Welcome %s %s" % (user[0],user[1]))
       
        selectedOption = input("What would you like to do? (1) Deposit (2) Withrawal (3) Logout (4) Exit \n")

        if(selectedOption == 1):
            
            depositOperation()
        elif(selectedOption == 2):
            
            withdrawalOperation()
        elif(selectedOption == 3):
            
            login()
        elif(selectedOption == 4):

            
            exit()
        else:

            print("Invalid option selected")
            bankOperation(User)
    
    def withdrawalOperation():
        print("withdrawal")


    def depositOperation():
        print("Deposit Operations") 

    def generateAccountNumber():

        return random.randrange(111111111,999999999)


    init()


    