# Changelog - Traduzione Italiana di Fatekeeper

Tutte le modifiche rilevanti a questo progetto sono documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/it/1.0.0/) e aderisce al [Semantic Versioning](https://semver.org/).

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
