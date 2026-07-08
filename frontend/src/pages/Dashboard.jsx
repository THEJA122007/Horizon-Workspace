import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import KPICards from "../components/KPICards";

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-slate-900 text-white">
      <Sidebar />

      <main className="flex-1 p-6">
        <Header />
        <KPICards />

        <div className="grid grid-cols-2 gap-6">
          <div className="bg-slate-800 rounded-xl h-96 flex items-center justify-center">
            Network Graph
          </div>

          <div className="bg-slate-800 rounded-xl h-96 flex items-center justify-center">
            Crime Hotspot Map
          </div>
        </div>
      </main>
    </div>
  );
}