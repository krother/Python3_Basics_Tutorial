
code = {
    '   ': ' ',
    '  #': '#',
    ' # ': '#',
    ' ##': ' ',
    '#  ': '#',
    '# #': ' ',
    '## ': ' ',
    '###': ' ',
}

N = 32
line = " " * N + "#" + " " * N
for _ in range(N):
    print(line)
    new = " "
    for start in range(len(line) - 2):
        sub = line[start: start + 3]
        new += code[sub]
    line = new + " "
