str = input("hi everyone :) , please enter input ->>>")

lenght_string =len(str)

palindrome = lenght_string - 1

index = 0 

while palindrome > index:
    if str[palindrome] == str[index] :
        index += 1
        palindrome -=1

        if palindrome == index or palindrome == index+1 :
            print("yes :) , your input is palindrome")
    else:
        print("opps :( , your input is not palindrome")
        break
















