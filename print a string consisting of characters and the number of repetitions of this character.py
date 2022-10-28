text = input('введите строку')
first = text[0]
count = 0
result = ''
for c in text:
    if c == first:
        count += 1
    else:
        result += first + str(count)
        first = c
        count = 1
result += first + str(count)
print(result)
