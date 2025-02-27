# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lapeliculera_pelicula(models.Model):
    _name = 'lapeliculera.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, help="Introduce el título de la película")
    director = fields.Char(string="Director", required=True, help="Introduce el director de la película")
    color = fields.Boolean(string="Color", help="Indica si la película es en color")
    duracion = fields.Integer(string="Duración en minutos", help="Indica la duración de la película en minutos")
    industria = fields.Selection([('hollywood', 'Hollywood'), ('europea', 'Europea'), ('bollywood', 'Bollywood'), ('otra', 'Otra')], string="Industria", required=True, help="Indica la industria de la película")
    fecha = fields.Date(string="Fecha de estreno en españa", help="Indica la fecha de estreno en España de la película")
    sinopsis = fields.Text(string="sinopsis", help="Introduce la sinopsis de la película")
    genero = fields.Many2one('lapeliculera.genero', string="Género", required=True, help="Indica el género de la película")
    portada = fields.Binary(string="Portada", help="Sube la imagen de la película")

class lapeliculera_genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Género cinematográfico'
    name = fields.Char(string="Género", required=True, help="Introduce el género cinematográfico")
    comentario = fields.Text(string="Comentarios", help="Introduce comentarios sobre el género") 
    pelicula = fields.One2many('lapeliculera.pelicula', 'genero', string="Películas", help="Indica las películas de este género")
    
class Reparto(models.Model):
    _name = 'lapeliculera.reparto'
    _description = 'Reparto'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del actor o actriz")
    nacionalidad = fields.Char(string="Nacionalidad", help="Nacionalidad del actor o actriz")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", help="Fecha de nacimiento del actor o actriz")
    foto = fields.Binary(string="Foto", help="Sube la imagen del actor o actriz")
