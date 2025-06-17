import random
import string
from DBcm import UseDatabase

dbconfig = {'host':'127.0.0.1',
            'user':'PassMan',
            'password':'qwe123',
            'database':'passmandb'}

class StorContol:
    def add_entry(link_res: str, login: str) -> None:
        password = passwd_gen()
        with UseDatabase(dbconfig) as cursor:
            _SQL = """insert into storage
                      (link, login, password)
                      values
                      (%s, %s, %s)"""
            cursor.execute(_SQL, (link_res, login, password))

    def rem_entry(ident: str) -> None:
        with UseDatabase(dbconfig) as cursor:
            _SQL = """DELETE FROM storage WHERE id = %s"""
            cursor.execute(_SQL, (ident,))
