def assertAreEqual(expected, actual):
    print expected == actual

def translateNumber(number):
    if (number is None or number == ""):
        return ""
    elif (len(str(number)) == 1):
      return ["zero","one","two","three","four","five","six","seven","eight","nine"][number]
    elif (len(str(number)) == 2 and number > 9 and number < 20):
        return ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][number - 10]
    else:
        return ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][(number/10)-2]
    
    
    
assertAreEqual(translateNumber(""), "")
assertAreEqual(translateNumber(None), "")
assertAreEqual(translateNumber(0), "zero")
assertAreEqual(translateNumber(1), "one")
assertAreEqual(translateNumber(9), "nine")
assertAreEqual(translateNumber(10), "ten")
assertAreEqual(translateNumber(15), "fifteen")
assertAreEqual(translateNumber(20), "twenty")