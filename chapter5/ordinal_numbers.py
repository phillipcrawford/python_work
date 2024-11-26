base = []
for value in range(1,10):
    if value == 1:
        mod = f"{value}st"
        base.append(mod)
        print(mod)
    elif value == 2:
        mod = f"{value}nd"
        base.append(mod)
        print(mod)
    elif value == 3:
        mod = f"{value}rd"
        base.append(mod)
        print(mod)
    else:
        mod = f"{value}th"
        base.append(mod)
        print(mod)

