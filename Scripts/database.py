from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from numpy import nan
import pandas as pd

Base = declarative_base()

engine = create_engine('sqlite:///main.db', echo=True)

df = pd.read_csv()

df.to_sql("Pleiades", engine, if_exists='replace', index=False)