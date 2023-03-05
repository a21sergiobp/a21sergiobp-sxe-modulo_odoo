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

    def get_datetime_four_hours_later():
        current_datetime = datetime.now()
        future_datetime = current_datetime + timedelta(hours=4)
        return future_datetime
    
    def get_date_time():
        current_datetime = datetime.now()
        return current_datetime
    
    date_loan_finish = fields.Datetime('Data de vencemento', default=get_datetime_four_hours_later(), required=True)
    date_loan = fields.Datetime('Data do prestamo', default=get_date_time(), required=True)

    @api.model
    def create(self, vals):
        if vals.get('id', 'New') == 'New':
            vals['id'] = self.env['ir.sequence'].next_by_code('loan.sequence') or 'Error'
        return super(Loans, self).create(vals)

