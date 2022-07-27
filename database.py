from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:

    def __init__(self, host, database, username, password):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')

    def start_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def end_session(self):
        self.session.close()

    def get_or_create(self, model, **kwargs):
        instance = self.session.query(model).filter_by(**kwargs).first()
        created = False
        if instance:
            return instance, created
        else:
            instance = model(**kwargs)
            self.session.add(instance)
            self.session.commit()
            created = True
        return instance, created

    def does_item_exist(self, model, **kwargs):
        instance = self.session.query(model).filter_by(**kwargs).first()
        if instance:
            return True
        return False

    def bulk_create_objs(self, obj_list):
        self.session.add_all(obj_list)
        self.session.commit()
