import { useEffect, useState } from "react";
import { getPermissions } from "../api/api"; // adapte le chemin
import Sidebar from "../composant/sidebar";

export default function Permissions() {
  const [permissions, setPermissions] = useState([]);

  useEffect(() => {
    getPermissions()
      .then((res) => {
        setPermissions(res.data);
      })
      .catch(() => {
        setPermissions([]);
      });
  }, []);

  return (
    <div>
      <Sidebar />
      <h1 className="text-xl font-semibold mb-4">Permissions</h1>
      <table className="min-w-full border">
        <thead>
          <tr>
            <th className="border px-2 py-1">ID</th>
            <th className="border px-2 py-1">Permission Name</th>
            <th className="border px-2 py-1">Description</th>
          </tr>
        </thead>
        <tbody>
          {permissions.length === 0 ? (
            <tr>
              <td className="border px-2 py-1" colSpan="3">
                No permissions found
              </td>
            </tr>
          ) : (
            permissions.map((permission) => (
              <tr key={permission.id}>
                <td className="border px-2 py-1">{permission.id}</td>
                <td className="border px-2 py-1">{permission.name ?? permission.permissionname}</td>
                <td className="border px-2 py-1">{permission.description ?? "-"}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
