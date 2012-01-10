import gtk
from gourmet.gglobals import *
from gourmet.gdebug import *
from gourmet.gtk_extras.cb_extras import *
import gourmet.GourmetRecipeManager
from gettext import gettext as _
import os

try:
    current_path = os.path.split(os.path.join(os.getcwd(),__file__))[0]
except:
    current_path = ''

class PriceSetterGui:
    """This is a simple interface for the price setter."""
    def __init__ (self, unitModel=None):
        self.ui = gtk.Builder()
        self.ui.add_from_file(os.path.join(current_path,'priceSetter.ui'))

    def close (self, *args):
        self.window.hide()
        if self.okcb:
            self.okcb(cb_get_active_text(self.unit2ComboBox),resultLabel.get_text())
        if __name__ == '__main__':
            gtk.main_quit()

if __name__ == '__main__':
    ps=PriceSetterGui()
    gtk.main()
    
