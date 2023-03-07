# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class LoansMaterial(models.Model):
    _name = 'loans.material'
    _description = 'Materiais para prestar'

    name = fields.Char('Nome', required=True)
    available = fields.Boolean('Dispoñible', default=True)
    description = fields.Char('Descrición', required=True)
    id = fields.Integer(string='ID', readonly=True)
    loans = fields.One2many('loans.loan', 'material_name',string='Prestamos')


    @api.model
    def create(self, vals):
        if vals.get('id', 'New') == 'New':
            vals['id'] = self.env['ir.sequence'].next_by_code('loan.sequence') or 'Error'
        return super(LoansMaterial, self).create(vals)

    state = fields.Selection([
        ('indisponible', 'Non dispoñible'),
        ('disponible', 'Dispoñible'),
        ('prestado', 'Prestado'),
        ('roto', 'Roto')],
        'Estado', default='disponible')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('indisponible', 'disponible'),
                   ('disponible', 'roto'),
                   ('roto', 'disponible'),
                   ('disponible', 'indisponible')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for material in self:
            if material.is_allowed_transition(material.state, new_state):
                material.state = new_state
            else:
                message = _('Mover de %s a %s non está permitido') % (material.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('disponible')
        self.available = True

    def make_borrowed(self):
        self.change_state('prestado')
        self.available = False

    def make_lost(self):
        self.change_state('roto')
        self.available = False

    def make_unavailable(self):
        self.change_state('indisponible')
        self.available = False
