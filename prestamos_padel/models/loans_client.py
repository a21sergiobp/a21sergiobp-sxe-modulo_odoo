# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class LoansCliente(models.Model):
    _inherit =["res.partner"]
    _name = 'loans.client'
    _description = 'Clientes inscritos'

    birthDate = fields.Date("Data nacemento", required=True)
