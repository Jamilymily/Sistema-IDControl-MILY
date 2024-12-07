# Colocar a importaân da classe e a relaçaõ
from datetime import date, time
class Relatorio:
  def __init__(self, id, tipo, dataEntrada, dataSaida=None, visitantes=0):
    self.__id= id
    self.__tipo= tipo
    self.__dataEntrada = dataEntrada
    self.__dataSaida = dataSaida
    self.__Visitantes = visitantes
    
  def get_idRelatorio(self):
    return self.__id
    
  def get_tipoRelatorio(self):
    return self.__tipo
    
  def get_dataEntrada(self):
    return self.__dataEntrada
    
  def get_dataSaida(self):
    return self.__dataSaida
    
  def get_quantVisitantes(self):
    return self.__Visitantes

# Função para exibir o Relatório
def exibirRelatorio(self):
  print(f"ID:{self.__id}")
  print(f"Tipo:{self.__tipo}")
  print(f"Tipo:{self.__dataEntrada.strftime('%Y-%m-%d %H:%M:%S')}")
if self.__dataSaida:  # Se a saída foi registrada
   print(f"Saída: {self.__dataSaida.strftime('%Y-%m-%d %H:%M:%S')}")
else:
  print("Saída: Não registrada.")
  print(f"Visitantes: {self.__visitantes}")

 # Função para registrar a saída
def registrar_saida(self, saida):
  self.__saida = saida
  
    