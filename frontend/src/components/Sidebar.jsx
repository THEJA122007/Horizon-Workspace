import {
  FaChartBar,
  FaProjectDiagram,
  FaMapMarkedAlt,
  FaBell,
} from "react-icons/fa";

export default function Sidebar() {
  return (
    <div className="w-64 bg-slate-950 p-6 border-r border-slate-800">
      <h2 className="text-2xl font-bold text-cyan-400 mb-8">
        KSP
      </h2>

      <ul className="space-y-5">
        <li className="flex items-center gap-3 hover:text-cyan-400 cursor-pointer">
          <FaChartBar />
          Dashboard
        </li>

        <li className="flex items-center gap-3 hover:text-cyan-400 cursor-pointer">
          <FaProjectDiagram />
          Network
        </li>

        <li className="flex items-center gap-3 hover:text-cyan-400 cursor-pointer">
          <FaMapMarkedAlt />
          Hotspots
        </li>

        <li className="flex items-center gap-3 hover:text-cyan-400 cursor-pointer">
          <FaBell />
          Alerts
        </li>
      </ul>
    </div>
  );
}