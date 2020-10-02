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
        print("Case {}: {} {} -> {}".format(i+1, case[0][0], case[0][1], test))
