from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.Table import Table

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)

usuario = Usuario()
usuario.nome = 'Ana'
usuario.email = 'email@teste.com.br'
usuario.senha = 'senha'
print(dao.inserirUsuario(usuario))

#usuario = Usuario()
#usuario.id = 25
#usuario.nome = 'Maria'
#usuario.email = 'email@teste.com.br'
#usuario.senha = '1234567'
#print(dao.alterarUsuario(usuario))

#usuario = Usuario()
#usuario.nome = 'Maria'
#usuario.email = 'email@teste.com.br'
#usuario.senha = 'senha'
#print(dao.excluirUsuario(usuario))

#lista = dao.selecionarUsuarios()
#tela = Table(lista)
