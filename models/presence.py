# -*- coding: utf-8 -*-
from odoo import models, fields

class EcolePresence(models.Model):
    _name = 'ecole.presence'
    _description = 'Registre des Presences'

    etudiant_id = fields.Many2one('ecole.etudiant', string="Etudiant", required=True)
    date_presence = fields.Date(string="Date", required=True, default=fields.Date.today)
    statut_presence = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
    ], string="Statut", default='present', required=True)

    _sql_constraints = [
        ('etudiant_date_unique', 'unique(etudiant_id, date_presence)', 'La presence de cet etudiant a deja ete enregistree pour cette date !'),
    ]