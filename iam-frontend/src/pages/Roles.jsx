import { useEffect, useState } from "react";
import { getRoles } from "../api/api";  // adapte le chemin si besoin

export default function Roles() {
  const [roles, setRoles] = useState([]);

  useEffect(() => {
    getRoles()
      .then(res => {
        setRoles(res.data);
      })
      .catch(() => {
        setRoles([]);
      });
  }, []);

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Roles</h1>
      <table className="min-w-full border">
        <thead>
          <tr>
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Roles</th>
            <th className="border px-2 py-1">Description</th>
            <th className="border px-2 py-1">Users</th>
            <th className="border px-2 py-1">Permissions</th>
          </tr>
        </thead>
        <tbody>
          {roles.length === 0 ? (
            <tr>
              <td className="border px-2 py-1" colSpan="5">
                No roles found
              </td>
            </tr>
          ) : (
            roles.map(role => (
              <tr key={role.id}>
                <td className="border px-2 py-1">{role.id}</td>
                <td className="border px-2 py-1">{role.name}</td>
                <td className="border px-2 py-1">{role.description ?? "-"}</td>
                {/* Si users et permissions sont des listes d'objets, tu peux faire par ex : */}
                <td className="border px-2 py-1">
                  {role.users ? role.users.length : 0}
                </td>
                <td className="border px-2 py-1">
                  {role.permissions ? role.permissions.length : 0}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
