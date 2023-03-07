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
    returned = fields.Boolean('Devolto', defaul=False)
    date_loan_finish = fields.Datetime('Data de devolucion')

    state = fields.Selection([
        ('prestado', 'Prestado'),
        ('devolto', 'Devolto')],
        'Estado', default='prestado')
    
    def get_date_time():
        current_datetime = datetime.now()
        return current_datetime
    
    date_loan = fields.Datetime('Data do prestamo', default=get_date_time(), required=True)
    
    #método que devolve o material, cambia a data de devolución
    #e volve a poñer o material como dispoñible
    def return_material(self):
        if self.returned==True:
            raise UserError(_('Non se pode devolver, xa está devolto.'))
        else:
            self.returned = True
            self.state='devolto'
            self.date_loan_finish=datetime.now()
            self.material_name.write({'state': 'disponible'})
            self.material_name.write({'available': True})

    #Sobreescribimos método create para que comprobe 
    #si o material está dispoñoble
    #e que cambie o estado do material.
    @api.model
    def create(self, vals):
        new_record = super(Loans, self).create(vals)
        material = new_record.material_name
        if material.available==False:
            raise UserError(_('Ese material non está dispoñible.'))
        else:
            material.write({'state': 'prestado'})
            material.write({'available': False})
        return new_record
    
    #Función que borra un rexistro e volve a vista de árbore
    def action_delete_record(self):
        if self.returned==False:
            raise UserError(_('Non se pode borrar un rexistro non devolto'))
        else:
            self.ensure_one()
            self.unlink()
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'loans.loan',
                'view_mode': 'tree',
                'target': 'current',
            }
