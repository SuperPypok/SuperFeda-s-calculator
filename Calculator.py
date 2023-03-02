# Кучерявый калькулятор (RU, EN, CH and DE)

lang = "asdff"        # Здесь я переиграл stupid dutch python, сохранил в переменные всякие не понятные штуки, чтобы он мне не говорил: " NameError: name 'aboba' is not defined ".
aboba = "fg"          # А потом инпутами в следущих строках перезаписал информацию, чтобы while мне её посравнивал, и если пользватель ввёл черт пойми чо, то заставил его снова и снова вводить информацию.
while lang != "RU" and lang != "EN" and lang != "CH" and lang != "DE":   # Операция выбора яыка.
    print("Select language, RU, EN, CH or DE")   # print("") - выводит написанный в ковычках текст в консоль.
    lang = input()                    # input() - сохраняет в переменную (буква перед "=") информацию которую вводит пользователь.
    lang = lang.upper()               # Делает все буквы, введенные в переменную "lang" заглавными.
    if lang == "RU":
        print("Калькулятор для деления, умножения, сложения и тому подобных действий.")
        print("Продолжить?")
    elif lang == "EN":
        print("A calculator for division, multiplication, integer division and similar operations.")
        print("Continue?")
    elif lang == "CH":
        print("一个用于除法、乘法、加法等的计算器。")
        print("我可以继续吗？")
    elif lang == "DE":
        print("Rechner für Division, Multiplikation, Addition und dergleichen.")
        print("Weiter?")

while aboba != "yes" and aboba != "Yes" and aboba != "да" and aboba != "Да" and aboba != "是" and aboba != "ja" and aboba != "Ja":  # Проверка на то, что ввёл пользователь. Если он ввел не "да", то ему снова
    if lang == "RU":                                                                                                                # напишется "(Если нет, введите 'нет', если да, то 'да')"
        print('(Если нет, введите "нет", если да, то "да")')
        aboba = input()
    elif lang == "EN":
        print('(If no, enter "no", if yes, enter "yes")')
        aboba = input()
    elif lang == "CH":
        print('(如果没有，请输入 "没有"，如果有，请输入 "有"）。')
        aboba = input()
    elif lang == "DE":
        print('(Wenn nein, geben Sie "nein" ein, wenn ja, geben Sie "ja" ein)')
        aboba = input()

if lang == "RU":
    while aboba == "да" or aboba == "Да":
        print("Введите первое число:")
        a = float(input())
        print("Введите второе число:")
        b = float(input())
        c = "sdfg"  # Тут тот же самый ход мегамозга, что и в самом начале кода.
        while c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":      # Проверка, если пользватель ввёл не то что нужно,
            print("Введите действие (* + - : % ** //) :")                                                    # то заствил его ввеодить это снова. (Это правда.)
            c = input() # В этой строке нет "int()" потому что это действие заставляет Python воспринивать введенную
            # Информацию как число, а в данном случае это совсем не нужно. Если сделать так, то код может работать не правильно.
            if c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
                print("Такого действия нет.")

        if b == 0 and c in ("//", ":", "%"):  # Проверяет ввел ли пользователь в пременную "b" ноль, и не начал ли он на него делить.
            print("На ноль делить нельзя!")   # Это действие в коде нужно для того, чтобы исправить ошибку "НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ".

        elif c == "+":                        # Тут идет сравнение введенной информации в переменную "с".
            print(a, "+", b, "=", a + b)      # Если она будет ровна "+", то соответственно выражение будет складываться.
        elif c == "-":                        # И так с умножением, вычитанием, делением и т.д.
            print(a, "-", b, "=", a - b)
        elif c == "*":
            print(a, "*", b, "=", a * b)
        elif c == ":":
            print(a, "/", b, "=", a / b)
        elif c == "%":
            print(a, "%", b, "=", a % b)
        elif c == "//":
            print(a, "//", b, "=", a // b)
        elif c == "**":
            print(a, "**", b, "=", a ** b)

        while aboba != "да" or aboba != "Да":                                                                # Здесь идет очередная проверка, если пользователь ввёл что-то помимо "да",
            print('Хотите ли вы продолжить складывать числа? Если да, то введите "да", если нет, то "нет"')  # то процесс (тоесть весь калькулятор) полностью завершает работу.
            aboba = input()
            break

elif lang == "EN":
    while aboba == "yes" or aboba == "Yes":
        print("Enter the first number:")
        a = float(input())
        print("Enter the second number:")
        b = float(input())
        c = "sdfg"
        while c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
            print("Enter action (* + - : % ** //) :")
            c = input()
            if c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
                print("There is no such action.")

        if b == 0 and c in ("//", ":", "%"):
            print("You cannot divide by zero!")

        elif c == "+":
            print(a, "+", b, "=", a + b)
        elif c == "-":
            print(a, "-", b, "=", a - b)
        elif c == "*":
            print(a, "*", b, "=", a * b)
        elif c == ":":
            print(a, "/", b, "=", a / b)
        elif c == "%":
            print(a, "%", b, "=", a % b)
        elif c == "//":
            print(a, "//", b, "=", a // b)
        elif c == "**":
            print(a, "**", b, "=", a ** b)

        while aboba != "yes" or aboba != "Yes":
            print('Do you want to continue adding numbers? If yes, enter "yes", if no, enter "no".')
            aboba = input()
            break

elif lang == "CH":
    while aboba == "是":
        print("输入第一个数字。")
        a = float(input())
        print("输入第二个数字。")
        b = float(input())
        c = "sdg"
        while c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
            print("输入动作（* + - : % ** //）。")
            c = input()
            if c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
                print("没有这样的行动。")

        if b == 0 and c in ("//", ":", "%"):
            print("你不能除以零!")

        elif c == "+":
            print(a, "+", b, "=", a + b)
        elif c == "-":
            print(a, "-", b, "=", a - b)
        elif c == "*":
            print(a, "*", b, "=", a * b)
        elif c == ":":
            print(a, "/", b, "=", a / b)
        elif c == "%":
            print(a, "%", b, "=", a % b)
        elif c == "//":
            print(a, "//", b, "=", a // b)
        elif c == "**":
            print(a, "**", b, "=", a ** b)

        while aboba != "是":
            print('你想继续添加数字吗？如果是，请输入 "是"，如果不是，请输入 "不是"。')
            aboba = input()
            break

elif lang == "DE":
    while aboba == "yes" or aboba == "Yes" or aboba == "ja" or aboba == "Ja":
        print("Geben Sie die erste Zahl ein:")
        a = float(input())
        print("Geben Sie die zweite Nummer ein:")
        b = float(input())
        c = "sdfg"
        while c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
            print("Aktion eingeben (* + - : % ** //) :")
            c = input()
            if c != "*" and c != "+" and c != "-" and c != ":" and c != "**" and c != "//" and c != "%":
                print("Eine solche Maßnahme gibt es nicht.")

        if b == 0 and c in ("//", ":", "%"):
            print("Man kann nicht durch Null dividieren!")

        elif c == "+":
            print(a, "+", b, "=", a + b)
        elif c == "-":
            print(a, "-", b, "=", a - b)
        elif c == "*":
            print(a, "*", b, "=", a * b)
        elif c == ":":
            print(a, "/", b, "=", a / b)
        elif c == "%":
            print(a, "%", b, "=", a % b)
        elif c == "//":
            print(a, "//", b, "=", a // b)
        elif c == "**":
            print(a, "**", b, "=", a ** b)

        while aboba != "yes" or aboba != "Yes" or aboba != "ja" or aboba != "Ja":
            print('Möchten Sie weiterhin Zahlen hinzufügen? Wenn ja, geben Sie "ja" ein, wenn nein, geben Sie "nein" ein.')
            aboba = input()
            break
            # if aboba == "No" or aboba == "no" or aboba == "keine" or aboba == "Keine" or aboba == "nein" or aboba == "Nein":