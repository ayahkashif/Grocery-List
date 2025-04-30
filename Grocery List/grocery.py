#control-d: EOFError
#output in all uppercase, sorted alphabetically
#number of times

list = {}

while True:
    try:
        item = input("").upper()
    except EOFError:
        break
    else:
        try:
            list[item]
        except KeyError:
            list.update({item: 1})
        else:
            list[item] += 1

for item in sorted(list):
    print(list[item], item)
