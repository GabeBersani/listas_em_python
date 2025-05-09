from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///listalivros.sqlite3')
db_sesion = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_sesion.query_property()

class Livros(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    Titulo = Column(String(40), nullable=False, index=True)
    Autor = Column(String(11), nullable=False, index=True, unique=True)
    ano_de_nascimento = Column(Integer, nullable=False, index=True)
    endereco = Column(String(40), nullable=False, index=True)
    cpf = Column(String(11), nullable=False, index=True, unique=True)
    email = Column(String(50), nullable=False, index=True, unique=True)

    def __repr__(self):
        return '<Funcionario: Nome: {} CPF: {}>'.format(self.nome, self.cpf)

    def save(self):
        db_sesion.add(self)
        db_sesion.commit()

    def delete(self):
        db_sesion.delete(self)
        db_sesion.commit()

    def serialize_user(self):
        dados_funcionario = {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'ano_de_nascimento': self.ano_de_nascimento,
            'endereco': self.endereco,
            'cpf': self.cpf,
            'email': self.email,
        }

        return dados_funcionario
