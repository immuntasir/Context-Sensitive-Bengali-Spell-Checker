od = open("out.txt", "r")

temstr=od.read().split()
M = {}
for temstrs in temstr:
    M[str(temstrs)] = 1

od.close()

od = open("dict.txt", "r")
md = open("dictionary.txt", "w")

temstr=od.read().split()

for temstrs in temstr:
    if temstrs in M:
        md.write(temstrs + '\n')

od.close()
md.close()
