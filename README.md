# Fatekeeper - Traduzione Italiana Completa

[![GitHub release](https://img.shields.io/badge/release-0.1.4--R1-blue.svg)](https://github.com/Sici29/Fatekeeper-Italian-Translation/releases)
[![Translation Coverage](https://img.shields.io/badge/traduzione-100%25-brightgreen.svg)](#)
[![Steam Build](https://img.shields.io/badge/Steam%20Build-0.1.4-orange.svg)](#)
[![Game Engine](https://img.shields.io/badge/Unreal%20Engine-5.6.1-purple.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Offrimi un caffè](https://img.shields.io/badge/Offrimi_un_caff%C3%A8-Sostieni_il_progetto-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000)](https://buymeacoffee.com/sici29)

<!-- gioca-in-italiano:inizio -->
<p align="center"><a href="https://sici29.github.io/gioca-in-italiano/"><img src="https://sici29.github.io/gioca-in-italiano/img/banner.jpg" alt="Gioca in Italiano: tutte le traduzioni italiane di Sici29 in un'app sola" width="100%"></a></p>

> [!TIP]
> **Tutte le mie traduzioni in un'app sola: [Gioca in Italiano](https://sici29.github.io/gioca-in-italiano/)**
>
> Installa e aggiorna questa traduzione con un clic, ti avvisa quando esce una nuova versione e ti fa scoprire le altre: [Aniimo](https://sici29.github.io/gioca-in-italiano/aniimo/), [Neverness to Everness](https://sici29.github.io/gioca-in-italiano/neverness-to-everness/), [ARK: Survival Ascended](https://sici29.github.io/gioca-in-italiano/ark-survival-ascended/) e [Star Citizen](https://sici29.github.io/gioca-in-italiano/star-citizen/).
>
> **Manca il tuo gioco?** [Proponilo](https://sici29.github.io/gioca-in-italiano/#proponi) e vota quelli proposti dagli altri: i più votati diventano le prossime traduzioni.
>
> **[⬇ Scarica Gioca in Italiano](https://github.com/Sici29/gioca-in-italiano/releases/latest/download/GiocaInItaliano.exe)** · gratis, per Windows 10 e 11
<!-- gioca-in-italiano:fine -->

Traduzione italiana completa, professionale e fedele per l'action RPG dark fantasy **Fatekeeper** (Steam AppID: [2186990](https://store.steampowered.com/app/2186990/Fatekeeper/)).

[☕ **Offrimi un caffè e sostieni le future traduzioni**](https://buymeacoffee.com/sici29)

Progetto sviluppato da **Sici29** e distribuito con installer automatico one-file standalone per Windows (Release **0.1.4-R1** per build Steam **0.1.4** / BuildID `26328649`).

---

## 🗡️ Caratteristiche della Traduzione

- **Copertura Totale (100%)**: 1.795 voci tradotte e revisionate.
- **Scheda Attributi Dettagliata**: Localizzazione integrale di tutti i parametri del personaggio (`ST_AttributeUI`, 184 voci): resistenze elementali, penetrazioni al danno, tempi di recupero e regressione stati alterati, finestre di parata e deviazione, parametri telecinesi ed efficienza alchemica.
- **Interfaccia & Menu**: Menu principale, schermate di caricamento con approfondimenti di lore, popup di sistema e impostazioni audio/video/comandi interamente localizzati.
- **Supporto Controller Esteso**: Traduzione dei nuovi profili di layout per gamepad (PlayStation, Xbox, Steam) e controllo luminosità HDR.
- **Lore & Oggetti**: Armi, armature, amuleti, chiavi, ingredienti e descrizioni narrative storiche (Mar Guran, il Portale Lunare, le Gallerie di Trasporto) arricchite con terminologia fantasy coerente.
- **Alchimia & Talenti**: Calderone alchemico, elisir, unguenti, granate, modificatori procedurali e costellazioni di abilità.
- **Dialoghi & Sottotitoli**: Fedeltà narrativa per tutti i personaggi (Kor Tenarim, Kor Maretan, Terul, Chukran, Vekran Xulratan).
- **Stabilità Assoluta**: Piena compatibilità con l'update 0.1.4, preservato intatto il file base originale di Steam (`pakchunk0-Windows.pak`, 90.088.270 byte).

---

## 📦 Installazione Rapida (Per i Giocatori)

### Metodo 1: Installer Automatico (Consigliato)
1. Scarica l'ultima versione di **`Fatekeeper-Italian-Translation.exe`** dalla sezione [Releases](https://github.com/Sici29/Fatekeeper-Italian-Translation/releases).
2. Chiudi il gioco se in esecuzione ed avvia l'eseguibile.
3. Seleziona **`[1] Installa Traduzione Italiana`**. L'installer rileverà automaticamente la cartella di Fatekeeper nelle tue librerie Steam, effettuerà un backup di sicurezza ed installerà la patch.
4. Avvia **Fatekeeper** da Steam e goditi il gioco in italiano!

### Metodo 2: Script Batch
Se preferisci usare gli script inclusi nel pacchetto release:
- Fai doppio clic su `Installa_Traduzione_Italiana.bat`.
- Per verificare l'integrità dei file in qualsiasi momento, avvia `Controlla_Integrita.bat`.
- Per disinstallare la traduzione e tornare ai file originali di Steam al 100%, avvia `Ripristina_Originale.bat`.

---

## 🛠️ Architettura Tecnica & Modding Unreal Engine 5

In Fatekeeper (basato su Unreal Engine 5.6.1 Shipping), l'engine ignora i `.pak` di modding classici se non rispettano determinati requisiti tecnici:

1. **Cifratura Indici UE V11**:
   - Gli indici del file `.pak` (*Primary Index*, *Path Hash Index*, *Full Directory Index*) richiedono crittografia **AES-256-ECB** con la chiave di spedizione del gioco (`0x3AB2785AB187B2089737DB4BE249A3C1E885D7ED7F0BBF225B5320B0529A511F`) e il seed di hash dei percorsi `0xC623D5C0` (3324237248).
2. **Registrazione Cultura (`Game.locmeta`)**:
   - Unreal Engine non carica i testi localizzati se la cultura non è esplicitamente dichiarata all'interno del file metadati binario `Game.locmeta`. Con la build 0.1.4, `Game.locmeta` include la cultura `it` registrata insieme alle culture ufficiali native (`de-DE`, `en`, `fr`, `ru`, `uk`, `zh-Hans`).
3. **Corrispondenza `SourceStringHash` (CityHash64)**:
   - Ogni voce nel file binario `Game.locres` è validata da UE5 tramite il checksum CityHash64 della stringa sorgente. Tutte le 1.795 stringhe sono allineate al 100% con gli asset di gioco aggiornati.

---

## 📂 Struttura della Repository

```text
├── assets/                             # Icone e risorse visive per l'installer
├── data/                               # Dataset completi della traduzione (CSV, JSON)
│   ├── master_strings.json             # Stringhe originali estratte
│   ├── master_translated.json          # Testi tradotti e revisionati
│   └── translation_master.csv          # Tabella completa di allineamento
├── docs/                               # Documentazione di revisione e stile
│   ├── QUALITY_AUDIT.md                # Report di qualità e fedeltà stilistica
│   └── TERMINOLOGY.md                  # Glossario terminologico ufficiale
├── payload/                            # File compilati inclusi nell'installer
│   ├── Game.locmeta                    # Metadati culture (en, it)
│   ├── Game.locres                     # File binario CityHash64 tradotto
│   ├── pakchunk0-Windows_P.pak         # Patch Pak V11 cifrata AES-256-ECB
│   └── SLASHER.uproject                # Descrittore progetto UE
├── tools/
│   └── fatekeeper_it_installer.py      # Codice sorgente completo dell'installer
├── Fatekeeper-Italian-Translation.spec  # Specifica di compilazione PyInstaller
├── Installa_Traduzione_Italiana.bat    # Launcher rapido installazione
├── Controlla_Integrita.bat             # Launcher verifica crittografica
├── Ripristina_Originale.bat            # Launcher disinstallazione pulita
├── CHANGELOG.md                        # Storico dettagliato di tutte le versioni
├── LICENSE                             # Licenza MIT
└── README.md                           # Questa guida
```

---

## 💻 Compilazione da Sorgenti

Per compilare l'eseguibile autonomo `Fatekeeper-Italian-Translation.exe` partendo dai sorgenti:

```bash
# Installa PyInstaller se non presente
pip install pyinstaller

# Compila l'eseguibile one-file con icona e payload incorporati
pyinstaller --clean Fatekeeper-Italian-Translation.spec
```

L'eseguibile generato sarà disponibile nella cartella `dist/`.

---

## 📜 Licenza e Note

- Questo progetto è una localizzazione non ufficiale creata dalla community per i giocatori italiani.
- I diritti del gioco, dei marchi e degli asset originali appartengono ai rispettivi sviluppatori e publisher di **Fatekeeper**.
- Il codice dell'installer e gli script ausiliari sono rilasciati sotto licenza [MIT](LICENSE).
