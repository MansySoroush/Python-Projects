# print logo
import art

print(art.logo)
print("Welcome to the Higher/Lower Game!\n")

# fetch two random data from the data, A & B
import random
from game_data import data

score = 0


def check_new_score(result):
    global score

    if result:
        score += 1


def check_answer(answer, p_a, p_b):
    answer_correct = False
    p_a_cnt = p_a["follower_count"]
    p_b_cnt = p_b["follower_count"]

    if (answer.lower() == "a" and p_a_cnt > p_b_cnt) or (answer.lower() == "b" and p_b_cnt > p_a_cnt):
        answer_correct = True

    check_new_score(answer_correct)
    print(f"Your score is {score}")

    if not answer_correct:
        print(f"Sorry, that's wrong. Final score: {score}")
        _name = p_b["name"] if answer.lower() == "a" else p_a["name"]
        _followers = p_b_cnt if answer.lower() == "a" else p_a_cnt
    else:
        print(f"Congrats! that's correct. Final score: {score}")
        _name = p_a["name"] if answer.lower() == "a" else p_b["name"]
        _followers = p_a_cnt if answer.lower() == "a" else p_b_cnt

    print(f"The Correct Answer is: {_name} with {_followers} followers")

    return answer_correct


def get_random_data():
    return random.choice(data)


def play_game():
    """ Return False if the user's answer is correct, otherwise return True"""
    person_a = get_random_data()
    person_b = get_random_data()

    while person_a == person_b:
        person_b = get_random_data()

    print(f'Compare A: {person_a["name"]}, {person_a["description"]}, from {person_a["country"]}')
    print(art.vs)
    print(f'Against B: {person_b["name"]}, {person_b["description"]}, from {person_b["country"]}')

    user_answer = input("\nWho has more followers? Type 'A' or 'B':")
    answer_correct = check_answer(answer=user_answer, p_a=person_a, p_b=person_b)

    return not answer_correct


game_over = False
while not game_over:
    game_over = play_game()

    if game_over:
        play_again = input("\nDo you want to play again? Type 'y' or 'n'\n: ")
        if play_again.lower() == 'y':
            game_over = False
