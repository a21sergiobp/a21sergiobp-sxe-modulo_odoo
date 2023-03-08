# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from lxml import etree

logger = logging.getLogger(__name__)

class LoansCliente(models.Model):
    _name = 'loans.client'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Clientes inscritos'

    partner_id = fields.Many2one('res.partner', string='Partner',  ondelete='cascade')
    #id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(related='partner_id.name', string='Nome', required=True, readonly=False)
    dni = fields.Char('DNI', required=True)
    birthDate = fields.Date("Data nacemento", required=True)
    loans = fields.One2many('loans.loan', 'client_name',string='Prestamos', readonly=True)
    email = fields.Char(related='partner_id.email', string='Correo electrónico', readonly=False)
    phone = fields.Char(related='partner_id.phone', string='Teléfono', required=True, readonly=False)

    #Cando creamos un rexistro engadimos os valores no modelo res.partner tamén
    @api.model
    def create(self, vals):
        partner_vals = {'name': vals.get('name'), 'email': vals.get('email'), 'phone': vals.get('phone')}
        partner = self.env['res.partner'].create(partner_vals)
        vals['partner_id'] = partner.id
        return super(LoansCliente, self).create(vals)
    
    #se se modifica un rexistro cambiamolo en res.partner tamén
    def write(self, vals):
        result = super(LoansCliente, self).write(vals)
        if 'name' in vals or 'email' in vals or 'phone' in vals:
            partner_vals = {}
            if 'name' in vals:
                partner_vals['name'] = vals['name']
            if 'email' in vals:
                partner_vals['email'] = vals['email']
            if 'phone' in vals:
                partner_vals['phone'] = vals['phone']
            self.partner_id.write(partner_vals)
        return result
