# Working Base — Initial Architecture Record

**Record date:** 2026-08-16  
**Origin:** ChatGPT project-chat response immediately preceding repository initialization  
**Requested preservation:** Explicitly requested by Kai as Working Base  
**Status:** HISTORICAL WORKING BASE / NON-CANONICAL INPUT  
**Preservation note:** The substantive chat response is preserved below. Chat-UI citation tokens are omitted because they are interface-specific; the referenced handout is registered separately as `SOURCE-INTAKE-0001`.

---

Ja. Und bei diesem Thema würde ich **die Architektur vor der Mathematik festziehen**. Sonst haben wir nach drei Monaten hundert PDFs, numerische Experimente, halbfertige Beweisideen und externe Audits, aber keine belastbare Provenienz mehr.

Ich habe das Handout vollständig vorliegen. Sein Status ist ziemlich klar: Es ist ein **sauberer Intake-/Seed-Artefakt**, aber noch kein mathematisches Grundlagendokument des neuen Forschungsstrangs. Es enthält das verifizierte Video-Transkript, die elementare Formulierung der Riemannschen Vermutung, einige geprüfte Basisfakten und erste Quellenhinweise. Gerade die bereits dokumentierte Korrektur der Pratt-Quelle zeigt übrigens, warum wir von Beginn an eine explizite Provenienz- und Korrekturschicht brauchen.

Für mich ergibt sich daraus folgende **Projektkonstruktion**:

## 1. Eigenständiges Repository

Nicht in TIG, nicht in Consciousness und zunächst auch nicht als Unterordner eines bestehenden Physik-Repos.

Arbeitsname beispielsweise:

**`Riemann_Integrity_Research`**

oder, neutraler:

**`Riemann_Hypothesis_Research`**

Ich würde momentan den zweiten Namen bevorzugen. Er behauptet nichts und bleibt wissenschaftlich neutral.

Das Repo bekommt zunächst ausdrücklich den Status:

**RESEARCH PROGRAM — OPEN PROBLEM — NO CLAIM OF PROOF**

Das ist wichtig. Die Riemannsche Vermutung ist kein normales Paper-Projekt, sondern ein Forschungsprogramm.

## 2. Sechs strikt getrennte Ebenen

```text
Riemann_Hypothesis_Research/
│
├── 00_GOVERNANCE/
├── 01_SOURCE_CORPUS/
├── 02_MATHEMATICAL_FOUNDATIONS/
├── 03_RESEARCH_PROGRAM/
├── 04_COMPUTATION/
├── 05_PROOF_ATTEMPTS/
└── 06_AUDIT_AND_RESULTS/
```

Der entscheidende Punkt ist die **semantische Trennung**.

`01_SOURCE_CORPUS` enthält das, was andere bewiesen oder publiziert haben.

`02_MATHEMATICAL_FOUNDATIONS` enthält unsere rekonstruierte mathematische Wissensbasis.

`03_RESEARCH_PROGRAM` enthält Forschungsfragen, Strategien und Hypothesen.

`04_COMPUTATION` enthält numerische Experimente und Code.

`05_PROOF_ATTEMPTS` enthält tatsächliche eigene Ableitungen.

`06_AUDIT_AND_RESULTS` enthält Belastungstests, Widerlegungen und gegebenenfalls valide Resultate.

Damit kann eine numerische Beobachtung niemals versehentlich zu einem Lemma und ein Lemma niemals versehentlich zu einem Beweis werden.

## 3. Das Handout bekommt einen klaren Platz

Das jetzige PDF würde ich **nicht** unter mathematische Grundlagen legen.

Sondern beispielsweise:

```text
01_SOURCE_CORPUS/
└── 00_INTAKE/
    └── Handout_Riemann_V3_final.pdf
```

Status:

**SOURCE-INTAKE / ORIENTATION / NON-CANONICAL**

Denn das Dokument selbst bezeichnet seinen Inhalt als Transkript und Wahrheitsprüfung eines kurzen Videos.

Es enthält beispielsweise die elementare Beschreibung

\[
\zeta(s)=1+\frac1{2^s}+\frac1{3^s}+\cdots
\]

sowie die Aussage, dass die nichttrivialen Nullstellen gemäß RH den Realteil

\[
\operatorname{Re}(s)=\frac12
\]

haben sollen.

Aber **unsere eigentliche mathematische Basis darf später nicht auf diesem Handout beruhen**.

Dafür brauchen wir Riemann selbst sowie die Primärliteratur und Standardreferenzen.

## 4. Ein Claim-/Theorem-Ledger wird hier unverzichtbar

Das würde ich von Tag 1 an führen.

Beispielsweise:

```text
00_GOVERNANCE/
    CLAIM_LEDGER.md
    OPEN_QUESTIONS.md
    SOURCE_REGISTER.md
    NOTATION_STANDARD.md
    RESEARCH_STATUS.md
```

Jede mathematische Aussage bekommt einen Status:

**D — Definition**

**T — etabliertes Theorem**

**L — eigenes bewiesenes Lemma**

**C — Conjecture / Kandidat**

**N — numerische Beobachtung**

**H — Heuristik**

**OQ — Open Question**

**R — Refuted**

Das ist bei RH noch wichtiger als bei unseren bisherigen Arbeiten. Eine typische Katastrophe in diesem Forschungsfeld besteht darin, dass irgendwo zwischen numerischem Muster, analytischer Fortsetzung, Spektralintuition und tatsächlichem Satz die logische Modalität verloren geht.

Das darf uns nicht passieren.

## 5. Das Forschungsprogramm darf nicht mit „Wir beweisen RH“ beginnen

Die erste Phase sollte heißen:

**PHASE 0 — DOMAIN RECONSTRUCTION**

und nicht „Proof Attempt“.

Wir rekonstruieren zunächst vollständig:

- Dirichlet-Reihe und Euler-Produkt
- analytische Fortsetzung
- Funktionalgleichung
- Gamma-Faktor
- \(\xi(s)\)
- triviale und nichttriviale Nullstellen
- kritischer Streifen
- kritische Gerade
- Primzahlsatz
- explizite Formeln
- \(\psi(x)\), \(\pi(x)\), \(\Lambda(n)\)
- zero-free regions
- zero-density results
- Hardy/Littlewood
- Selberg
- Montgomery pair correlation
- Hilbert–Pólya
- Random-Matrix-Verbindungen
- bekannte Äquivalenzen zur RH
- bekannte stärkere und schwächere Aussagen
- gescheiterte Beweisfamilien und bekannte Fallstricke.

Erst danach kann man seriös entscheiden, **welcher Angriffsraum überhaupt sinnvoll ist**.

## 6. Wir sollten außerdem drei Wissensklassen voneinander isolieren

Das wird später entscheidend für Nexus/TIG.

**Klasse A — klassische Mathematik**

Alles, was unabhängig von TIG/Riemann-Synthesen etabliert ist.

**Klasse B — externe Forschungsprogramme**

Hilbert–Pólya, Spektraltheorie, Operatoransätze, Random Matrices, dynamische Systeme usw.

**Klasse C — Nexus/TIG-eigene Hypothesen**

Falls später eine Verbindung zu X5/X6, Integrität, Spektralbedingungen oder geometrischen Strukturen untersucht wird.

Klasse C darf **niemals rückwirkend Klasse A umdeuten**.

Das halte ich für eine der wichtigsten Governance-Regeln des gesamten Vorhabens.

## 7. Versionsstrategie

Bei einem Projekt über Monate würde ich keine ständig überschriebenen „Masterdateien“ verwenden.

Stattdessen:

```text
Research_Status_2026-08-16_v0.1.md
Research_Status_2026-08-23_v0.2.md
...
```

und zusätzlich einen kleinen:

```text
CURRENT_STATE.md
```

Der verweist immer auf den aktuellen kanonischen Stand.

Das verhindert genau den Effekt, den wir bei großen Chat-/Auditketten bereits kennen: historische Aussagen werden unmerklich zu aktuellen Aussagen.

## 8. Der allererste wissenschaftliche Output sollte noch kein Beweisversuch sein

Sondern ein Dokument ungefähr dieser Art:

**`Riemann_Hypothesis_Research_Baseline_v0.1.md`**

mit:

1. exakt formuliertem Problem,
2. Definitionsraum,
3. Voraussetzungen,
4. etablierten Resultaten,
5. offenen Resultaten,
6. bekannten äquivalenten Formulierungen,
7. bekannten Proof Barriers,
8. relevanten Forschungsrichtungen,
9. Corpus-Plan,
10. unseren Forschungsfragen.

Erst wenn dieses Dokument auditiert ist, öffnen wir `05_PROOF_ATTEMPTS`.

Damit hätten wir meines Erachtens eine Konstruktion, die **auch nach sechs Monaten und mehreren hundert Quellen noch beherrschbar bleibt**.

Und noch etwas ist mir beim vorliegenden Handout wichtig: Die darin genannten Quellen sind ein Ausgangspunkt, kein Corpus. Für Phase 0 würde ich daraus eine systematische **Primärquellen-Rekonstruktion** machen und nicht einfach diese Liste übernehmen.

Mein nächster Schritt wäre deshalb **nicht Mathematik**, sondern die Erstellung einer verbindlichen **Repository- und Governance-Spezifikation v0.1** – einschließlich Verzeichnisbaum, Dateinamenregeln, Claim-Klassen, Source-Intake-Prozess und Forschungsphasen. Danach können wir das Repo eröffnen und das jetzige PDF als `SOURCE-INTAKE-0001` registrieren.

---

## Initialization correction record

The repository name was subsequently fixed by explicit author decision as **`Riemann_Integrity_Research`**. The earlier preference for `Riemann_Hypothesis_Research` remains preserved above as historical working context and is not silently rewritten.

The local `D/T/L/C/N/H/OQ/R` proposal above is also preserved historically. In active governance it is treated as a **Statement Type** vocabulary, not as the canonical Nexus `Claim Status` axis. This avoids a cross-axis collision with Integrity Nexus governance.