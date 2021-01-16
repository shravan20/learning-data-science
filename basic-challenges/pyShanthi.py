def change_charater_case(str):
    result = ""
    for letter in str:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result
print(change_charater_case("Www.GooGle.com"))
