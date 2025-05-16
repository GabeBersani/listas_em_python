from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///listafuncionario.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    cargo = Column(String(40), nullable=False, index=True)
    salario = Column(String(40), nullable=False, index=True)



    def __repr__(self):
        return '<Funcionarios: Cargo: {} Salario: {}>'.format(self.cargo, self.salario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_livros = {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario,
        }

        return dados_livros

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
