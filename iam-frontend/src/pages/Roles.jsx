
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
            <th className="border px-2 py-1">Username</th>
            <th className="border px-2 py-1">Email</th>
          </tr>
        </thead>
        <tbody>
          {roles.length === 0 ? (
            <tr><td className="border px-2 py-1" colSpan="3">No roles found</td></tr>
          ) : (
            roles.map(role => (
              <tr key={role.id}>
                <td className="border px-2 py-1">{role.id}</td>
                <td className="border px-2 py-1">{role.rolename}</td>
                <td className="border px-2 py-1">{role.email}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
