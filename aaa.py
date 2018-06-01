import time


def test(flag, sleep_time):
    for i in range(3):
        print(flag + ': ' + str(i))
        time.sleep(sleep_time)


def run():
    yield test('A', 3)
    yield test('B', 1)

for i in run():
    print(i)