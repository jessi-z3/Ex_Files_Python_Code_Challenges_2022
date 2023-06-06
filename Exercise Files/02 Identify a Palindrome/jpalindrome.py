import string


def isPalindrome(answer):
    tester = []
    response = []
    for i in answer[::-1]:
        tester.append(i)
    for i in answer[::1]:
        response.append(i)
    if (tester == response):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    run = True
    while (run == True):
        answer = input("Enter a word to test or 'exit' to quit:")
        while (answer == 'exit'):
            run = False
            break
        else:
            answer = answer.translate(
                str.maketrans('', '', string.punctuation))
            answer = (answer.replace(" ", ""))
            answer = answer.lower()
            isPalindrome(answer)
