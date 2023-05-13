name = input("Please enter your name: ")
print("Dear " + name)

list = ["small", "medium", "big"]
mistake_level = input("Enter my mistake level: ")

if mistake_level == list[0] :
    print("You have been scolded! ")

elif mistake_level == list[1] :
    print("You have to do situps! ")

elif mistake_level == list[2] :
    print("You have have been beated! ")

else :
    print("I think you typed something wrong. You only have 3 options 'small', 'medium' and 'big' please type one of this statement only! ")
