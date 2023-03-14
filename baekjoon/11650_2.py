from sys import stdin, stdout

coord = stdin.readlines()[1:]
coord.sort(key=lambda x: int(x.split()[1]))
coord.sort(key=lambda x: int(x.split()[0]))
stdout.write(''.join(coord))