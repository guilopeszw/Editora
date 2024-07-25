# jornal:
dicJornal = {"mural": 200.00, "o coreto": 235.00}
precoCoreto = dicJornal["o coreto"]
precoMural = dicJornal["mural"]

# revista:
dicRevista = {"meu lar": 180.00, "sua mesa": 230.00}
precoMeuLar = dicRevista["meu lar"]
precoSuaMesa = dicRevista["sua mesa"]

# input jornal:
tipoServico = str(input(("Olá, seja bem-vindo à Editora Majima. \
Você deseja assinar serviços de jornal ou de revista? "))).lower().strip()

# jornal:
if tipoServico == "jornal" or tipoServico == "jornais":
    tipoJornal = str(
        input("Você deseja assinar com o Mural ou o O Coreto? ")).lower().strip()
    if tipoJornal == "mural" or tipoJornal == "jornal mural" or tipoJornal == "o mural":  # mural
        tempoAssinatura = int(input(
            "Durante quantos anos você deseja manter a assinatura (digite em número)? "))
        valorAssinatura = precoMural * tempoAssinatura
        print(f"Sua assinatura para o jornal Mural, que irá durar {tempoAssinatura} anos,\
irá custar R$: {valorAssinatura:.2f}.")
    elif tipoJornal == "coreto" or tipoJornal == "o coreto" or tipoJornal == "correto"\
        or tipoJornal == "o correto" or tipoJornal == "jornal coreto":
        tempoAssinatura = int(input(
        "Durante quantos anos você deseja manter a assinatura (digite em número)? "))
    valorAssinatura = precoCoreto * tempoAssinatura
    print(f"Sua assinatura para o jornal O Coreto, que irá durar {tempoAssinatura} \
anos, irá custar R$: {valorAssinatura:.2f}.")

# revistas:
if tipoServico == "revistas" or tipoServico == "revista":
    tipoRevista = str(
        input("Você deseja assinar com a Meu Lar ou a Sua Mesa? ")).lower().strip()
    if tipoRevista == "meular" or tipoRevista == "meu lar" or tipoRevista == "meu la":
        tempoAssinatura = int(input(
            "Durante quantos anos você deseja manter a assinatura (digite em número)? "))
        valorAssinatura = (precoMeuLar * tempoAssinatura)
        valorAssinaturaDesc = valorAssinatura * 0.9
        print(f"Sua assinatura para a revista Meu Lar, que irá durar {tempoAssinatura} anos, \
iria custar R$: {valorAssinatura:.2f} mas, devido à um desconto de nossa editora\
, o preço novo é R$: {valorAssinaturaDesc:.2f}.")
    elif tipoRevista == "sua mesa" or tipoRevista == "suamesa":
        tempoAssinatura = int(input(
            "Durante quantos anos você deseja manter a assinatura (digite em número)? "))
        valorAssinatura = (precoSuaMesa * tempoAssinatura)
        valorAssinaturaDesc = valorAssinatura * 0.9
        print(f"Sua assinatura para a revista Sua Mesa, que irá durar {tempoAssinatura} anos, \
iria custar R$: {valorAssinatura:.2f} mas, devido à um desconto de nossa editora\
, o preço novo é R$: {valorAssinaturaDesc:.2f}.")
