# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EcoleEtudiant(models.Model):
    _name = 'ecole.etudiant'
    _description = 'Informations Etudiant'

    name = fields.Char(string='Nom Complet', required=True)
    date_naissance = fields.Date(string='Date de Naissance')
    classe_id = fields.Many2one('ecole.classe', string='Classe')
    adresse = fields.Text(string='Adresse')
    email = fields.Char(string='Email')
    note_ids = fields.One2many('ecole.note', 'etudiant_id', string='Notes')
    
    # Champ pour la moyenne générale calculée avec les coefficients
    moyenne_generale = fields.Float(string='Moyenne Generale', compute='_compute_moyenne', store=True)

    @api.depends('note_ids.valeur_note', 'note_ids.matiere_id.coefficient')
    def _compute_moyenne(self):
        for etudiant in self:
            if etudiant.note_ids:
                total_pondere = 0
                total_coefficients = 0
                for note in etudiant.note_ids:
                    coefficient = note.matiere_id.coefficient or 1 # Utiliser 1 si le coefficient n'est pas defini
                    total_pondere += note.valeur_note * coefficient
                    total_coefficients += coefficient
                etudiant.moyenne_generale = total_pondere / total_coefficients
            else:
                etudiant.moyenne_generale = 0.0