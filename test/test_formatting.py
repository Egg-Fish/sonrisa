from sonrisa.functions import formatting

def test_convert_12_to_24():
    cases = [
        [["12:00", "am"], "0000"],
        [["12:00", "pm"], "1200"],
        [[ "1:00", "am"], "0100"],
        [["10:00", "am"], "1000"],
        [[ "1:00", "pm"], "1300"],
        [["10:00", "pm"], "2200"]
    ]

    for i in range(len(cases)):
        case = cases[i]

        test = formatting.convert_12_to_24(case[0][0], case[0][1])

        if test != case[1]:
            print("test_convert_12_to_24():")
            print("Case {}: {} {} -> {}".format(i+1, case[0][0], case[0][1], case[1]))
            print("Result: {}". format(test))
            print("Status: FAIL\n")

def test_date_to_day_number():
    cases = [
        ["1/1/20", 0],
        ["1/1/19", 0],
        ["1/1/21", 0],
        ["2/1/20", 1],
        ["31/12/20", 365],
        ["31/12/21", 364],
        ["1/2/20", 31],
        ["29/2/20", 59],
    ]

    for i in range(len(cases)):
        case = cases[i]

        test = formatting.date_to_day_number(case[0])

        if test != case[1]:
            print("test_date_to_day_number():")
            print("Case {}: {} -> {}".format(i+1,case[0],case[1]))
            print("Result: {}".format(test))
            print("Status: FAIL\n")

def test_separate_categories():
    pass

def test_message_valid():
    pass

def test_strip_emoji():
    pass

def test_formatting():
    test_convert_12_to_24()
    test_date_to_day_number()
    test_separate_categories()
    test_message_valid()
    test_strip_emoji()