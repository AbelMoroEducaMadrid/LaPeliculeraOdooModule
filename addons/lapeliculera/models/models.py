# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lapeliculera_pelicula(models.Model):
    _name = 'lapeliculera.pelicula'
    _description = 'Película'

    name = fields.Char(String="Título", required=True, help="Introduce el título de la película")
    director = fields.Char(String="Director", required=True, help="Introduce el director de la película")
    color = fields.Boolean(String="Color", help="Indica si la película es en color")
    duracion = fields.Integer(String="Duración en minutos", help="Indica la duración de la película en minutos")
    industria = fields.Selection([('hollywood', 'Hollywood'), ('europea', 'Europea'), ('bollywood', 'Bollywood'), ('otra', 'Otra')], String="Industria", required=True, help="Indica la industria de la película")
    fecha = fields.Date(String="Fecha de estreno en españa", help="Indica la fecha de estreno en España de la película")
    sinopsis = fields.Text(String="sinopsis", help="Introduce la sinopsis de la película")
    genero = fields.Many2one('lapeliculera.genero', String="Género", required=True, help="Indica el género de la película")
    portada = fields.Binary(string="Portada", help="Sube la imagen de la película")

class lapeliculera_genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Género cinematográfico'
    name = fields.Char(String="Género", required=True, help="Introduce el género cinematográfico")
    comentario = fields.Text(String="Comentarios", help="Introduce comentarios sobre el género") 
    pelicula = fields.One2many('lapeliculera.pelicula', 'genero', String="Películas", help="Indica las películas de este género")

