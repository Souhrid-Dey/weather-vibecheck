import { dbService } from './db.js';

const API_BASE = '/api';

/**
 * Helper to fetch with offline caching fallback.
 */
async function fetchWithOfflineFallback(endpoint, bodyData, cacheKey) {
  try {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(bodyData)
    });

    if (!response.ok) {
      const err = await response.json().catch(() => ({ detail: 'API Error' }));
      throw new Error(err.detail || 'Network response was not ok');
    }

    const data = await response.json();
    
    // Save to offline cache
    await dbService.saveCache(cacheKey, data);
    return { data, offline: false };

  } catch (error) {
    console.warn(`Fetch to ${endpoint} failed. Attempting offline fallback...`, error);
    
    const cachedData = await dbService.getCache(cacheKey);
    if (cachedData) {
      return { data: cachedData, offline: true };
    }
    
    throw new Error('You are offline and no cached data is available for this request.');
  }
}

export const apiClient = {
  getPlan: (data) => fetchWithOfflineFallback('/plan', data, 'vibecheck_plan'),
  getPantry: (data) => fetchWithOfflineFallback('/pantry', data, 'pantry_plan'),
  getCommute: (data) => fetchWithOfflineFallback('/commute', data, 'commute_plan'),
  getSOS: (data) => fetchWithOfflineFallback('/sos', data, 'sos_plan')
};
