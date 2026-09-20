# Fatekeeper - Traduzione Italiana Completa

[![GitHub release](https://img.shields.io/badge/release-0.1.3--R1-blue.svg)](https://github.com/Sici29/Fatekeeper-Italian-Translation/releases)
[![Translation Coverage](https://img.shields.io/badge/traduzione-100%25-brightgreen.svg)](#)
[![Steam Build](https://img.shields.io/badge/Steam%20Build-0.1.3-orange.svg)](#)
[![Game Engine](https://img.shields.io/badge/Unreal%20Engine-5.6.1-purple.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Offrimi un caffè](https://img.shields.io/badge/Offrimi_un_caff%C3%A8-Sostieni_il_progetto-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000)](https://buymeacoffee.com/sici29)

Traduzione italiana completa, professionale e fedele per l'action RPG dark fantasy **Fatekeeper** (Steam AppID: [2186990](https://store.steampowered.com/app/2186990/Fatekeeper/)).

[☕ **Offrimi un caffè e sostieni le future traduzioni**](https://buymeacoffee.com/sici29)

Progetto sviluppato da **Sici29** e distribuito con installer automatico one-file standalone per Windows (Release **0.1.3-R1** per build Steam **0.1.3**).

---

## 🗡️ Caratteristiche della Traduzione

- **Copertura Totale (100%)**: 1.514 voci tradotte e revisionate.
- **Interfaccia & Menu**: Menu principale, schermate di caricamento, popup di sistema e impostazioni audio/video/comandi interamente localizzati.
- **Impostazioni & Controlli**: Allineamento al 100% di tutti gli hash binari `CityHash64` (`SourceStringHash`) per le descrizioni delle opzioni e i comandi di ripristino.
- **Lore & Oggetti**: Armi, armature, gioielli, pergamene, ingredienti e descrizioni narrative storiche arricchite con terminologia fantasy coerente.
- **Alchimia & Talenti**: Calderone alchemico, elisir, unguenti, bombe e costellazioni di abilità.
- **Dialoghi & Sottotitoli**: Fedeltà narrativa per tutti i personaggi (Druido, Topo Kor Guran, Terul e creature del mondo di gioco).
- **Stabilità Assoluta**: Risolto ogni problema di crash memory access (`0x0000000000000148`), rimosse lingue fantasma e preservato intatto il file base originale di Steam (`pakchunk0-Windows.pak`).

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
   - Gli indici del file `.pak` (*Primary Index*, *Path Hash Index*, *Full Directory Index*) richiedono crittografia **AES-256-ECB** con la chiave di spedizione del gioco (`0x3AB2785AB187B2089737DB4BE249A3C1E885D7ED7F0BBF225B5320B0529A511F`) e il seed di hash dei percorsi `0xBF5F7DEF`.
2. **Registrazione Cultura (`Game.locmeta`)**:
   - Unreal Engine non carica i testi localizzati se la cultura non è esplicitamente dichiarata all'interno del file metadati binario `Game.locmeta`. Sono registrate esattamente le due culture supportate `en` e `it`, garantendo un selettore lingue pulito a 2 opzioni senza duplicati.
3. **Corrispondenza `SourceStringHash` (CityHash64)**:
   - Ogni voce nel file binario `Game.locres` è validata da UE5 tramite il checksum CityHash64 della stringa sorgente. Se il testo originale non coincide esattamente con quello compilato negli asset `.uasset`, il motore rigetta la traduzione. Tutte le 101 discrepanze originali sono state allineate con gli asset di gioco.

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
