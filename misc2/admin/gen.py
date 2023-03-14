# https://png2svg.com/
# generate secret.svg.txt

# generate secret
with open('txt/mushroom.txt') as f:
    lines = f.readlines()
out = open("txt/secret.svg.txt", "w")
for line in lines:
    if "<g>" not in line:
        continue
    hex = line.split("fill=\"")[1].split("\"")[0]
    vals = line.split("d=\"")[1].split("\"")[0]
    vals = vals.replace(",", " ")
    vals = vals.replace("C", " C ")
    vals = vals.split()
    cmds = []
    nums = []
    for val in vals:
        try:
            nums.append(float(val))
        except Exception as e:
            cmds.append(val)

    out.write(f"{hex}\n")
    out.write(f"{''.join(cmds)}\n")
    out.write(f"{' '.join([str(x) for x in nums])}\n")
    out.write("\n")
out.close()


with open('txt/secret.svg.txt') as f:
    lines = f.readlines()


file = open('txt/test.svg', 'w')
file.write('''
<svg id="svg" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="2000"
    height="2000" >
    <g id="svgg">
''')

# solution
for path in range(0, len(lines), 4):
    hex = lines[path]
    cmds = lines[path + 1]
    vals = lines[path + 2].split()
    ind = 0
    arr = []
    for cmd in cmds[:-1]:
        if cmd == "M":
            arr.append("M")
            arr.extend(vals[ind:ind + 2])
            ind += 2
        elif cmd == "C":
            arr.append("C")
            arr.extend(vals[ind:ind + 6])
            ind += 6
        elif cmd == "Z":
            arr.append("Z")
        else:
            print(cmds)
            print(repr(cmd))
            assert False
    file.write(f"<path fill=\"{hex}\" d=\"{' '.join(arr)}\"></path>\n")
file.write("</g></svg>")


file.close()