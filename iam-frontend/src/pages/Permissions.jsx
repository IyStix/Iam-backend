
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Permissions() {
  const [permissions, setPermissions] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/permissions').then(res => {
      setPermissions(res.data)
    }).catch(() => {
      setPermissions([])
    })
  }, [])

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Permissions</h1>
      <table className="min-w-full border">
        <thead>
          <tr>
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Username</th>
            <th className="border px-2 py-1">Email</th>
          </tr>
        </thead>
        <tbody>
          {permissions.length === 0 ? (
            <tr><td className="border px-2 py-1" colSpan="3">No permissions found</td></tr>
          ) : (
            permissions.map(permission => (
              <tr key={permission.id}>
                <td className="border px-2 py-1">{permission.id}</td>
                <td className="border px-2 py-1">{permission.permissionname}</td>
                <td className="border px-2 py-1">{permission.email}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
