# -*- coding: utf-8 -*-
from odoo import models, fields

class EcoleMatiere(models.Model):
    _name = 'ecole.matiere'
    _description = 'Informations Matiere'

    name = fields.Char(string='Nom de la matiere', required=True)
    description = fields.Text(string='Description')
    professeur_ids = fields.Many2many('ecole.professeur', string='Professeurs')
    note_ids = fields.One2many('ecole.note', 'matiere_id', string='Notes')
    coefficient = fields.Integer(string='Coefficient', default=1, required=True)