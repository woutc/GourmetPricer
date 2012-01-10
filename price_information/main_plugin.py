from gourmet.plugin import MainPlugin
from gourmet.gglobals import add_icon
import os.path, gtk

class PricingMainPlugin (MainPlugin):

    def activate (self, pluggable):
        """Setup nutritional database stuff."""
        add_icon(os.path.join(os.path.split(__file__)[0],'images','pricing.svg'), 'price-info', _('Pricing Information'))
