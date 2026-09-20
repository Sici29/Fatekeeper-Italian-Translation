# Quality Audit - Traduzione Italiana di Fatekeeper

**Data**: 19 Settembre 2026  
**Versione**: 1.0.0  
**Target**: Fatekeeper (Steam AppID `2186990`)  
**Copertura**: 1.511 stringhe uniche (100% del gioco)  

---

## 1. Obiettivo e Standard di Qualità

L'obiettivo di questa localizzazione è fornire un adattamento italiano di **livello professionale editoriale**, superando i limiti delle traduzioni letterali o automatiche:
- **Tono dark fantasy / souls-like maturo**: linguaggio solenne, evocativo e coerente con l'immaginario fantasy cupo del titolo.
- **Armonizzazione della terminologia di combattimento**: adozione degli standard consolidati per i giochi di ruolo d'azione (Salute, Vigore, Equilibrio, Parata, Danni contundenti/da taglio/da perforazione).
- **Raffinamento dei testi narrativi e arcaici**: le descrizioni di pozioni, manufatti e dialoghi del druido e del topo Kor Guran riflettono registri aulici o ironici con precisione stilistica.

---

## 2. Metriche di Copertura

| Categoria / Namespace | Voci | Stato | Note |
| :--- | :--- | :--- | :--- |
| **Parte 1: Core UI & Menu** | 234 | 100% | Menu principale, schermate di morte, salvataggio, rarità, messaggi |
| **Parte 2: Impostazioni & Input** | 443 | 100% | Grafica, audio, comandi tastiera/mouse e gamepad, inventario, notifiche |
| **Parte 3: Abilità & Combattimento** | 364 | 100% | Albero abilità (nodi, costellazioni), attributi, magie, effetti attivi |
| **Parte 4: Oggetti, Equipaggiamento & Alchimia** | 289 | 100% | Armi, armature, trofei, ricette, calderone alchemico, descrizioni di lore |
| **Parte 5: Narrazione, Dialoghi & Mondo** | 181 | 100% | Sottotitoli dialoghi (Druido, Topo, Guerriero), missioni, toponimi |
| **TOTALE MASTER** | **1.511** | **100%** | **Nessuna riga lasciata non tradotta o omessa** |

---

## 3. Integrità Tecnica e Validazione Tag

Tutte le stringhe sono state sottoposte a validazione automatica per garantire il rispetto dei token del motore di gioco Unreal Engine 5:
- Tag di formattazione XML: `<PosStat>...</>`, `<NegStat>...</>`, `<cf>`, `<br>`, `<bold>`, `<highlight>`.
- Variabili d'input dinamiche: `<var input="..."/>`.
- Parametri di calcolo dinamici: `{Duration}`, `{DamageValue}`, `{MaxHits}`, `{ValuePerc}`, `{Caster.HealValue}`.
- Nessuna alterazione o corruzione di segnaposto durante il rendering.

---

## 4. Glossario e Convenzioni Principali

1. **Attributi Fondamentali**:
   - `Health` -> *Salute* (o *PV* nei contesti abbreviati)
   - `Stamina` -> *Vigore*
   - `Mana` -> *Mana*
   - `Poise` -> *Equilibrio*
   - `Critical Chance / Multiplier` -> *Probabilità di critico* / *Moltiplicatore critico*

2. **Danni e Resistenze**:
   - `Slash / Pierce / Blunt` -> *Taglio* / *Perforazione* / *Contundente*
   - `Fire / Ice / Lightning / Poison / Wind` -> *Fuoco* / *Gelo* / *Fulmine* / *Veleno* / *Vento*

3. **Alchimia & Consumabili**:
   - `Coating / Vial` -> *Unguento*
   - `Hand Bomb` -> *Bomba a mano*
   - `Alchemy Pot` -> *Calderone alchemico*
   - `Everkin` -> *Eternicino*
   - `Firecap` -> *Cappellofuoco*
   - `Blue Dogbane` -> *Apocino azzurro*

4. **Entità & Fazioni**:
   - `Underdwellers` -> *Popolo del Sottosuolo* / *Sotterranei*
   - `Sundwellers` -> *Abitanti della Luce*
   - `Watchers of Solace` -> *Custodi di Solace*
   - `Darkguards` -> *Guardiani Oscuri*
   - `Haven` -> *Haven* (Toponimo conservato come nome proprio)
