# Cavalaire App

Web-App für das Ferienhaus in Cavalaire-sur-Mer: eine animierte Startseite plus drei Unterseiten (Cavalaire-Reiseführer, Maison, Belegungsplan). Läuft unabhängig von Claude als eigenständige Webseite (GitHub + Hostinger) und speichert Buchungsdaten in einer eigenen Supabase-Datenbank.

## Seitenstruktur

- **`index.html`** – Startseite mit Animation (Seestern, Haus, Kalender), Live-Wetterdaten und drei Links zu den Unterseiten
- **`cavalaire.html`** – Reiseführer: Strände (mit Fotos & offizieller Strandkarte), Wassersport, Wandern & Radfahren, Essen & Trinken, Notrufnummern, 360°-Rundblick vom Aussichtspunkt
- **`maison.html`** – Infos rund ums Haus – **noch größtenteils im Aufbau**, bisher nur 360°-Rundblick von der Terrasse enthalten
- **`belegung.html`** – der Belegungsplan (Kalender, Buchungsanfragen, Admin-Bereich)

Der Home-Button (oben rechts, auf jeder Unterseite fixiert/immer sichtbar beim Scrollen) führt immer zurück zur Startseite (`index.html`). Auf `belegung.html` ist zusätzlich das Zahnrad-Symbol (Admin-Zugang) vorhanden, das normal mit der Seite mitscrollt.

Die Start-Animation läuft nur beim ersten Öffnen einer Sitzung; kommt man von einer Unterseite zurück, erscheint sofort der fertige Zustand (per `sessionStorage`-Merker).

## Funktionen (Belegungsplan / `belegung.html`)

- **Kalenderansicht** (Monat/Jahr umschaltbar; in der Jahresansicht auf einen Monat tippen, um direkt in die Monatsansicht zu springen)
- **Zeitraum-Auswahl direkt im Kalender**: Antippen von Anreise- und Abreisetag direkt auf den Kalenderkacheln
- **Buchungsanfrage-Formular**: Jeder mit dem Link kann einen Zeitraum anfragen (Name, Kategorie, Notiz)
- **Freigabe-Workflow**: Neue Anfragen erscheinen zunächst als "ausstehend" und werden erst nach Bestätigung im Kalender sichtbar
- **Admin-Bereich** (Zahnrad-Symbol, PIN-geschützt): Anfragen bestätigen/ablehnen, bestehende Buchungen bearbeiten oder löschen. Erneuter Klick auf das Zahnrad sperrt den Bereich wieder
- **Öffentlicher Hinweis**: Anzahl offener Anfragen ist für alle sichtbar (ohne Namen/Datum)
- **Zwei Status-Kacheln**: "Heute" (inkl. vollständig ausgeschriebenem Datum, z. B. "Heute · Mittwoch, 12. August 2026") und "Anreise" – beide im Salbeiton `#A9BFB7` mit dunklem Text
- **Installierbar als App** (PWA): "Zum Home-Bildschirm hinzufügen" auf dem Smartphone möglich
- **Sofort sichtbar**: Kalender-Gerüst rendert direkt beim Laden, Buchungen werden nachträglich eingeblendet (kein blockierender Ladebildschirm mehr)

Hinweis: Wetterdaten (Luft/Wasser) werden **nicht mehr** auf `belegung.html` angezeigt – die sind jetzt auf der Startseite (`index.html`).

## Funktionen (Startseite / `index.html`)

- Live-Wetterdaten von Open-Meteo, links übereinander angeordnet: Lufttemperatur oben (auf Höhe des Glow-Hintergrunds), Luftfeuchtigkeit mittig, Wassertemperatur unten in den Wellen
- Drei animierte Symbole (Seestern/Cavalaire, Haus/Maison, Kalender/Belegung) verlinken zu den Unterseiten

## Funktionen (Cavalaire-Reiseführer / `cavalaire.html`)

- Hero-Header mit Frankreich-Umriss, Seestern-Ortsmarke bei Cavalaire und Gezeiten-Wellen-Illustration
- **Strände**: alle 5 Strände mit französischen Namen (Plage du Centre-Ville, Plage du Parc, Plage des Dauphins, Plage de Pardigon, Plage de Bonporteau), aufklappbare Foto-Karten, eingebettete offizielle Strandkarte (verlinkt zum PDF)
- **Wassersport, Wandern & Radfahren, Essen & Trinken**: Infos von der offiziellen Tourismusseite (cavalairesurmer.fr)
- **Notrufnummern**: 112, Feuerwehr, SAMU, Gendarmerie, Stadtpolizei, Zahnnotdienst, Giftnotruf, Tourismusbüro
- **360°-Rundblick** vom Aussichtspunkt über die Bucht (Photo Sphere Viewer, Kachel-Technik für scharfes Reinzoomen)

## 360°-Panoramafotos

Fotos werden mit einer Insta360 X4 Air aufgenommen und in Insta360 Studio als **"360 Photo" / Equirectangular** (nicht "Reframed"!) im 2:1-Seitenverhältnis exportiert. Wichtig: Bei hochauflösenden Panoramen (~7000+ Pixel breit) zeigt eine einzelne Bilddatei im Viewer beim Reinzoomen deutliche Unschärfe – das liegt an einer WebGL-Textur-Beschränkung, nicht an der Bildqualität selbst.

**Lösung**: Jedes Panorama wird in ein 8×4-Raster (32 Kacheln à 960×960px) zerlegt; der Viewer lädt dann nur die gerade sichtbaren Kacheln in voller Auflösung nach (wie bei digitalen Kartendiensten). Verwendete Bibliothek: **Photo Sphere Viewer Version 5** (ESM/Import-Map, siehe `<script type="importmap">` in `cavalaire.html`/`maison.html`) mit dem `EquirectangularTilesAdapter`.

- `assets/tiles/aussicht_{spalte}_{zeile}.jpg` (0–7 / 0–3) + `assets/aussicht-360-low.jpg` (Vorschaubild) → Cavalaire-Seite
- `assets/tiles/terrasse_{spalte}_{zeile}.jpg` (0–7 / 0–3) + `assets/terrasse-360-low.jpg` (Vorschaubild) → Maison-Seite

Neues Panorama hinzufügen: Originalfoto (2:1, möglichst hochauflösend) hochladen, ich zerlege es in Kacheln und baue den Viewer-Block ein.

## Design

**Alle Unterseiten** (`index.html`, `cavalaire.html`, `maison.html`, `belegung.html`) nutzen inzwischen dieselbe Design-Sprache ("Cavalaire Design System"): warmes Creme (`#F5EFE3`) als Hintergrund, dunkles Petrol (`#123A4E`) als Textfarbe, Türkis-Verlauf (`#63BDB2`/`#2F8F86` → `#2A6A7E`) als Akzent, Koralle (`#D97748`) für Notrufe/Warnungen, Gold (`#E3A857`) als Highlight. Schriften: **Fraunces** (Überschriften), **Inter** (Fließtext), **IBM Plex Mono** (kleine Beschriftungen/Zahlen).

Die Designs wurden über **Claude Design** (claude.ai/design) entworfen und hier im Chat in eigenständige, direkt lauffähige HTML-Dateien integriert (kein Build-Schritt nötig).

## Technischer Aufbau

| Teil | Technologie |
|---|---|
| Startseite, Cavalaire, Maison | reines HTML/CSS + SVG-Animationen (kein React) |
| Belegungsplan-Oberfläche | React (über CDN, vorkompiliert zu reinem JavaScript) |
| 360°-Viewer | Photo Sphere Viewer 5 (ESM via Import-Map) + Kachel-Technik |
| Styling | Eigenes CSS je Seite |
| Datenbank | Supabase (Projekt `belegungsplan-cavalaire`, Region eu-central-1/Frankfurt) |
| Hosting | GitHub-Repository → Hostinger (Node.js-Deployment) |

### Dateien in diesem Ordner

- `index.html`, `cavalaire.html`, `maison.html`, `belegung.html` – die vier Seiten
- `manifest.json` – Konfiguration für "Installieren als App"
- `icon-192-v2.png` / `icon-512-v2.png` – App-Icon (Seestern-Logo)
- `assets/` – Fotos und Panorama-Kacheln (siehe unten)
- `package.json` / `server.js` – Node.js-Server für Hostinger (liefert automatisch jede angefragte Datei aus, mit Fallback auf `index.html` bei unbekannten Pfaden)

### Inhalt von `assets/`

```
assets/
├── plage-centre-ville.jpg       (Strandfoto)
├── plage-parc.jpg               (Strandfoto)
├── plage-dauphin.jpg            (Strandfoto)
├── plage-pardigon.jpg           (Strandfoto)
├── plage-bonporteau.jpg         (Strandfoto)
├── strand-karte.jpg             (offizielle Strandkarte, aus PDF)
├── aussicht-360-low.jpg         (Panorama-Vorschau, Cavalaire-Seite)
├── terrasse-360-low.jpg         (Panorama-Vorschau, Maison-Seite)
└── tiles/
    ├── aussicht_0_0.jpg … aussicht_7_3.jpg     (32 Kacheln, Cavalaire)
    └── terrasse_0_0.jpg … terrasse_7_3.jpg     (32 Kacheln, Maison)
```

**Wichtig beim Hochladen von Kachel-Zips**: Die Ordnerstruktur `assets/tiles/` muss erhalten bleiben – nicht die Dateien direkt in `assets/` legen, sonst findet der Viewer sie nicht (führt zu gelben Warndreiecken statt Bild).

## Datenbank (Supabase)

- **Projekt-ID**: `rtfpduqyrarktmxaiise`
- **Tabelle**: `bookings` (Spalten: `id`, `guest_name`, `category`, `start_date`, `end_date`, `notes`, `status`, `created_at`)
- **Status**: `pending` (Anfrage, noch nicht bestätigt) oder `confirmed` (sichtbar im Kalender)
- **Zugriff**: über den öffentlichen "anon"-Schlüssel, der direkt im Code von `belegung.html` steht (siehe `SUPABASE_URL` / `SUPABASE_ANON_KEY`)

### Datenbank-Funktionen (RPC)

- `pending_count()` – öffentlich, gibt nur die Anzahl offener Anfragen zurück
- `owner_list_all(pin)` – listet alle Buchungen inkl. ausstehender Anfragen
- `owner_confirm_booking(booking_id, pin)` – bestätigt eine Anfrage
- `owner_update_booking(booking_id, pin, p_guest_name, p_category, p_start_date, p_end_date, p_notes)` – bearbeitet eine bestehende Buchung
- `owner_delete_booking(booking_id, pin)` – löscht eine Buchung

**PIN**: bewusst nicht hier dokumentiert – dieses Repository ist öffentlich. Der PIN liegt im Passwortmanager; geändert wird er in den Supabase-Funktionen `owner_*`.

## Etwas ändern lassen

Neuen Chat mit Claude starten und hochladen:

1. Dieses `README.md`
2. Die betroffene(n) Seite(n)

Nach jeder Änderung: Datei(en) bei GitHub hochladen → bei Hostinger redeployen → App auf dem Smartphone komplett schließen und neu öffnen.

## Bekannte Einschränkungen

- Der PIN wird im Klartext in einer Datenbankfunktion verglichen – ausreichend für einen privaten Familienkalender, kein Hochsicherheitsstandard
- Wetterdaten stammen von Open-Meteo (Modellschätzung, keine Live-Messung vor Ort); bei Meereshitzewellen können reale Werte deutlich vom saisonalen Durchschnitt abweichen
- `cavalaire.html`-Strandfotos: Das Centre-Ville-Foto trägt ein fremdes Wasserzeichen ("Cavalaire ProvenceWeb") – für private Nutzung unproblematisch, bei öffentlichem Teilen ggf. ersetzen
- `maison.html` ist inhaltlich noch nicht ausgebaut (nur 360°-Rundblick vorhanden)
- Browser-Zoom in 360°-Panoramen ohne Kachel-Technik ist grundsätzlich unscharf (WebGL-Textur-Limit) – deshalb nutzen beide Panoramen die Kachel-Lösung
