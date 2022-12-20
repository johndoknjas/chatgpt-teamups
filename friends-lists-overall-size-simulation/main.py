import random
import sys
import time

def main():
    # Total number of players on the server
    server_size = int(sys.argv[1])

    # Number of players to generate friends lists for
    num_players = int(sys.argv[2])

    # Lower and upper bounds for the number of friends
    lower_bound = int(sys.argv[3])
    upper_bound = int(sys.argv[4])

    # List of sets containing the friends lists for the selected players
    friends_lists = []

    # Start time
    start_time = time.time()

    # Generate the friends lists for the selected players
    for i in range(num_players):
        friends = set()
        num_friends = random.randint(lower_bound, upper_bound)
        while len(friends) < num_friends:
            friends.add(random.randint(0, server_size - 1))
        friends_lists.append(friends)

        # Print message after 10, 20, 30, etc. seconds of runtime
        elapsed_time = time.time() - start_time
        if elapsed_time >= 10 and int(elapsed_time) % 10 == 0:
            print(f"{int(elapsed_time)} seconds elapsed")

    # Print message after all iterations of the first for loop are completed
    print("First for loop completed")

    # Combine all the elements in the friends lists into a single set
    all_friends = set()
    for friends in friends_lists:
        all_friends = all_friends.union(friends)

    # Calculate the percentage of the server covered by the friends lists
    percent_covered = len(all_friends) / server_size

    print(f"Percentage of server covered: {percent_covered:.2%}")

if __name__ == "__main__":
    main()