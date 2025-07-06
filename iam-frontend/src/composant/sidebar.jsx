import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Sidebar = ({ className }) => {
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();
  const currentPath = window.location.pathname.toLowerCase();
  const normalizedPath = currentPath.endsWith("/")
    ? currentPath.slice(0, -1)
    : currentPath;

  const goToUsers = () => {
    navigate("/users");
  };

  const goToRoles = () => {
    navigate("/roles");
  };

  const goToPermissions = () => {
    navigate("/permissions");
  };

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      {isOpen ? (
        <div className="fixed h-full bg-gray-800 text-white transition-all duration-300 w-64 z-50">
          <button
            onClick={toggleSidebar}
            className={`left-1 p-4 focus:outline-none hover:bg-gray-700 ${className}`}
          >
            ❌
          </button>
          <nav className="mt-4 cursor-pointer">
            <ul className="overflow-hidden">
              <li
                onClick={goToUsers}
                className={`p-4 hover:bg-gray-700 ${
                  normalizedPath === "/users" ? "bg-gray-600" : ""
                }`}
              >
                Utilisateurs
              </li>
              <li
                onClick={goToRoles}
                className={`p-4 hover:bg-gray-700 ${
                  normalizedPath === "/roles" ? "bg-gray-600" : ""
                }`}
              >
                Rôles
              </li>
              <li
                onClick={goToPermissions}
                className={`p-4 hover:bg-gray-700 ${
                  normalizedPath === "/permissions" ? "bg-gray-600" : ""
                }`}
              >
                Permissions
              </li>
              <li
                onClick={logout}
                className={`p-4 hover:bg-gray-700 ${
                  normalizedPath === "/login" ? "bg-gray-600" : ""
                }`}
              >
                Déconnexion
              </li>
            </ul>
          </nav>
        </div>
      ) : (
        <button
          onClick={toggleSidebar}
          className={`fixed left-2 top-2 rounded-2xl p-4 focus:outline-none opacity-70 bg-gray-700 hover:bg-gray-700 text-white transition-all duration-300 size-fit z-50 ${className}`}
        >
          ☰
        </button>
      )}
    </div>
  );
};

export default Sidebar;
