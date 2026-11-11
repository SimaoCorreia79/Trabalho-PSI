class Livro:

    def _init_(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponibilidade = True
        self.aluno_emprestado = None

    
    def registar(self):
        return {
            "Livro": self.titulo,
            "Autor": self.autor,
            "Codigo": self.codigo,
            "Disponibilidade": self.disponibilidade
        }

    
    def vrfc_disponibilidade(self):
        if self.disponibilidade:
            print("Livro disponivel")
        else:
            print("Livro indisponivel")

    
    def Emprestar(self, aluno):
        if self.disponibilidade:
            self.disponibilidade = False
            self.aluno_emprestado = aluno
            aluno.adicionar_livro(self)

            print("Livro emprestado com sucesso!")
        else:
            print("Este livro ja esta emprestado.")

    
    def devolver(self):
        if not self.disponibilidade:
            self.disponibilidade = True

            self.aluno_emprestado.remover_livro(self)
            self.aluno_emprestado = None

            print("Livro devolvido com sucesso!")
        else:
            print("Este livro ja esta disponivel.")




class Aluno:

    def _init_(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.LivrosEmprestados = []

   
    def registar(self):
        return {
            "Nome": self.nome,
            "Matricula": self.matricula,
            "Livros Emprestados": [
                livro.titulo for livro in self.LivrosEmprestados
            ]
        }

    
    def consultar_dados(self):
        print("\n------ DADOS DO ALUNO ------")
        print("Nome:", self.nome)
        print("Matricula:", self.matricula)

    
    def listar_livros(self):
        if self.LivrosEmprestados:
            print("\nLivros emprestados por", self.nome)

            for livro in self.LivrosEmprestados:
                print("-", livro.titulo)
        else:
            print("Este aluno nao tem livros emprestados.")

   
    def adicionar_livro(self, livro):
        self.LivrosEmprestados.append(livro)

    
    def remover_livro(self, livro):
        if livro in self.LivrosEmprestados:
            self.LivrosEmprestados.remove(livro)




class Biblioteca:

    def _init_(self):
        self.cadastro = []
        self.catalogo = []

    
    def Cadastro_Alunos(self):

        nome = input("Introduza o nome do aluno: ")
        matricula = input("Introduza a matricula: ")

        for aluno in self.cadastro:
            if aluno.matricula == matricula:
                print("Esse aluno ja existe no sistema!")
                return

        aluno = Aluno(nome, matricula)
        self.cadastro.append(aluno)

        print("Aluno registado com sucesso!")

    
    def Catalogo_Livros(self):

        titulo = input("Introduza o nome do livro: ")
        autor = input("Introduza o autor: ")
        codigo = input("Introduza o codigo do livro: ")

        for livro in self.catalogo:
            if livro.codigo == codigo:
                print("Esse livro ja existe no sistema!")
                return

        livro = Livro(titulo, autor, codigo)
        self.catalogo.append(livro)

        print("Livro registado com sucesso!")

    
    def Listar_Alunos(self):

        if not self.cadastro:
            print("Nao existem alunos registados.")
            return

        for aluno in self.cadastro:
            aluno.consultar_dados()
            aluno.listar_livros()

    
    def Listar_Livros(self):

        if not self.catalogo:
            print("Nao existem livros registados.")
            return

        for livro in self.catalogo:
            print("\n----------------------")
            print("Titulo:", livro.titulo)
            print("Autor:", livro.autor)
            print("Codigo:", livro.codigo)

            livro.vrfc_disponibilidade()

    
    def Editar_Livro(self):

        codigo = input("Introduza o codigo do livro: ")

        for livro in self.catalogo:

            if livro.codigo == codigo:

                livro.titulo = input("Introduza o novo titulo: ")
                livro.autor = input("Introduza o novo autor: ")

                print("Livro editado com sucesso!")
                return

        print("Livro nao encontrado.")

    
    def Apagar_Livro(self):

        codigo = input("Introduza o codigo do livro: ")

        for livro in self.catalogo:

            if livro.codigo == codigo:

                if not livro.disponibilidade:
                    print("Nao pode apagar um livro emprestado!")
                    return

                self.catalogo.remove(livro)

                print("Livro apagado com sucesso!")
                return

        print("Livro nao encontrado.")

    
    def Emprestar_Livro(self):

        matricula = input("Introduza a matricula do aluno: ")
        codigo = input("Introduza o codigo do livro: ")

        aluno_encontrado = None
        livro_encontrado = None

        for aluno in self.cadastro:
            if aluno.matricula == matricula:
                aluno_encontrado = aluno

        for livro in self.catalogo:
            if livro.codigo == codigo:
                livro_encontrado = livro

        if aluno_encontrado is None:
            print("Aluno nao encontrado!")
            return

        if livro_encontrado is None:
            print("Livro nao encontrado!")
            return

        livro_encontrado.Emprestar(aluno_encontrado)

    # Devolver livro
    def Devolver_Livro(self):

        codigo = input("Introduza o codigo do livro: ")

        for livro in self.catalogo:

            if livro.codigo == codigo:
                livro.devolver()
                return

        print("Livro nao encontrado.")




biblioteca = Biblioteca()

while True:

    print("\n========== MENU BIBLIOTECA ==========")
    print("\n1 - Adicionar aluno")
    print("\n2 - Adicionar livro")
    print("\n3 - Listar alunos")
    print("\n4 - Listar livros")
    print("\n5 - Editar livro")
    print("\n6 - Apagar livro")
    print("\n7 - Emprestar livro")
    print("\n8 - Devolver livro")
    print("\n9 - Sair")

    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        biblioteca.Cadastro_Alunos()

    elif opcao == "2":
        biblioteca.Catalogo_Livros()

    elif opcao == "3":
        biblioteca.Listar_Alunos()

    elif opcao == "4":
        biblioteca.Listar_Livros()

    elif opcao == "5":
        biblioteca.Editar_Livro()

    elif opcao == "6":
        biblioteca.Apagar_Livro()

    elif opcao == "7":
        biblioteca.Emprestar_Livro()

    elif opcao == "8":
        biblioteca.Devolver_Livro()

    elif opcao == "9":
        print("A sair do programa...")
        break

    else:
        print("Opcao invalida!")












   



    


