import random


logo = """              _ _       _       _                    _   _   __                           
     /\      | (_)     (_)     | |                  | \ | | /_/                           
    /  \   __| |___   ___ _ __ | |__   ___    ___   |  \| |_   _ _ __ ___   ___ _ __ ___  
   / /\ \ / _` | \ \ / / | '_ \| '_ \ / _ \  / _ \  | . ` | | | | '_ ` _ \ / _ \ '__/ _ \ 
  / ____ \ (_| | |\ V /| | | | | | | |  __/ | (_) | | |\  | |_| | | | | | |  __/ | | (_) |
 /_/    \_\__,_|_|_\_/ |_|_|_|_|_| |_|\___|  \___/  |_| \_|\__,_|_| |_| |_|\___|_|  \___/ 
        |  _ \_   _| |    / __ \| |/ /    /\   | |  | |                                   
  ______| |_) || | | |   | |  | | ' /    /  \  | |__| |                                   
 |______|  _ < | | | |   | |  | |  <    / /\ \ |  __  |                                   
        | |_) || |_| |___| |__| | . \  / ____ \| |  | |                                   
        |____/_____|______\____/|_|\_\/_/    \_\_|  |_|                                   
                                                                                          
                                                                                          """

print(logo)
print("Seja bem-vindo ao 'Adivinhe o Número' de BILOKAH!")
print("Pensei em um número entre 1 e 100.")

correct_number = random.randrange (1, 101)

while True:
    difficulty = input("Escolha uma dificuldade: 'fácil' ou 'difícil': ")
    
    if difficulty == "fácil" or difficulty == "facil":
        trys = 10
        break
    elif difficulty == "difícil" or difficulty == "dificil":
        trys = 5
        break
    else:
        print("Resposta inválida.")


while trys != 0:
    print(f"Você tem {trys} chances.")
    number_guessed = input("Adivinhe um número: ")
    if not number_guessed.isnumeric():
        print("Inválido!!!")
        continue
    else:
        number_guessed = int(number_guessed)

        if number_guessed not in range (1, 101):
            print("Inválido!!!")
            continue
        else:
        
            if number_guessed != correct_number:
                if number_guessed > correct_number:
                    print("𝑴𝒖𝒊𝒕𝒐 𝒂𝒍𝒕𝒐!")
                    trys -= 1
                if number_guessed < correct_number:
                    print("𝑴𝒖𝒊𝒕𝒐 𝒃𝒂𝒊𝒙𝒐!")
                    trys -= 1
            else:
                print(f"Acertou! O número correto é {correct_number}!")
                break
        
            if trys == 0:
                print("Você não tem mais chances. Perdeu!")
            
    
    
    
    
    
    
