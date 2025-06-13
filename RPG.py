import random
import time
print("=" * 40)
print("{:^40}".format("🛡️  MUNDO DE AVENTURAS  🗡️"))
print("=" * 40)
print("\n----- BEM-VINDO A ESTA JORNADA! -----\n")

nome = input("🧙‍♂️  Entre com seu nome de aventureiro: ")
print()
print("  (*)   ")
print(" 0/|\\| ")
print("  / \\  ")
print()
print(f"\n✨ Olá, {nome}! Prepare-se para o desafio.\n")

print("Escolha sua classe para começar:")

print("1 - 🗡️  CAVALEIRO")
print("    />")
print("   /#\\     🛡️  CAVALEIRO")
print("  |###|    Forte e corajoso!")
print("  |###|")
print("  |###|")
print("   | |")
print("  /   \\")
print()
print("2 - ✝️  CLÉRIGO")
print("    __")
print("   (oo)   ✝️  CLÉRIGO")
print("  /|==|\\  Mestre das curas!")
print("   ||||")
print("   ||||")
print()
print("3 - ⚔️  PALADINO")
print("    /\\")
print("   /__\\    ⚔️ PALADINO")
print("  |/  \\|   Guerreiro da luz!")
print("  | () |")
print("  |____|")
print("   |  |")
print("  /____\\")
print()

classe = int(input("➡️  Qual sua escolha? (1-3): "))

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
    print("    ( )")
    print("   (o_o)   🧺 CAMPONÊS")
    print("  /( : )\\  Simples, mas valente.")
    print("   / \\")
    print("  /   \\")

magia = ataque * 1.4

print(f"\n/STATUS/\nClasse: {tipo}\nLife: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
print(f"Você está pronto para sua jornada, {nome}! Boa sorte!!!\n")

def inimigos(life, atk, spd):
    return {"vida": life, "ataque": atk, "spd": spd}

goblin = inimigos(70, 20, 30)
esqueleto = inimigos(50, 35, 20)
orc = inimigos(100, 25, 25)
dragao = inimigos(170, 60, 10)

monstros = [
    ("Goblin", goblin),
    ("Esqueleto", esqueleto),
    ("Orc", orc),
    ("Dragão", dragao)
]

escolha = True
while escolha:
    print("       /\\")
    print("      /  \\")
    print("     /____\\   ⛺ ACAMPAMENTO")
    print("    /\\    /\\")
    print("   /__\\  /__\\")
    print("\n╔══════════════════════╗")
    print("║ O que deseja fazer? ║")
    print("╠══════════════════════╣")
    print("║ 1 - 🗺️ Explorar        ║")
    print("║ 2 - 💤 Descansar       ║")
    print("║ 3 - 📈 Evoluir Status ║")
    print("║ 4 - 📚 Bisbilhotar    ║")
    print("║ 5 - ❌ Sair do Jogo   ║")
    print("╚══════════════════════╝")
    caminho = int(input(">>> "))

    if caminho == 1:
        nome_monstro, monstro = random.choice(monstros)
        monstro["vida"] = random.randint(50, 120)
        print(f"\nVocê encontrou um {nome_monstro}!")
        print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")
        print(f"Status do monstro: {monstro}")

        if nome_monstro == "Dragão":
            print("Você se depara com uma fera abominável temida por todos ")
            print("-------UM DRAGÃO!!!!!!!-------")
            print("               _______________")
            print("   ,===:'.,            `-._")
            print("        `:.`---.__         `-._  🐉 DRAGÃO")
            print("          `:.     `--.         `.")
            print("            \\.        `.         `.")
            print("    (,,(,    \\.         `.   ____,-`.,")
            print(" (,'     `/   \\.   ,--.___`.'")
            print("      ,  `._    \\_/       `-")
            print("           `-.__.'")

        if nome_monstro == "Esqueleto":
            print("Você encontra uma criatura terrível, um Esqueleto!!!")
            print("   _____ ")
            print("  /     \\")
            print(" | () () |   💀 ESQUELETO")
            print("  \\  ^  /    Ossos que se movem...")
            print("   |||||")
            print("   |||||")

        if nome_monstro == "Orc":
            print("De todas as bestas que você poderia encontrar... um Orc!")
            print("   .----.")
            print("  / .===.\\   👹 ORC")
            print("  \/ 6 6 \\/   Feroz e brutal!")
            print("  ( \\___/ )")
            print("  ^^-----^^")

        if nome_monstro == "Goblin":
            print("Você encontrou um goblin da floresta")
            print("    ,      ,")
            print("   /(.-\"\"-.)\\   👺 GOBLIN")
            print("   |\\ o o /|    Pequeno e traiçoeiro.")
            print("   \\   ᴥ   /")
            print("   /'-._.-'\\")
            print("  //     \\\\")
            print(" ||       ||")
            print(" ||       ||")
            print("  \\__||__/")

        while monstro["vida"] > 0 and vida > 0:
            print("\n📜 Escolha sua ação:")
            print("🔸 [1] ✦⚔️ Combater")
            print("🔸 [2] ✦💖 Restaurar Vida")
            print("🔸 [3] ✦🔮 Usar Magia")
            print("🔸 [4] ✦🌀 Tentar Escapar")

            acao = int(input(">>> "))
            if acao == 1:
                monstro["vida"] -= ataque
                print("\nVocê se prepara para atacar!")
                time.sleep(0.4)
                print("   *    ")
                time.sleep(0.2)
                print("  /|\\   ")
                time.sleep(0.2)
                print("  / \\ ⚔️")
                time.sleep(0.4)
                print("Você avança com sua espada!")
                time.sleep(0.5)
                print("     💥")
                print("   -⚔️->")
                time.sleep(0.3)
                print("Acertou um golpe poderoso!")
                print("Você avança rapidamente e desfere um golpe certeiro!")
                print(f"Você causou {ataque} de dano ao {nome_monstro}!")
                if monstro["vida"] <= 0:
                    print("╔══════════════════╗")
                    print("║  VITÓRIA É SUA!  ║")
                    print("╚══════════════════╝")
                    break
                vida -= monstro["ataque"]
                print(f"O {nome_monstro} atacou você e causou {monstro['ataque']} de dano!")
                print(f"Vida atual: {vida}")

            elif acao == 2:
                vida += 10
                print("\nVocê ergue as mãos aos céus...")
                time.sleep(0.5)
                print(" ✨✨✨")
                print("💖+10💖")
                time.sleep(0.5)
                print("   ✨ (•‿•) ✨")
                print("   VIDA RESTAURADA")
                print("Sua energia vital é restaurada!")
                print("Você se sente renovado!")
                print("Você recuperou 10 de vida!")
                print(f"Vida atual: {vida}")

            elif acao == 3:
                monstro["vida"] -= magia
                vida -= monstro["ataque"]
                print("Você conjura uma poderosa magia!")
                print("\nVocê concentra seu poder mágico...")
                time.sleep(0.5)
                print("    🔮")
                time.sleep(0.3)
                print("  ~~~💨~~~")
                time.sleep(0.3)
                print("   ⚡⚡⚡")
                time.sleep(0.5)
                print("Lança uma explosão mística!")
                print("   ✴️✨⚡✨✴️")
                print("   (∩｀-´)⊃━☆ﾟ.*･｡ﾟ")
                print("Você invoca uma explosão de energia mística!")
                print("      *💥*")
                print("Magia devastadora atinge o inimigo!")
                print(f"Causou {magia:.0f} de dano ao {nome_monstro}!")
                if monstro["vida"] <= 0:
                    print("╔══════════════════╗")
                    print("║  VITÓRIA É SUA!  ║")
                    print("╚══════════════════╝")
                    break
                print(f"O {nome_monstro} atacou você e causou {monstro['ataque']} de dano!")
                print(f"Vida atual: {vida}")

            elif acao == 4:
                if evasiva > monstro["spd"]:
                    print("\nVocê tenta fugir da batalha!")
                    time.sleep(0.5)
                    print("🏃💨💨")
                    time.sleep(0.3)
                    print("⌛ Avaliando chance de fuga...")
                    time.sleep(0.5)
                    print("🌪️🌀 Você corre entre as sombras...")
                    print("Você fugiu do combate!")
                    break
                else:
                    print("\nVocê tenta fugir da batalha!")
                    time.sleep(0.5)
                    print("🏃💨💨")
                    time.sleep(0.3)
                    print("⌛ Avaliando chance de fuga...")
                    time.sleep(0.5)
                    print("Você não conseguiu fugir! O combate continua.")
                    vida -= monstro["ataque"]
                    print(f"O {nome_monstro} atacou você e causou {monstro['ataque']} de dano!")
            else:
                print("Ação inválida.")
        if vida <= 0:
            print("\n💀💀💀 VOCÊ FOI DERROTADO! 💀💀💀\n")
            print("████████████████████████████████████████")
            print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
            print("██░░░░░░░░░░░░  GAME OVER  ░░░░░░░░░░░░░░██")
            print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
            print("████████████████████████████████████████")
            print("        █▄█ █▀█ █▄░█ █▀▀              ")
            print("        ░█░ █▄█ █░▀█ ██▄              ")
            print("\nVocê caiu em batalha, mas sua lenda viverá...")
            break

    elif caminho == 2:
        vida += 15
        print("Você descansou e recuperou 15 de vida!")
        print(f"Sua vida atual: {vida}")

    elif caminho == 3:
        status = ["vida", "ataque", "evasiva"]
        escolhido = random.choice(status)
        valor = random.randint(1, 30)
        if escolhido == "vida":
            vida += valor
            print(f"Vida💖 aumentada para {vida} pontos")
        elif escolhido == "ataque":
            ataque += valor
            print(f"Ataque🗡️ aumentado para {ataque} pontos")
        elif escolhido == "evasiva":
            evasiva += valor
            print(f"Evasiva🌀 aumentada para {evasiva} pontos")
        print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")

    elif caminho == 4:
        print("Você vai em busca por novas riquezas e encontra um castelo")
        print("      |>>>")
        print("      |")
        print("  _  _|_  _   🏰 CASTELO")
        print(" |;|_|;|_|;|")
        print(" \\.    .  /")
        print("  \:  .  /")
        print("   ||:   |")
        print("   ||:.  |")
        print("   ||:  .|")
        print("   ||:   |")
        print(f"{nome} entra no castelo e encontra muitos livros...")
        print("Você encontrou um livro pedindo para derrotar mais monstros......")
        print(f"Life: {vida}\nAtk: {ataque}\nSpd: {evasiva}")

    elif caminho == 5:
        print("JOGO FINALIZADO| OBRIGADO POR JOGAR!!! :)")
        print("╔══════════════════╗")
        print("║ ESPERO QUE GOSTE ║")
        print("╚══════════════════╝")
        escolha = False
    else:
        print("Escolha inválida.")

        #
        # 🧙 Personagens
        # Extras
        # 🧙‍♂️
        # Mago
        # python
        # Copiar
        # Editar
        # print("     /^\\")
        # print("    / o \\   🧙 MAGO")
        # print("   |     |  Mestre das artes arcanas")
        # print("   | (*) |")
        # print("   |_____|")
        # print("     | |")
        # print("    /   \\")
        # 🦹 Ladino
        # python
        # Copiar
        # Editar
        # print("    (•_•)")
        # print("   <)   )╯  🗡️ LADINO")
        # print("    /   \\   Ágil e sorrateiro.")
        # 🧛 Vampiro
        # python
        # Copiar
        # Editar
        # print("   .-'''-.")
        # print("  / .===. \\  🧛 VAMPIRO")
        # print("  \/ 6 6 \\/  Criatura das sombras")
        # print("  ( \\___/ )")
        # print("___ooo__ooo___")
        # 📜 Animações
        # simples
        # com
        # texto(efeito
        # dramático)
        # Entrada
        # de
        # chefe
        # python
        # Copiar
        # Editar
        # print("⚠️ Uma presença sombria se aproxima...")
        # time.sleep(1)
        # print("⚠️ Você sente o chão tremer sob seus pés...")
        # time.sleep(1)
        # print("🔥 O CHEFE SUPREMO SURGE ANTE VOCÊ! 🔥")
        # 🎭 Emoções
        # e
        # expressões
        # 😠 Inimigo
        # irritado: >:(
        #
        #     😵 Jogador ferido: x_x
        #
        #     😎 Vitória épica: B-)
        #
        # 😱 Surpreso::O
        #
        # 💖 Cura: (｡♥‿♥｡)
        #
        # 💪 Subir
        # de
        # nível: (ง •̀_•́ ง)
#     print("     ()_()       🐀 RATO")
#     print("    ( o.o )      Rápido e sorrateiro.")
#     print("     > ^ <")
#
# print("      __     __")
# print("     /  \\~~~/  \\   🐀 RATO GIGANTE")
# print(" ,----(     . . )")
# print("/      \\__     @ )   Espreita pelos esgotos escuros...")
# print("\\_/|\\_/|  \\__/--/")
# print("  _| |_     ||")
# print(" (___)_)    ()")
