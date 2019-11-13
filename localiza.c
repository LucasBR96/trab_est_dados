#include <stdlib.h>
#include "estruturas.c"

int * pos_chave( TreeB * T , char key ){

/**
 * dada uma arvore T e um chave key, essa funcão retorna a posção de key em T
 * nos termos dos inteiros i , j , k. tais que:
 * i -> nivel do no que contem key
 * j -> posicao desse no nivel i
 * k -> posicao de key no no
 */

     int pos[3];
     int i , j , k;
     int aux1, aux2;
     noB * no, aux_no;
     
     // todos os nos que antecedem o no que contem key, isso ajuda a calcular j no nivel
     noB_Lista * inicio , * fim;

     i = k = 0;
     no = T -> raiz;
     inicio = fim = NULL;

     while( ( no -> chaves )[ k ] != key ){

          k = 0;
          while( ( ( no -> chaves )[ k ] < key ) && ( k < no ->n  ) )
               k++;

          if( ( no -> chaves )[ k ] == key )
               continue;
          
          //para o proximo nivel
          i++;

          

     }


}