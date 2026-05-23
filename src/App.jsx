import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {

  const [contactos, setContactos] = useState([])
  const [form, setForm] = useState({
    nombre: '',
    correo: '',
    telefono: '',
    mensaje: ''
  })

  const API = 'http://127.0.0.1:8000/api/contactos/'

  useEffect(() => {
    obtenerContactos()
  }, [])

  const obtenerContactos = async () => {
    const res = await axios.get(API)
    setContactos(res.data)
  }

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    })
  }

  const guardarContacto = async () => {
    await axios.post(API, form)
    obtenerContactos()

    setForm({
      nombre: '',
      correo: '',
      telefono: '',
      mensaje: ''
    })
  }

  const eliminarContacto = async (id) => {
    await axios.delete(`${API}${id}/`)
    obtenerContactos()
  }

  return (
    <div>

      {/* Banner */}
      <div className="bg-dark text-white text-center p-5">
        <h1>Mi Página Web Dinámica</h1>
        <p>CRUD de Contactos con React y Django</p>
      </div>

      {/* Imágenes */}
      <div className="container mt-4">
        <div className="row">

          <div className="col-md-4">
            <img
              src="https://picsum.photos/400/300"
              className="img-fluid rounded"
            />
          </div>

          <div className="col-md-4">
            <img
              src="https://picsum.photos/401/300"
              className="img-fluid rounded"
            />
          </div>

          <div className="col-md-4">
            <img
              src="https://picsum.photos/402/300"
              className="img-fluid rounded"
            />
          </div>

        </div>
      </div>

      {/* Formulario */}
      <div className="container mt-5">

        <h2>Formulario de Contacto</h2>

        <input
          className="form-control mb-2"
          placeholder="Nombre"
          name="nombre"
          value={form.nombre}
          onChange={handleChange}
        />

        <input
          className="form-control mb-2"
          placeholder="Correo"
          name="correo"
          value={form.correo}
          onChange={handleChange}
        />

        <input
          className="form-control mb-2"
          placeholder="Teléfono"
          name="telefono"
          value={form.telefono}
          onChange={handleChange}
        />

        <textarea
          className="form-control mb-2"
          placeholder="Mensaje"
          name="mensaje"
          value={form.mensaje}
          onChange={handleChange}
        />

        <button
          className="btn btn-primary"
          onClick={guardarContacto}
        >
          Guardar
        </button>

      </div>

      {/* Tabla CRUD */}
      <div className="container mt-5">

        <h2>Lista de Contactos</h2>

        <table className="table">

          <thead>
            <tr>
              <th>Nombre</th>
              <th>Correo</th>
              <th>Teléfono</th>
              <th>Mensaje</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>

            {contactos.map(contacto => (
              <tr key={contacto.id}>
                <td>{contacto.nombre}</td>
                <td>{contacto.correo}</td>
                <td>{contacto.telefono}</td>
                <td>{contacto.mensaje}</td>

                <td>
                  <button
                    className="btn btn-danger"
                    onClick={() => eliminarContacto(contacto.id)}
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}

          </tbody>

        </table>

      </div>

    </div>
  )
}

export default App