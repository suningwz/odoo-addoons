# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

from odoo import models, fields, api


class ResBank(models.Model):

    _inherit = "res.bank"

    abi = fields.Char(size=5, string='ABI')
    cab = fields.Char(size=5, string='CAB')


class ResPartnerBank(models.Model):

    _inherit = "res.partner.bank"

    bank_abi = fields.Char(
        size=5,
        string='ABI',
        related='bank_id.abi',
        store=True)
    bank_cab = fields.Char(
        size=5,
        string='CAB',
        related='bank_id.cab',
        store=True)

    @api.onchange('bank_id')
    def onchange_bank_id(self):
        if self.bank_id:
            self.bank_abi = self.bank_id.abi
            self.bank_cab = self.bank_id.cab
