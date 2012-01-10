from gourmet.plugin import ToolPlugin
import gtk
import priceSetterGui
from gettext import gettext as _

class PriceSetterPlugin (ToolPlugin):
    menu_items = '''<placeholder name="StandaloneTool">
    <menuitem action="PriceSetter"/>
    </placeholder>'''

    def setup_action_groups (self):
        self.action_group = gtk.ActionGroup('PriceSetterPluginActionGroup')
        self.action_group.add_actions([
            ('PriceSetter',None,_('Ingredient _prices'),
             None,_('Ingredient prices'),self.show_price_setter)
            ]
                                      )
        self.action_groups.append(self.action_group)

    def show_price_setter (self, *args):
        try:
            umodel = self.pluggable.umodel
        except AttributeError:
            try:
                umodel = self.pluggable.rg.umodel
            except:
                umodel = None
        priceSetterGui.PriceSetterGui(unitModel=umodel)
        
plugins = [PriceSetterPlugin]
