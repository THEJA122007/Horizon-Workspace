const cards = [
  { title: "Total Cases", value: "2,145" },
  { title: "Active Offenders", value: "389" },
  { title: "Hotspot Zones", value: "18" },
  { title: "High Alerts", value: "7" },
];

export default function KPICards() {
  return (
    <div className="grid grid-cols-4 gap-5 mb-8">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-slate-800 rounded-xl p-5 shadow-lg"
        >
          <p className="text-slate-400">{card.title}</p>
          <h2 className="text-3xl font-bold text-cyan-400 mt-2">
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}