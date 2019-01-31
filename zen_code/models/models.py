# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class zee_code(models.Model):
    _name = 'zen.code'

    name = fields.Char()
    partner_id = fields.Many2one('res.partner', string="Customer", domain="[('customer','=', True)]")
    partner_email = fields.Char(related='partner_id.email', string="Email")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if not self.partner_id:
          pass
        if self.partner_id:
            res = {'warning': {
                'title': _('Warning'),
                'message': _('Alert message.')
            }
            }
            return res

    @api.one
    def action_email(self):
        mail_compose = self.env['mail.mail']

        # get the template
        template_id = self.env.ref('zen_code.email_template_zen')
        # template_id.send_mail(self.ids[0], force_send=True)

        # modify the context
        ctx = dict()
        ctx.update(
            {'default_model': 'zen.code', 'default_use_template': bool(template_id),
             'default_template_id': template_id.id, 'default_composition_mode': 'comment', 'mark_so_as_sent': True,
             'default_subject': template_id.subject})

        # compose message
        new_message = mail_compose.with_context(ctx).create(
            {'email_to': self.partner_id.email, 'subject': template_id.subject,  'body_html': template_id.body_html, })

        # send
        mail = new_message.send()
        print("....", mail)
        return True

        # self.ensure_one()
        # ir_model_data = self.env['ir.model.data']
        # try:
        #     template_id = ir_model_data.get_object_reference('zen_code', 'email_template_zen')[1]
        # except ValueError:
        #     template_id = False
        # try:
        #     compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        # except ValueError:
        #     compose_form_id = False
        # ctx = {
        #     'default_model': 'zen.code',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'custom_layout': "zen_code.email_template_zen",
        #     'force_email': True
        # }
        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'mail.compose.message',
        #     'views': [(compose_form_id, 'form')],
        #     'view_id': compose_form_id,
        #     'target': 'new',
        #     'context': ctx,
        # }

        # customer_name = self.partner_id.name
        # customer_email = self.partner_id.email
        # print("...", customer_email)
        # url = "www.odoo.com"
        # mail_content = "Dear " + customer_name + "," + "<br> Welcome to Odoo World. " \
        #                                                " Please click on this URL: " + url
        # mail_values = {
        #     'email_to': customer_email,
        #     'subject': self.name,
        #     'body_html': mail_content,
        # }
        # create_and_send_email = self.env['mail.mail'].create(mail_values)
        # print ("............", create_and_send_email)
        # mail = create_and_send_email.send()
        # print("....", mail)