# A simple Banking App

f = open("bankData.txt", "r")
currentbalance = f.read()
f.close()

f = open("Transaction_log.txt", "a")
f.close()

Yes = "Yes"
No = "No"

print("Do you want to make a transaction?")
answer = input("Yes /  No  : ")

if(answer == Yes):
    print("Enter\n 1-Withdraw\n 2-Deposit\n 3-Check Balance")
    choose = int(input("1,2,3 :  "))

    if (choose == 1):
        file = open("bankData.txt", "r")
        currentbalance = open("bankData.txt", "r").read()
        floatCurrent = float(currentbalance)
        file.close()
    
        print("How much would you like to withdraw?")
        addedAmount = input()

        if(addedAmount <= currentbalance):

            floatAddedAmount = float(addedAmount)
            file = open("bankData.txt", "w")
            newAmount = floatCurrent - floatAddedAmount
            newAmount = str(newAmount)
            file.write(newAmount)
            file.close()
            file = open("bankData.txt", "r")
            print("New Amount is: ")
            print(file.read())
            file.close()
            print("----Withdrawl successful!----")
            transactionOccured = "-"

            LOG = open("Transaction_log.txt", "a")
            oldAmount = floatCurrent
            oldAmount = str(floatCurrent)
            LOG = open("Transaction_log.txt", "a")
            oldAmount = floatCurrent
            oldAmount = str(floatCurrent)
            transactionType = transactionOccured
            transactionAmount = floatAddedAmount
            transactionAmount = str(transactionAmount)
            updatedAmount = newAmount
            updatedAmount = str(newAmount)
            LOG.write("\n\nWithdrawl Transaction")
            LOG.write("\nOld Balance: " + oldAmount)
            LOG.write("\nTransaction Occured: " + transactionType + transactionAmount)
            LOG.write("\nNew Balance: " + updatedAmount)
           
        else:
            print("Insufficient Funds")

    elif (choose == 2):

        file = open("bankData.txt", "r")
        currentbalance = open("bankData.txt", "r").read()
        floatCurrent = float(currentbalance)
        file.close()

        print("How much would you like to deposit?")
        addedAmount = input()

        floatAddedAmount = float(addedAmount)

        file = open("bankData.txt", "w")
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()

        file = open("bankData.txt", "r")
        print("New Amount is: ")
        print(file.read())
        file.close()
        transactionOccured = "+"
        print("----Deposition successful!----")

        LOG = open("Transaction_log.txt", "a")
        oldAmount = floatCurrent
        oldAmount = str(floatCurrent)
        LOG = open("Transaction_log.txt", "a")
        oldAmount = floatCurrent
        oldAmount = str(floatCurrent)
        transactionType = transactionOccured
        transactionAmount = floatAddedAmount
        transactionAmount = str(transactionAmount)
        updatedAmount = newAmount
        updatedAmount = str(newAmount)
        LOG.write("\n\nDeposition Transaction")
        LOG.write("\nOld Balance: " + oldAmount)
        LOG.write("\nTransaction Occured: " + transactionType + transactionAmount)
        LOG.write("\nNew Balance: " + updatedAmount)

    elif (choose == 3):
        file = open("bankData.txt", "r")
        print("Current balance")
        print(file.read())
        currentbalance = open("bankData.txt", "r").read()
        floatCurrent = float(currentbalance)
        file.close()

    else:
        print("You provided an invalid input")

elif(answer == No):
    print("Thank you, Enjoy your day")

else:
    print("You provided an invalid input")


