# This program is to count the character entered in Input.
#Author - Mujahid Fulari

print("")
string = input("Please enter the content : ").lower()
count = input("Enter any character that you have used in above string to count : ").lower()
a = 0
for i in range(len(string)):
    if(string[i] == count):
        a = a + 1

print(f"The character {count} has been used {a} times in the given content. ")
