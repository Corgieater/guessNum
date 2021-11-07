from random import randint
print("Let's play guessing number")
print("The number is between 1-100, go ahead!")


def time_limit():
    """
    Limit guessing times
    """
    mode = input("Easy or hard mode? easy/hard\n").lower()
    while mode != "easy" and mode != "hard":
        print("Invalid input")
        mode = input("Easy or hard mode? easy/hard\n").lower()
    if mode == "easy":
        guess_times = 10
        print("You have 10 chances to guess!")
        return guess_times
    elif mode == "hard":
        guess_times = 5
        print("You have 5 chances to guess!")
        return guess_times


def random_num():
    """Return a random number"""
    return randint(1, 100)


def play():
    """Game itself"""
    keep_playing = True
    while keep_playing:
        player_lives = time_limit()
        ans = random_num()
        game_over = False
        while player_lives != 0 and game_over is not True:
            player = int(input("Guess a number\n"))
            if player < ans:
                print("Too low\nTry again")
                player_lives -= 1
                print(f"{player_lives} chances left")
            elif player > ans:
                print("Too high\nTry again")
                player_lives -= 1
                print(f"{player_lives} chances left")
            else:
                print(f"Win! The answer was {ans}")
                game_over = True
        if player_lives == 0:
            print("You lose:(")
        play_again = input("Another run? y/n\n").lower()
        if play_again != "y":
            print("OK, bye!")
            keep_playing = False


try:
    play()
except Exception as e:
    print(e)
