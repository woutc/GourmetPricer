import gtk
from gourmet.gglobals import *
from gourmet.gdebug import *
from gourmet.gtk_extras.cb_extras import *
import gourmet.GourmetRecipeManager
from gettext import gettext as _
import os
import gobject
import gourmet.convert as convert

try:
    current_path = os.path.split(os.path.join(os.getcwd(),__file__))[0]
except:
    current_path = ''

class PriceAdderGui:
    """This is a simple interface for the price adder."""
    def __init__ (self, unitModel=None):
        debug("Opening PriceAdder screen",2)
        self.ui = gtk.Builder()
        self.ui.add_from_file(os.path.join(current_path,'priceAdder.ui'))
        self.window = self.ui.get_object("window1")
        self.window.show()

        signals = {"on_add_clicked": self.add_ingredient,
                   "on_cancel_clicked": self.cancel}
        self.ui.connect_signals(signals)
                
        converter=convert.get_converter()

        if unitModel: 
            self.unitModel = unitModel
        else: 
            self.unitModel = gourmet.GourmetRecipeManager.UnitModel(converter)  
        
        self.comboboxUnit = self.ui.get_object("comboboxUnit")
        self.comboboxUnit.set_model(self.unitModel)
        self.comboboxUnit.set_wrap_width(3)
        self.comboboxUnit.set_wrap_width(3)   
        
    def cancel(self, widget, *args):
        self.window.destroy()
        
    def add_ingredient(self, widget, *args):
        self.window.destroy()        
        
if __name__ == '__main__':
    ps=PriceAdderGui()
    gtk.main()
    
