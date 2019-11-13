class Bno:

     def __init__( self ):
          
          self.n = 0
          self.chaves = []
          self.filhos = []
          self.folha = False

class Btree:

     def __init__( self , ordem ):

          self.ordem = ordem
          self.raiz = Bno()
          self.raiz.folha = True

class BPtree:

     def __init__( self , ordem ):

          self.ordem = ordem
          self.raiz = None

class BPno:

     def __init__( self ):
          
          self.n = 0
          self.chaves = []
          self.filhos = []
          self.folha = False
          self.prox = None
