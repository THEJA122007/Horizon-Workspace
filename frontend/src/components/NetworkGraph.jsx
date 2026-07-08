import CytoscapeComponent from "react-cytoscapejs";

const elements = [
  { data: { id: "O1", label: "Offender A" } },
  { data: { id: "O2", label: "Offender B" } },
  { data: { id: "L1", label: "Location" } },
  { data: { id: "E1", label: "Vehicle Theft" } },

  { data: { source: "O1", target: "O2" } },
  { data: { source: "O1", target: "L1" } },
  { data: { source: "O2", target: "E1" } },
];

export default function NetworkGraph() {
  return (
    <div className="bg-slate-800 rounded-xl p-4 h-96">
      <h2 className="text-xl font-semibold mb-3">POLE Relationship Network</h2>

      <CytoscapeComponent
        elements={elements}
        style={{ width: "100%", height: "320px" }}
        layout={{ name: "cose" }}
        stylesheet={[
          {
            selector: "node",
            style: {
              label: "data(label)",
              "background-color": "#06b6d4",
              color: "#fff",
              "text-valign": "center",
            },
          },
          {
            selector: "edge",
            style: {
              width: 2,
              "line-color": "#94a3b8",
            },
          },
        ]}
      />
    </div>
  );
}