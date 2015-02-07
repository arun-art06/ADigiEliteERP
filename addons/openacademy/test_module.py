from openerp.osv import osv
from  openerp.osv import fields

class test_base(osv.osv):

    "'Test Base Class'"

    _name='test.base'

    _columns={

            'name':fields.char("Name",size=128,),

            'code':fields.char("Code",size=64)

    }

test_base()
