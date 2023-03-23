import random
# Get the number of friends joining
num_friends = int(input("Enter the number of friends joining (including you):\n"))

# Check if the number of friends is valid
if num_friends <= 0:
    print("No one is joining for the party")
else:
    # Initialize the dictionary to store friends and their bill values
    friends_dict = {}

    # Get the names of friends and add them to the dictionary
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        friend_name = input()
        friends_dict[friend_name] = 0
    #  friends_dict.update((name, average_amount) for name in friends_dict)
    # Print the dictionary
    #  print(friends_dict)
    amount = float(input('Enter the total bill value:\n'))
    lucky_one = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if lucky_one == 'Yes':
        lucky_num = random.randint(0, num_friends - 1)
        lucky_name = list(friends_dict.keys())[lucky_num]
        print(f"{lucky_name} is the lucky one!\n")
        average_amount = round(amount / (num_friends - 1), 2)
        for name in friends_dict:
            if name == lucky_name:
                friends_dict[name] = 0
            else:
                friends_dict[name] = round(average_amount, 2)
        print(friends_dict)
    else:
        print("No one is going to be lucky\n")
        average_amount = round((amount / num_friends), 2)
        for name in friends_dict:
            friends_dict[name] = round(average_amount, 2)
        print(friends_dict)
