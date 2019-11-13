from estruturas import *
from collections import deque

def codifica_B( key , T ):
     '''
     dada uma arvore T de ordem k e uma chave 'key', esta funcao expressa
     a posicao de 'key' em T em termos de i , j , k. onde:

     i -> nivel do noh que contem 'key'
     j -> posicao do noh nivel 
     k -> posicao da chave no noh

     se 'key' inexiste em T, retorna ( -1 , -1 , -1 )
     '''

     no = T.raiz
     i = 0
     anterior = deque( [] ) #nos a esquerda do noh escolhido, usado para computar j

     while no != None:

          #achando a posicao que pode conter a chave
          for k in range( no.n ):
               if no.chaves[ k ] >= key:
                    break
          j = len( anterior )

          if no.chave[ k ] == key:
               return ( i , j , k )
          
          #a partir daqui a chave não foi encontrada, antes de se descer o nivel tem-se que listar todos os
          #nos que antecedem o novo no
          
          #primeiro, os filhos dos irmaos anteriores
          if j != 0:
               aux = 0
               while aux < j:
                    irmao = anterior.popleft()
                    for x in irmao.filhos:
                         anterior.append( x )
                    aux += 1
          
          #depois, filhos do proprio no, que antecedem k
          aux = 0
          while aux < k:
               anterior.append( no.filhos[ aux ] )
               aux += 1
          
          #por fim, descendo para o novo nivel
          no = no.filhos[ k ]
          i += 1
     
     #se saiu do loop , é que o no nao existe, então:
     return ( -1 , -1 , -1 )

def decodifica_B( i_arg , j_arg , k_arg , T ):
     '''
     Exatamente o opostdo da função codificaB

     essa funcao da erro em tres casos:
     1 - se i for maior ou igual a alutra da arvore
     2 - se na altura i, j for maior ou igual a qualtidade de nos na largura
     3 - se k não estiver ente 0 e 2 vezes a ordem da arvore

     '''

     niveis = deque( [T.raiz] )
     i = 0
     while i < i_arg:

          if niveis[0].folha: # i maior que a altura da arvore
               return None 

          tam = len( niveis )
          aux = 0
          while aux < tam:
               no = niveis.popleft()
               for x in no.filhos:
                    niveis.append( x )
               aux += 1
          
          i += 1
     
     #a partir daqui a fila niveis ja representa os nos no nivel i_arg
     
     try:
          no = niveis[ j_arg ]
     except IndexError:
          return None
     
     if k_arg > 2*T.ordem:
          return None

     return no.chaves[ k_arg ]

def codifica_Bp( key , T ):
     
     #achando o primeiro no folha, e achando a altura:

     nivel = 0
     no = T.raiz 

     while not no.folha:
          no = no.filhos[ 0 ]
          nivel += 1
     
     primeira_folha = no
     
     #buscando o no
     no = T.raiz
     while not no.folha:

          for k in range( no.n ):
               if no.chaves[ k ] > key:
                    break
          no = no.filhos[ k ]
     
     
     nivel_pos = 0
     while primeira_folha.prox != no:
          primeira_folha = primeira_folha.prox
          nivel_pos += 1

     if key not in no.chaves:
          return ( -1 , -1 , -1 )
     
     for k in range( no.n ):
          if no.chaves[ k ] == key:
               break
     
     return ( nivel , nivel_pos , k )

def decodifica_Bp( i , j_arg , k_arg , T ):

     nivel = 0
     no = T.raiz 

     while not no.folha:
          no = no.filhos[ 0 ]
          nivel += 1
     
     primeira_folha = no

     j = 0
     while j < j_arg:
          primeira_folha = primeira_folha.prox
          j += 1
     
     return primeira_folha.chaves[ k_arg ]
     