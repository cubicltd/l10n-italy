# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from codicefiscale import isvalid
from odoo.exceptions import UserError, ValidationError

class AccountBankingMandate(models.Model):
    _inherit = "account.banking.mandate"

    subscriber_full_name = fields.Char(
        "Full Name", help="Subscriber's Full Name")
    subscriber_fiscalcode = fields.Char(
        "Fiscal Code", size=16, help="Subscriber's Italian Fiscal Code")

    @api.multi
    @api.constrains('subscriber_fiscalcode')
    def _check_subscriber_fiscalcode(self):
        for mandate in self:
            if mandate.subscriber_fiscalcode and not isvalid(mandate.subscriber_fiscalcode):
                raise ValidationError(
                    _("This fiscal code is not formally correct: '%s'") % mandate.subscriber_fiscalcode)
