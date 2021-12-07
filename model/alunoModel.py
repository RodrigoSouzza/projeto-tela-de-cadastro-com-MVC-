
class AlunoModel:

    def __init__(self):
        self.__matricula = str
        self.__nome = str
        self.__email = str
        self.__genero = str
        self.__senha = str

    def setMatricula(self, matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome

    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email

    def setGenero(self, genero):
        self.__genero = genero
    def getGenero(self):
        return self.__genero

    def setSenha(self, senha):
        self.__senha = senha
    def getSenha(self):
        return self.__senha
