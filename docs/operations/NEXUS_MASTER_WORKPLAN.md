# NEXUS_PROJECTS — MASTER WORKPLAN
**Stand:** 16.08.2026, 09:31 MESZ  
**Version:** v2  
**Status:** Arbeitsreferenz / aktueller Wiedereinstiegspunkt — noch nicht vollständig reconciliert

## 0. Arbeitsregel für diesen Plan
Diese Datei ist ab jetzt der Referenzpunkt für die Reihenfolge der offenen Arbeiten.  
Nicht aus dem Chatverlauf rekonstruieren, wenn dieser Plan verfügbar ist.

Änderungsregel:
1. Bestehenden Stand prüfen.
2. Änderung/Fehler ausdrücklich benennen.
3. Abhängigkeiten prüfen.
4. Plan aktualisieren.
5. Neue Version speichern.

---

# A. Sofortiger Recovery-Block — Claude / Works

## A1 — Heutigen fehlerhaften Claude-/Works-Strang nicht weiter propagieren
- Vorhandene Ergebnisse bleiben Prüfmaterial.
- Nichts daraus wird automatisch neue Baseline.

## A2 — Grundlagendokument v1.0 korrigieren
- Das fehlerhafte bzw. unvollständige v1.0 ist der aktuelle Root Error.
- Erst die fachliche und architektonische Basis richtigstellen.

## A3 — v1.0 gegen den letzten belastbaren Vorzustand prüfen
- Delta sichtbar machen.
- Fehlerursache benennen.
- Betroffene Dependencies identifizieren.
- Keine stillen Korrekturen.

## A4 — Claude-Arbeitsanweisung neu formulieren
- Ausschließlich aus dem korrigierten v1.0 ableiten.
- Rollen, Dependencies, Terminologie, Authority, Statuslogik und Scope prüfen.

## A5 — Claude-Arbeitsanweisung vor Ausführung auditieren

## A6 — Claude erneut ausführen lassen

## A7 — Claude-Ergebnis verifizieren
Prüfung gegen:
- korrigiertes v1.0
- korrigierte Arbeitsanweisung
- letzten belastbaren Vorzustand

Erst nach Closure dieses Blocks darf der nachgelagerte Auditoren-Strang weitergezogen werden.


## A8 — ΩE / Consciousness Corpus Recovery — paralleler State-Recovery-Gate

Dieser Block ist **offen** und darf nicht aus dem Masterplan herausfallen.

### Bekannter Sollbestand
**CORE TARGET = 20 Dateien**
- 14 eindeutige externe Quellen
- 6 interne ΩE-Grundlagen

Davon waren im zuletzt rekonstruierten Chatstand:
- 6/20 direkt vorhanden
- 14/20 zu ergänzen

### 11 externe Quellen nachzuladen / exakt zu versionieren
1. CR-08 — Hoffman (2008), *Conscious Realism and the Mind-Body Problem*
2. BIO-13 — Chernet & Levin (2013), *Endogenous Voltage Potentials and the Microenvironment*
3. CA-14 — Hoffman & Prakash (2014), *Objects of Consciousness*
4. CA-18 — Fields et al. (2018), *Conscious Agent Networks: Formal Analysis and Application to Cognition*
5. ITP-19 — Prakash (2019), *On Invention of Structure in the World: Interfaces and Conscious Agents*
6. BIO-19 — Levin (2019), *The Computational Boundary of a “Self”*
7. CRIT-21 — Gruber (2021), *Questioning Conscious Realism*
8. BIO-21 — McMillen et al. (2021), *Beyond Neurons*
9. CA-23 — Hoffman, Prakash & Prentner (2023), *Fusions of Consciousness*
10. CAT-24 — Prentner & Hoffman (2024), *Interfacing Consciousness*
11. TR-25 — Hoffman, Prakash & Chattopadhyay, *Traces of Consciousness*

### 3 interne ΩE-Grundlagen wieder einbinden
- `OmegaE_END_OF_SESSION_WORKING_STATE_SNAPSHOT_2026-08-07.md`
- `Consciousness_Research_Operating_Contract_v0.1_Working_Draft.pdf`
- `Gesamtstatus_Handoff_External_Grounding_v1_2_AuditReady_2026-08-10.md`

### 3 zusätzliche Audit-Artefakte — Lokationsstatus ungeklärt
- `External_Grounding_Audit_v1.md`
- `External_Grounding_Claim_Source_Locator_v1.md`
- `OmegaE_Comparison_Gate_Template_v1.md`

Diese Artefakte gelten **nicht als gelöscht**, solange nur feststeht, dass sie derzeit nicht als eigenständige Datei aufgefunden wurden.

Recovery-Reihenfolge:
1. Library / bekannte Arbeitsbestände / Repositories nach exakten Dateinamen und Varianten durchsuchen.
2. Vorhandene Originalartefakte bevorzugen; nicht vorschnell rekonstruieren.
3. Falls ein Artefakt tatsächlich nicht wiederauffindbar ist: nur aus belegten Vorstufen rekonstruieren.
4. Rekonstruktionen ausdrücklich als `RECONSTRUCTED` / `RECOVERED` kennzeichnen; keine stillschweigende Gleichsetzung mit dem verlorenen Original.
5. Load-bearing Claims weiterhin gegen Originalquellen prüfen.
6. Nach Recovery ein Corpus-/Audit-Manifest mit Dateinamen, Version, Herkunft, Hash/Checksum und Authority-Status erzeugen.

### Zielzustand
- 20/20 Core Files vorhanden
- zusätzlich 3/3 Audit Files vorhanden oder transparent rekonstruiert
- vollständiger Arbeitsbestand = 23 Artefakte
- klarer Authority-/Provenienzstatus
- erst danach weitere ΩE-Vergleichs- oder Consciousness-Arbeit auf diesem Corpus fortsetzen

## A9 — Noch nicht reconciliert: historische Aufgaben-/Fragenbestände

Der Masterplan ist weiterhin **noch nicht vollständig kanonisch**, solange folgende Bestände nicht gemappt wurden:
- 21 historische Tagesaufgaben
- ca. 70 Open Questions aus den Forschungssträngen

Diese werden nicht als flache Anhänge übernommen, sondern gegen den Critical Path gemappt:
- offen
- erledigt
- überholt
- zusammengeführt
- blockiert
- Dependency / Expert Gate

---

# B. Projektübergreifende Notebook-/Corpus-Research-Pipeline

## B1 — Pipeline als eigene Infrastruktur definieren
Ziel:
**Discovery → Grounding → Corpus → Synthese → Adversarial Audit → Expert Gate → Canonical Research**

NotebookLM ist dabei Corpus-/Analyse-Schicht, nicht wissenschaftliche Letztautorität.

## B2 — Referenzimplementierung: Operationalisierung von Emergenz
Aktueller Stand:
- Literatur-Discovery läuft.
- erster Suchlauf: 32 Arbeiten
- zweiter Suchlauf: mindestens 103 unterschiedliche Kandidaten
- Qualitätskontrolle / Corpus Qualification steht als nächstes an

Nächste Schritte:
1. Bibliographische Verifikation
2. Dubletten-/Versionsabgleich
3. Primär-/Sekundärquellen klassifizieren
4. CORE / SUPPORTING / CRITICAL-ADVERSARIAL / BACKGROUND / EXCLUDE
5. Gap Analysis
6. NotebookLM-Corpus aufbauen
7. Notebook 1: Forschungsraum / Taxonomie / Cross-Paper-Matrix
8. Notebook 2: Formalisierung / mathematische Operationalisierung
9. adversarialer Audit
10. Fachwissenschaftliche Prüfung

## B3 — Dieselbe Pipeline später übertragen auf
- Intuition
- Kristallisation
- weitere fundamentale Begriffe / Forschungsfragen
- ausgewählte TIG-/TIG-E-Themen
- kontrollierte Repository-/Dokument-Corpora

---

# C. Früher wissenschaftlicher Anschluss — hohe Priorität

## C1 — Operationalisierung von Emergenz
**OFFEN — hohe Priorität**

Begründung:
- nicht abgeschlossen
- fachlich zentral
- hält den wissenschaftlichen Austausch mit Herrn Professor Conchik aktiv
- Unterstützung seiner Arbeit zur Operationalisierung von Emergenz ist strategisch wertvoll

Dieser Punkt darf nicht ans Ende des Gesamtprogramms verschoben werden.

## C2 — Operationalisierung von Intuition
**OFFEN**
- ebenfalls nicht abgeschlossen
- sauber trennen zwischen intuitiver Erkenntnisgewinnung, Operationalisierung, Mechanismus und wissenschaftlicher Validierung

## C3 — Operationalisierung von Kristallisation
**OFFEN / Forschungsstrang**
- mit derselben Corpus-/Notebook-Pipeline vorbereiten
- erst Literatur-/Begriffsraum, dann eigene Formalisierung

---

# D. Audit-System — Architektur aktualisieren

## D1 — Audit Operating System / gemeinsame Governance-Basis
- aktueller kontrollierter Stand weiterführen
- keine voreilige Ratifikation / v1.0, solange Closure offen ist

## D2 — Auditoren-Inventar herstellen
Je Auditor:
- Master Prompt
- Evidence-/Domain-Profil
- Version
- Status
- bisherige Tests/Audits
- Findings
- offene Lücken

## D3 — Arbeitsarchitektur derzeit: 6 Auditoren + vorgelagerte Intake-Pipeline
**Provisorische Zielstruktur:**
1. Governance Auditor
2. General / Cross-Domain Auditor
3. Repository Auditor
4. Physics Auditor
5. Mathematics Auditor
6. Field Equation Auditor

Die bisherigen YouTube- und Instagram-Auditoren werden nicht einfach gelöscht, sondern ihre Funktion wird in eine allgemeine vorgelagerte **Scientific Source Intake & Grounding Pipeline** überführt.

## D4 — Scientific Source Intake & Grounding Pipeline
Für YouTube, Instagram, Vorträge, Podcasts, KI-Handouts und andere Discovery Sources:

1. Originalquelle sichern
2. Claims extrahieren
3. Visualisierung/Metapher von fachlicher Aussage trennen
4. wissenschaftliche Primärquellen recherchieren
5. Claim↔Evidence-Mapping
6. NotebookLM-Corpus / Analyse
7. Evidenzstatus bestimmen
8. an Physics / Mathematics / Field Equation / General routen
9. erst nach Domain-Audit repository-fähig machen

Schutzregel:
**Discovery Source ≠ Evidence Source**

## D5 — Governance Auditor
- Governance vor General / Cross-Domain
- bestehende Artefakte reconciliieren, nicht neu erfinden

## D6 — General / Cross-Domain Auditor
- bestehenden Stand erhalten
- veraltete Dependencies kontrolliert aktualisieren

## D7 — Repository Auditor

## D8 — Physics Auditor

## D9 — Mathematics Auditor

## D10 — Field Equation Auditor
- abhängig von Physics + Mathematics
- kein isolierter Freigabekanal

## D11 — Audit-System erst nach Tests als operativ bezeichnen

---

# E. TIG

## E1 — TIG-Findings / Reparaturlisten dependency-geordnet abarbeiten

## E2 — TIG-Repositories korrigieren

## E3 — TIG re-auditieren

## E4 — wissenschaftliche TIG-Konsolidierung
Insbesondere:
- Open Questions
- Feldgleichungsarchitektur
- variationale Fundierung
- fundamentale Herleitung
- Kovarianz
- dynamische Schließung
- mikroskopische Update-Struktur
- Metrikrekonstruktion

## E5 — Cross-Repository-Konsistenz
- Authority
- Status
- Terminologie
- Provenienz
- P0/P1
- Citations
- Dependencies

---

# F. Physik-/Mathematik-Expert-Gates — früh einbauen

## F1 — bestimmen, welche Fragen intern nicht weiter selbstvalidiert werden dürfen

## F2 — präzise Expert Questions erzeugen

## F3 — Aachen/Jülich/RWTH/FZJ/JARA-Mapping aktualisieren

## F4 — fachwissenschaftliche Rückkopplung kontrolliert integrieren

Wichtig:
Nicht erst „alles intern fertigstellen“ und danach Experten fragen.

---

# G. TIG-E

## G1 — echte TIG-E-Abhängigkeiten erst aus korrigiertem TIG ableiten

## G2 — TIG-E-Reparaturlisten abarbeiten

## G3 — TIG-E-Repository korrigieren und re-auditieren

## G4 — Related Work & Delta
- Assurance
- Provenienz
- Workflow
- Governance
- Expert Elicitation
- keine starken Neuheitsclaims ohne belastbaren Vergleich

## G5 — Leistungsmetriken / Falsifizierbarkeit operationalisieren

---

# H. Runtime

## H1 — vorhandenen Runtime-Bestand reconciliieren
Nicht neu anfangen.

Trennen:
- Research Orchestration Runtime
- Governance Enforcement Runtime

Prüfen:
- konkurrierende/gleichnamige Architekturartefakte
- Authority
- Reifeangaben
- „ARCHITECTURE COMPLETE“
- „READY FOR IMPLEMENTATION“

## H2 — Governance / Rule Inventory herstellen

## H3 — Runtime operationalisieren
- Zustände
- Routing
- Orchestrierung
- Regelprüfung
- Blocking
- Escalation
- Logging
- kontrollierte Übergänge

---

# I. Assurance / External Readiness

## I1 — Domain Grounding operationalisieren

## I2 — Human Expert Gates fest verankern

## I3 — Security Governance adversarial auditieren

## I4 — External Readiness Gate

## I5 — Strategic Research Briefing
- v1.0 historisch erhalten
- für ernsthaften Outreach v2 mit Change Summary erstellen

## I6 — Public Entry Layer synchronisieren
- Website
- GitHub
- öffentliche Forschungsseite

---

# J. Aachen / Jülich / externe Fachwelt

## J1 — institutionelles Routing neu validieren

## J2 — geeignete Gruppen/Personen fachlich zuordnen

## J3 — eng umrissene wissenschaftliche Fragen adressieren

## J4 — Feedback als externe Evidenz / Expert Review integrieren

---

# K. ΩE / External Grounding — paralleler geschützter Forschungsstrang

- aktueller External-Grounding-Handoff bleibt eigener Forschungsstand
- nicht mit dem Claude-/Auditoren-Root-Recovery vermischen
- External Validation weiterhin offen
- ΩE-Vergleich nur kontrolliert auf kanonischer ΩE-Spezifikation
- Claim-to-Source / Non-Equivalence-Regeln erhalten

---

# L. Weitere offene, aber derzeit nachrangige Arbeiten

- Produkt-/Positionierungsdokumente konsolidieren
- IMMUNIT / Website
- öffentliche Webverknüpfung
- LinkedIn
- Asset Register / Unternehmenswert
- Dokumentations- und Arbeitsregeln weiter formalisieren
- ältere Runtime-Dokumente bereinigen
- Wissensarchitektur / zentrale Rolle von Integrität weiterführen
- Environment Congruence / Integrity Friction weiterführen
- Bewusstseinsforschung separat halten

---

# M. Aktueller Hauptpfad in einem Satz

**Masterplan einfrieren → Claude-v1.0-Rootfehler beheben → Claude-Anweisung korrigieren → Claude neu ausführen und verifizieren → parallel Emergenz-Corpus/Notebook-Pipeline als Referenzimplementierung aufbauen → Audit-System mit 6 Auditoren + Source-Intake-Pipeline konsolidieren → TIG korrigieren + Expert-Gates → TIG-E → Runtime/Assurance → External Readiness → Aachen/Jülich → wirtschaftliche Verwertung.**