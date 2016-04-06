class DB:
    def __init__(self):
        pass
    def persist(self, person):
        pass
    
class Person:
    def __init__(self, db, name):
        self.db = db
        self.name = name
        
    def save(self):
        self.db.persist(self)
    