# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from lxml import etree

logger = logging.getLogger(__name__)


class LoansCliente(models.Model):
    _name = 'res.partner'
    _inherit ='res.partner'
    _description = 'Clientes inscritos'

    id = fields.Integer(string='ID', readonly=True)
    birthDate = fields.Date("Data nacemento", required=True)

    @api.model
    def create(self, vals):
        if vals.get('id', 'New') == 'New':
            vals['id'] = self.env['ir.sequence'].next_by_code('loan.sequence') or 'Error'
        return super(LoansCliente, self).create(vals)
