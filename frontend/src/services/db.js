/**
 * IndexedDB Wrapper for Offline Storage
 * Critical for disaster apps where network connectivity is unreliable.
 */

const DB_NAME = 'WeatherVibeCheckDB';
const DB_VERSION = 1;
const STORE_NAME = 'offline_cache';

function openDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);

    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result);

    request.onupgradeneeded = (e) => {
      const db = e.target.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: 'id' });
      }
    };
  });
}

export const dbService = {
  /**
   * Save a generated AI response to cache.
   * @param {string} id - The cache key (e.g., "plan", "pantry").
   * @param {Object} data - The JSON response from the API.
   */
  async saveCache(id, data) {
    try {
      const db = await openDB();
      return new Promise((resolve, reject) => {
        const tx = db.transaction(STORE_NAME, 'readwrite');
        const store = tx.objectStore(STORE_NAME);
        const item = { id, data, timestamp: Date.now() };
        
        const request = store.put(item);
        request.onsuccess = () => resolve(true);
        request.onerror = () => reject(request.error);
      });
    } catch (e) {
      console.warn('IndexedDB save failed:', e);
      return false;
    }
  },

  /**
   * Retrieve cached data.
   * @param {string} id - The cache key.
   * @returns {Promise<Object|null>}
   */
  async getCache(id) {
    try {
      const db = await openDB();
      return new Promise((resolve, reject) => {
        const tx = db.transaction(STORE_NAME, 'readonly');
        const store = tx.objectStore(STORE_NAME);
        
        const request = store.get(id);
        request.onsuccess = () => resolve(request.result ? request.result.data : null);
        request.onerror = () => reject(request.error);
      });
    } catch (e) {
      console.warn('IndexedDB get failed:', e);
      return null;
    }
  }
};
