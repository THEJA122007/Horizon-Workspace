import { FaUserCircle, FaSearch } from "react-icons/fa";

export default function Header() {
  return (
    <header className="flex items-center justify-between mb-8">
      <div>
        <h1 className="text-4xl font-bold text-cyan-400">
          KSP Crime Analytics Dashboard
        </h1>
        <p className="text-slate-400 mt-1">
          Real-Time Crime Intelligence & Investigation Platform
        </p>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center bg-slate-800 px-3 py-2 rounded-lg">
          <FaSearch className="text-slate-400 mr-2" />
          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent outline-none text-white"
          />
        </div>

        <FaUserCircle size={35} className="text-cyan-400" />
      </div>
    </header>
  );
}