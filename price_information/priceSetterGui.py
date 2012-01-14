import gtk
from gourmet.gglobals import *
from gourmet.gdebug import *
from gourmet.gtk_extras.cb_extras import *
import gourmet.GourmetRecipeManager
from gettext import gettext as _
import os
import gobject
import priceAdderGui

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
        
        signals = {"on_add_clicked": self.add_ingredient,
                   "on_remove_clicked": self.remove_ingredient}
        self.ui.connect_signals(signals)
        
        self.iter = {}
        self.model = gtk.ListStore(gobject.TYPE_INT, gobject.TYPE_OBJECT, gobject.TYPE_STRING, gobject.TYPE_FLOAT)
        self.listview = self.ui.get_object("ingTree")
        self.listview.set_model(self.model)
        self.listview.set_flags(gtk.TREE_MODEL_ITERS_PERSIST)
        
        if unitModel: 
            self.unitModel = unitModel
        else: 
            self.unitModel = gourmet.GourmetRecipeManager.UnitModel(self.conv)        
        
        columns = [_("Amt"), _("Unit"), _("Ingredient"), _("Price")]          
        
        for column_ in columns:
            if column_ == _("Unit"):
                column_renderer = gtk.CellRendererCombo()
                column_renderer.set_property('model',self.unitModel)
                column_renderer.set_property('text-column',0)
               
            else:
                column_renderer = gtk.CellRendererText()
            
            column_renderer.set_property("editable", True)    
            column = gtk.TreeViewColumn(column_, column_renderer, text=2, weight=5)
            column.set_expand(True)
            column.set_resizable(True)
            self.listview.append_column(column)              
        
    def add_ingredient(self, widget, *args):   
        w = priceAdderGui.PriceAdderGui(self.unitModel)       
        
    def remove_ingredient(self, widget, *args):           
        model, iter = self.listview.get_selection().get_selected()
        
        if iter != None and self.model.iter_is_valid(iter):
            self.model.remove(iter)
           
        
if __name__ == '__main__':
    ps=PriceSetterGui()
    gtk.main()
    
