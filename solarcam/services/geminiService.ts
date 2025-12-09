import { GoogleGenAI } from "@google/genai";
import { Coordinates } from "../types.ts";

const initGenAI = () => {
  const apiKey = process.env.API_KEY;
  if (!apiKey || apiKey === '') throw new Error("API Key not configured");
  return new GoogleGenAI({ apiKey });
};

export const analyzeSolarLocation = async (
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
      return "⚠️ Clé API non détectée. Pour activer l'assistant IA, une clé API valide est requise dans l'environnement.";
    }
    return "Impossible de contacter l'assistant solaire pour le moment.";
  }
};