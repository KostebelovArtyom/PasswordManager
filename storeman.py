import secrets
import string
from DBcm import UseDatabase

dbconfig = {'host':'127.0.0.1',
            'user':'PassMan',
            'password':'qwe123',
            'database':'passmandb'}

class StoreContol:
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig

    @classmethod
    def passwd_gen(self):
        total = string.ascii_letters + string.punctuation + string.digits
        val = ''
        for i in range(16):
            val += secrets.choice(total)
        return val
            
    def add_entry(self, link_res: str, login: str) -> None:
        password = self.passwd_gen()
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """insert into storage
                      (link, login, password)
                      values
                      (%s, %s, %s)"""
            cursor.execute(_SQL, (link_res, login, password))

    def rem_entry(self, ident: int) -> None:
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """DELETE FROM storage WHERE id = %s"""
            cursor.execute(_SQL, (ident,))
