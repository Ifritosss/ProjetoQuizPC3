print("+-------------------------------------------------------+")
print("|################### SHOW DO MILHÃO ###################|")
print("+-------------------------------------------------------+")

Reais = 0
count = 1
print("ESCOLHA ENTRE: \n 1 para Começar \n 2 para Sair")

Resposta = int(input("Digite sua escolha: "))

if Resposta == 1:
    print(">>>>Responda as perguntas com o número das alternativas!<<<<")
    print("\nPERGUNTA NUMERO 1")
    print("Qual o nome dado para o órgão responsável por distribuir a internet para os clientes? \n [Alternativa 1] - Modem \n [Alternativa 2] - Provedores de Internet \n [Alternativa 3] - IP/TCP \n [Alternativa 4] - Nenhuma dessas \n [Alternativa 5] - Placa de Rede")
    questao1 = int(input("Digite sua resposta: "))
    if questao1 == 2:
        print("Certa Resposta")
        print("Provedores de Internet são os órgão responsáveis pela distribuição de internet para as pessoas (clientes)")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Provedores de Internet que são os reponsáveis por distribuir internet para os clientes, a resposta correta era [Alternativa 2] - Provedores de Internet")
        Reais -= 1

    print("\nPERGUNTA NUMERO 2")
    print("Qual o protocolo de internet amplamente usado para transferência de páginas da web? \n [Alternativa 1] - FTP \n [Alternetiva 2] - SMTP \n [Alternativa 3] - HTTP \n [Alternativa 4] - TCP \n [Alternativa 5] - UDP")
    questao2 = int(input("Digite sua resposta: "))
    if questao2 == 3:
        print("Certa resposta!")
        print("O protocolo de internet usado para transferência de páginas é HTTP!")
        Reais += 1
    else:
        print("Resposta errada!")
        print("HTTP é o protocolo usado para transferência de páginas da web, você pode observa-lo presente em todo início de endereço web, a resposta correta era [Alternativa 3] - HTTP")
        Reais -= 1

    print("\nPERGUNTA NUMERO 3")
    print("O que é um sistema operacional? \n [Alternativa 1] - Um programa de edição de texto. \n [Alternativa 2] - Uma rede popular. \n [Alternativa 3] - Um software que controla o hardware e permite a execução de aplicativos. \n [Alternativa 4] - Um dispositivo de entrada. \n [Alternativa 5] - Um aplicativo de gerenciamento de e-mail.")
    questao3 = int(input("Digite sua resposta: "))
    if questao3 == 3:
        print("Certa resposta")
        print("Sistema operacional é o responsável por controlar o hardware e permitir a execução de aplicativos assim como esse que você está jogando! :)")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Sistema operacional é o sistema usado para controlar o hardware e permitir que aplicações sejam executadas, resposta correta é [Alternativa 3] - Um software que controla o hardware e permite a execução de aplicativos.")
        Reais -= 1

    print("\nPERGUNTA NUMERO 4")
    print("Qual protocolo é usado para enviar e-mails? \n [Alternativa 1] - HTML. \n [Alternativa 2] - HTTP. \n [Alternativa 3] - IP. \n [Alternativa 4] - SMTP. \n [Alternativa 5] - POP3.")
    questao4 = int(input("Digite sua resposta: "))
    if questao4 == 4:
        print("Certa reposta")
        print("SMTP é o protocolo reponsável por envio de e-mails")
        Reais += 1
    else:
        print("Resposta errada!")
        print("SMTP é o protocolo responsávle por envio de e-mails, a resposta certa seria [Alternativa 4] - SMTP")
        Reais -= 1

    print("\nPERGUNTA NUMERO 5")
    print("Qual o significado da sigla 'URL'? \n [Alternativa 1] - Universal Resource Locator. \n [Alternativa 2] - United Resource Language. \n [Alternativa 3] - Ultra-Reliable Link. \n [Alternativa 4] - Uniform Request Layer. \n [Alternativa 5] - User Recognition Link.")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 1:
        print("Certa resposta")
        print("URL também conhecido como 'Universal Resource Locator' se refere ao endereço de rede no qual se encontra algum recurso informático.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("URL significa 'Universal Resource Locator' ou em português: 'Localizador uniforme de recursos', por isso, a resposta certa seria [Alternativa 1] - Universal Resource Locator")
        Reais -= 1

    print("\nPERGUNTA NUMERO 6")
    print("Qual dessas opções é um exemplo de sistemas de gerenciamento de banco de dados (SGBD)? \n [Alternativa 1] - Windows. \n [Alternativa 2] - Microsoft Word. \n [Alternativa 3] - MySQL. \n [Alternativa 4] - Photoshop. \n [Alternativa 5] - Google Chrome.")
    questao4 = int(input("Digite sua resposta: "))
    if questao4 == 3:
        print("Certa reposta")
        print("MySQL é um sistema relacional de gerenciamento de banco de dados")
        Reais += 1
    else:
        print("Resposta errada!")
        print("MySQL é um sistema relacional de gerenciamento de banco de dados, então a resposta certa seria a [Alternativa 3] - MySQL.")
        Reais -= 1

    print("\nPERGUNTA NUMERO 7")
    print("O que é um 'firewall' em relação à segurança de rede? \n [Alternativa 1] - Um dispositivo de entrada com teclado e mouse. \n [Alternativa 2] - Uma ferramenta de busca na web. \n [Alternativa 3] - Um software antivírus. \n [Alternativa 4] - Um sistema de segurança que controla o tráfego de rede e protege contra ameaças. \n [Alternativa 5] - Um serviço de e-mail.")
    questao7 = int(input("Digite sua resposta: "))
    if questao7 == 4:
        print("Certa resposta")
        print("Firewall é o sistema responsável por gerenciar o tráfego web e proteger contra ameaças.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Firewall é o sistema de segurança responsável por gerenciar o tráfego da web e proteger contra as ameaças dela, por isso, a resposta certa seria [Alternativa 4] - Um sistema de segurança que controla tráfego de rede e protege contra ameaças.")
        Reais -= 1

    print("\nPERGUNTA NUMERO 8")
    print("Qual protocolo é usado para transferência de arquivos em uma rede? \n [Alternativa 1] - HTTP. \n [Alternativa 2] - FTP. \n [Alternativa 3] - SMTP. \n [Alternativa 4] - IP. \n [Alternativa 5] - UDP.")
    questao8 = int(input("Digite sua resposta: "))
    if questao8 == 2:
        print("Certa resposta")
        print("FTP também conhecido como 'File Transfer Protocol' é o responsável pela transferência de arquivos em sistemas web.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("File Transfer Protocol - também conhecido como FTP é o reponsável por transferência de arquivos na web, por isso, a alternativa correta seria [Alternativa 2] - FTP.")
        Reais -= 1

    print("\nPERGUNTA NUMERO 9")
    print("O que é 'Phishing'? \n [Alternativa 1] - Uma técnica de impressão digital. \n [Alternativa 2] - Um programa antivírus \n [Alternativa 3] - Um sistema operacional \n [Alternativa 4] - Uma rede social \n [Alternativa 5] - Um tipo de ataque cibernético")
    questao9 = int(input("Digite sua resposta: "))
    if questao9 == 5:
        print("Certa resposta")
        print("Phishing é um ataque cibernético que visa coletar informações pessoais e financeiras da vítima.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Phishing é o nome dado para o ataque cibernético que visa enganar uma pessoa e coletar informações financeiras e pessoais da mesma, por isso, a resposta correta seria [Alternativa 5] - Um ataque cibernético")
        Reais -= 1

    print("\nPERGUNTA NUMERO 10")
    print("O que significa 'Wi-Fi'? \n [Alternativa 1] - Wireless Fiber \n [Alternativa 2] - Wireless Fidelity \n [Alternativa 3] - World Wide Web \n [Alternativa 4] - Wireless Finance \n [Alternativa 5] - Wireless File")
    questao10 = int(input("Digite sua resposta: "))
    if questao10 == 2:
        print("Certa resposta")
        print("'WI-Fi' é a abreviação de Wireless Fidelity")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Wireless Fidelity é o nome completo da abreviação 'Wi-Fi', a resposta correta seria [Alternativa 2] - Wireless Fidelity")
        Reais -= 1
        
    print("\nPARABÉNS! Você conseguiu um total de R$ %1.6f" % (Reais))
    print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
else:
    print("Até logo!")