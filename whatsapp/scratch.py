def test():
    test_date = {
        "Key1" : "response1",
        "Key2" : "response"
    }
    for key in test_date:
        if "Key1" in key:
            print(test_date[key])
    if "Key3" in test_date.keys():
        print("Success")

    print(test_date.keys())
    print(test_date)


test()