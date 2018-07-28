def romanToNumber(roman):
     #roman = romano
     #listOfRomans = list(roman)
     #print(listOfRomans)
     nums = []
     dict = {"IV":4, "IX":9, "XL":40, "XC":90, "I":1, "V":5, "X":10, "L":50, "C":100}
     i = 0
     print("C")

     if roman.count("IV"):
        nums.append(4 * roman.count("IV"))
        roman = roman.replace("IV", "")#, roman.count("IV"))
     if roman.count("IX"):
        nums.append(9 * roman.count("IX"))
        roman = roman.replace("IX", "")
     if roman.count("XI"):
        nums.append(11)
        roman = roman.replace("XI", "")
     if roman.count("XL"):
        roman.replace("XL", "")
        nums.append(40 * roman.count("XL"))
     if roman.count("XC"):
        roman = roman.replace("XC","")
        nums.append(90)
     if roman.count("I"):
        nums.append(1 * roman.count("I"))
        roman = roman.replace("I", "")
     if roman.count("V"):
        roman = roman.replace("V", "")
        nums.append(5)
     if roman.count("X"):
        roman = roman.replace("X","")
        nums.append(10)
     if roman.count("L"):
        roman = roman.replace("L", "")
        nums.append(50)
     if roman.count("C"):
        roman = roman.replace("C", "")
        nums.append(100)

     return nums

r = "XCVIIIIIII"
x = romanToNumber(r)
print(x)
#p = "hello wisam"
#p = p.replace("wisam", "sir")
#print(p)