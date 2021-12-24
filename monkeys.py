import random

list_of_letters = "abcdefghijklmnopqrstuvwxyz "
answer = "monkeys will try to type this text at random but every time they keep the correct letters"
ans_len = len(answer)

def gen(word):
    word_list = [x for x in word]
    for i in range(ans_len):
        if (word_list[i] != answer[i]):
            word_list[i] = list_of_letters[random.randint(0,26)]
    return "".join(word_list)

def compare(word):
    score = 0
    for i in range(ans_len):
        if (word[i] == answer[i]):
            score += 1
    return score / float(ans_len)

def main():
    word = ["" for x in range(ans_len)]
    #print(word)
    word = gen(word)
    count = 1
    while (compare(word) != 1):
        word = gen(word)
        count += 1
        if (count % 1 == 0):
            print(f"Attempt {count:>6}: Score: {compare(word):>6.2f}")

main()