import random
import sys
import time

def output_instructions() -> None:
    with open('../README.md', 'r') as f:
        reached_desired_section = False
        for line in f:
            line = line.rstrip()
            if line.startswith('  -'):
                if reached_desired_section:
                    break
                elif '  - The friends lists' in line:
                    print()
                    reached_desired_section = True
            if reached_desired_section:
                print(line)
    print()
    sys.exit()

def main():
    if 'readme' in [arg.lower() for arg in sys.argv]:
        output_instructions()
    

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