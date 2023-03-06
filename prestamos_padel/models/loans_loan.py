# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class Loans(models.Model):
    _name = 'loans.loan'
    _description = 'Préstamos'

    id = fields.Integer(string='ID', readonly=True)
    date_loan = fields.Date('Data do prestamo', default=datetime.now, required=True)
    client_name = fields.Many2one('res.partner', string='Cliente', required=True)
    material_name = fields.Many2one('loans.material', string='Material', required=True)
    expired = fields.Boolean('Vencido', compute='_compute_expired', default=False)
    returned = fields.Boolean('Devolto', defaul=False)

    state = fields.Selection([
        ('prestado', 'Prestado'),
        ('devolto', 'Devolto')],
        'Estado', default='prestado')

    def get_datetime_four_hours_later():
        current_datetime = datetime.now()
        future_datetime = current_datetime + timedelta(hours=4)
        return future_datetime
    
    def get_date_time():
        current_datetime = datetime.now()
        return current_datetime
    
    date_loan_finish = fields.Datetime('Data de devolucion')
    date_loan = fields.Datetime('Data do prestamo', default=get_date_time(), required=True)

    # Función que pon expired a true si se pasa da entrega e ainda non o devolveu
    @api.depends('date_loan_finish', 'returned')
    def _compute_expired(self):
        for record in self:
            if not record.returned and record.date_loan_finish <= fields.Datetime.now():
                record.expired = True
            else:
                record.expired = False
    
    def return_material(self):
        if self.returned==True:
            raise UserError(_('Non se pode devolver, xa está devolto.'))
        else:
            self.expired=False
            self.returned = True
            self.state='devolto'
            self.date_loan_finish=datetime.now()
            self.material_name.write({'state': 'disponible'})
            self.material_name.write({'available': True})

    @api.model
    def create(self, vals):
        new_record = super(Loans, self).create(vals)
        material = new_record.material_name
        #cliente = new_record.client_name
        if material.available==False:
            raise UserError(_('Ese material non está dispoñible.'))
        #else:
        #    domain=[('client_name', '=', cliente), ('expired', '=', True)]
        #    expired_loans=self.search(domain)
        #    if expired_loans:
        #        raise UserError(_('O cliente ten prestamos vencidos.'))
        #    else:
        material.write({'state': 'prestado'})
        material.write({'available': False})
        return new_record
