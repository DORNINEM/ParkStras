import SunCalc from 'suncalc';
import { Coordinates, SunPathData, Season } from '../types.ts';

// Helper to get array of hours from 6h to 20h
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

export const calculateSunPaths = (coords: Coordinates): SunPathData[] => {
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

/**
 * Projects a point from an origin based on distance (meters) and bearing (radians).
 * Used to draw the sun lines on the map relative to the center.
 */
export const projectPoint = (origin: Coordinates, distanceMeters: number, bearing: number): Coordinates => {
  const R = 6371e3; // Earth radius in meters
  const lat1 = (origin.lat * Math.PI) / 180;
  const lon1 = (origin.lng * Math.PI) / 180;

  // Bearing in suncalc is South = 0, West = PI/2, but for geography typically North = 0.
  // Suncalc: azimuth is radians south to west.
  // Formula expects bearing clockwise from north.
  // Let's adjust: SunCalc azimuth 0 is South.
  // We need to convert SunCalc azimuth to standard map bearing (0 = North, PI/2 = East).
  // Azimuth in SunCalc: 0 is South, increasing westward.
  // Real Map Bearing (0 North): = (PI) + Azimuth.
  const mapBearing = Math.PI + bearing;

  const lat2 = Math.asin(
    Math.sin(lat1) * Math.cos(distanceMeters / R) +
    Math.cos(lat1) * Math.sin(distanceMeters / R) * Math.cos(mapBearing)
  );

  const lon2 = lon1 + Math.atan2(
    Math.sin(mapBearing) * Math.sin(distanceMeters / R) * Math.cos(lat1),
    Math.cos(distanceMeters / R) - Math.sin(lat1) * Math.sin(lat2)
  );

  return {
    lat: (lat2 * 180) / Math.PI,
    lng: (lon2 * 180) / Math.PI,
  };
};