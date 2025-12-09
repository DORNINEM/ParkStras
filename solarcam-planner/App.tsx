import React, { useState, useEffect, useMemo } from 'react';
import { Search, MapPin, Navigation } from 'lucide-react';
import SolarMap from './components/SolarMap';
import InfoPanel from './components/InfoPanel';
import { calculateSunPaths } from './utils/sunCalculations';
import { Coordinates, LocationInfo } from './types';

function App() {
  // Default to Paris
  const [location, setLocation] = useState<LocationInfo>({
    coords: { lat: 48.8566, lng: 2.3522 },
    address: 'Paris, France'
  });
  const [searchQuery, setSearchQuery] = useState('');
  const [loadingGeo, setLoadingGeo] = useState(false);

  // Calculate sun paths whenever location changes
  const sunPaths = useMemo(() => calculateSunPaths(location.coords), [location.coords]);

  // Geolocation on mount
  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const coords = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          // Reverse geocoding using Nominatim (free)
          try {
             const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${coords.lat}&lon=${coords.lng}`);
             const data = await res.json();
             setLocation({ coords, address: data.display_name });
          } catch (e) {
             setLocation({ coords, address: 'Ma Position' });
          }
        },
        (error) => console.warn("Geolocation blocked", error)
      );
    }
  }, []);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setLoadingGeo(true);
    try {
      // Direct Geocoding using Nominatim (free, open)
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
      {/* Header */}
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

      {/* Main Content */}
      <main className="flex-1 flex flex-col md:flex-row overflow-hidden relative">
        
        {/* Map Area */}
        <div className="flex-1 relative h-[60vh] md:h-full">
            <SolarMap location={location.coords} sunPaths={sunPaths} />
            
            {/* Map Legend overlay */}
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

        {/* Sidebar Info */}
        <div className="h-[40vh] md:h-full md:w-96 bg-white border-l border-slate-200 z-10 overflow-hidden flex flex-col">
            <InfoPanel paths={sunPaths} locationInfo={location} />
        </div>

      </main>
    </div>
  );
}

export default App;
