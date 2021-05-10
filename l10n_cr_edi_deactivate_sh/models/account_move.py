# Copyright 2020 Vauxoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import os

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'    

    def action_post(self):
        if os.environ.get('environment') in ['staging', 'dev'] and not self.env.company.sudo().l10n_cr_edi_test_env:
            self.env.company.sudo().l10n_cr_edi_test_env = True
        return super().action_post()
