range = [0, 20, 40, 60, 80, 100, 120]
progressCount, trailerCount, retrieverCount, excludeCount = 0, 0, 0, 0
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []
CwDictionary = {}

while True:

    UoW_number = input("Enter your UoW number: ")
    
    while True:
        try:
            passCredit = int(input("Enter Credit at pass: "))
            if not passCredit in range:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            deferCredit = int(input("Enter Credit at defer: "))
            if not deferCredit in range:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            failCredit = int(input("Enter Credit at fail: "))
            if not failCredit in range:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    #Total Checking
    Total = passCredit + deferCredit + failCredit
    if Total != 120:
        print("Total incorrect")
    else:    
        #Outputs checking
        if passCredit == 120:
            print("Progress")
            progressCount += 1
            progress_list.append([passCredit, deferCredit, failCredit])
        elif passCredit == 100:
            print("Progress (module trailer)")
            trailer_list.append([passCredit, deferCredit, failCredit])
            trailerCount += 1
        elif failCredit >= 80:
            print("Exclude")
            exclude_list.append([passCredit, deferCredit, failCredit])
            excludeCount += 1
        else:
            print("module retriever")
            retriever_list.append([passCredit, deferCredit, failCredit])
            retrieverCount += 1
    
    
    Order = input("Enter q to exit the program \nor press any key to continue: ")
    if Order == "q":
        print("Exiting program")
        break
        
        
#Histogram
print("Histogram")
print(f"Progress {progressCount} : ", end="")
print("*" * progressCount)
print(f"Trailer {trailerCount}  : " , end='' )
print("*" * trailerCount)
print(f"Retriever {retrieverCount}: ", end='')
print("*" * retrieverCount)
print(f"Exclude {excludeCount}  : ", end='')
print("*" * excludeCount)

outcome_count = progressCount + trailerCount + retrieverCount  + excludeCount 
print(outcome_count, end="")
print(" outcomes in total.")
        
#Print out the list
print("Second part")
for item in progress_list:
    print(f"Progress - {', '.join(str(i) for i in item)}")
    
for item in trailer_list:
    print(f"Trailer - {', '.join(str(i) for i in item)}")
    
for item in exclude_list:
    print(f"Exclude - {', '.join(str(i) for i in item)}")

for item in retriever_list:
    print(f"Retriever - {', '.join(str(i) for i in item)}")
    
    
    
    
#part 3 (text file)
with open("output.txt", "w") as newfile: # w/ r/ a
    newfile.write("Part 3: \n")
    for item in progress_list:
        newfile.write(f"Progress - {', '.join(str(i) for i in item)}\n")
        
    for item in trailer_list:
        newfile.write(f"Trailer - {', '.join(str(i) for i in item)}\n")
        
    for item in exclude_list:
        newfile.write(f"Exclude - {', '.join(str(i) for i in item)}\n")

    for item in retriever_list:
        newfile.write(f"Retriever - {', '.join(str(i) for i in item)}\n")

    
#Part 4
#key : value
for k,l in CwDictionary.items():
    print(f"{k} : {l}", end=" ")
    
print()
