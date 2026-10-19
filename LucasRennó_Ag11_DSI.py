from colorama import Fore, Style, init

# Inicializa o colorama para resetar as cores automaticamente
init(autoreset=True)

# Lista simples apenas com os textos das situações
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def mostrar_alerta(nivel):
    # O nível vai de 1 a 5, mas os itens na lista começam no índice 0.
    # Por isso usamos (nivel - 1).
    if nivel == 1:
        print(f"{Fore.RED}Nível {nivel}: {niveis[0]}")
    elif nivel == 2:
        print(f"{Fore.YELLOW}Nível {nivel}: {niveis[1]}")
    elif nivel == 3:
        print(f"{Fore.GREEN}Nível {nivel}: {niveis[2]}")
    elif nivel == 4:
        print(f"{Fore.CYAN}Nível {nivel}: {niveis[3]}")
    elif nivel == 5:
        print(f"{Fore.BLUE}Nível {nivel}: {niveis[4]}")
    else:
        print(f"{Fore.RED}Nível inválido!")

# Programa Principal
print("--- Controle de Nível de Água ---")

# Testa todos os níveis de 1 a 5 usando um laço de repetição
for i in range(1, 6):
    mostrar_alerta(i)
