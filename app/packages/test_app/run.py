import sys


def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    # they are the same:
    user_input = input('need a input to inside')
    # print('need a input to inside')
    # user_input = sys.stdin.readline()

    user_password = input('your password?')

    feedback = test_func(user_input)
    print(feedback)
    confirm = sys.stdin.readline()
