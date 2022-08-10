lines = []
with open('prueba.txt') as f:
    lines = f.readlines()
count = 0
contador=0
for line in lines:
    count += 1
    duos = line.count("el")
    print(f'line {count}: {line}')
print(f"la palabra (el) aparece:  {duos}")


