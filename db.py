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
            print('Erro. Arquivo nao existe. Criando um padrao')
            print('usuario: admin, senha: admin')
            conta = {'admin': {'senha': 'admin', 'nome': '-', 'msg': '-'}}
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
        print(f'Minha mensagem: {conta[self.usuario]["msg"]}')
       
        
    def atualiza(self, opc):
        db = open('contas.pck', 'rb')
        conta = pickle.load(db)
        db.close()        

        if opc == 's':
            senha = input('Digite a nova senha: ')
            conta[self.usuario]['senha'] = senha
            print('Senha alterada.\n')            
            
        elif opc == 'n':
            nome = input('Digite o novo nome: ')
            conta[self.usuario]['nome'] = nome
            print('Nome alterado.\n')            

        else:
            msg = input('Digite a nova mensagem: ')
            conta[self.usuario]['msg'] = msg
            print('Mensagem alterada.\n')           
        

        db = open('contas.pck', 'wb')
        pickle.dump(conta, db)
        db.close()


    def deleta(self):        
        db = open('contas.pck', 'rb')
        conta = pickle.load(db)
        db.close()
        
        del conta[self.usuario]
        
        db = open('contas.pck', 'wb')
        pickle.dump(conta, db)
        db.close()


    def ver_usuarios(self):        
        try:
            db = open('contas.pck', 'rb')
            conta = pickle.load(db)
            db.close()

            for usuario in conta:
                print(usuario)

        except FileNotFoundError:
            Conta.logar(None)
    
