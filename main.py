from db import *


# Como eh usado varias vezes o login, decidi criar esse metodo para diminuir um pouco o codigo
def verificar():
    tentativas = 0
            
    while tentativas <= 2:
        usuario = input('Nome de usuario: ')
        usuario = usuario.lower()
        
        # Tenta fazer login com esse usuario
        conta = Conta(usuario)
        existe = conta.logar()
        
        if existe:
            senha = input('Digite a senha: ')
            verifica = conta.verificaSenha(senha)
            
            if verifica:
                tentativas = 2
                return True, usuario
            else:
                print('Senha incorreta\n')
                
        else:
            print('Esse nome de usuario nao existe\n')
            
        tentativas += 1

    # Caso saia do loop
    return False, usuario


def criar():
    while True:
        usuario = input('Nome de usuario: ')
        usuario = usuario.lower()        
        
        # Tenta fazer login com esse usuario
        # Caso nao exista pode criar uma conta
        conta = Conta(usuario)
        existe = conta.logar()
        
        if not existe:            
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
        print('Ver usuarios - ("v")')
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
            verificado, usuario = verificar()
            conta = Conta(usuario)
            
            if verificado:
                resp = input('\nTem certeza que quer deletar? [s/n]: ')
                if resp == 's':
                    conta.deleta()
                    print('Conta deletada com sucesso!\n')
                   
        elif resp.startswith('v'):            
            conta = Conta(None)
            conta.ver_usuarios()
        
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

