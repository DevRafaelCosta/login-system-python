import pickle

class Conta:    
    def __init__(self, usuario):
        self.usuario = usuario        
        
       
    def criar(self, senha, nome, msg):

        # Abre o banco de dados
        db = open('contas.pck', 'rb')
        conta = pickle.load(db)
        db.close()

        # Adiciona no dicionario o novo usuario, junto com suas dependencias
        conta[self.usuario] = {'senha': senha, 'nome': nome, 'msg': msg}

        # Escreve o dicionario de volta junto com o novo usuario
        db = open('contas.pck', 'wb')
        pickle.dump(conta, db)
        db.close()
        
    
    # Verifica se o usuario existe
    def logar(self):
        
        try:
            db = open('contas.pck', 'rb')
            conta = pickle.load(db)
            db.close()
                    
            if self.usuario in conta:
                return True

        # Caso nao exista um arquivo ele cria um
        except FileNotFoundError:
            print('\nErro. Arquivo nao existe. Criando um padrao')
            print('usuario: admin, senha: admin')
            conta = {'admin': {'senha': 'admin', 'nome': 'Admin', 'msg': 'Somente uma primeira mensagem caso nao exista um arquivo'}}
            db = open('contas.pck', 'wb')
            pickle.dump(conta, db)
            db.close()
               

    def verificaSenha(self, senha):
        db = open('contas.pck', 'rb')
        conta = pickle.load(db)
        db.close()
        
        if conta[self.usuario]['senha'] == senha:
            return True

    
    def mostramsg(self):
        # Le o DB
        db = open('contas.pck', 'rb')
        conta = pickle.load(db)
        db.close()

        # E imprime as informacoes do usuario
        print(f'\nMensagem de {self.usuario}')
        print(f'Meu nome eh: {conta[self.usuario]["nome"]}')
        print(f'Minha mensagem: {conta[self.usuario]["msg"]}\n')
       
        
    def atualiza(self):
        pass


    def deleta(self):
        pass
    
    
def main():    
    while True:
        print('-'*20)
        print('  SISTEMA DE LOGIN  ')
        print('-'*20)

        print('Criar - ("c")')
        print('Logar - ("l")')
        print('Sair - ("s")')
        resp = input('-> ').lower()
        print()
        
        if resp.startswith('c'):

            while True:            
                usuario = input('Nome de usuario: ')
                usuario = usuario.lower()
                
                print('Verificando se o usuario ja existe...')
                
                # Tentar fazer login com esse usuario
                # Caso nao exista pode criar uma conta
                conta = Conta(usuario)
                existe = conta.logar()

                if not existe:
                    print('Usuario nao existe')
                    break

                print('Esse usuario ja existe\n')                      
            

            # Cria senha e confere
            while True:
                senha = input('Digite uma senha: ')
                senha_check = input('Comfirme sua senha: ')
                
                if senha == senha_check:
                    break                
                else:
                    print('\nSenha nao confere. Digite novamente.')

            nome = input('Digite seu nome: ')
            msg = input('Digite sua mensagem: ')

            conta.criar(senha, nome, msg)
            print('Conta criada com sucesso!\n')
            conta.mostramsg()                
                    
        
        elif resp.startswith('l'):
            tentativas = 0
            
            while tentativas <= 5:            
                usuario = input('Nome de usuario: ')
                usuario = usuario.lower()
                
                # Tentar fazer login com esse usuario                
                conta = Conta(usuario)
                existe = conta.logar()

                if existe:
                    senha = input('Digite a senha: ')
                    verifica = conta.verificaSenha(senha)

                    if verifica:
                        tentativas = 5
                        mostra = True
                    else:
                       print('Senha incorreta\n') 

                else:
                    print('Esse nome de usuario nao existe\n')

                tentativas += 1

            # Como esta fora do while
            # Eu tenho que ter certeza que foi digitado a senha corretamente
            if mostra:    
                conta.mostramsg()              


        elif resp.startswith('s'):
            break
        
        else:
            print('Opcao Invalida')

            # Opcao de continuar
            resp = input('Quer sair? (s/n): ').lower()

            if resp.startswith('s'):
                break            

    print('\nPrograma finalizado')


if __name__ == '__main__':
    main()

