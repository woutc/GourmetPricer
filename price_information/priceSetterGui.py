import gtk
from gourmet.gglobals import *
from gourmet.gdebug import *
from gourmet.gtk_extras.cb_extras import *
import gourmet.GourmetRecipeManager
from gettext import gettext as _
import os
import gobject

try:
    current_path = os.path.split(os.path.join(os.getcwd(),__file__))[0]
except:
    current_path = ''

class PriceSetterGui:
    """This is a simple interface for the price setter."""
    def __init__ (self, unitModel=None):
        debug("Opening PriceSetter screen",2)
        self.ui = gtk.Builder()
        self.ui.add_from_file(os.path.join(current_path,'priceSetter.ui'))
        
        signals = {"on_add_clicked": self.add_ingredient}
        self.ui.connect_signals(signals)
        
        self.iter = {}
        self.model = gtk.ListStore(gobject.TYPE_INT, gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_INT)
        self.listview = self.ui.get_object("ingTree")
        self.listview.set_model(self.model)
        self.listview.set_flags(gtk.TREE_MODEL_ITERS_PERSIST)  
        
        ### Quantity
        self.columnQuantity_renderer = gtk.CellRendererText()
        self.columnQuantity_renderer.set_property("editable", True)
        self.columnQuantity = gtk.TreeViewColumn(_("Quantity"), self.columnQuantity_renderer, text=2, weight=5)
        self.columnQuantity.set_expand(True)
        self.columnQuantity.set_resizable(True)
        self.listview.append_column(self.columnQuantity)            
        
        ### Units
        self.columnUnitAmt_renderer = gtk.CellRendererText()
        self.columnUnitAmt_renderer.set_property("editable", True)
        self.columnUnitAmt = gtk.TreeViewColumn(_("Unit"), self.columnUnitAmt_renderer, text=2, weight=5)
        self.columnUnitAmt.set_expand(True)
        self.columnUnitAmt.set_resizable(True)
        self.listview.append_column(self.columnUnitAmt)           
        
        ### Name
        self.columnName_renderer = gtk.CellRendererText()
        self.columnName_renderer.set_property("editable", True)
        self.columnName = gtk.TreeViewColumn(_("Ingredient"), self.columnName_renderer, text=2, weight=5)
        self.columnName.set_expand(True)
        self.columnName.set_resizable(True)
        self.listview.append_column(self.columnName)           
        
        ### Price
        self.columnPrice_renderer = gtk.CellRendererText()
        self.columnPrice_renderer.set_property("editable", True)
        self.columnPrice = gtk.TreeViewColumn(_("Price"), self.columnPrice_renderer, text=2, weight=5)
        self.columnPrice.set_expand(True)
        self.columnPrice.set_resizable(True)
        self.listview.append_column(self.columnPrice)   
        
    def add_ingredient(self, widget, *args):             
        self.iter[0] = self.model.insert_before(None, None)
        self.model.set_value(self.iter[0], 0, 0)
        self.model.set_value(self.iter[0], 1, "")
        self.model.set_value(self.iter[0], 2, "")
        self.model.set_value(self.iter[0], 3, 0)
        
if __name__ == '__main__':
    ps=PriceSetterGui()
    gtk.main()
    
