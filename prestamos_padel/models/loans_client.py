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
    def fields_view_get(self, view_id='view_partners_form_crm1', view_type='form', toolbar=False, submenu=False):
        res = super(LoansCliente, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='city'] | //field[@name='country_id'] | //field[@name='is_company'] | //field[@name='activity_type_id'] | //field[@name='commercial_partner_id']"):
                node.set('invisible', '1')
            res['arch'] = etree.tostring(doc)
        return res

    @api.model
    def create(self, vals):
        if vals.get('id', 'New') == 'New':
            vals['id'] = self.env['ir.sequence'].next_by_code('loan.sequence') or 'Error'
        return super(LoansCliente, self).create(vals)
