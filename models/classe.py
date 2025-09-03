# -*- coding: utf-8 -*-
from odoo import models, fields

class EcoleClasse(models.Model):
    _name = 'ecole.classe'
    _description = 'Informations Classe'

    name = fields.Char(string='Nom Classe', required=True)
    niveau = fields.Char(string='Niveau')
    professeur_principal_id = fields.Many2one('ecole.professeur', string='Professeur Principal')
    etudiant_ids = fields.One2many('ecole.etudiant', 'classe_id', string='Etudiants')