# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class MaterialLoans(models.Model):
    _name = 'material.loans'
    _description = 'Materiales to loan'

    name = fields.Char('Name', required=True)
