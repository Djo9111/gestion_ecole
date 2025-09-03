# -*- coding: utf-8 -*-
# Fichier __manifest__.py

{
    'name': 'Gestion Etablissement Scolaire',
    'version': '1.0',
    'summary': 'Module de gestion pour un etablissement scolaire',
    'description': """
        Module Odoo pour gerer les etudiants, professeurs et classes d'une ecole.
    """,
    'author': 'Ton Nom',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ecole_classe_views.xml',
        'views/ecole_matiere_views.xml',
        'views/ecole_professeur_views.xml',
        'views/ecole_note_views.xml',
        # D'abord les modèles de rapport (template et action)
        'reports/bulletin_de_notes_template.xml', 
        'reports/reports.xml', 
        # Ensuite les vues qui font référence aux actions de rapport
        'views/ecole_etudiant_views.xml',
        'views/ecole_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}