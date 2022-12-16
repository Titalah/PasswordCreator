import termcolor

OK_TAG = f"[ {termcolor.colored('OK', 'green')}]"
KO_TAG = f"[ {termcolor.colored('KO', 'red')}]"


def check(res, answer):
    assert res == answer


def testeur(name, res, answer):
    try:
        check(res, answer)
    except AssertionError as err:
        print(f"{KO_TAG} {name}, expected {answer} got {res}")
    else:
        print(f"{OK_TAG} {name}")
