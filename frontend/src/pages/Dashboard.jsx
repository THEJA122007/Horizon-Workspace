import Sidebar from "../components/Sidebar";

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-slate-900 text-white">
      <Sidebar />

      <main className="flex-1 p-6">
        <h1 className="text-4xl font-bold text-cyan-400">
          KSP Crime Analytics Dashboard
        </h1>

        <p className="mt-2 text-slate-300">
          Karnataka State Police Crime Intelligence Platform
        </p>
      </main>
    </div>
  );
}