from db import *


# Como eh usado varias vezes o login, decidi criar esse metodo para diminuir um pouco o codigo
def verificar():
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
                return True, usuario
            else:
                print('Senha incorreta\n')
                
        else:
            print('Esse nome de usuario nao existe\n')
            
        tentativas += 1

    # Caso saio do loop
    return False, usuario

def criar():
    while True:
        usuario = input('Nome de usuario: ')
        usuario = usuario.lower()
        print('Verificando se o usuario ja existe')
        
        # Tentar fazer login com esse usuario
        # Caso nao exista pode criar uma conta
        conta = Conta(usuario)
        existe = conta.logar()
        
        if not existe:
            print('Usuario nao existe, prosseguindo\n')
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
    

def main():    
    while True:
        print('-'*20)
        print('  SISTEMA DE LOGIN  ')
        print('-'*20)
        print('Criar - ("c")')
        print('Logar - ("l")')
        print('Deletar - ("d")')
        print('Sair - ("s")')
        resp = input('-> ').lower()
        print()
        
        if resp.startswith('c'):
            criar()                    
        
        elif resp.startswith('l'):            
            verificado, usuario = verificar()
            conta = Conta(usuario)            
            if verificado:    
                conta.mostramsg()

        elif resp.startswith('d'):
            print('Em construcao')
            #verificado = verificar()        

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

