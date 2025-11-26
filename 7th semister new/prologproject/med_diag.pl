% File: med_diag.pl
% Run with SWI-Prolog:   swipl -q -s med_diag.pl
% Then call:    ?- start.
%
% Short description:
% - Interactive yes/no questions about symptoms (text-based).
% - Computes % match for each disease and prints a detailed report.
% - Keeps a simple symptom->label mapping for readable questions.

:- dynamic yes_symptom/1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Disease knowledge base
% disease(Name, [list_of_symptom_atoms]).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disease(flu, [fever, cough, headache, sore_throat, body_ache, fatigue]).
disease(common_cold, [sneezing, runny_nose, sore_throat, cough, low_fever]).
disease(dengue, [high_fever, headache, joint_pain, retro_orbital_pain, rash, nausea]).
disease(typhoid, [prolonged_fever, headache, abdominal_pain, loss_of_appetite, constipation_or_diarrhea]).
disease(covid19, [fever, cough, shortness_of_breath, loss_of_taste_or_smell, fatigue, sore_throat]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Symptom labels (for better questions)
% symptom_label(symptom_atom, "Readable description").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

symptom_label(fever, "fever (high temperature)").
symptom_label(low_fever, "low fever / mild fever").
symptom_label(high_fever, "high fever").
symptom_label(cough, "cough").
symptom_label(headache, "headache").
symptom_label(sore_throat, "sore throat").
symptom_label(body_ache, "body ache / muscle pain").
symptom_label(fatigue, "fatigue / tiredness").
symptom_label(sneezing, "sneezing").
symptom_label(runny_nose, "runny nose").
symptom_label(joint_pain, "joint pain").
symptom_label(retro_orbital_pain, "pain behind the eyes (eye/retro-orbital pain)").
symptom_label(rash, "skin rash").
symptom_label(nausea, "nausea or vomiting").
symptom_label(prolonged_fever, "fever lasting several days (prolonged fever)").
symptom_label(abdominal_pain, "abdominal (stomach) pain").
symptom_label(loss_of_appetite, "loss of appetite").
symptom_label(constipation_or_diarrhea, "constipation or diarrhea").
symptom_label(shortness_of_breath, "shortness of breath / difficulty breathing").
symptom_label(loss_of_taste_or_smell, "loss of taste or smell").

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Helper: collect all unique symptoms from diseases
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

all_symptoms(Symptoms) :-
    setof(S, Sym^(
        disease(_, L),
        member(S, L)
    ), Symptoms).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Start / main flow
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

start :-
    retractall(yes_symptom(_)),
    format("~n--- Medical Diagnosis Expert System ---~n", []),
    format("This is an educational tool, not a substitute for professional medical advice.~n~n", []),
    all_symptoms(AllSymptoms),
    ask_symptoms(AllSymptoms),
    compute_results(Results),
    print_report(Results),
    retractall(yes_symptom(_)),
    format("~nThank you. Stay safe and consult a healthcare professional if needed.~n", []).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Ask user about each symptom (text-based yes/no)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ask_symptoms([]).
ask_symptoms([Sym|Rest]) :-
    ask_about(Sym),
    ask_symptoms(Rest).

ask_about(Symptom) :-
    (   symptom_label(Symptom, Label) -> true ; Label = Symptom ),
    format("Do you have ~w? (yes/no)  ", [Label]),
    read_line_to_string(user_input, Raw),
    normalize_answer(Raw, Answer),
    handle_answer(Answer, Symptom).

% normalize possible user inputs
normalize_answer(Raw, yes) :-
    string_lower(Raw, L),
    member(L, ["yes","y","true","t","1"]), !.
normalize_answer(Raw, no) :-
    string_lower(Raw, L),
    member(L, ["no","n","false","f","0"]), !.
normalize_answer(_, invalid).

handle_answer(invalid, Symptom) :-
    writeln("Please answer 'yes' or 'no'."),
    ask_about(Symptom).
handle_answer(yes, Symptom) :-
    assertz(yes_symptom(Symptom)), !.
handle_answer(no, _Symptom) :- !.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Compute match % for each disease
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

compute_results(Results) :-
    findall(disease_score(Name, Matched, Total, Percent, MatchedList),
            ( disease(Name, SList),
              length(SList, Total),
              findall(S, (member(S, SList), yes_symptom(S)), MatchedList),
              length(MatchedList, Matched),
              ( Total =\= 0 -> PercentFloat is (Matched / Total) * 100 ; PercentFloat is 0 ),
              Percent is round(PercentFloat)
            ),
            ResultsUnsorted),
    % sort by Percent desc
    sort_results_by_percent(ResultsUnsorted, Results).

sort_results_by_percent(ResultsUnsorted, Results) :-
    map_list_to_pairs(calc_percent_key, ResultsUnsorted, Pairs),
    keysort(Pairs, SortedPairsAsc),
    reverse(SortedPairsAsc, SortedDesc),
    pairs_values(SortedDesc, Results).

calc_percent_key(disease_score(_Name, _M, _T, Percent, _List), Percent).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Printing report (Detailed)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print_report([]) :-
    writeln("No diseases available in the knowledge base."), !.
print_report(Results) :-
    writeln("\n--- Diagnosis Detailed Report ---"),
    print_each_result(Results),
    nl,
    print_recommendation(Results).

print_each_result([]).
print_each_result([disease_score(Name, Matched, Total, Percent, MatchedList)|Rest]) :-
    human_readable_disease(Name, HumanName),
    format("~n~w (~w):~n", [HumanName, Name]),
    format("  Matched symptoms: ~w / ~w (~w%)~n", [Matched, Total, Percent]),
    ( MatchedList = [] -> format("  Matching list: None~n", [])
    ; format("  Matching list: ~w~n", [MatchedList])
    ),
    print_each_result(Rest).

human_readable_disease(flu, "Flu").
human_readable_disease(common_cold, "Common Cold").
human_readable_disease(dengue, "Dengue").
human_readable_disease(typhoid, "Typhoid").
human_readable_disease(covid19, "COVID-19").
human_readable_disease(Other, Other).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Recommendation and explanation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print_recommendation(Results) :-
    Results = [disease_score(BestName, BestMatched, BestTotal, BestPercent, BestList)|_],
    ( BestPercent =:= 0 ->
        writeln("No likely disease detected from the asked symptoms."),
        writeln("If you feel unwell, consult a healthcare professional.")
    ;   human_readable_disease(BestName, BestHuman),
        format("Most probable diagnosis: ~w (~w%)~n", [BestHuman, BestPercent]),
        ( BestList = [] -> true ; format("Matched symptoms: ~w~n", [BestList]) ),
        advice_for(BestName, Advice),
        format("Advice: ~s~n", [Advice]),
        ( BestPercent >= 50 ->
            writeln("Recommendation: Consider seeking medical consultation for confirmation and treatment.")
        ;   writeln("Recommendation: Monitor your symptoms; consult a doctor if they worsen.")
        )
    ).

% Simple general advice per disease (non-prescriptive)
advice_for(flu, "Rest, take fluids, use antipyretics (e.g., paracetamol) for fever if needed. Consult a doctor if symptoms are severe.").
advice_for(common_cold, "Rest, fluids, saline nasal drops, and symptomatic care. Most colds resolve in a few days.").
advice_for(dengue, "Dengue can be serious. Seek prompt medical care if high fever, severe pain, bleeding, or warning signs occur. Avoid NSAIDs (e.g., ibuprofen) unless instructed by a doctor.").
advice_for(typhoid, "Typhoid often requires medical diagnosis (blood test) and antibiotic treatment prescribed by a physician. Seek medical attention.").
advice_for(covid19, "Isolate, monitor breathing and oxygen level if possible. Seek testing and medical care according to local guidelines. Consult a doctor if shortness of breath occurs.").
advice_for(_, "Monitor symptoms and consult a healthcare professional if concerned.").

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% End of file
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
