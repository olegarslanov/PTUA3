m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

a, b, c = map(int, input().split())

result = ""
for i, n in enumerate([a, b, c]):
    nota = m[n - 1]
    result += "#" + nota if nota in (m[0], m[3]) else nota
    if i < 2:
        result += " "

print(result)
