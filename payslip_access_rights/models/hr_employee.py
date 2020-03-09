# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
     _inherit = 'hr.employee'
     
     payslip_count = fields.Integer(compute='_compute_payslip_count', string='Payslips', groups="hr_payroll.group_hr_payroll_user,base.group_user")
     

class HrPayslip(models.Model):
    _inherit = "hr.payslip"
    
    new_details_by_salary_rule_category = fields.Many2many('hr.payslip.line', string='Lines', compute='_get_line_ids')
    
    @api.depends('line_ids','line_ids.amount')
    def _get_line_ids(self):
        for rec in self:
            ids = []
            for line in rec.line_ids:
                if line.appears_on_payslip:
                    ids.append(line.id)
            rec.new_details_by_salary_rule_category = [(6, 0, ids)]

