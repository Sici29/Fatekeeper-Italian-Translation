# Changelog - Traduzione Italiana di Fatekeeper

Tutte le modifiche rilevanti a questo progetto sono documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/it/1.0.0/) e aderisce al [Semantic Versioning](https://semver.org/).

---

## [1.3.0] - 31/10/2026

### Aggiornamento di Compatibilità (Build Steam v0.1.4 / BuildID 26328649)
- **Database Tradotto Espanso a 1.795 Voci (100% dell'intero gioco)**:
  - **301 Nuove Voci Aggiunte**:
    - Scheda attributi e parametri avanzati del personaggio (`ST_AttributeUI`, 184 stringhe): penetrazioni elementali e fisiche, resistenze al danno, tempi di recupero e regressione alterazioni di stato, deviazione, respinta, efficienza calderone alchemico e consumabili.
    - Nuovi oggetti ed equipaggiamento (Runa dell'abisso, Quercia antica, Bastone dell'arcanista, Chiave del cortile, Chiave di rame decorata, Leviatano, Amuleto poliedrico, ecc.).
    - Modificatori procedurali (`ST_GeneratedModifiers`) per armi, magie e attacchi disarmati.
    - Nuove impostazioni per controller (profili layout PlayStation, Xbox, Steam) e calibrazione luminosità HDR.
    - Schermate di caricamento e approfondimenti storici di lore (`ST_LoadingScreen`) su Mar Guran, le Gallerie di Trasporto e i Custodi di Solace.
    - Nuovi messaggi d'interazione e tutorial per la telecinesi e l'alchimia.
  - **124 Voci Aggiornate e Riallineate**:
    - Riconciliazione totale degli hash binari `CityHash64` con gli asset UE5 della patch 0.1.4.
    - Testi delle descrizioni alchemiche e delle armature allineati alle versioni estese introdotte dagli sviluppatori.
    - Denominazioni canoniche dei personaggi e nemici allineate (Kor Maretan, Chukran, Vekran Xulratan, Guerriero degli Abitanti della Luce).
- **Adeguamento Architettura Tecnica Unreal Engine 5.6.1**:
  - File base di Steam `pakchunk0-Windows.pak` aggiornato alla dimensione ufficiale di 90.088.270 byte.
  - Seed di hash dei percorsi aggiornato a `0xC623D5C0` (3324237248).
  - File metadati `Game.locmeta` (v2) aggiornato con inclusione ufficiale della cultura `it`.
  - Cifratura indici AES-256-ECB V11 applicata al nuovo archivio patch `pakchunk0-Windows_P.pak`.
- **Nuovo Installer Autonomo One-File v1.3.0**:
  - Ricompilato `Fatekeeper-Italian-Translation.exe` con i nuovi payload e verifica crittografica SHA-256 aggiornata.
  - Backup automatico ad alta affidabilità del nuovo file base originale.

---

## [0.1.3-R1] - 20/09/2026

### Prima Release Ufficiale (Build Steam 0.1.3)
- **Localizzazione integrale al 100% dell'intero gioco (1.514 voci uniche)**:
  - Menu principale, schermate di caricamento, popup di sistema e impostazioni audio/video/comandi.
  - Albero completo delle abilità, costellazioni di talenti, alchimia, lore, armi, armature, descrizioni e dialoghi sottotitolati.
  - Allineamento al 100% di tutti gli hash binari `CityHash64` (`SourceStringHash`) con gli asset `.uasset` di gioco.
- **Configurazione di Localizzazione Nativa UE5**:
  - Registrata la cultura in `Game.locmeta` (67 byte, culture supportate: `en`, `Italiano`) e mappature trasparenti `it` / `it-IT` in `DefaultGame.ini`.
  - Sincronizzazione atomica del database tradotto per garantire la visualizzazione immediata in lingua italiana dal primo avvio.
  - Normalizzazione automatica delle impostazioni utente (`GameSettings.json`) per prevenire conflitti o blocchi dopo i filmati introduttivi.
- **Stabilità e Sicurezza**:
  - File base originale di Steam `pakchunk0-Windows.pak` (29.988.335 byte) preservato intatto al 100%.
  - Patch pacchettizzata in formato UE V11 (`pakchunk0-Windows_P.pak`) cifrata con chiave nativa AES-256-ECB.
- **Installer Autonomo One-File**:
  - Rilasciato `Fatekeeper-Italian-Translation.exe` (7.8 MB) con rilevamento automatico della libreria Steam, backup di sicurezza e ripristino 100% pulito.
  - Script ausiliari inclusi: `Installa_Traduzione_Italiana.bat`, `Controlla_Integrita.bat`, `Ripristina_Originale.bat`.
