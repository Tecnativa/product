# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class ResUsers(models.Model):

    _inherit = "res.users"

    salesman_group_id = fields.Many2one(
        'sale.salesman.group',
        string='Salesman Group', )
