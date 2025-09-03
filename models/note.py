# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EcoleNote(models.Model):
    _name = 'ecole.note'
    _description = 'Gestion des notes'

    etudiant_id = fields.Many2one('ecole.etudiant', string='Etudiant', required=True)
    matiere_id = fields.Many2one('ecole.matiere', string='Matiere', required=True)
    valeur_note = fields.Float(string='Note', required=True)
    date_evaluation = fields.Date(string='Date', required=True, default=fields.Date.today)
    commentaires = fields.Text(string='Commentaires')
    
    # Champ calculé pour l'agrégation dans la vue pivot
    moyenne_pour_pivot = fields.Float(
        string='Moyenne',
        compute='_compute_moyenne_pour_pivot',
        store=True,
        group_operator='avg' 
    )
    
    # Champ related qui pointe vers la classe de l'etudiant
    classe_id = fields.Many2one(
        'ecole.classe',
        string='Classe',
        related='etudiant_id.classe_id',
        store=True, # Le stocker pour les performances
    )

    @api.depends('valeur_note')
    def _compute_moyenne_pour_pivot(self):
        for rec in self:
            rec.moyenne_pour_pivot = rec.valeur_note