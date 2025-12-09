export interface Coordinates {
  lat: number;
  lng: number;
}

export interface SunPosition {
  azimuth: number; // in radians
  altitude: number; // in radians
  time: Date;
}

export interface SunPathData {
  date: Date;
  label: string;
  color: string;
  points: SunPosition[];
}

export enum Season {
  SUMMER = 'Ete',
  WINTER = 'Hiver',
  TODAY = 'Aujourd\'hui'
}

export interface LocationInfo {
  coords: Coordinates;
  address?: string;
}
