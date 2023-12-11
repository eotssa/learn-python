# Write your solution here





while True: 
    input_str = input()
    if "visual studio code" == input_str.lower():
        print("an excellent choice!")
        break
    elif "word" == input_str.lower() or "notepad" == input_str.lower():
        print("awful")
    else:
        print("not good")