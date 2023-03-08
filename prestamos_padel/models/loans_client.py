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
    #_inherit='res.partner'
    _description = 'Clientes inscritos'

    partner_id = fields.Many2one('res.partner', string='Partner',  ondelete='cascade')
    #id = fields.Integer(string='ID', readonly=True)
    name = fields.Char('Nome', required=True)
    dni = fields.Char('DNI', required=True)
    birthDate = fields.Date("Data nacemento", required=True)
    #email = fields.Char('E-mail')
    #phone = fields.Char('Teléfono', required=True)
    loans = fields.One2many('loans.loan', 'client_name',string='Prestamos', readonly=True)

    #crea un id único para cada rexistro
    #@api.model
    #def create(self, vals):
    #    if vals.get('id', 'New') == 'New':
    #        vals['id'] = self.env['ir.sequence'].next_by_code('loan.sequence') or 'Error'
    #    return super(LoansCliente, self).create(vals)

    @api.model
    def create(self, vals):
        partner = self.env['res.partner'].create({'name': vals.get('name')})
        vals['partner_id'] = partner.id
        return super(LoansCliente, self).create(vals)
