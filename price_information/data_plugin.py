import sqlalchemy, sqlalchemy.orm
from sqlalchemy import Integer, Binary, String, Float, Boolean, Numeric, Table, Column, ForeignKey, Text
from sqlalchemy.sql import and_, or_
import gourmet.backends.db
from gourmet.plugin import DatabasePlugin
from gourmet.gdebug import *

class PricingDataPlugin (DatabasePlugin):
    name = 'pricingdata'
    version = 1

    def setup_prices_table (self):
        self.db.prices_table = Table('pricingdata',self.db.metadata,
                                                Column('id',Integer(),primary_key=True),
                                                Column('amount',String(length=None),**{}),
                                                Column('unit',String(length=None),**{}), 
                                                Column('price',Float(),**{})
                                                ) 
        class PricingData (object):
            pass
        self.db._setup_object_for_table(self.db.prices_table, PricingData)

    def create_tables (self, *args):
        debug("Create tables",2)
        self.setup_prices_table()                           
