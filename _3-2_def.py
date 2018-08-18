import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'That\'s right.'
    elif answer_number == 2:
        return 'Absolutely.'
    elif answer_number == 3:
        return 'Yes.'
    elif answer_number == 4:
        return 'Not sure, try again.'
    elif answer_number == 5:
        return 'Tell me later.'
    elif answer_number == 6:
        return 'Ask me carefully.'
    elif answer_number == 7:
        return 'No.'
    elif answer_number == 8:
        return 'Looks not so good.'
    elif answer_number == 9:
        return 'Doubtful.'

r = random.randint(1, 9)
print(get_answer(r))
