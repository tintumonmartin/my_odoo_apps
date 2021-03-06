# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools
from odoo.exceptions import ValidationError


class BaseModuleUninstall(models.TransientModel):
    _inherit = "base.module.uninstall"

    is_restrict = fields.Boolean()
    password = fields.Char(required=True)

    def action_uninstall(self):
        if not tools.config.get('uninstall_password'):
            raise ValidationError("Uninstall password not yet set!")
        if self.password != tools.config.get('uninstall_password').replace('\'', ''):
            raise ValidationError("Invalid Password!")
        return super(BaseModuleUninstall, self).action_uninstall()
