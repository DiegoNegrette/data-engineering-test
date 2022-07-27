from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class VaccineData(Base):
    __tablename__ = 'vaccine_data'

    id = Column(Integer, primary_key=True)
    comarca = Column(String)
    first_vaccine_doses = Column(Integer)
    day = Column(Date)

    def __init__(self, comarca, first_vaccine_doses, day):
        self.comarca = comarca
        self.first_vaccine_doses = first_vaccine_doses
        self.day = day

    def __repr__(self):
        return f"<VaccineData comarca={self.comarca} first_vaccine_doses={self.first_vaccine_doses} day={self.day}>"
