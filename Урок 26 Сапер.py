import random

def tab_generate():
    size = 3
    tab = ["?" for _ in range(size*size)]
    mine = random.sample(range(size*size), 1)
    for index in mine:
        tab[index] = '*'
    return tab

def print_tab(tab):
    size = 3
    row = '?'
    for i in range(size):
        print(' '.join(row*size))
        

def get_user():
    while True:
        row = int(input("Введите координату X от 0 до 2: "))
        col = int(input("Введите уоординату Y от 0 до 2: "))
        if col in [0,1,2] and row in [0,1,2]:
            return row, col
        else:
            print("Повторите попытку")

def exit_answer():
    answer = int(input("Выйти из игры?: да - 1, нет -2: "))
    return answer

def game():
    tab = tab_generate()
    size = 3
    while True:
        print_tab(tab)
        row, col = get_user()
        index = row * size + col
        if tab[index] == '*':
            for i in range(size):
                print(' '.join(tab[size*i:(i+1)*size]))
            tab[index] == '*'
            print("Мина открылась!")
            break
        else:
            print("Вы открыли пустое поле")
        answer = exit_answer()
        if answer == 1:
            print("Игра закончена")
            break
        elif answer == 2:
            continue
        else:
            print("Выйти из игры?: да - 1, нет -2: ")
            continue
        
game()
