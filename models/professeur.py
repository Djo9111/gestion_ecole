# -*- coding: utf-8 -*-
from odoo import models, fields

class EcoleProfesseur(models.Model):
    _name = 'ecole.professeur'
    _description = 'Informations Professeur'

    name = fields.Char(string='Nom Professeur', required=True)
    matiere_ids = fields.Many2many('ecole.matiere', string='Matieres Enseignees')
    email = fields.Char(string='Email')