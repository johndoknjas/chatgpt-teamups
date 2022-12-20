import random
import sys

def main():
    # Total number of players on the server
    server_size = int(sys.argv[1])

    # Number of players to generate friends lists for
    num_players = int(sys.argv[2])

    # Lower and upper bounds for the number of friends
    lower_bound = int(sys.argv[3])
    upper_bound = int(sys.argv[4])

    # Set of all friends among the selected players
    all_friends = set()

    # Generate the friends lists for the selected players
    for i in range(num_players):
        friends = set()
        num_friends = random.randint(lower_bound, upper_bound)
        while len(friends) < num_friends:
            friends.add(random.randint(0, server_size - 1))
        all_friends = all_friends.union(friends)

    # Calculate the percentage of the server covered by the friends lists
    percent_covered = len(all_friends) / server_size

    print(f"Percentage of server covered: {percent_covered:.2%}")

if __name__ == "__main__":
    main()