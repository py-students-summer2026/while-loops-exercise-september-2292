def get_starting_number():
    while True:
        starting_num = input("How many bottles of beer on the wall? ")
        if starting_num.isdigit():
            starting_num = int(starting_num)
            if starting_num > 1:
                return starting_num
            else:
                continue
        else:
            continue

def sing(num_bottles):
    num_holder = num_bottles
    while num_holder > 0:
        if num_holder > 2:
            print(str(num_holder) + " bottles of beer on the wall, " + str(num_holder) + " bottles of beer.")
            num_holder = num_holder - 1
            print("Take one down, pass it around, " + str(num_holder) + " bottles of beer on the wall.")
        elif num_holder == 2:
            print(str(num_holder) + " bottles of beer on the wall, " + str(num_holder) + " bottles of beer.")
            num_holder = num_holder - 1
            print("Take one down, pass it around, " + str(num_holder) + " bottle of beer on the wall.")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            num_holder = num_holder - 1
