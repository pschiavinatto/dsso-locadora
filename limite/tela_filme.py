class TelaFilme():
    def tela_opcoes(self):
        # fazer aqui tratamento caso a entrada seja diferente do esperado
        print(" --------- FILME ---------")
        print("Escolha a opcao")
        print("1 - Incluir Filme")
        print("2 - Alterar Filme")
        print("3 - Listar Filme")
        print("4 - Excluir Filme")
        print("0 - Retornar")

        opcao = int(input("\n Escolha a opcao: "))
        return opcao

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_filme(self):
        print("-------- DADOS FILME ----------")
        titulo = input("Titulo: ")
        codigo = input("Codigo: ")
        sinopse = input("Sinopse: ")
        faixa_etaria = input("Faixa etária: ")
        idioma = input("Idioma: ")
        link_acesso = input("Link de acesso:")


        return {"titulo": titulo, "codigo": codigo, "sinopse": sinopse, "faixa_etaria": faixa_etaria, "idioma": idioma, "link_acesso": link_acesso}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado, tbm alterar modo de mostrar
    def mostra_filme(self, dados_filme):
        print("TITULO DO FILME: ", dados_filme["titulo"])
        print("CODIGO DO FILME: ", dados_filme["codigo"])
        print("\n")

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_filme(self):
        codigo = input("Código do filme que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
