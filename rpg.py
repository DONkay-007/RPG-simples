import random
"""Esse código todo está bem simples e bem identado, nesse só de entender cada parte do python ele """
"""não precisa de muita explicação"""
print("-----BEM VINDO-----")
nome = input("Entre com seu nome de usuário: ")
print(f"Olá {nome}")
print("ESCOLHA SUA CLASSE PARA COMEÇAR:")
print("1-CAVALEIRO 2-CLÉRIGO 3-PALADINO")

classe = int(input("Qual sua escolha? :"))

if classe == 1:
    tipo = "CAVALEIRO"
    vida = 100
    ataque = 30
    evasiva = 25
elif classe == 2:
    tipo = "CLÉRIGO"
    vida = 75
    ataque = 40
    evasiva = 40
elif classe == 3:
    tipo = "PALADINO"
    vida = 130
    ataque = 20
    evasiva = 30
else:
    tipo = "CAMPONÊS"
    vida = 50
    ataque = 10
    evasiva = 10
    print("Classe inválida. Você será um CAMPONÊS... boa sorte.")

print(f"\n/STATUS/\nClasse: {tipo}\nLife: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
print(f"Você está pronto para sua jornada, {nome}! Boa sorte!!!\n")

def inimigos(life, atk, spd):
    return {"vida": life, "ataque": atk, "spd": spd}


goblin = inimigos(70, 20, 30)
esqueleto = inimigos(50, 35, 20)
troll = inimigos(100, 10, 25)
boss = inimigos(130, 40, 10)

monstros = [
    ("Goblin", goblin),
    ("Esqueleto", esqueleto),
    ("Troll", troll),
    ("Boss", boss)
]
escolha=True
while escolha == True:
    caminho = int(input("\nEscolha o que deseja fazer:\n"
                        "1 - Explorar\n"
                        "2 - Descansar\n"
                        "3 - Evoluir um Status\n"
                        "4 - Bisbilhotar\n"
                        "5 - Sair do jogo\n"
                        ">>> "))
    if caminho == 1:
        nome_monstro, monstro = random.choice(monstros)
        monstro["vida"] = random.randint(50, 120)
        print(f"\nVocê encontrou um {nome_monstro}!")
        print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
        print(f"Status do monstro: {monstro}")

        while monstro["vida"] > 0 and vida > 0:
            acao = int(input("\nO que deseja fazer?\n"
                             "1 - Atacar\n"
                             "2 - Recuperar Vida\n"
                             "3 - Fugir\n"
                             ">>> "))
            if acao == 1:
                monstro["vida"] -= ataque
                print(f"Você causou {ataque} de dano ao {nome_monstro}!")
                if monstro["vida"] <= 0:
                    print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
                    print(f"Você derrotou o {nome_monstro}!")
                    break
                vida -= monstro["ataque"]
                print(f"O {nome_monstro} atacou você e causou {monstro['ataque']} de dano!")
                print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
                print(f"Vida atual: {vida}")
            elif acao == 2:
                vida += 10
                print("Você recuperou 10 de vida!")
                print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
                print(f"Vida atual: {vida}")
            elif acao == 3:
                if evasiva > monstro['velocidade']:
                    print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
                    print("Você fugiu do combate!")
                    break
                else:
                    print("Você não conseguiu fugir! O combate continua.")
                    print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
            else:
                print("Ação inválida.")
        if vida <= 0:
            print("Você foi derrotado! Fim de jogo.")
            break
    if caminho == 2:
        vida+= 15
        print(f"Vocé recuperou 15 pontos de vida \n"
              f"Sua vida atual: {vida}")
    if caminho == 3:
        status = ["vida", "ataque", "evasiva"]
        escolhido = random.choice(status)
        if escolhido == "vida":
         vida += random.randint(1, 30)
         print(f"Vida aumentada para {vida} pontos")
         print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
        if escolhido == "ataque":
         ataque += random.randint(1, 30)
         print(f"ataque aumentada para {ataque} pontos")
         print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
        if escolhido == "evasiva":
         evasiva += random.randint(1, 30)
         print(f"Evasiva aumentada para {evasiva} pontos")
         print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
    if caminho == 4:
        print("Você encontrou um livro pedindo para derrotar mais montros......")
        print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
    if caminho == 5:
        print("JOGO FINALIZADO| OBRIGADO POR JOGAR!!!:)")
        escolha = False
