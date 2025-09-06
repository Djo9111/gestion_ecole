# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EcoleEmploiDuTemps(models.Model):
    _name = 'ecole.emploi_du_temps'
    _description = 'Emploi du Temps'
    _order = 'horaire_id'

    name = fields.Char(string="Nom de la session", compute='_compute_name', store=True)
    classe_id = fields.Many2one('ecole.classe', string="Classe", required=True)
    matiere_id = fields.Many2one('ecole.matiere', string="Matière", required=True)
    professeur_id = fields.Many2one('ecole.professeur', string="Professeur", required=True)
    horaire_id = fields.Many2one('ecole.horaire', string="Créneau Horaire", required=True)

    @api.depends('classe_id', 'matiere_id', 'horaire_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.matiere_id.name} pour {rec.classe_id.name} ({rec.horaire_id.name})"

    @api.constrains('horaire_id', 'professeur_id', 'classe_id')
    def _check_unicity(self):
        for record in self:
            domain_prof = [
                ('id', '!=', record.id),
                ('horaire_id', '=', record.horaire_id.id),
                ('professeur_id', '=', record.professeur_id.id),
            ]
            if self.search_count(domain_prof):
                raise ValidationError(_("Ce professeur est déjà assigné à un autre cours sur ce créneau horaire."))

            domain_classe = [
                ('id', '!=', record.id),
                ('horaire_id', '=', record.horaire_id.id),
                ('classe_id', '=', record.classe_id.id),
            ]
            if self.search_count(domain_classe):
                raise ValidationError(_("Cette classe a déjà un cours sur ce créneau horaire."))