# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields


class TmsResPartners(models.Model):
    _inherit = 'res.partner'

    tms = fields.Boolean(help="tms")

class TmsFinalView(models.Model):
    _inherit = 'res.partner'

    
