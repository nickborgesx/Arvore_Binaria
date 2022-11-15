import sys


class _No():  # Classe Elemento
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.right is None and self.left is None

    def __str__(self):
        return f'{self.data}'


class ArvoreBinaria():  # Classe Arvore
    def __init__(self):
        self.root = None  # Raiz (início)
        self.height = 0  # Altura do elemento
        self.elements = 0  # Elementos

    def __addNo(self, no, perc):
        if no.data > perc.data:  # Se o elemento for maior que o primeiro elemento
            if perc.right == None:  # Irá adicionar na direita
                perc.right = no
            else:
                self.__addNo(no, perc.right)
        elif no.data < perc.data:  # Se o elemento for menor que o primeiro elemento
            if perc.left == None:  # Irá adicionar na esquerda
                perc.left = no
            else:
                self.__addNo(no, perc.left)
        else:
            return print("Número já existe na árvore.")

    def add(self, data):  # Adicioanr elemento na árvore
        no = _No(data)
        if self.root == None:  # Verificar se a árvore está vazia.
            self.root = no
        else:
            self.__addNo(no, self.root)  # Adicionar elemento na posição correta da árvore
        self.elements += 1

    def buscarNivel(self, data, percorredor):
        perc = percorredor  # Criando um perc
        if perc == None:  # Verificar se a árvore está vazia
            return None
        if perc.data == data:  # Verificar se é o atual
            print(f'O nível em que o elemento se encontra é: ', arvore.height)
            self.height = 0
            return perc
        else:
            if data > perc.data:  # Verificar se o elemento que está procurando é maior que o primeiro elemento da árvore
                self.height += 1
                return self.buscarNivel(data, perc.right)
            else:  # Se não for irá procurar pelo menor
                self.height += 1
                return self.buscarNivel(data, perc.left)

    def buscarN(self, data):
        if self.elements == 0:
            return print("Valor não existe na árvore")
        nivel = self.buscarNivel(data, self.root)
        if nivel == None:
            return print("Valor não existe na árvore")

    def buscarNo(self, data, percorredor):
        perc = percorredor  # Criando um perc
        if perc == None:  # Verificar se a árvore está vazia
            return None
        if perc.data == data:  # Verificar se é o atual
            self.height = 0
            return perc
        else:
            if data > perc.data:  # Verificar se o elemento que está procurando é maior que o primeiro elemento da árvore
                self.height += 1
                return self.buscarNo(data, perc.right)
            else:  # Se não for irá procurar pelo menor
                self.height += 1
                return self.buscarNo(data, perc.left)

    def buscar(self, data):
        if self.elements == 0:
            return print("Valor não existe na árvore")
        buscar = self.buscarNo(data, self.root)
        if buscar == None:
            return print("Valor não existe na árvore")

    def sucessorManual(self):
        sucessorlista = list()

        def _sucessor(destiny):
            if destiny != None:
                _sucessor(destiny.left)
                sucessorlista.append(destiny.data)
                _sucessor(destiny.right)

        _sucessor(self.root)
        suc = int(input("Digite o valor: "))
        if suc not in sucessorlista:
            print("valor não existe na árvore")
        else:
            indice = sucessorlista.index(suc)
            antecessor_ = indice - 1
            tamanho = len(sucessorlista)
            sucessor_ = indice + 1
            if sucessor_ >= tamanho:
                print(f"Sucessor não exite")
            elif antecessor_ <= tamanho - (tamanho + 1):
                print(f"O Sucessor de {suc} é {sucessorlista[sucessor_]}")
            elif antecessor_ >= tamanho - (tamanho + 1) and tamanho >= sucessor_:
                print(f"O Sucessor de {suc} é {sucessorlista[sucessor_]}")

    def sucessor(self, perc):
        perc = self._minimo(perc.right)
        return perc

    def predecessor(self, perc):
        perc = self._maximo(perc.left)
        return perc

    def antecessor(self, ):
        antecessorlista = list()

        def _antecessor(destiny):
            if destiny != None:
                _antecessor(destiny.left)
                antecessorlista.append(destiny.data)
                _antecessor(destiny.right)

        _antecessor(self.root)
        ant = int(input("Digite o valor: "))
        if ant not in antecessorlista:
            print("valor não existe na árvore")
        else:
            indice = antecessorlista.index(ant)
            antecessor_ = indice - 1
            tamanho = len(antecessorlista)
            sucessor_ = indice + 1
            if sucessor_ >= tamanho:
                print(f"O Antecessor de {ant} é {antecessorlista[antecessor_]}")
            elif antecessor_ <= tamanho - (tamanho + 1):
                print(f"O Antecessor não exite")
            elif antecessor_ >= tamanho - (tamanho + 1) and tamanho >= sucessor_:
                print(f"O Antecessor de {ant} é {antecessorlista[antecessor_]}")

    def remover(self, data):
        buscar = self.buscarNo(data, self.root)
        if buscar == None:
            return print('Valor não existe na árvore')
        if self.elements == None:
            raise ValueError("lista Vazia")
        if self.elements == 1:
            self.root = None
            return
        perc, perc_anterior = self._get_perc(self.root, data)
        self._remover(perc, perc_anterior)
        self.elements -= 1

    def _remover(self, no, no_anterior):
        if no.is_leaf():
            self._remover_folha(no, no_anterior)
        elif no.right is None or no.left is None:
            self._remover_um_filho(no, no_anterior)
        else:
            self._remover_dois_filhos(no, no_anterior)

    def _remover_um_filho(self, no, no_anterior):
        if no is self.root:
            if no.right:
                self.root = no.right
                no.right = None
            elif no.left:
                self.root = no.left
                no.left = None
        else:
            if no.data < no_anterior.data:
                if no.right:
                    no_anterior.left = no.right
                    no.right = None
                elif no.left:
                    no_anterior.left = no.left
                    no.left = None
            else:
                if no.right:
                    no_anterior.right = no.right
                    no.right = None
                elif no.left:
                    no_anterior.right = no.left
                    no.left = None
        print('Elemento Deletado')

    def _remover_dois_filhos(self, no, no_anterior):
        sub = self.sucessor(no)
        if no is self.root:
            sub, sub_anterior = self._get_perc(no, sub.data)
            sub.left = no.left
            if sub.right:
                sub_anterior.left = sub.right
            else:
                sub_anterior.left = None
            if no.right is not sub:
                sub.right = no.right
            no.left, no.right = None, None

            self.root = sub
        else:
            sub, sub_anterior = self._get_perc(no, sub.data)
            sub.left = no.left
            if sub.right:
                sub_anterior.left = sub.right
            else:
                sub_anterior.left = None
            if no.right is not sub:
                sub.right = no.right
            if sub.data < no_anterior.data:
                no_anterior.left = sub
            else:
                no_anterior.right = sub
            no.left = None
            no.right = None
        print('Elemento Deletado')

    def _remover_folha(self, no, no_anterior):
        if no.data < no_anterior.data:
            no_anterior.left = None
        else:
            no_anterior.right = None
        print('Elemento Deletado')

    def _get_perc(self, perc, data, anterior=None):
        if not perc:
            return
        elif perc.data == data:
            return perc, anterior
        elif data > perc.data:
            return self._get_perc(perc.right, data, perc)
        else:
            return self._get_perc(perc.left, data, perc)

    def get(self, perc, data):  # Percorredor
        perc, anteior = self._get_perc(self.root, data)  # Verificar elemento na árvore
        return perc

    def minimo(self):
        return self._minimo(self.root)

    def _minimo(self, no_root):
        while no_root and no_root.left:
            no_root = no_root.left
        return no_root

    def maximo(self):
        return self._maximo(self.root)

    def _maximo(self, no_root):
        while no_root and no_root.right:
            no_root = no_root.right
        return no_root

    def minimoManual(self, perc):
        if self.elements == 0:
            return print('Árvore está vázia.')
        while perc.left != None:  # Enquanto o próximo elemento da esquerda não dor None irá procurar o menor elemento
            perc = perc.left
        return perc

    def maximoManual(self, perc):
        if self.elements == 0:
            return print('Árvore está vázia.')
        while perc.right != None:  # Enquanto o próximo elemento da direita não dor None irá procurar o maior elemento
            perc = perc.right
        return perc

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
        elif self.elements == 0:
            print('Lista está vazia.')
        else:
            return

    def imprimir(self):
        self.printHelper(self.root, '', True)

    def criar_arvore_com_lista(self):
        print('Arvore-Lista Pré-determinada')
        print('Inserindo números na árvore\n')
        nums = [8, 10, 9, 7, 12, 11]
        for i in nums:
            arvore.add(i)
        arvore.imprimir()

    def ordem(self):
        ordem1 = list()
        ordem2 = list()
        ordem3 = list()

        def InOrdem(ordem):
            if ordem != None:
                InOrdem(ordem.left)
                ordem1.append(ordem.data)
                InOrdem(ordem.right)

        def preOrdem(ordem):
            if ordem != None:
                ordem2.append(ordem.data)
                preOrdem(ordem.left)
                preOrdem(ordem.right)

        def posOrdem(ordem):
            if ordem != None:
                posOrdem(ordem.left)
                posOrdem(ordem.right)
                ordem3.append(ordem.data)

        InOrdem(self.root)
        preOrdem(self.root)
        posOrdem(self.root)
        print(f"Lista em InOrdem {ordem1}\nLista em preOrdem {ordem2}\nLista em posOrdem {ordem3}")

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def criar_lista_com_arvore(self):
        arvoreLista = list()
        
        def arvoreL(criar_lista_com_arvore):
            if criar_lista_com_arvore != None:
                arvoreL(criar_lista_com_arvore.left)
                arvoreLista.append(criar_lista_com_arvore.data)
                arvoreL(criar_lista_com_arvore.right)
        arvoreL(self.root)
        print('Árvore atual em forma de Lista')
        print(arvoreLista)

    def menu(self):
        while True:
            print('\n', '-' * 10, 'Árvore', '-' * 10)
            print('[1] - Criar elemento\n'
                  '[2] - Remover elemento\n'
                  '[3] - Imprimir a árvore\n'
                  '[4] - Valor mínimo\n'
                  '[5] - Valor máximo\n'
                  '[6] - Inserir lista pré-determinada na árvore\n'
                  '[7] - Ordenamento da árvore\n'
                  '[8] - Sucessor\n'
                  '[9] - Antecessor\n'
                  '[10] - Árvore para Lista\n'
                  '[11] - Nível elemento\n'
                  '[12] - Sair')
            opcao = input('Digite a opção: ')
            print('')
            if opcao == '1':
                elemento = int(input('Digite a quantidade de elementos: '))
                for i in range(0, elemento):
                    elemento2 = int(input('Digite o elemento: '))
                    arvore.add(elemento2)
            elif opcao == '2':
                elemento = int(input('Digite o valor do elemento que deseja remover: '))
                arvore.remover(elemento)
            elif opcao == '3':
                arvore.imprimir()
            elif opcao == '4':
                print(f"O valor mínimo da árvore é: {arvore.minimoManual(arvore.root)}")
            elif opcao == '5':
                print(f"O valor maximo da árvore é: {arvore.maximoManual(arvore.root)}")
            elif opcao == '6':
                arvore.criar_arvore_com_lista()
            elif opcao == '7':
                arvore.ordem()
            elif opcao == '8':
                arvore.sucessorManual()
            elif opcao == '9':
                arvore.antecessor()
            elif opcao == '10':
                arvore.criar_lista_com_arvore()
            elif opcao == '11':
                elemento = int(input('Digite o número do elemento: '))
                arvore.buscarN(elemento)
            elif opcao == '12':
                print('Bye')
                break
            else:
                print('Opção Inválida', '\n')
                return


arvore = ArvoreBinaria()
arvore.menu()
