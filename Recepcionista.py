# O construtor da classe Recepcionista herda o comportamento do construtor de Servidor
class Recepcionista(Servidor):
  def __init__ (self,nome,cpf,senha,matricula,departamento):
    # Aqui usamos super() para chamar o construtor da classe base (Servidor),
    # que inicializa os atributos nome, cpf, senha, matricula e departamento
  super().__init__(nome,cpf,senha,matricula, departamento)
  
  # Método específico de Recepcionista para liberar visitantes
  def liberarVisitante(self):
  # Pergunta ao recepcionista se ele deseja liberar ou negar o acesso a um visitante
    while True:
      liberar = int(input("Deseja liberar visitante? SIM [1] ou NÃO [2]")):
      if liberar == 1:
        print("Acesso liberado!")
        break
      elif liberar == 2:
        print("Acesso negado!")
        break
      else:
        print("Tente novamente")
        continue