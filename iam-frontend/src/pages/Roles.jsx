
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Roles() {
  const [roles, setRoles] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/roles').then(res => {
      setRoles(res.data)
    }).catch(() => {
      setRoles([])
    })
  }, [])

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Roles</h1>
      <table className="min-w-full border">
        <thead>
          <tr>
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Roles</th>
            <th className="border px-2 py-1">description</th>
            <th className="border px-2 py-1">users</th>
            <th className="border px-2 py-1">permissions</th>

          </tr>
        </thead>
        <tbody>
          {roles.length === 0 ? (
            <tr><td className="border px-2 py-1" colSpan="3">No roles found</td></tr>
          ) : (
            roles.map(role => (
              <tr key={role.id}>
                <td className="border px-2 py-1">{role.id}</td>
                <td className="border px-2 py-1">{role.name}</td>
                <td className="border px-2 py-1">{role.description}</td>
                <td className="border px-2 py-1">{role.users}</td>
                <td className="border px-2 py-1">{role.permissions}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
