import { initTabs } from './ui/tabs.js';
import { initForms } from './ui/forms.js';

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Tab UI (with A11y support)
  initTabs();
  
  // Initialize Form Event Listeners
  initForms();
});
