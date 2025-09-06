# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class EcoleHoraire(models.Model):
    _name = 'ecole.horaire'
    _description = 'Creneaux Horaires'
    _order = 'jour, heure_debut'

    name = fields.Char(string="Nom du créneau", compute='_compute_name', store=True)
    jour = fields.Selection([
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ], string="Jour", required=True, default='lundi')
    
    heure_debut = fields.Float(string="Heure de début", required=True)
    heure_fin = fields.Float(string="Heure de fin", required=True)
    
    _sql_constraints = [
        ('duree_non_negative', 'CHECK(heure_fin > heure_debut)', 'La durée du créneau doit être positive.'),
    ]
    
    @api.depends('jour', 'heure_debut', 'heure_fin')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.jour.capitalize()} de {int(rec.heure_debut)}h à {int(rec.heure_fin)}h"