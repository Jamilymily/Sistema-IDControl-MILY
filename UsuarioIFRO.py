import time
from abc import ABC

#Apresentação - Alice
#Superclasse abstrata(UsuarioIFRO):

#Usuario(IFRO) é uma superclasse pois herda seus atributos para duas subclasses: Aluno, Servidor. (processo nomeado de Herança)
#além disso, ela é uma classe abstrata pois não pode instanciar objetos, ou seja, não existe um "UsuarioIFRO do tipo UsuarioIFRO"
class UsuarioIFRO(ABC):
  def __init__(self,nome,cpf, matricula, senha):
    self.__nome= nome
    self.__cpf=cpf
    self.__matricula = matricula
    self.__senha=senha

  def get_nome(self):
    return self.__nome 

  def get_cpf(self):
    return self.__cpf

  def get_matricula(self):
    return self.__matricula

  def get_senha(self):
    return self.__senha

  def criar_senha (self):
    self.__senha = int(input("Digite sua senha: "))
    return self.__senha
  
  def set_senha(self):
    self.__novasenha =("Digite sua nova senha:")
    self.__novasenha = self.__senha
    print("Senha alterada com sucesso")

#Apresentação - Jamily
#Aluno é subclasse de de UsuarioIFRO pois HERDA seus atributos (herança)