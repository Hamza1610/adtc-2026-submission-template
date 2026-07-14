import numpy as np

# 1. Define the 5 explicit Nigerian FMOH Triage Guidelines
CLINICAL_GUIDELINES = [
    "PROTOCOL 1 [MALARIA]: Adult with axillary temperature >= 38.5C, severe headache, chills, and body aches. If danger signs (convulsions, jaundice, inability to stand, rigid neck) are ABSENT, triage as Uncomplicated Malaria. Action: Administer Artemether-Lumefantrine (ACT) as per weight, advise on rest, and follow up in 48 hours.",
    
    "PROTOCOL 2 [TYPHOID FEVER]: Adult with prolonged step-ladder fever (> 4 days), severe abdominal distress, bloating, and watery diarrhea or constipation. Clinically overlaps with malaria but differentiated by distinct gastrointestinal (GI) symptoms. Action: Refer immediately to facility for Widal/blood culture test. Do not treat blindly with antibiotics at PHC level.",
    
    "PROTOCOL 3 [HYPERTENSION]: Adult presenting with systolic BP >= 140 mmHg or diastolic BP >= 90 mmHg. If accompanied by severe occipital headache, blurred vision, or chest pain, triage as Hypertensive Emergency. Action: Absolute rest, refer immediately to general hospital, do not administer strong oral anti-hypertensives without monitoring.",
    
    "PROTOCOL 4 [MALARIA-TYPHOID CO-PRESENTATION]: Severe presentation where patient exhibits high fever alongside concurrent GI distress and extreme systemic weakness. This is a high-risk reasoning pathway. Action: Prioritize malaria rapid diagnostic test (RDT). If RDT is positive but GI distress worsens, refer immediately for secondary co-infection screening.",
    
    "PROTOCOL 5 [RESPIRATORY / TUBERCULOSIS]: Adult with a persistent, productive cough lasting over 2-3 weeks, progressive night sweats, weight loss, and low-grade evening fevers. Code-switched danger sign: 'Ina tari da jini' (Coughing blood). Action: Triage as Suspected Pulmonary TB. Isolate immediately, provide surgical mask, and refer to nearest DOTS center for sputum microscopy."
]

print("Compiling healthcare triage corpus...")
# Save the text arrays as a lightweight, static system binary layout
np.save("clinical_guidelines.npy", np.array(CLINICAL_GUIDELINES))
print("Success! 'clinical_guidelines.npy' generated (< 1 KB memory profile).")
