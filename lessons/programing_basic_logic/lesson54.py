import os

lista_compra = []

while True:
  opcao = input("Selecione a opcao\n[i]nserir [a]pagar [l]istar: ")

  if opcao == "i":
    os.system('cls')
    valor = input("Valor: ")
    lista_compra.append(valor)
  elif opcao == 'a':
    indice = input("Escolha o índice para apagar: ")
    
    try:
      indice_int = int(indice)  
      del lista_compra[indice_int]
    except ValueError:
      print("Por favor digite um número!")
    except IndexError:
      print("Índice não existe na lista!")
    except Exception:
      print("Erro desconhecido!")
  elif opcao == 'l':
    os.system('cls')
    if len(lista_compra) == 0:
      print('Não há nenhum item adicionado!') 
    else:
      for indice, nome in enumerate(lista_compra):
        print(indice, nome) 
  else:
    print("Selecione outra opção![i], [a] ou [l]")