# -*- coding: utf-8 -*-
import time

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResCompany(models.Model):
        _inherit = 'res.company'
        invoice_header_image = fields.Binary('Header Image')
