import React, { useState } from 'react';
import { SunPathData, LocationInfo } from '../types';
import { Sun, Calendar, Info, Loader2, MapPin } from 'lucide-react';
import { analyzeSolarLocation } from '../services/geminiService';

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
           // Find max altitude (noon usually)
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
          <div className="bg-indigo-50 p-4 rounded-lg text-sm text-indigo-900 prose prose-sm max-w-none">
             {/* Simple markdown rendering */}
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

export default InfoPanel;
