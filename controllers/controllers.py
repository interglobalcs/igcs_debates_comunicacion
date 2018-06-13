# -*- coding: utf-8 -*-
from odoo import http

# class IgcsDebatesComunicacion(http.Controller):
#     @http.route('/igcs_debates_comunicacion/igcs_debates_comunicacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/igcs_debates_comunicacion/igcs_debates_comunicacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('igcs_debates_comunicacion.listing', {
#             'root': '/igcs_debates_comunicacion/igcs_debates_comunicacion',
#             'objects': http.request.env['igcs_debates_comunicacion.igcs_debates_comunicacion'].search([]),
#         })

#     @http.route('/igcs_debates_comunicacion/igcs_debates_comunicacion/objects/<model("igcs_debates_comunicacion.igcs_debates_comunicacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('igcs_debates_comunicacion.object', {
#             'object': obj
#         })