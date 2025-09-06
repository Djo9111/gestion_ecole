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
    presence_ids = fields.One2many('ecole.presence', 'etudiant_id', string='Présences')
    
    # Champ pour la moyenne générale calculée avec les coefficients
    moyenne_generale = fields.Float(string='Moyenne Generale', compute='_compute_moyenne', store=True)

    # Nouveaux champs pour le calcul d'assiduité
    total_jours = fields.Integer(string='Jours de Classe', compute='_compute_assiduite', store=True)
    jours_presents = fields.Integer(string='Jours de Présence', compute='_compute_assiduite', store=True)
    jours_absents = fields.Integer(string='Jours d\'Absence', compute='_compute_assiduite', store=True)
    jours_excuses = fields.Integer(string='Jours Excusés', compute='_compute_assiduite', store=True)
    taux_presence = fields.Float(string='Taux de Présence (%)', compute='_compute_assiduite', store=True)

    @api.depends('note_ids.valeur_note', 'note_ids.matiere_id.coefficient')
    def _compute_moyenne(self):
        for etudiant in self:
            if etudiant.note_ids:
                total_pondere = sum(note.valeur_note * (note.matiere_id.coefficient or 1) for note in etudiant.note_ids)
                total_coefficients = sum(note.matiere_id.coefficient or 1 for note in etudiant.note_ids)
                etudiant.moyenne_generale = total_pondere / total_coefficients if total_coefficients > 0 else 0.0
            else:
                etudiant.moyenne_generale = 0.0

    @api.depends('presence_ids.statut_presence')
    def _compute_assiduite(self):
        for etudiant in self:
            etudiant.total_jours = len(etudiant.presence_ids)
            etudiant.jours_presents = len(etudiant.presence_ids.filtered(lambda p: p.statut_presence == 'present'))
            etudiant.jours_absents = len(etudiant.presence_ids.filtered(lambda p: p.statut_presence == 'absent'))
            etudiant.jours_excuses = len(etudiant.presence_ids.filtered(lambda p: p.statut_presence == 'excusé'))
            if etudiant.total_jours > 0:
                etudiant.taux_presence = (etudiant.jours_presents / etudiant.total_jours) * 100
            else:
                etudiant.taux_presence = 0.0