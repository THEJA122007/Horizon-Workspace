import { MapContainer, TileLayer, CircleMarker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const hotspots = [
  {
    id: 1,
    district: "Bengaluru",
    lat: 12.9716,
    lng: 77.5946,
    count: 42,
  },
  {
    id: 2,
    district: "Mysuru",
    lat: 12.2958,
    lng: 76.6394,
    count: 21,
  },
];

export default function CrimeMap() {
  return (
    <div className="bg-slate-800 rounded-xl p-4 h-96">
      <h2 className="text-xl font-semibold mb-3">
        Crime Hotspots
      </h2>

      <MapContainer
        center={[12.9716, 77.5946]}
        zoom={7}
        style={{ height: "320px", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {hotspots.map((spot) => (
          <CircleMarker
            key={spot.id}
            center={[spot.lat, spot.lng]}
            radius={spot.count / 4}
            pathOptions={{ color: "red" }}
          >
            <Popup>
              <strong>{spot.district}</strong>
              <br />
              Crime Count: {spot.count}
            </Popup>
          </CircleMarker>
        ))}
      </MapContainer>
    </div>
  );
}