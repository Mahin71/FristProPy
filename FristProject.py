n = 18
var3 = 1
while var3 <= 9:
    var2 = int(input("guess the number\n"))
    if var2 < 18:
        print("please less the number")
    elif var2 > 18:
        print("please greater then number")
    else:
        print("you success")
        break
    print(9 - var3, "no. of guesses left")
    var3 += 1
