from model.alunoModel import AlunoModel

class AlunoController:

    def __init__(self):
        pass

    def pegarMatricula(self,alunoView):
        matricula = alunoView.getTexto(3)
        obj = AlunoModel()
        obj.setMatricula(matricula)
        return obj.getMatricula()

    def pegarNome(self, alunoView):
        nome = alunoView.getTexto(5)
        obj = AlunoModel()
        obj.setNome(nome)
        return obj.getNome()

    def pegarEmail(self, alunoView):
        email = alunoView.getTexto(7)
        obj = AlunoModel()
        obj.setEmail(email)
        return obj.getEmail()

    def pegarGenero(self, alunoView):
        genero = alunoView.getTexto(9)
        obj = AlunoModel()
        obj.setGenero(genero)
        return obj.getGenero()

    def pegarSenha(self, alunoView):
        senha = alunoView.getTexto(11)
        obj = AlunoModel()
        obj.setSenha(senha)
        return obj.getSenha()
