import random
import sys
import time

def main():
    server_size = int(sys.argv[1])
    num_players = int(sys.argv[2])
    lower_bound = int(sys.argv[3])
    upper_bound = int(sys.argv[4])

    # List of friends in friends lists of selected players (will contain duplicates initially).
    friends_in_f_lists = []

    start_time = time.time()

    # Generate the friends lists for the selected players
    for i in range(num_players):
        friends = set()
        num_friends = random.randint(lower_bound, upper_bound)
        while len(friends) < num_friends:
            friends.add(random.randint(0, server_size - 1))
        friends_in_f_lists.extend(list(friends))

    print("First for loop completed")
    all_friends = set(friends_in_f_lists)
    percent_covered = len(all_friends) / server_size
    print(f"Percentage of server covered: {percent_covered:.2%}")

if __name__ == "__main__":
    main()