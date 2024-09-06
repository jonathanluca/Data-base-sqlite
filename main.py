from db import createTable
from db import insertDado

def menu():
    
    voltar_menu = "s"
    
    while voltar_menu == "s":
        
        opcao = input('''
                ====================
                [1] CRIAR TABELA
                [2] CADASTRO
                [3] LISTAR
                [4] DELETAR
                [5] SAIR
                ====================
                Escolha uma opção
                    ''')
        
        match opcao:
            
            case '1':
                createTable()
                
            case '2':
                insertDado()
                
            case '3':
                print("LISTAR")
                
            case '4':
                print("DELETAR")
                
            case '5':
                print("SAIR")
                
        voltar_menu = input("Deseja retornar para o menu principal? (s/n) ").lower()   
        
menu()
insertDado()
