import { apiClient } from '../services/api-client.js';
import { escapeHTML, setLoading, displayError, renderOfflineBadge } from '../utils/dom.js';

export function initForms() {
  initVibeCheckForm();
  initPantryForm();
  initCommuteForm();
  initSOSForm();
}

function initVibeCheckForm() {
  const form = document.getElementById('vibecheck-form');
  const results = document.getElementById('vibecheck-results');
  if (!form || !results) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true, "Assessing situation and anxiety levels...");
    results.innerHTML = '';
    results.classList.add('hidden');
    results.classList.remove('animate-fade-in');

    const formData = new FormData(form);
    const data = {
      location: formData.get('location'),
      family_size: parseInt(formData.get('family_size')),
      anxiety_level: formData.get('anxiety_level')
    };

    try {
      const { data: plan, offline } = await apiClient.getPlan(data);
      
      let html = `<h3>Plan Generated ${renderOfflineBadge(offline)}</h3>`;
      html += `<p style="font-size:1.1rem; margin-bottom:1rem; padding: 10px; border-left: 4px solid var(--accent-safe); background: var(--surface-hover)">"${escapeHTML(plan.greeting_and_tone)}"</p>`;
      
      html += `<h4>⚠️ Immediate Actions</h4><ul>`;
      plan.immediate_actions.forEach(a => html += `<li><strong>${escapeHTML(a.task)}</strong>: ${escapeHTML(a.why)}</li>`);
      html += `</ul>`;

      html += `<h4>☔ Pre-Storm Checklist</h4><ul>`;
      plan.pre_storm_checklist.forEach(t => html += `<li>${escapeHTML(t)}</li>`);
      html += `</ul>`;

      html += `<h4>🛑 During Storm Rules</h4><ul>`;
      plan.during_storm_rules.forEach(t => html += `<li>${escapeHTML(t)}</li>`);
      html += `</ul>`;

      html += `<p><strong>Contacts Suggestion:</strong> ${escapeHTML(plan.emergency_contacts_suggestion)}</p>`;
      
      results.innerHTML = html;
      results.classList.remove('hidden');
      results.classList.add('animate-fade-in');
    } catch (err) {
      displayError(results, err.message);
    } finally {
      setLoading(false);
    }
  });
}

function initPantryForm() {
  const form = document.getElementById('pantry-form');
  const results = document.getElementById('pantry-results');
  if (!form || !results) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true, "Rationing ingredients...");
    results.innerHTML = '';
    results.classList.add('hidden');
    results.classList.remove('animate-fade-in');

    const data = { ingredients: new FormData(form).get('ingredients') };

    try {
      const { data: plan, offline } = await apiClient.getPantry(data);
      
      let html = `<h3>Survival Meal Plan ${renderOfflineBadge(offline)}</h3>`;
      
      ['day_1', 'day_2', 'day_3'].forEach(day => {
        if(plan[day]) {
          html += `<div style="margin-bottom:1rem; padding:10px; border:1px solid var(--border-color); border-radius:4px;">
            <h4 style="color:var(--accent-warning); text-transform:capitalize">${escapeHTML(day.replace('_', ' '))}</h4>
            <p><strong>Breakfast:</strong> ${escapeHTML(plan[day].breakfast)}</p>
            <p><strong>Lunch:</strong> ${escapeHTML(plan[day].lunch)}</p>
            <p><strong>Dinner:</strong> ${escapeHTML(plan[day].dinner)}</p>
          </div>`;
        }
      });

      if(plan.shopping_list && plan.shopping_list.length > 0) {
        html += `<div style="margin: 1rem 0; padding: 10px; background-color: rgba(var(--accent-success-rgb), 0.1); border-left: 4px solid var(--accent-success);">
          <h4 style="color:var(--accent-success); margin-bottom: 0.5rem;">🛒 Shopping List (Buy Immediately)</h4>
          <ul style="margin:0; padding-left: 20px;">`;
        plan.shopping_list.forEach(item => html += `<li>${escapeHTML(item)}</li>`);
        html += `</ul></div>`;
      }

      if(plan.dietary_information) {
        html += `<div style="margin: 1rem 0; padding: 10px; background-color: rgba(var(--accent-info-rgb), 0.1); border-left: 4px solid var(--accent-info);">
          <h4 style="color:var(--accent-info); margin-bottom: 0.5rem;">🥗 Dietary Information</h4>
          <p style="font-size: 0.9em; margin:0;">${escapeHTML(plan.dietary_information)}</p>
        </div>`;
      }

      html += `<h4>💡 Rationing Tips</h4><ul>`;
      plan.rationing_tips.forEach(t => html += `<li>${escapeHTML(t)}</li>`);
      html += `</ul>`;

      results.innerHTML = html;
      results.classList.remove('hidden');
      results.classList.add('animate-fade-in');
    } catch (err) {
      displayError(results, err.message);
    } finally {
      setLoading(false);
    }
  });
}

function initCommuteForm() {
  const form = document.getElementById('commute-form');
  const results = document.getElementById('commute-results');
  if (!form || !results) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true, "Analyzing route hazards...");
    results.innerHTML = '';
    results.classList.add('hidden');
    results.classList.remove('animate-fade-in');

    const formData = new FormData(form);
    const data = {
      start_location: formData.get('start_location'),
      end_location: formData.get('end_location')
    };

    try {
      const { data: route, offline } = await apiClient.getCommute(data);
      
      let riskColor = "var(--accent-warning)";
      if (route.risk_level.toLowerCase().includes('severe')) riskColor = "var(--accent-emergency)";
      else if (route.risk_level.toLowerCase().includes('low')) riskColor = "var(--accent-safe)";

      let html = `<h3>Route Advisory ${renderOfflineBadge(offline)}</h3>`;
      html += `<p style="font-size:1.2rem; color:${riskColor}; font-weight:bold; margin-bottom:1rem">Risk Level: ${escapeHTML(route.risk_level)}</p>`;
      
      html += `<h4>🌊 Primary Hazards</h4><ul>`;
      route.primary_hazards.forEach(h => html += `<li>${escapeHTML(h)}</li>`);
      html += `</ul>`;

      html += `<p><strong>Alternatives:</strong> ${escapeHTML(route.alternative_suggestions)}</p>`;
      html += `<div style="margin-top:1rem; padding:1rem; background:var(--surface-hover); border-left:4px solid ${riskColor}">
        <strong>Final Decision:</strong> ${escapeHTML(route.go_no_go_decision)}
      </div>`;

      results.innerHTML = html;
      results.classList.remove('hidden');
      results.classList.add('animate-fade-in');
    } catch (err) {
      displayError(results, err.message);
    } finally {
      setLoading(false);
    }
  });
}

function initSOSForm() {
  const form = document.getElementById('sos-form');
  const results = document.getElementById('sos-results');
  if (!form || !results) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true, "Translating alerts...");
    results.innerHTML = '';
    results.classList.add('hidden');
    results.classList.remove('animate-fade-in');

    const formData = new FormData(form);
    const data = {
      situation: formData.get('situation'),
      location: formData.get('location')
    };

    try {
      const { data: sos, offline } = await apiClient.getSOS(data);
      
      let html = `<h3>SOS Texts Generated ${renderOfflineBadge(offline)}</h3>`;
      html += `<p style="color:var(--text-secondary); margin-bottom:1rem">Copy/paste these to send via SMS. They are optimized for character limits.</p>`;
      
      const langs = [
        { name: 'English', text: sos.english },
        { name: 'Hindi', text: sos.hindi },
        { name: 'Marathi', text: sos.marathi }
      ];

      langs.forEach(l => {
        html += `<div style="margin-bottom:1rem">
          <h4>${escapeHTML(l.name)}</h4>
          <textarea readonly rows="3" style="font-size:1rem; cursor:pointer" onclick="this.select()">${escapeHTML(l.text)}</textarea>
        </div>`;
      });

      html += `<p><strong>🔋 Tip:</strong> ${escapeHTML(sos.advice)}</p>`;

      results.innerHTML = html;
      results.classList.remove('hidden');
      results.classList.add('animate-fade-in');
    } catch (err) {
      displayError(results, err.message);
    } finally {
      setLoading(false);
    }
  });
}
