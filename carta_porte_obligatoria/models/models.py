# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields
from odoo.exceptions import ValidationError

class TmsResPartners(models.Model):
    _inherit = 'tms.travel'

    bool = fields.Boolean()

    #@api.onchange('order_line')
    #def progress(self):
        #if self.order_line:
        #    self.bool = self.order_line

    @api.onchange('waybill_ids')
    def action_progress_cron(self):
        for rec in self:
            rec.validate_driver_license()
            rec.validate_vehicle_insurance()
            travels = rec.search(
                [('state', '=', 'progress'), '|',
                 ('employee_id', '=', rec.employee_id.id),
                 ('unit_id', '=', rec.unit_id.id)])
            if len(travels) >= 1:
                raise ValidationError(
                    _('The unit or driver are already in use!'))
            rec.state = "progress"
            rec.date_start_real = fields.Datetime.now()
            if self.waybill_ids:
                self.bool = True
            else:
                raise ValidationError("Debe llenar las lineas de Carta Porte")
