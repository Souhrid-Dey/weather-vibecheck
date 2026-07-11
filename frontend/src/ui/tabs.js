export function initTabs() {
  const tabs = document.querySelectorAll('.tab-btn');
  const sections = document.querySelectorAll('section.card');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Deactivate all
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      sections.forEach(s => {
        s.classList.add('hidden');
        s.classList.remove('active-section');
      });
      
      // Activate target
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');
      const targetId = tab.getAttribute('data-target');
      const targetSec = document.getElementById(targetId);
      
      if (targetSec) {
        targetSec.classList.remove('hidden');
        targetSec.classList.add('active-section');
      }
    });
  });
}
