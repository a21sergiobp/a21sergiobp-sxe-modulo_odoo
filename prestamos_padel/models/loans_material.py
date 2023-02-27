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
    available = fields.Boolean('Dispoñible', default=False)
    description = fields.Char('Descrición')
    state = fields.Selection([
        ('draft', 'Non dispoñible'),
        ('disponible', 'Dispoñible'),
        ('prestado', 'Prestado'),
        ('roto', 'Roto')],
        'State', default='draft')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'disponible'),
                   ('disponible', 'prestado'),
                   ('prestado', 'disponible'),
                   ('disponible', 'roto'),
                   ('prestado', 'roto'),
                   ('roto', 'disponible'),
                   ('disponible', 'draft')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                message = _('Mover de %s a %s non está permitido') % (book.state, new_state)
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
        self.change_state('draft')
        self.available = False
