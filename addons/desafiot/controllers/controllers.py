from odoo import http
from odoo.http import request

class DesafiotController(http.Controller):

    @http.route('/desafiot/alumnos', auth='public', website=True)
    def list_alumnos(self, **kwargs):
        alumnos = request.env['desafiot.alumno'].search([])
        return http.request.render('desafiot.alumno_tree', {'alumnos': alumnos})

    @http.route('/desafiot/alumno/<int:alumno_id>', auth='public', website=True)
    def view_alumno(self, alumno_id, **kwargs):
        alumno = request.env['desafiot.alumno'].browse(alumno_id)
        return http.request.render('desafiot.alumno_form', {'alumno': alumno})

    @http.route('/desafiot/programas', auth='public', website=True)
    def list_programas(self, **kwargs):
        programas = request.env['desafiot.programa'].search([])
        return http.request.render('desafiot.programa_tree', {'programas': programas})

    @http.route('/desafiot/programa/<int:programa_id>', auth='public', website=True)
    def view_programa(self, programa_id, **kwargs):
        programa = request.env['desafiot.programa'].browse(programa_id)
        return http.request.render('desafiot.programa_form', {'programa': programa})

    @http.route('/desafiot/inscripciones', auth='public', website=True)
    def list_inscripciones(self, **kwargs):
        inscripciones = request.env['desafiot.inscripcion'].search([])
        return http.request.render('desafiot.inscripcion_tree', {'inscripciones': inscripciones})

    @http.route('/desafiot/inscripcion/<int:inscripcion_id>', auth='public', website=True)
    def view_inscripcion(self, inscripcion_id, **kwargs):
        inscripcion = request.env['desafiot.inscripcion'].browse(inscripcion_id)
        return http.request.render('desafiot.inscripcion_form', {'inscripcion': inscripcion})

