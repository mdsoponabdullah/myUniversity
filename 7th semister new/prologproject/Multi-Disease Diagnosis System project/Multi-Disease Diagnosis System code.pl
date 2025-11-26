% Multi-Disease Diagnosis System with Probabilities
% Interactive Yes/No Question Format
% Author: Medical Expert System
% Date: 2025

% ============================================
% DISEASE DEFINITIONS WITH SYMPTOMS
% ============================================

% disease(DiseaseName, [Symptoms], BaseRate)
disease(influenza, [fever, cough, fatigue, body_aches, headache], 0.15).
disease(covid19, [fever, cough, fatigue, shortness_of_breath, loss_of_taste_smell], 0.10).
disease(common_cold, [runny_nose, sneezing, sore_throat, mild_cough], 0.25).
disease(pneumonia, [fever, cough, chest_pain, shortness_of_breath, fatigue], 0.08).
disease(bronchitis, [persistent_cough, mucus_production, chest_discomfort, fatigue], 0.12).
disease(allergies, [sneezing, runny_nose, itchy_eyes, nasal_congestion], 0.20).
disease(strep_throat, [severe_sore_throat, fever, swollen_lymph_nodes, difficulty_swallowing], 0.07).
disease(asthma, [wheezing, shortness_of_breath, chest_tightness, coughing], 0.10).
disease(migraine, [severe_headache, nausea, sensitivity_to_light, visual_disturbances], 0.09).
disease(gastroenteritis, [nausea, vomiting, diarrhea, abdominal_pain, fever], 0.11).

% ============================================
% SYMPTOM LIKELIHOOD FOR EACH DISEASE
% ============================================

% symptom_probability(Disease, Symptom, Probability)
% Influenza
symptom_probability(influenza, fever, 0.95).
symptom_probability(influenza, cough, 0.80).
symptom_probability(influenza, fatigue, 0.90).
symptom_probability(influenza, body_aches, 0.85).
symptom_probability(influenza, headache, 0.75).

% COVID-19
symptom_probability(covid19, fever, 0.88).
symptom_probability(covid19, cough, 0.82).
symptom_probability(covid19, fatigue, 0.85).
symptom_probability(covid19, shortness_of_breath, 0.70).
symptom_probability(covid19, loss_of_taste_smell, 0.65).

% Common Cold
symptom_probability(common_cold, runny_nose, 0.90).
symptom_probability(common_cold, sneezing, 0.85).
symptom_probability(common_cold, sore_throat, 0.75).
symptom_probability(common_cold, mild_cough, 0.70).

% Pneumonia
symptom_probability(pneumonia, fever, 0.90).
symptom_probability(pneumonia, cough, 0.85).
symptom_probability(pneumonia, chest_pain, 0.80).
symptom_probability(pneumonia, shortness_of_breath, 0.75).
symptom_probability(pneumonia, fatigue, 0.80).

% Bronchitis
symptom_probability(bronchitis, persistent_cough, 0.95).
symptom_probability(bronchitis, mucus_production, 0.85).
symptom_probability(bronchitis, chest_discomfort, 0.70).
symptom_probability(bronchitis, fatigue, 0.75).

% Allergies
symptom_probability(allergies, sneezing, 0.90).
symptom_probability(allergies, runny_nose, 0.88).
symptom_probability(allergies, itchy_eyes, 0.85).
symptom_probability(allergies, nasal_congestion, 0.80).

% Strep Throat
symptom_probability(strep_throat, severe_sore_throat, 0.95).
symptom_probability(strep_throat, fever, 0.80).
symptom_probability(strep_throat, swollen_lymph_nodes, 0.75).
symptom_probability(strep_throat, difficulty_swallowing, 0.85).

% Asthma
symptom_probability(asthma, wheezing, 0.90).
symptom_probability(asthma, shortness_of_breath, 0.85).
symptom_probability(asthma, chest_tightness, 0.80).
symptom_probability(asthma, coughing, 0.75).

% Migraine
symptom_probability(migraine, severe_headache, 0.98).
symptom_probability(migraine, nausea, 0.80).
symptom_probability(migraine, sensitivity_to_light, 0.85).
symptom_probability(migraine, visual_disturbances, 0.70).

% Gastroenteritis
symptom_probability(gastroenteritis, nausea, 0.90).
symptom_probability(gastroenteritis, vomiting, 0.85).
symptom_probability(gastroenteritis, diarrhea, 0.95).
symptom_probability(gastroenteritis, abdominal_pain, 0.88).
symptom_probability(gastroenteritis, fever, 0.70).

% ============================================
% SYMPTOM QUESTIONS WITH USER-FRIENDLY TEXT
% ============================================

% symptom_question(Symptom, QuestionText)
symptom_question(fever, 'Do you have a fever or elevated body temperature?').
symptom_question(cough, 'Do you have a cough?').
symptom_question(fatigue, 'Are you experiencing unusual tiredness or fatigue?').
symptom_question(body_aches, 'Do you have body aches or muscle pain?').
symptom_question(headache, 'Do you have a headache?').
symptom_question(shortness_of_breath, 'Do you have difficulty breathing or shortness of breath?').
symptom_question(loss_of_taste_smell, 'Have you lost your sense of taste or smell?').
symptom_question(runny_nose, 'Do you have a runny nose?').
symptom_question(sneezing, 'Are you sneezing frequently?').
symptom_question(sore_throat, 'Do you have a sore throat?').
symptom_question(mild_cough, 'Do you have a mild, dry cough?').
symptom_question(chest_pain, 'Do you have chest pain?').
symptom_question(persistent_cough, 'Do you have a persistent, ongoing cough?').
symptom_question(mucus_production, 'Are you coughing up mucus or phlegm?').
symptom_question(chest_discomfort, 'Do you feel discomfort in your chest?').
symptom_question(itchy_eyes, 'Do you have itchy or watery eyes?').
symptom_question(nasal_congestion, 'Do you have nasal congestion or a stuffy nose?').
symptom_question(severe_sore_throat, 'Do you have a severe sore throat?').
symptom_question(swollen_lymph_nodes, 'Do you have swollen lymph nodes in your neck?').
symptom_question(difficulty_swallowing, 'Do you have difficulty swallowing?').
symptom_question(wheezing, 'Do you hear wheezing sounds when breathing?').
symptom_question(chest_tightness, 'Do you feel tightness in your chest?').
symptom_question(coughing, 'Do you have a cough (especially at night or with activity)?').
symptom_question(severe_headache, 'Do you have a severe or throbbing headache?').
symptom_question(nausea, 'Are you feeling nauseous?').
symptom_question(sensitivity_to_light, 'Are you sensitive to light?').
symptom_question(visual_disturbances, 'Are you experiencing visual disturbances (blurred vision, flashing lights)?').
symptom_question(vomiting, 'Have you been vomiting?').
symptom_question(diarrhea, 'Do you have diarrhea?').
symptom_question(abdominal_pain, 'Do you have abdominal pain or cramping?').

% ============================================
% INTERACTIVE YES/NO QUESTION SYSTEM
% ============================================

% Get all unique symptoms from disease database
get_all_symptoms(AllSymptoms) :-
    setof(Symptom, 
          Disease^Symptoms^Prior^(
              disease(Disease, Symptoms, Prior), 
              member(Symptom, Symptoms)
          ), 
          AllSymptoms).

% Ask yes/no question and get response
ask_symptom(Symptom) :-
    symptom_question(Symptom, Question),
    format('~n~w~n', [Question]),
    format('Answer (yes/no): ', []),
    read(Answer),
    (Answer = yes ; Answer = y).

% Collect symptoms through questions
collect_symptoms([], []).
collect_symptoms([Symptom|RestSymptoms], PresentSymptoms) :-
    (ask_symptom(Symptom) ->
        collect_symptoms(RestSymptoms, RestPresent),
        PresentSymptoms = [Symptom|RestPresent]
    ;
        collect_symptoms(RestSymptoms, PresentSymptoms)
    ).

% ============================================
% PROBABILITY CALCULATION FUNCTIONS
% ============================================

% Calculate match score based on present symptoms
calculate_match_score(Disease, PatientSymptoms, Score) :-
    disease(Disease, DiseaseSymptoms, _),
    findall(Prob, 
        (member(Symptom, PatientSymptoms), 
         member(Symptom, DiseaseSymptoms),
         symptom_probability(Disease, Symptom, Prob)),
        Probs),
    (Probs = [] -> Score = 0 ; average(Probs, Score)).

% Calculate average of a list
average(List, Avg) :-
    length(List, Len),
    Len > 0,
    sum_list(List, Sum),
    Avg is Sum / Len.

% Calculate Bayesian probability (improved version)
bayesian_probability(Disease, PatientSymptoms, Probability) :-
    disease(Disease, DiseaseSymptoms, Prior),
    
    % Calculate match between patient symptoms and disease symptoms
    intersection(PatientSymptoms, DiseaseSymptoms, MatchingSymptoms),
    length(MatchingSymptoms, NumMatching),
    length(PatientSymptoms, NumPatient),
    length(DiseaseSymptoms, NumDisease),
    
    % Avoid division by zero
    (NumPatient > 0 -> 
        MatchRatio is NumMatching / NumPatient 
    ; 
        MatchRatio = 0
    ),
    
    % Calculate average probability of matching symptoms
    (NumMatching > 0 ->
        findall(P, 
            (member(Symptom, MatchingSymptoms),
             symptom_probability(Disease, Symptom, P)),
            MatchProbs),
        average(MatchProbs, AvgMatchProb)
    ;
        AvgMatchProb = 0.01
    ),
    
    % Improved probability calculation
    % Uses: Prior * MatchRatio * AvgSymptomProbability * Boost
    Boost is 1 + (NumMatching / NumDisease),
    RawProb is Prior * MatchRatio * AvgMatchProb * Boost * 2,
    
    % Cap at 95%
    Probability is min(0.95, RawProb).

% Product of list elements
product_list([], 1).
product_list([H|T], Product) :-
    product_list(T, Rest),
    Product is H * Rest.

% ============================================
% DIAGNOSIS PREDICATES
% ============================================

% Main diagnosis predicate
diagnose(PatientSymptoms, DiagnosisList) :-
    findall(
        disease(Disease, Prob),
        (disease(Disease, _, _),
         bayesian_probability(Disease, PatientSymptoms, Prob),
         Prob > 0.05),
        UnsortedList
    ),
    sort_by_probability(UnsortedList, DiagnosisList).

% Sort diseases by probability (descending)
sort_by_probability(List, Sorted) :-
    predsort(compare_disease_prob, List, Desc),
    reverse(Desc, Sorted).

compare_disease_prob(Order, disease(_, P1), disease(_, P2)) :-
    compare(Order, P1, P2).

% Get top N diagnoses
top_diagnoses(PatientSymptoms, N, TopList) :-
    diagnose(PatientSymptoms, FullList),
    take_first(N, FullList, TopList).

take_first(_, [], []).
take_first(0, _, []).
take_first(N, [H|T], [H|Rest]) :-
    N > 0,
    N1 is N - 1,
    take_first(N1, T, Rest).

% Display diagnosis results (improved with better handling)
display_diagnosis(PatientSymptoms) :-
    format('~n~n========================================~n', []),
    format('       DIAGNOSIS REPORT~n', []),
    format('========================================~n', []),
    format('~nPatient Symptoms: ~w~n', [PatientSymptoms]),
    length(PatientSymptoms, NumSymptoms),
    format('Total Symptoms Reported: ~d~n', [NumSymptoms]),
    diagnose(PatientSymptoms, DiagnosisList),
    format('~n--- Possible Diseases (ranked by probability) ---~n~n', []),
    (DiagnosisList = [] ->
        format('No matching diseases found with current symptoms.~n', []),
        format('Please consult a healthcare professional for evaluation.~n', [])
    ;
        display_disease_list(DiagnosisList, 1)
    ),
    format('~n========================================~n', []).

display_disease_list([], _).
display_disease_list([disease(Disease, Prob)|Rest], N) :-
    Percentage is Prob * 100,
    format('~d. ~w: ~2f%~n', [N, Disease, Percentage]),
    N1 is N + 1,
    display_disease_list(Rest, N1).

% ============================================
% INTERACTIVE DIAGNOSIS WITH YES/NO QUESTIONS
% ============================================

% Main entry point - Interactive diagnosis with questions
start_diagnosis :-
    format('~n~n', []),
    format('╔════════════════════════════════════════════════╗~n', []),
    format('║   MEDICAL DIAGNOSIS EXPERT SYSTEM              ║~n', []),
    format('║   Interactive Symptom Assessment               ║~n', []),
    format('╚════════════════════════════════════════════════╝~n', []),
    format('~n', []),
    format('Welcome! I will ask you a series of questions about~n', []),
    format('your symptoms. Please answer with "yes" or "no".~n', []),
    format('~nPress ENTER to begin...', []),
    get_char(_),
    get_all_symptoms(AllSymptoms),
    format('~n~n--- SYMPTOM ASSESSMENT ---~n', []),
    collect_symptoms(AllSymptoms, PresentSymptoms),
    (PresentSymptoms = [] ->
        format('~n~nNo symptoms reported. Unable to provide diagnosis.~n', [])
    ;
        display_diagnosis(PresentSymptoms),
        format('~n*** DISCLAIMER ***~n', []),
        format('This is a preliminary assessment tool only.~n', []),
        format('Please consult a qualified healthcare professional~n', []),
        format('for proper medical diagnosis and treatment.~n', [])
    ),
    format('~n========================================~n~n', []).

% Quick diagnosis - ask only relevant questions
quick_diagnosis :-
    format('~n~n', []),
    format('╔════════════════════════════════════════════════╗~n', []),
    format('║   QUICK DIAGNOSIS MODE                         ║~n', []),
    format('╚════════════════════════════════════════════════╝~n', []),
    format('~n', []),
    format('I will ask about common symptoms.~n', []),
    format('Answer with "yes" or "no".~n~n', []),
    
    CommonSymptoms = [fever, cough, headache, sore_throat, fatigue, 
                      nausea, shortness_of_breath, body_aches],
    collect_symptoms(CommonSymptoms, PresentSymptoms),
    
    (PresentSymptoms = [] ->
        format('~n~nNo common symptoms reported.~n', []),
        format('Would you like a full assessment? (yes/no): ', []),
        read(Answer),
        (Answer = yes -> start_diagnosis ; 
         format('~nThank you. Stay healthy!~n', []))
    ;
        display_diagnosis(PresentSymptoms),
        format('~n*** DISCLAIMER ***~n', []),
        format('Please consult a healthcare professional.~n', [])
    ),
    format('~n========================================~n~n', []).

% ============================================
% EXAMPLE QUERIES (FOR TESTING)
% ============================================

% Example 1: Flu-like symptoms
example1 :-
    Symptoms = [fever, cough, fatigue, body_aches],
    display_diagnosis(Symptoms).

% Example 2: Respiratory symptoms
example2 :-
    Symptoms = [cough, shortness_of_breath, chest_pain],
    display_diagnosis(Symptoms).

% Example 3: Cold symptoms
example3 :-
    Symptoms = [runny_nose, sneezing, sore_throat],
    display_diagnosis(Symptoms).

% Example 4: Severe headache
example4 :-
    Symptoms = [severe_headache, nausea, sensitivity_to_light],
    display_diagnosis(Symptoms).

% Example 5: Gastrointestinal symptoms
example5 :-
    Symptoms = [nausea, vomiting, diarrhea, abdominal_pain],
    display_diagnosis(Symptoms).

% ============================================
% UTILITY PREDICATES
% ============================================

% List all available diseases
list_diseases :-
    format('~n=== AVAILABLE DISEASES IN KNOWLEDGE BASE ===~n~n', []),
    forall(disease(Disease, Symptoms, Prior),
        (format('Disease: ~w~n', [Disease]),
         format('  Prior Probability: ~2f%~n', [Prior*100]),
         format('  Key Symptoms: ~w~n~n', [Symptoms]))).

% List all symptoms
list_symptoms :-
    format('~n=== ALL SYMPTOMS IN KNOWLEDGE BASE ===~n~n', []),
    get_all_symptoms(AllSymptoms),
    forall(member(S, AllSymptoms), 
        (symptom_question(S, Q),
         format('- ~w: ~w~n', [S, Q]))).

% Show help
help :-
    format('~n=== MEDICAL DIAGNOSIS SYSTEM - HELP ===~n~n', []),
    format('Available Commands:~n', []),
    format('  start_diagnosis.     - Full interactive diagnosis with all questions~n', []),
    format('  quick_diagnosis.     - Quick diagnosis with common symptoms only~n', []),
    format('  example1.            - Test with flu-like symptoms~n', []),
    format('  example2.            - Test with respiratory symptoms~n', []),
    format('  example3.            - Test with cold symptoms~n', []),
    format('  list_diseases.       - Show all diseases in knowledge base~n', []),
    format('  list_symptoms.       - Show all symptoms with questions~n', []),
    format('  help.                - Show this help message~n~n', []),
    format('For manual diagnosis:~n', []),
    format('  diagnose([symptom1,symptom2,...], Result).~n~n', []).