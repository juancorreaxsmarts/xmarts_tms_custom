# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields


class TmsResPartners(models.Model):
    _inherit = 'product.template'

    tms_product = fields.Boolean(help="tms")
