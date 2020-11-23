vals = {"A" : 0, "B" : 0}
curr = input().split(" ")

while curr[0] != "7":
    if curr[0] == "1":
        vals[curr[1]] = int(curr[2])
    elif curr[0] == "2":
        print(vals[curr[1]])
    elif curr[0] == "3":
        vals[curr[1]] = vals[curr[1]] + vals[curr[2]]
    elif curr[0] == "4":
        vals[curr[1]] = vals[curr[1]] * vals[curr[2]]
    elif curr[0] == "5":
        vals[curr[1]] = vals[curr[1]] - vals[curr[2]]
    elif curr[0] == "6":
        vals[curr[1]] = vals[curr[1]] // vals[curr[2]]
    curr = input().split()