from odoo import fields, models, api,_


class Company(models.Model):
    _inherit="hr.news"

    

    def cancel_pay(self):
        for line in self:
            if line.state=="done":
                line.state="approved"
            

   