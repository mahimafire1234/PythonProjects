#Check if a user id in valid or not
#Used set and list
#Works for one input only
def check_if_uid_is_valid(uid_input):
    uid_list = [item for item in uid_input]
    uid_set = set(uid_input)

    if len(uid_input) == 10 and uid_input.isalnum():
        count_uppercase = 0
        count_digit  = 0

        for i in uid_list:
            if i.isupper():
                count_uppercase = count_uppercase + 1
            if i.isnumeric() :
                count_digit =count_digit +1

        if count_uppercase >= 2 and count_digit >= 3 and len(uid_set) == 10:
            print("Valid")
        else:
            print ("Invalid")
    else:
        print("Invalid")

uid_input = str(input())

if __name__ == "__main__":
    check_if_uid_is_valid(uid_input)
