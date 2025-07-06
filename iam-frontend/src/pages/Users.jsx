
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Users() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/users').then(res => {
      setUsers(res.data)
    }).catch(() => {
      setUsers([])
    })
  }, [])

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Users</h1>
      <table className="min-w-full border">
        <thead>
          <tr>
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Username</th>
            <th className="border px-2 py-1">Email</th>
          </tr>
        </thead>
        <tbody>
          {users.length === 0 ? (
            <tr><td className="border px-2 py-1" colSpan="3">No users found</td></tr>
          ) : (
            users.map(user => (
              <tr key={user.id}>
                <td className="border px-2 py-1">{user.id}</td>
                <td className="border px-2 py-1">{user.username}</td>
                <td className="border px-2 py-1">{user.email}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
