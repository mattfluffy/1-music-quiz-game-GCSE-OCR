import random
import csv

loop = 0
while loop < 1:
    def is_authorized(username, password):
        with open('authorized_players.txt', 'r') as f:
            for line in f:
                player = line.strip().split(',')
                if player[0] == username and player[1] == password:
                    return True
        return False


    def sign_up():
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        username = new_username
        # Check if the username is already taken
        with open('authorized_players.txt', 'r') as f:
            for line in f:
                player = line.strip().split(',')
                if player[0] == new_username:
                    print("This username is already taken. Please try again.")
                    return

        # Add the new player to the list of authorized players
        with open('authorized_players.txt', 'a') as f:
            f.write(f"{new_username},{new_password}\n")
        print("Successfully signed up!")


    # Ask the user if they want to log in or sign up
    auth_choice = input("Do you want to log in or sign up? (L/S) ")
    if auth_choice.upper() == "L":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if not is_authorized(username, password):
            print("Unauthorized user. Exiting...")
            exit()
    elif auth_choice.upper() == "S":
        sign_up()
    else:
        print("Invalid choice. Exiting...")
        exit()

    # 2. Loadsong list from an external file
    song_list = []
    try:
        with open("songs.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                song_list.append(row)
    except FileNotFoundError:
        print("songs.csv is missing, please check if the file is present in the correct location or create the file.")
        exit()

    # 3. Select a song and display the artist and first letter of each word of the song title
    points = 0
    while True:
        song = random.choice(song_list)
        artist = song[0]
        title = song[1]
        print("Artist: ", artist)
        print("Title: ", ' '.join([word[0] for word in title.split()]))
        
        # 4. Allow the user to guess the song title
        for i in range(2):
            try:
                guess = input("Guess the title of the song: ")
                if not guess.strip():
                    raise ValueError("Input can't be empty or contain only whitespace")
                if guess.lower() == title.lower():
                    if i == 0:
                        points += 3
                        print("Correct! 3 points added.")
                    else:
                        points += 1
                        print("Correct! 1 point added.")
                    break
                else:
                    if i == 0:
                        print("Incorrect. Please try again.")
                    else:
                        print("Incorrect. Game over. The correct answer was", title)
            except ValueError as e:
                print(e)
        if i == 1:
            break
        play_again = input("Would you like to play again? (yes/no)")
        if play_again.lower() == "no":
            break
        else:
            continue

    # 6. Display the number of points the player has when the game ends
    print("Total points: ", points)

    # 7. Store the name of the player and their score in an external files
    try:
        with open("scores.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([username, points])
    except FileNotFoundError:
        print("scores.csv is missing, please check if the file is present in the correct location or create the file.")

    # 8. Display the score and player name of the top 5 winning scores from the external file
    scores = []
    try:
        with open("scores.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                scores.append(row)

        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
        print("Top 5 scores:")
        for i in range(min(5, len(scores))):
            print(i+1, ": ", scores[i][0], " - ", scores[i][1])
    except FileNotFoundError:
        print("scores.csv is missing, please check if the file is present in the correct location or create the file.")