from odoo import models, fields

class Alumno (models.model):
    _name = 'desafiot.alumno'
    _description = 'Modelo de Alumno'

    nombre = fields.Char(string='Nombre', required = True)
    apellido = fields.Char(string='Apellido', required = True)
    fecha_nac = fields.Date(string= 'Fecha de Nacimiento', required = True)
    nro_legajo = fields.Char(string= 'Numero de Legajo', required = True)
    email = fields.Char(string= 'Correo Electronico')
    telefono = fields.Char(string= 'Numero de telefono')
    direccion = fields.Many2one('res.country', string= 'Pais', required = True)

class Programa(models.Model):
    _name = 'desafiot.programa'
    _description= 'Modelo de programa'

    nombre = fields.Char(string = 'Nombre', required = True)
    _description = fields.Text(string = 'Descripcion')

class Inscripcion(models.Model):
    _name = 'desafiot.inscripcion'
    _description= 'Modelo de Inscripcion'

    alumnoId = fields.Many2one('desafiot.alumno', string='Alumno', required = True)
    programaId = fields.Many2one('desafiot.programa', string = 'Programa', required = True)

    @api.model
    def obtenerInscriptos(self,programaId):
        alumnos = self.search([('programaId' , '=' , programaId)])
        resultado = []
        for alumno in alumnos:
            datosAlumno = {
                'nombre': alumno.alumno_id.nombre,
                'apellido': alumno.alumno_id.apellido,
                'legajo': alumno.alumno_id.nro_legajo,
                'fecha_nacimiento': alumno.alumno_id.fecha_nacimiento,
                'email': alumno.alumno_id.email,
                'telefono': alumno.alumno_id.telefono,
                'pais': {
                    'id': alumno.alumno_id.pais.id,
                    'nombre': alumno.alumno_id.pais.name,
                }
            }
            resultado.append(datosAlumno)
        return resultado


    
