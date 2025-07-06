import { useEffect, useState } from "react";
import { getPermissions } from "../api/api";

export default function PermissionsPage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getPermissions().then(res => setItems(res.data)).catch(() => setItems([]));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-xl font-bold mb-4">Permissions</h1>
      <table className="min-w-full border border-gray-200">
        <thead><tr><th className="border p-2">ID</th><th className="border p-2">Name</th></tr></thead>
        <tbody>
          {items.length === 0 ? (
            <tr><td colSpan="2" className="text-center p-4">No data</td></tr>
          ) : items.map((i) => (
            <tr key={i.id}><td className="border p-2">{i.id}</td><td className="border p-2">{i.name}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}