export function escapeHTML(str) {
  if (!str) return '';
  return str.toString()
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

export function setLoading(isLoading, text = "Processing...") {
  const activeSection = document.querySelector('section.active-section');
  const loadingOverlay = document.getElementById('loading-overlay');
  const loadingText = document.getElementById('loading-text');

  if (isLoading) {
    if (activeSection) activeSection.classList.add('hidden');
    if (loadingText) loadingText.textContent = text;
    if (loadingOverlay) loadingOverlay.classList.remove('hidden');
  } else {
    if (loadingOverlay) loadingOverlay.classList.add('hidden');
    if (activeSection) activeSection.classList.remove('hidden');
  }
}

export function displayError(container, message) {
  container.innerHTML = `<p style="color: var(--accent-emergency)">❌ Error: ${escapeHTML(message)}</p>`;
  container.classList.remove('hidden');
}

export function renderOfflineBadge(isOffline) {
  return isOffline ? `<span class="offline-badge">⚡ Offline Mode (Cached)</span>` : '';
}
