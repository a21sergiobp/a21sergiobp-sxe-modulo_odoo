# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class LoansMaterial(models.Model):
    _name = 'loans.material'
    _description = 'Materials to loan'

    name = fields.Char('Name', required=True)
    available = fields.Boolean('Available', default=True)
    