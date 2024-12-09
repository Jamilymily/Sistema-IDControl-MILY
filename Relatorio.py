from collections import defaultdict
from datetime import datetime

class GerenciadorRelatorio:
  def __init__(self):
    self.__relatorio=defaultdict(list)


class Relatorio:
  def __init__(self, id, tipo, dataEntrada, dataSaida=None, visitantes=0):
    try:
      if not isinstance(dataEntrada, datetime):
        raise TypeError(" Data é um objeto datetime")
      self.__id= id
      self.__tipo= tipo
      self.__dataEntrada = dataEntrada
      self.__dataSaida = None
      self.__Visitantes = visitantes
    except TypeError as e:
      print(f" erro de criação do relatório: {e}")
    finally:
      print("final da inicialização do relatório")
    
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

def exibirRelatorio(self):
  try:
    print(f"ID:{self.__id}")
    print(f"Tipo:{self.__tipo}")
    print(f"Tipo:{self.__dataEntrada.strftime('%Y-%m-%d %H:%M:%S')}")
    if self.__dataSaida:
      print(f"Saída: {self.__dataSaida.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
      print("Saída: Não registrada.")
      print(f"Visitantes: {self.__visitantes}")
  except Exception as e:
    print(f"Erro na exibição do relatório")
  finally:
    print("Exibição finalizada")


def registrar_saida(self, dataSaida):
  try:
    if not isinstance(dataSaida, datetime):
      raise TypeError("A data de saída é um obejeto datetime")
    self.__dataSaida=dataSaida
  except TypeError as e:
    print(f"Erro ao registrar a saída:{e}")
  finally:
    print("Processo de registro de saída concluido")

def lista_relatorio(self, modo=None):
  try:
    if modo and modo not in self.__relatorio:
      raise ValueError(f"Nhenum relatório voltado para esse modo {'modo'}")
    relatorio= self.__relatorio[modo] if modo else self.__relatorio
    for modo, lista in relatorio.items():
      print(f"\n Modo: {modo}")
    for rel in lista:
      rel.exibirRelatorio()
  except ValueError as e:
    print(f"Erro ao exibir relatório lista:{e}")
  finally:
    print("Listagem realizada")
    