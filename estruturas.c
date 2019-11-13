#include <stdlib.h>


typedef struct nob{

     int n;
     char * chaves;
     struct nob * filhos;
}noB;

typedef struct nobl{
     noB * no;
     struct nobl * prox;

}noB_Lista;

typedef struct arvB{

     int ordem;
     noB * raiz;
} TreeB;
