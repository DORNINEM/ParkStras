
import React, { useState, useEffect, useMemo } from 'react';
import ReactDOM from 'react-dom/client';
import { MapContainer, TileLayer, Marker, Popup, useMap, Polyline, CircleMarker, Tooltip } from 'react-leaflet';
import L from 'leaflet';
import SunCalc from 'suncalc';
import { GoogleGenAI } from "@google/genai";
import { Sun, Calendar, Info, Loader2, MapPin, Navigation, Search } from 'lucide-react';

// --- TYPES ---

interface Coordinates {
  lat: number;
  lng: number;
}

interface SunPosition {
  azimuth: number; // in radians
  altitude: number; // in radians
  time: Date;
}

interface SunPathData {
  date: Date;
  label: string;
  color: string;
  points: SunPosition[];
}

enum Season {
  SUMMER = 'Ete',
  WINTER = 'Hiver',
  TODAY = 'Aujourd\'hui'
}

interface LocationInfo {
  coords: Coordinates;
  address?: string;
}

// --- UTILS: SUN CALCULATIONS ---

const getDayHours = (date: Date): Date[] => {
  const hours: Date[] = [];
  const start = new Date(date);
  start.setHours(6, 0, 0, 0);
  
  const end = new Date(date);
  end.setHours(20, 0, 0, 0);

  let current = start;
  while (current <= end) {
    hours.push(new Date(current));
    current = new Date(current.getTime() + 30 * 60 * 1000); // Every 30 mins
  }
  return hours;
};

const calculateSunPaths = (coords: Coordinates): SunPathData[] => {
  if (!coords || isNaN(coords.lat) || isNaN(coords.lng)) return [];

  const now = new Date();
  const currentYear = now.getFullYear();

  // Approximate solstices
  const winterSolstice = new Date(currentYear, 11, 21); // Dec 21
  const summerSolstice = new Date(currentYear, 5, 21); // June 21

  const dates = [
    { date: now, label: Season.TODAY, color: '#10b981' }, // Green
    { date: summerSolstice, label: Season.SUMMER, color: '#f59e0b' }, // Amber/Sun
    { date: winterSolstice, label: Season.WINTER, color: '#3b82f6' }, // Blue/Cold
  ];

  return dates.map(({ date, label, color }) => {
    const timePoints = getDayHours(date);
    const points = timePoints.map((time) => {
      const pos = SunCalc.getPosition(time, coords.lat, coords.lng);
      return {
        azimuth: pos.azimuth,
        altitude: pos.altitude,
        time: time
      };
    });

    return {
      date,
      label,
      color,
      points
    };
  });
};

const projectPoint = (origin: Coordinates, distanceMeters: number, bearing: number): Coordinates => {
  if (!origin || isNaN(origin.lat) || isNaN(origin.lng) || isNaN(bearing)) {
    return { lat: 0, lng: 0 };
  }

  const R = 6371e3; // Earth radius in meters
  const lat1 = (origin.lat * Math.PI) / 180;
  const lon1 = (origin.lng * Math.PI) / 180;

  // Bearing adjustment: SunCalc 0 is South, Map 0 is North.
  const mapBearing = Math.PI + bearing;

  const lat2 = Math.asin(
    Math.sin(lat1) * Math.cos(distanceMeters / R) +
    Math.cos(lat1) * Math.sin(distanceMeters / R) * Math.cos(mapBearing)
  );

  const lon2 = lon1 + Math.atan2(
    Math.sin(mapBearing) * Math.sin(distanceMeters / R) * Math.cos(lat1),
    Math.cos(distanceMeters / R) - Math.sin(lat1) * Math.sin(lat2)
  );

  const newLat = (lat2 * 180) / Math.PI;
  const newLng = (lon2 * 180) / Math.PI;

  if (isNaN(newLat) || isNaN(newLng)) return { lat: 0, lng: 0 };

  return {
    lat: newLat,
    lng: newLng,
  };
};

// --- SERVICE: GEMINI ---

const initGenAI = () => {
  // Safe access to process.env for static environments
  const env = (window as any).process?.env || {};
  const apiKey = env.API_KEY;
  if (!apiKey || apiKey === '') throw new Error("API Key not configured");
  return new GoogleGenAI({ apiKey });
};

const analyzeSolarLocation = async (
  coords: Coordinates,
  address: string
): Promise<string> => {
  try {
    const ai = initGenAI();
    
    const prompt = `
      Je suis installateur de caméras de sécurité solaires.
      J'ai une installation prévue à cette adresse approximative: "${address}" (Lat: ${coords.lat}, Lng: ${coords.lng}).
      
      Donne-moi 3 conseils brefs et techniques pour positionner le panneau solaire à cet endroit précis, en considérant:
      1. L'orientation optimale (Azimut) pour cette latitude en France/Europe.
      2. L'inclinaison recommandée (Tilt).
      3. Les obstacles potentiels typiques (s'il s'agit d'une zone urbaine ou rurale selon tes connaissances générales de la zone).

      Réponds en français, format Markdown, très concis.
    `;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt,
    });

    return response.text || "Analyse indisponible.";
  } catch (error: any) {
    console.error("Gemini Error:", error);
    if (error.message === "API Key not configured") {
      return "⚠️ Clé API non détectée. L'assistant IA nécessite une clé API.";
    }
    return "Impossible de contacter l'assistant solaire pour le moment.";
  }
};

// --- COMPONENTS ---

// Fix for default Leaflet markers
const iconUrl = 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png';
const iconShadow = 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png';
const DefaultIcon = L.icon({
    iconUrl: iconUrl,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});
L.Marker.prototype.options.icon = DefaultIcon;

const MapController: React.FC<{ coords: Coordinates }> = ({ coords }) => {
  const map = useMap();
  useEffect(() => {
    if (coords && !isNaN(coords.lat) && !isNaN(coords.lng)) {
      map.flyTo([coords.lat, coords.lng], 18, { duration: 1.5 });
    }
  }, [coords, map]);
  return null;
};

interface SolarMapProps {
  location: Coordinates;
  sunPaths: SunPathData[];
}

const SolarMap: React.FC<SolarMapProps> = ({ location, sunPaths }) => {
  const PATH_RADIUS = 80; 

  // Guard against invalid coordinates crashing Leaflet
  if (!location || isNaN(location.lat) || isNaN(location.lng)) {
    return (
      <div className="h-full w-full flex items-center justify-center bg-slate-100 text-slate-400">
        Coordonnées invalides
      </div>
    );
  }

  return (
    <div className="h-full w-full rounded-xl overflow-hidden shadow-inner border border-slate-200 z-0">
      <MapContainer
        center={[location.lat, location.lng]}
        zoom={18}
        scrollWheelZoom={true}
        style={{ height: '100%', width: '100%' }}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        <MapController coords={location} />

        <Marker position={[location.lat, location.lng]}>
          <Popup>Position de la caméra / panneau</Popup>
        </Marker>

        {sunPaths.map((path, idx) => {
          const latLngs = path.points
            .filter(p => p.altitude > 0)
            .map(p => {
               const projected = projectPoint(location, PATH_RADIUS, p.azimuth);
               // Filter out any NaN results from projection
               if (isNaN(projected.lat) || isNaN(projected.lng)) return null;
               return [projected.lat, projected.lng] as [number, number];
            })
            .filter((pt): pt is [number, number] => pt !== null);

          if (latLngs.length === 0) return null;

          return (
            <React.Fragment key={idx}>
              <Polyline 
                positions={latLngs} 
                pathOptions={{ color: path.color, weight: 4, opacity: 0.8, dashArray: path.label === 'Aujourd\'hui' ? undefined : '5, 10' }} 
              />
              
              {path.points.filter((_, i) => i % 2 === 0 && _.altitude > 0).map((p, pIdx) => {
                 const proj = projectPoint(location, PATH_RADIUS, p.azimuth);
                 if (isNaN(proj.lat) || isNaN(proj.lng)) return null;

                 const hours = p.time.getHours();
                 return (
                   <CircleMarker 
                    key={`${idx}-${pIdx}`}
                    center={[proj.lat, proj.lng]} 
                    pathOptions={{ color: path.color, fillColor: 'white', fillOpacity: 1 }} 
                    radius={4}
                   >
                     <Tooltip direction="top" offset={[0, -5]} opacity={0.9} permanent={false}>
                        <span className="font-bold">{hours}h</span>
                        <br/>
                        Alt: {(p.altitude * (180/Math.PI)).toFixed(1)}°
                     </Tooltip>
                   </CircleMarker>
                 );
              })}
            </React.Fragment>
          );
        })}

        {/* North Indicator */}
        <Polyline 
            positions={[
                [location.lat, location.lng],
                [
                  projectPoint(location, PATH_RADIUS + 20, Math.PI).lat || location.lat, 
                  projectPoint(location, PATH_RADIUS + 20, Math.PI).lng || location.lng
                ]
            ]}
            pathOptions={{ color: '#94a3b8', weight: 1, dashArray: '4, 4' }}
        />
      </MapContainer>
    </div>
  );
};

interface InfoPanelProps {
  paths: SunPathData[];
  locationInfo: LocationInfo;
}

const InfoPanel: React.FC<InfoPanelProps> = ({ paths, locationInfo }) => {
  const [advice, setAdvice] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleGetAdvice = async () => {
    setLoading(true);
    const result = await analyzeSolarLocation(
      locationInfo.coords, 
      locationInfo.address || `${locationInfo.coords.lat}, ${locationInfo.coords.lng}`
    );
    setAdvice(result);
    setLoading(false);
  };

  return (
    <div className="bg-white p-4 rounded-xl shadow-lg border border-slate-100 flex flex-col gap-4 h-full overflow-y-auto">
      <div>
        <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
          <Sun className="w-5 h-5 text-orange-500" />
          Données Solaires
        </h2>
        <p className="text-sm text-slate-500 mt-1">
          {locationInfo.address || `Lat: ${locationInfo.coords.lat.toFixed(4)}, Lng: ${locationInfo.coords.lng.toFixed(4)}`}
        </p>
      </div>

      <div className="space-y-3">
        {paths.map((path) => {
           const maxAlt = Math.max(...path.points.map(p => p.altitude));
           const maxAltDeg = (maxAlt * (180/Math.PI)).toFixed(1);
           
           return (
             <div key={path.label} className="flex items-center justify-between p-3 rounded-lg bg-slate-50 border border-slate-100">
               <div className="flex items-center gap-3">
                 <div className="w-3 h-3 rounded-full" style={{ backgroundColor: path.color }}></div>
                 <span className="font-medium text-slate-700">{path.label}</span>
               </div>
               <div className="text-sm text-slate-600">
                 Max Alt: <span className="font-bold">{maxAltDeg}°</span>
               </div>
             </div>
           );
        })}
      </div>

      <div className="mt-2 border-t border-slate-100 pt-4">
        <h3 className="text-sm font-semibold text-slate-900 flex items-center gap-2 mb-2">
          <Info className="w-4 h-4" />
          Assistant Installation
        </h3>
        
        {!advice && !loading && (
          <button 
            onClick={handleGetAdvice}
            className="w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-medium rounded-lg transition-colors flex items-center justify-center gap-2"
          >
            Obtenir l'avis IA (Gemini)
          </button>
        )}

        {loading && (
           <div className="flex items-center justify-center py-4 text-indigo-600">
             <Loader2 className="w-6 h-6 animate-spin" />
           </div>
        )}

        {advice && (
          <div className={`p-4 rounded-lg text-sm prose prose-sm max-w-none ${advice.includes('⚠️') || advice.includes('Impossible') ? 'bg-amber-50 text-amber-900' : 'bg-indigo-50 text-indigo-900'}`}>
             {advice.split('\n').map((line, i) => (
                <p key={i} className={line.startsWith('#') ? 'font-bold mt-2' : 'my-1'}>
                  {line.replace(/^#+\s/, '')}
                </p>
             ))}
          </div>
        )}
      </div>
    </div>
  );
};

// --- APP ---

function App() {
  const [location, setLocation] = useState<LocationInfo>({
    coords: { lat: 48.8566, lng: 2.3522 },
    address: 'Paris, France'
  });
  const [searchQuery, setSearchQuery] = useState('');
  const [loadingGeo, setLoadingGeo] = useState(false);

  const sunPaths = useMemo(() => calculateSunPaths(location.coords), [location.coords]);

  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const coords = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          try {
             const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${coords.lat}&lon=${coords.lng}`);
             const data = await res.json();
             setLocation({ coords, address: data.display_name });
          } catch (e) {
             setLocation({ coords, address: 'Ma Position' });
          }
        },
        (error) => console.warn("Geolocation blocked or failed", error)
      );
    }
  }, []);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setLoadingGeo(true);
    try {
      const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(searchQuery)}`);
      const data = await res.json();

      if (data && data.length > 0) {
        setLocation({
          coords: { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) },
          address: data[0].display_name
        });
      } else {
        alert("Adresse non trouvée.");
      }
    } catch (err) {
      alert("Erreur de connexion au service de carte.");
    } finally {
      setLoadingGeo(false);
    }
  };

  const handleLocateMe = () => {
     setLoadingGeo(true);
     if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const coords = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          try {
             const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${coords.lat}&lon=${coords.lng}`);
             const data = await res.json();
             setLocation({ coords, address: data.display_name });
          } catch (e) {
             setLocation({ coords, address: 'Position actuelle' });
          }
          setLoadingGeo(false);
        },
        () => setLoadingGeo(false)
      );
    } else {
        setLoadingGeo(false);
    }
  };

  return (
    <div className="h-screen w-screen flex flex-col bg-slate-100 overflow-hidden">
      <header className="bg-white border-b border-slate-200 px-4 py-3 flex items-center justify-between shadow-sm z-20">
        <div className="flex items-center gap-2">
            <div className="bg-orange-500 p-2 rounded-lg">
                <Navigation className="w-5 h-5 text-white transform -rotate-45" />
            </div>
            <h1 className="text-lg font-bold text-slate-800 hidden sm:block">SolarCam Planner</h1>
        </div>

        <form onSubmit={handleSearch} className="flex-1 max-w-lg mx-4 flex gap-2">
            <div className="relative flex-1">
                <input 
                    type="text" 
                    placeholder="Entrez une adresse..." 
                    className="w-full pl-10 pr-4 py-2 bg-slate-100 border-none rounded-lg text-slate-800 focus:ring-2 focus:ring-orange-500 focus:bg-white transition-all outline-none"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                />
                <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            </div>
            <button 
                type="submit"
                disabled={loadingGeo}
                className="bg-slate-800 text-white px-4 py-2 rounded-lg font-medium hover:bg-slate-900 transition-colors disabled:opacity-50"
            >
                {loadingGeo ? '...' : 'Aller'}
            </button>
            <button
                type="button"
                onClick={handleLocateMe}
                className="p-2 bg-white border border-slate-200 rounded-lg text-slate-600 hover:bg-slate-50 hover:text-orange-500 transition-colors"
                title="Me localiser"
            >
                <MapPin className="w-5 h-5" />
            </button>
        </form>
      </header>

      <main className="flex-1 flex flex-col md:flex-row overflow-hidden relative">
        <div className="flex-1 relative h-[60vh] md:h-full">
            <SolarMap location={location.coords} sunPaths={sunPaths} />
            
            <div className="absolute bottom-6 left-4 bg-white/90 backdrop-blur-sm p-3 rounded-lg shadow-lg text-xs space-y-2 z-[400] border border-slate-200">
                <div className="font-semibold text-slate-700 mb-1">Légende</div>
                <div className="flex items-center gap-2">
                    <span className="w-3 h-1 bg-orange-500 rounded-full"></span>
                    <span>Solstice d'Été</span>
                </div>
                <div className="flex items-center gap-2">
                    <span className="w-3 h-1 bg-green-500 rounded-full"></span>
                    <span>Aujourd'hui</span>
                </div>
                <div className="flex items-center gap-2">
                    <span className="w-3 h-1 bg-blue-500 rounded-full"></span>
                    <span>Solstice d'Hiver</span>
                </div>
            </div>
        </div>

        <div className="h-[40vh] md:h-full md:w-96 bg-white border-l border-slate-200 z-10 overflow-hidden flex flex-col">
            <InfoPanel paths={sunPaths} locationInfo={location} />
        </div>
      </main>
    </div>
  );
}

// --- RENDER ---

const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error("Could not find root element to mount to");
}

const root = ReactDOM.createRoot(rootElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
