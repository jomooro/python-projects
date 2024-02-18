def get_input():
    while True:
        try:
            id_number = int(input("Enter your ID number: "))
            return validate_id_main(id_number)
        except ValueError:
            print("Error: ID must not contain letters or any special characters")


def convert_list(lst):
    return int("".join(map(str, lst)))


def get_number(list_numbers, str_id):
    tester = 0
    list_numbers = [int(x) for x in str_id]
    
    for i in range(12):
        if i % 2 != 0:
            total = int(list_numbers[i]) * 2
            total = (total // 10) + (total % 10) if total > 9 else total
            list_numbers[i] = total
        tester += list_numbers[i]

    return tester


def validate_id_math(id_number, str_id):
    final_answer = id_number % 10
    check_this_num = get_number(id_number, str_id)

    if (check_this_num * 9) % 10 == final_answer:
        return False
    else:
        print("Validation failed. Check:", check_this_num, "Expected:", final_answer)
        return True


def validate_id_main(id_num):
    id_num_str = str(id_num)
    
    while len(id_num_str) != 13:
        if len(id_num_str) > 13:
            print("Error: Please enter a valid 13-digit ID number")
            return get_input()
        id_num_str = "0" + str(id_num_str)

    if id_num_str[12] == "0" or validate_id_math(id_num, id_num_str):
        print("Error: Please enter a valid ID number")
        return get_input()
    else:
        return id_num_str


if __name__ == "__main__":
    id_num = get_input()
    print("Valid ID:", id_num)
