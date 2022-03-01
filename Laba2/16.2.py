# 4
# Дама,сдавала в багаж
# диван, чемодан, саквояж
# картину, корзину, картонку
# и маленькую собачонку,,
# 4
# 0,0
# 1,2
# 3,1
# 3,0

text = []
lineCount = int(input("Введите количество строк: "))
for i in range(lineCount):
    line = input().split(",")
    text.append(line)
print(text)
wordCount = int(input("Введите количество необходимых слов: "))
for i in range(wordCount):
    coordinate = [int(i) for i in input("Координаты слова: ").split(", ")]
    d = text[coordinate[0]]
    word = d[coordinate[1]]
    print(word)
