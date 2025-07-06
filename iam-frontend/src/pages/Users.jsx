import { useEffect, useState } from "react";
import { getUsers } from "../api/api";  // adapte le chemin si besoin

export default function Users() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getUsers()
      .then((res) => {
        setUsers(res.data);
        setError(null);
      })
      .catch((err) => {
        console.error("Error fetching users:", err);
        setError("Impossible de récupérer les utilisateurs");
        setUsers([]);
      });
  }, []);

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Users</h1>
      {error && <p className="text-red-600 mb-2">{error}</p>}
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
            <tr>
              <td className="border px-2 py-1" colSpan={3}>
                No users found
              </td>
            </tr>
          ) : (
            users.map((user) => (
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
  );
}
