import { useEffect, useState } from "react";
import { getUsers, addUser } from "../api/api"; // addUser à créer côté API
import Sidebar from "../composant/sidebar";

export default function Users() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);

  // States du formulaire
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [hashed_password, sethashed_password] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = () => {
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
  };

  const handleAddUser = async (e) => {
    e.preventDefault();
    try {
      await addUser({ username, email, hashed_password });  // tu peux adapter selon ton API
      alert("Utilisateur ajouté avec succès");
      setShowForm(false);
      setUsername("");
      setEmail("");
      sethashed_hashed_password("");
      fetchUsers();  // rafraîchir la liste
    } catch (err) {
      console.error("Erreur ajout utilisateur", err);
      alert("Erreur lors de l'ajout de l'utilisateur");
    }
  };

  return (
    <div>
      <Sidebar />
      <h1 className="text-xl font-semibold mb-4">Liste des utilisateurs</h1>
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
      {error && <p className="text-red-600 mb-2">{error}</p>}

      <button
        onClick={() => setShowForm(!showForm)}
        className="my-4 px-4 py-2 bg-green-600 text-white rounded"
      >
        {showForm ? "Annuler" : "Add User"}
      </button>

      {showForm && (
        <form onSubmit={handleAddUser} className="space-y-4 mb-6 max-w-sm">
          <input
            className="border p-2 w-full"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            className="border p-2 w-full"
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            className="border p-2 w-full"
            type="password"
            placeholder="Password"
            value={hashed_password}
            onChange={(e) => sethashed_password(e.target.value)}
            required
          />
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded"
            type="submit"
          >
            Ajouter
          </button>
        </form>
      )}
    </div>
  );
}
