def assertAreEqual(original, expected):
    out = translateNumber(original)
    print '%s == %s : %s' % (original, expected, out == expected)

def translateNumber(number):
    if (number is None or number == ""):
        return ""
    elif (len(str(number)) == 1):
      return ["zero","one","two","three","four","five","six","seven","eight","nine"][number]
    elif (len(str(number)) == 2 and number > 9 and number < 20):
        return ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][number - 10]
    else:
        return ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][(number/10)-2]
    
    
    
assertAreEqual("", "")
assertAreEqual(None, "")
assertAreEqual(0, "zero")
assertAreEqual(1, "one")
assertAreEqual(9, "nine")
assertAreEqual(10, "ten")
assertAreEqual(15, "fifteen")
assertAreEqual(20, "twenty")