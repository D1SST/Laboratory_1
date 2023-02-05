from num2words import num2words

main_sequence = []
f = open("random.txt", "r")
main_sequence = [int(i) for i in f.read().split(",")]
for i in range(len(main_sequence)):
    if (main_sequence[i] != 0) and (main_sequence[i] % 2 == 0) and (main_sequence[i] <= len(main_sequence)):
        if (i % 2 != 0):
            print(num2words(main_sequence[i], lang = "ru"), "| иднекс числа -", i)

        else:
            print(main_sequence[i], "| индекс числа -", i)
        i += 1










