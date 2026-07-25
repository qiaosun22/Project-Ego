const datasets = [
  { name: "Ego4D", year: 2022, type: "human", label: "Human ego", scale: "3,670 h", modalities: ["RGB", "audio", "gaze", "IMU"], access: "Gated", evidence: "Sampled", fit: 74 },
  { name: "Ego-Exo4D", year: 2024, type: "paired", label: "Ego–exo", scale: "1,286 h", modalities: ["RGB", "pose", "audio", "3D"], access: "Gated", evidence: "Sampled", fit: 86 },
  { name: "EPIC-KITCHENS-100", year: 2022, type: "human", label: "Human ego", scale: "100 h", modalities: ["RGB", "audio", "actions"], access: "Open", evidence: "Verified", fit: 81 },
  { name: "EgoDex", year: 2025, type: "human", label: "Human ego", scale: "829 h", modalities: ["RGB", "hands", "language"], access: "Open", evidence: "Metadata", fit: 88 },
  { name: "Open X-Embodiment", year: 2024, type: "robot", label: "Robot ego", scale: "1M+ traj.", modalities: ["RGB", "state", "action", "language"], access: "Open", evidence: "Sampled", fit: 93 },
  { name: "DROID", year: 2024, type: "robot", label: "Robot ego", scale: "76K traj.", modalities: ["RGB", "state", "action", "language"], access: "Open", evidence: "Verified", fit: 91 },
  { name: "HOT3D", year: 2024, type: "human", label: "Human ego", scale: "833 min", modalities: ["RGB", "gaze", "hands", "3D"], access: "Open", evidence: "Metadata", fit: 79 }
];

const dimensions = {
  integrity: { title: "Data integrity", description: "Tests whether the released files are complete, internally consistent and technically usable before any model sees them.", metrics: ["Corrupt & missing files", "Temporal continuity", "Sensor synchronization", "Duplicate detection"], note: "Automated · file and sequence level" },
  perception: { title: "Perceptual quality", description: "Measures how often the visual stream contains usable evidence for hands, objects, actions and spatial reasoning.", metrics: ["Motion blur", "Exposure & sharpness", "Hand–object visibility", "Action density"], note: "Automated + stratified human audit" },
  semantics: { title: "Semantic quality", description: "Audits whether annotations are accurate, consistent, temporally grounded and sufficiently rich for the intended task.", metrics: ["Label coverage", "Annotator agreement", "Language grounding", "Taxonomy consistency"], note: "Schema, model-assisted and human verified" },
  diversity: { title: "Diversity & scale", description: "Separates raw volume from meaningful coverage across tasks, objects, people, places, devices and behaviors.", metrics: ["Task entropy", "Scene coverage", "Participant balance", "Device diversity"], note: "Distribution-aware · saturation adjusted" },
  access: { title: "Access & governance", description: "Tracks whether data can actually be obtained and responsibly used, including changes after initial publication.", metrics: ["License clarity", "Commercial use", "Download health", "Privacy documentation"], note: "Continuously monitored · versioned evidence" },
  utility: { title: "Robot utility", description: "Measures real downstream value under fixed compute and data budgets instead of inferring usefulness from metadata alone.", metrics: ["VLA transfer", "Policy learning", "Cross-dataset generalization", "Utility per GPU-hour"], note: "Controlled training runs · task-specific scores" }
};

let activeFilter = "all";

function renderDatasets() {
  const query = document.querySelector("#dataset-search").value.trim().toLowerCase();
  const filtered = datasets.filter((dataset) => {
    const matchesType = activeFilter === "all" || dataset.type === activeFilter;
    const haystack = [dataset.name, dataset.label, ...dataset.modalities].join(" ").toLowerCase();
    return matchesType && haystack.includes(query);
  });

  document.querySelector("#dataset-rows").innerHTML = filtered.map((dataset) => {
    const evidenceClass = dataset.evidence === "Verified" ? "verified-dot" : "claimed-dot";
    const accessClass = dataset.access === "Open" ? "access-open" : "access-gated";
    return `<tr>
      <td><span class="dataset-name">${dataset.name}</span><span class="dataset-year">${dataset.year}</span></td>
      <td><span class="type-tag">${dataset.label}</span></td>
      <td>${dataset.scale}</td>
      <td><div class="modality-list">${dataset.modalities.map(item => `<span>${item}</span>`).join("")}</div></td>
      <td class="${accessClass}">${dataset.access}</td>
      <td><span class="evidence"><i class="${evidenceClass}"></i>${dataset.evidence}</span></td>
      <td class="score-cell"><div class="score-top"><span>Preview</span><strong>${dataset.fit}</strong></div><div class="score-track"><i style="width:${dataset.fit}%"></i></div></td>
    </tr>`;
  }).join("");
  document.querySelector("#empty-state").hidden = filtered.length > 0;
}

function renderDimension(key) {
  const dimension = dimensions[key];
  document.querySelector("#dimension-detail").innerHTML = `
    <div><h3>${dimension.title}</h3><p>${dimension.description}</p><div class="metric-chips">${dimension.metrics.map(metric => `<span>${metric}</span>`).join("")}</div></div>
    <div class="detail-note">${dimension.note}</div>`;
}

document.querySelector("#dataset-search").addEventListener("input", renderDatasets);
document.querySelectorAll(".filter").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".filter").forEach(item => item.classList.remove("active"));
  button.classList.add("active");
  activeFilter = button.dataset.filter;
  renderDatasets();
}));

document.querySelectorAll(".dimension").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".dimension").forEach(item => {
    item.classList.remove("active");
    item.setAttribute("aria-selected", "false");
  });
  button.classList.add("active");
  button.setAttribute("aria-selected", "true");
  renderDimension(button.dataset.dimension);
}));

renderDatasets();
renderDimension("integrity");
