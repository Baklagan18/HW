print("Игра в Камень, Ножницы, Бумага.")
import random

def get_computer():
  possible_action = ["Камень","Ножницы","Бумага"]
  computer_choice = random.choice(possible_action)
  return computer_choice

def get_user():
  while True:
    user_choice = int(input("Чем будете ходить?: Камень -1, Ножницы -2, Бумага-3: "))  
    if user_choice in [1,2,3]:
     return user_choice
    else:
     print("Повторите попытку")

def comparison_action(computer_choice, user_choice):
  possible_action = {1:"Камень", 2:"Ножнцы", 3:"Бумага"}
  user_action = possible_action[user_choice]
  computer_action = computer_choice
  print(f"Вы выбрали {user_action}")
  print(f"Компьютер выбрал {computer_choice}")
  if user_action == computer_action:
   return "Ничья"
#   print("Ничья")
  elif (user_action == "Камень" and computer_action == "Ножницы" or user_action == "Ножницы" and computer_action == "Бумага" or user_action == "Бумага" and computer_action == "Камень"):
   return "Попеда"
#   print("Выигрыш")
  else:
   return "Проигрыш"
    
def exit_answer():  
  answer = int(input("Выйти из игры?: Да - 1, Нет - 2: "))
  return answer

def game():
  while True:
    user_choice = get_user()
    computer_choice = get_computer()
    result_game= comparison_action(computer_choice, user_choice)
    print(result_game)
    if exit_answer() == 1:
      print("Игра закончена")
      break
 
game()
