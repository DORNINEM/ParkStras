import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap, Polyline, CircleMarker, Tooltip } from 'react-leaflet';
import L from 'leaflet';
import { Coordinates, SunPathData } from '../types';
import { projectPoint } from '../utils/sunCalculations';

// Fix for default Leaflet markers in React
// Using CDN URLs instead of imports to avoid bundler/loader issues in browser-only environments
const iconUrl = 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png';
const iconShadow = 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png';

const DefaultIcon = L.icon({
    iconUrl: iconUrl,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});

L.Marker.prototype.options.icon = DefaultIcon;

interface SolarMapProps {
  location: Coordinates;
  sunPaths: SunPathData[];
}

const MapController: React.FC<{ coords: Coordinates }> = ({ coords }) => {
  const map = useMap();
  useEffect(() => {
    map.flyTo([coords.lat, coords.lng], 18, {
      duration: 1.5
    });
  }, [coords, map]);
  return null;
};

const SolarMap: React.FC<SolarMapProps> = ({ location, sunPaths }) => {
  // Visual radius of the sun path on the map (in meters)
  const PATH_RADIUS = 80; 

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

        {/* Central Position (Camera/Panel) */}
        <Marker position={[location.lat, location.lng]}>
          <Popup>
            Position de la caméra / panneau
          </Popup>
        </Marker>

        {/* Sun Paths */}
        {sunPaths.map((path, idx) => {
          // Calculate projected coordinates for the path
          const latLngs = path.points
            .filter(p => p.altitude > 0) // Only show when sun is above horizon
            .map(p => {
               const projected = projectPoint(location, PATH_RADIUS, p.azimuth);
               return [projected.lat, projected.lng] as [number, number];
            });

          if (latLngs.length === 0) return null;

          return (
            <React.Fragment key={idx}>
              {/* The Curve */}
              <Polyline 
                positions={latLngs} 
                pathOptions={{ color: path.color, weight: 4, opacity: 0.8, dashArray: path.label === 'Aujourd\'hui' ? undefined : '5, 10' }} 
              />
              
              {/* Hour Markers */}
              {path.points.filter((_, i) => i % 2 === 0 && _.altitude > 0).map((p, pIdx) => {
                 const proj = projectPoint(location, PATH_RADIUS, p.azimuth);
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

        {/* Compass Rose Helper (North Line) */}
        <Polyline 
            positions={[
                [location.lat, location.lng],
                [projectPoint(location, PATH_RADIUS + 20, Math.PI).lat, projectPoint(location, PATH_RADIUS + 20, Math.PI).lng] // North is Azimuth PI in suncalc logic inversion
            ]}
            pathOptions={{ color: '#94a3b8', weight: 1, dashArray: '4, 4' }}
        />

      </MapContainer>
    </div>
  );
};

export default SolarMap;