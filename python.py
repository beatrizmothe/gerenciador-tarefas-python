# Cores ANSI para o texto colorido
verde = '\033[92m' # Mensagem de sucesso 
vermelho = '\033[91m' # Mensagem de erro e avisos
rosa = '\033[95m' # Mensagem de boas-vindas e despedida
azul = '\033[94m' # Títulos 
reset = '\033[0m' # Reseta a cor do texto 

tarefas = []

def adicionar_tarefa(descricao):
    tarefas.append({"Descrição": descricao, "Concluída": False})
    print(f"{verde}Tarefa '{descricao}' adicionada com sucesso!{reset}")

def visualizar_tarefa():
    if not tarefas:
        print(f"{vermelho}Nenhuma tarefa cadastrada.{reset}")
        return
    print(f"\n{azul}Tarefas cadastradas:{reset}")
    for i, tarefa in enumerate(tarefas):
        status = f"{verde}Concluída{reset}" if tarefa["Concluída"] else f"{vermelho}Pendente{reset}"
        print(f"{i + 1}. {tarefa['Descrição']} - {status}")

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["Concluída"] = True
        print(f"{verde}Tarefa '{tarefas[indice]['Descrição']}' marcada como concluída!{reset}")
    else:
        print(f"{vermelho}Índice inválido. Por favor, tente novamente.{reset}")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        descricao = tarefas.pop(indice)["Descrição"]
        print(f"{vermelho}Tarefa '{descricao}' removida com sucesso!{reset}")
    else:
        print(f"{vermelho}Índice inválido. Por favor, tente novamente.{reset}")

# Menu principal
def menu():
    print(f"{rosa}Olá! Bem-vindo ao sistema de gerenciamento de tarefas{reset}")
    while True:
        print(f"\n{rosa}Selecione uma opção:{reset}")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            descricao = input("Digite uma tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == '2':
            visualizar_tarefa()
        elif opcao == '3':
            visualizar_tarefa()
            try:
                indice = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
                concluir_tarefa(indice)
            except ValueError:
                print(f"{vermelho}Por favor, insira um número válido.{reset}")
        elif opcao == '4':
            visualizar_tarefa()
            try:
                indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                remover_tarefa(indice)
            except ValueError:
                print(f"{vermelho}Por favor, insira um número válido.{reset}")
        elif opcao == '5':
            print(f"{rosa}Obrigada por usar o nosso sistema. Até logo!{reset}")
            break
        else:
            print(f"{vermelho}Opção inválida. Por favor, tente novamente.{reset}")

menu()
