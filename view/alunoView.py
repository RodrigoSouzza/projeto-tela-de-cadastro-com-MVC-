from view.Tkfull import Janela
from controller.alunoController import AlunoController

class AlunoView:

    titulo = [[{'Cadastro de Aluno': 'assets/img/perfil.png'}]]
    objetos = [['Matricula:', input],
               ['Nome:', input],
               ['E-mail:', input],
               ['Gênero:', ('Masculino', 'Feminino')],
               ['Senha:', complex],
               [{'*Sair': 'assets/img/exit.png'}, {'*Cadastrar': 'assets/img/registro.png'}]]

    def __init__(self):
        self.tela = Janela()
        self.tela.titulo("Cadastro")
        self.tela.icone("assets/img/cadastro.png")
        self.tela.tamanho('350x300')
        self.tela.gerar(self.titulo)
        self.tela.gerar(self.objetos)
        self.tela.setEvento(13, self.evento)
        self.tela.setEvento(12, self.fechar)
        self.tela.start()

    def evento(self):
        obj = AlunoController()
        msg = "SALVO COM SUCESSO!" '\n' + obj.pegarMatricula(self.tela) + '\n' + obj.pegarNome(self.tela) +\
              '\n' + obj.pegarEmail(self.tela) + '\n' + obj.pegarGenero(self.tela) + '\n' + obj.pegarSenha(self.tela)
        self.tela.mensagem(msg)

    def fechar(self):
        if(self.tela.pergunta("deseja fechar?")):
            pass #Sim
            self.tela.fechar()
        else:
            pass #Não


