text = input()
shift = input()
modShift = shift
checkStr = []
shiftStrings = []
shiftContain = ""

for i in range (len(shift)):
    modShift = modShift[1:] + modShift[0]
    shiftStrings.append(modShift)

for i in range (len(text) - len(shift)+1):
    checkStr.append(text[i:len(shift)+i])

for i in range(len(shiftStrings)):
    for x in range(len(checkStr)):
        if shiftStrings[i] != checkStr[x]:
            shiftContain = "no"
        else:
            shiftContain = "yes"
            break
    if shiftContain == "yes":
        break

print(shiftContain)
