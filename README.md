# Cavalaire App

Web-App für das Ferienhaus in Cavalaire-sur-Mer: eine animierte Startseite, drei Unterseiten (Cavalaire-Reiseführer, Maison, Belegungsplan) und Geräte-Anleitungen. Läuft unabhängig von Claude als eigenständige Webseite (GitHub + Hostinger) und speichert Buchungsdaten in einer eigenen Supabase-Datenbank.

Diese Datei beschreibt **was** die App ist und wie sie aufgebaut ist. Wie in diesem Repo gearbeitet wird und welche Entscheidungen bewusst so getroffen wurden, steht in `CLAUDE.md` – bitte beides lesen.

## Seitenstruktur

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Animation (Seestern, Haus, Kalender), Live-Wetter, drei Links |
| `cavalaire.html` | Reiseführer: Strände, Wassersport, Touren, Essen, Notrufnummern, 360°-Rundblick |
| `maison.html` | Rund ums Haus: Ankunft, Internet, Geräte, Müll, Abreise, Kontakte, 360°-Rundblick |
| `belegung.html` | Belegungsplan: Kalender, Buchungsanfragen, Admin-Bereich |
| `ofen.html` | Kurzanleitung für den Ofen, verlinkt aus dem Geräte-Abschnitt |

**Navigation:** Auf jeder Unterseite sitzt oben rechts ein fest positionierter Home-Button (44 × 44 px, bei `right: 20px`), der beim Scrollen stehen bleibt und zur Startseite führt. Auf `ofen.html` steht links daneben zusätzlich ein Zurück-Pfeil nach `maison.html`; der Home-Button behält dabei seine Position, damit er beim Seitenwechsel nicht springt. Auf `belegung.html` gibt es zusätzlich das Zahnrad für den Admin-Bereich.

Die Start-Animation läuft nur beim ersten Öffnen einer Sitzung; kommt man von einer Unterseite zurück, erscheint sofort der fertige Zustand (`sessionStorage`-Merker).

## Funktionen (Belegungsplan / `belegung.html`)

- **Kalenderansicht**, Monat und Jahr umschaltbar; in der Jahresansicht auf einen Monat tippen springt in die Monatsansicht
- **Zeitraum-Auswahl direkt im Kalender** durch Antippen von Anreise- und Abreisetag
- **Buchungsanfrage-Formular**: Name, Kategorie, Notiz – jeder mit dem Link kann anfragen
- **Freigabe-Workflow**: Anfragen erscheinen als `pending` und werden erst nach Bestätigung im Kalender sichtbar
- **Admin-Bereich** (Zahnrad, PIN-geschützt): bestätigen, ablehnen, bearbeiten, löschen. Erneuter Klick sperrt wieder
- **Öffentlicher Hinweis** auf die Anzahl offener Anfragen, ohne Namen und Daten
- **Zwei Status-Kacheln** "Heute" und "Anreise" im Salbeiton `#A9BFB7`
- **Installierbar als App** (PWA)
- **Sofort sichtbar**: Kalendergerüst rendert beim Laden, Buchungen werden nachgeladen

Wetterdaten stehen **nicht** hier, sondern auf der Startseite.

## Funktionen (Startseite / `index.html`)

Live-Wetter von Open-Meteo, links übereinander: Lufttemperatur oben, Luftfeuchtigkeit mittig, Wassertemperatur unten in den Wellen. Drei animierte Symbole verlinken auf die Unterseiten.

## Funktionen (Maison / `maison.html`)

Sieben Abschnitte in einheitlichem Aufbau: Icon 64 × 64 px links, Überschrift in Fraunces 1.9rem daneben, darunter eine Kachel mit dem Inhalt. Reihenfolge folgt dem Aufenthalt.

| Abschnitt | Stand |
|---|---|
| Ankunft | Platzhalter |
| Internet | Hinweis, dass die WLAN-Daten nach bestätigter Buchung persönlich mitgeteilt werden, plus Link zum Belegungsplan |
| Geräte | Link auf `ofen.html`; Heizung, Klimaanlage, Waschmaschine fehlen noch |
| Müll | Platzhalter |
| Abreise | Platzhalter |
| Kontakte | `cavalaire-sur-mer@gmx.de` als `mailto`-Link; Ansprechpartner vor Ort fehlen noch |
| 360°-Eindrücke | Rundblick von der Terrasse |

## Funktionen (Cavalaire-Reiseführer / `cavalaire.html`)

Hero-Header mit Frankreich-Umriss und Seestern-Ortsmarke. Sechs Rubriken: Strände (alle fünf mit aufklappbaren Fotokarten und eingebetteter offizieller Strandkarte), Wassersport, Wandern & Radfahren, Essen & Trinken, Notrufnummern, 360°-Rundblick vom Aussichtspunkt.

## 360°-Panoramafotos

Aufgenommen mit einer Insta360 X4 Air, exportiert in Insta360 Studio als **"360 Photo" / Equirectangular** (nicht "Reframed") im Seitenverhältnis 2:1.

Bei hochauflösenden Panoramen (~7000+ px breit) wird eine einzelne Bilddatei im Viewer beim Zoomen unscharf – das ist eine WebGL-Textur-Beschränkung, kein Qualitätsproblem der Datei. **Lösung:** Jedes Panorama wird in ein 8 × 4-Raster aus 32 Kacheln à 960 × 960 px zerlegt; der Viewer lädt nur die sichtbaren Kacheln nach. Bibliothek: **Photo Sphere Viewer 5** (ESM über Import-Map) mit dem `EquirectangularTilesAdapter`, konfiguriert mit `width: 7680, cols: 8, rows: 4`.

- `assets/tiles/aussicht_{spalte}_{zeile}.jpg` (0–7 / 0–3) + `assets/aussicht-360-low.jpg` → Cavalaire-Seite
- `assets/tiles/terrasse_{spalte}_{zeile}.jpg` (0–7 / 0–3) + `assets/terrasse-360-low.jpg` → Maison-Seite

Neues Panorama: Originalfoto hochladen, Claude zerlegt es in Kacheln und baut den Viewer-Block ein.

## Eigene Grafiken

Statt Fotos aus Herstelleranleitungen sind mehrere Abbildungen als SVG nachgezeichnet – scharf auf jedem Display, wenige Kilobyte, in den Farben der Seite.

| Grafik | Wo |
|---|---|
| Bedienfeld des Ofens mit den Marken A–G | direkt in `ofen.html` |
| Fernbedienung Sony RMT-TX102D | `assets/fernbedienung.svg` |
| TV-Eingangsmenü, SATELIT ausgewählt | `assets/tv-eingaenge-satelit.svg` |
| TV-Eingangsmenü, HDMI 1 / ARC ausgewählt | `assets/tv-eingaenge-hdmi.svg` |

`tools/fernbedienung.py` erzeugt die Fernbedienung und kann dabei **einzelne Tasten hervorheben** – gedacht für eine Fernseher-Anleitung mit einer Zeichnung pro Schritt:

```
python3 tools/fernbedienung.py assets/ziel.svg input ok home
```

Hervorhebbare Tasten – alle 37 sind geprüft: `input oval power digital sync ok hoch runter links rechts home info nx jump mute audio sub title vol+ vol- prog+ prog-`, die Zifferntasten `k1`…`k9 k0 kEXIT kTXT` und die Wiedergabetasten `pbrew pbplay pbff pbprev pbpause pbnext pbrec pbstop pbgrid`. Hervorgehobene Tasten werden petrolfarben gefüllt, ihre Beschriftung cremefarben; `home` wird salbeigrün, `power` türkis.

Die Zeichnung bildet **die tatsächlich vorhandene Fernbedienung** ab, einen Nachbau mit weißer `NX`-Taste. Die Original-Sony-Fernbedienung hat an dieser Stelle eine rote NETFLIX-Taste – Abbildungen aus Sonys Anleitung passen also nicht zum Gerät im Haus.

Das einzige verbliebene Foto in einer Anleitung ist `assets/ofen-knoepfe.png` (Knopf drücken und drehen).

## Design

Alle Seiten nutzen dieselbe Design-Sprache ("Cavalaire Design System"):

| Rolle | Farbe |
|---|---|
| Hintergrund | `#F5EFE3` warmes Creme |
| Kacheln | `#FFFDF9`, oft mit Verlauf nach `#FAF2E4` |
| Text und Linien | `#123A4E` dunkles Petrol |
| Akzent | Türkis-Verlauf `#63BDB2` → `#2A6A7E` |
| Rahmen und Trennlinien | `#E7DFCF` Sand |
| Warnung, Notruf | `#D97748` Koralle |
| Highlight | `#E3A857` Gold |
| Status-Kacheln | `#A9BFB7` Salbei |

Schriften: **Fraunces** (Überschriften), **Inter** (Fließtext), **IBM Plex Mono** (kleine Beschriftungen und Zahlen).

Entworfen über **Claude Design** (claude.ai/design), dann im Chat in eigenständige, direkt lauffähige HTML-Dateien integriert – kein Build-Schritt.

## Technischer Aufbau

| Teil | Technologie |
|---|---|
| Startseite, Cavalaire, Maison, Ofen | reines HTML/CSS + SVG (kein React) |
| Belegungsplan | React über CDN, vorkompiliert zu reinem JavaScript |
| 360°-Viewer | Photo Sphere Viewer 5 (ESM via Import-Map) + Kachel-Technik |
| Styling | eigenes CSS je Seite, keine Framework-Abhängigkeit |
| Datenbank | Supabase (Projekt `belegungsplan-cavalaire`, eu-central-1) |
| Hosting | GitHub → Hostinger, Node.js 18 |

### Dateien

```
index.html  cavalaire.html  maison.html  belegung.html  ofen.html
manifest.json                 PWA-Konfiguration
icon-192-v2.png / -512-v2.png App-Icon (Seestern)
package.json / server.js      Node.js-Server für Hostinger
README.md                     diese Datei
CLAUDE.md                     Arbeitsweise und getroffene Entscheidungen
tools/fernbedienung.py        Generator für die Fernbedienungs-Grafik
assets/                       Fotos, Panorama-Kacheln, SVG-Grafiken
```

`server.js` ist ein einfacher Dateiserver ohne Anwendungslogik. Er liefert jede angefragte Datei aus, mit zwei Ausnahmen: Pfade außerhalb des Ordners werden mit 403 abgelehnt, und **`.md`-Dateien werden mit 404 beantwortet** – Dokumentation gehört nicht auf die öffentliche Webseite. Unbekannte Pfade fallen auf `index.html` zurück.

### Inhalt von `assets/`

```
plage-centre-ville.jpg  plage-parc.jpg  plage-dauphin.jpg
plage-pardigon.jpg      plage-bonporteau.jpg   (Strandfotos)
strand-karte.jpg                               (offizielle Strandkarte)
aussicht-360-low.jpg    terrasse-360-low.jpg   (Panorama-Vorschauen)
aussicht-360.jpg        terrasse-360.jpg
terrasse-360-v2.jpg     terrasse-360-v3.jpg    (Originale, siehe CLAUDE.md)
ofen-knoepfe.png                               (Zeichnung aus der Ofenanleitung)
fernbedienung.svg                              (nachgezeichnet)
tv-eingaenge-satelit.svg  tv-eingaenge-hdmi.svg (nachgezeichnet)
tiles/
  aussicht_0_0.jpg … aussicht_7_3.jpg          (32 Kacheln, Cavalaire)
  terrasse_0_0.jpg … terrasse_7_3.jpg          (32 Kacheln, Maison)
```

**Beim Hochladen von Kachel-Zips**: Die Struktur `assets/tiles/` muss erhalten bleiben – liegen die Dateien direkt in `assets/`, findet der Viewer sie nicht und zeigt gelbe Warndreiecke.

**Bilder an Claude schicken**: PNG und JPG werden von der Chat-Oberfläche als Bild eingebettet, nicht als Datei – Claude sieht sie dann, kann sie aber nicht ins Repo legen. **Bilddateien deshalb in ein ZIP packen und das anhängen**; ZIPs kommen als Datei an.

## Datenbank (Supabase)

- **Projekt-ID**: `rtfpduqyrarktmxaiise`
- **Tabelle**: `public.bookings` mit `id`, `guest_name`, `category`, `start_date`, `end_date`, `notes`, `created_at`, `status`
- **Status**: `pending` (angefragt) oder `confirmed` (im Kalender sichtbar)
- **Zugriff** über den öffentlichen Anon-Key, der im Quelltext von `belegung.html` steht. Das ist so vorgesehen: Der Key ist öffentlich, geschützt wird über Row Level Security

### Rechte

RLS ist aktiv. Zwei Policies:

- `Public read confirmed only` – `anon` sieht nur Zeilen mit `status = 'confirmed'`
- `Public insert as pending only` – `anon` darf nur mit `status = 'pending'` einfügen

Zusätzlich sind die **Tabellenrechte bewusst eng gesetzt** (Supabase vergibt hier standardmäßig alles):

| Rolle | Recht | Spalten |
|---|---|---|
| `anon`, `authenticated` | SELECT | die acht vorhandenen, namentlich benannt |
| `anon`, `authenticated` | INSERT | `guest_name`, `category`, `start_date`, `end_date`, `notes` |

UPDATE, DELETE, TRUNCATE, TRIGGER und REFERENCES sind entzogen. Alle Schreibvorgänge laufen über die `owner_*`-Funktionen, die als `SECURITY DEFINER` unabhängig von diesen Rechten arbeiten.

Weil die Leserechte namentlich vergeben sind, ist **eine später ergänzte Spalte nicht automatisch öffentlich lesbar** – sie muss einzeln freigegeben werden. Passend dazu fragt `belegung.html` einzelne Spalten ab statt `select=*`; ein `select=*` würde brechen, sobald eine nicht freigegebene Spalte existiert.

### Datenbank-Funktionen (RPC)

| Funktion | Zweck |
|---|---|
| `pending_count()` | öffentlich, gibt nur die Anzahl offener Anfragen zurück |
| `owner_list_all(pin)` | alle Buchungen inklusive offener Anfragen |
| `owner_confirm_booking(booking_id, pin)` | Anfrage bestätigen |
| `owner_update_booking(booking_id, pin, p_guest_name, p_category, p_start_date, p_end_date, p_notes)` | Buchung bearbeiten |
| `owner_delete_booking(booking_id, pin)` | Buchung löschen |

Der PIN steht bewusst nicht in dieser Datei – siehe `CLAUDE.md`.

## Deployment

`main` ist der Live-Branch. Hostinger ist mit GitHub verbunden, "Automatische Bereitstellung" ist aktiv: Jeder Push auf `main` ist nach etwa 3–5 Minuten unter `lavender-scorpion-500637.hostingersite.com` erreichbar. Pushes auf andere Branches lösen nichts aus.

Nach jedem Deployment die PWA auf dem Smartphone **komplett schließen und neu öffnen**, sonst bleibt der alte Stand im Cache.

## Bekannte Einschränkungen

- Der PIN wird im Klartext in einer Datenbankfunktion verglichen – ausreichend für einen privaten Familienkalender, kein Hochsicherheitsstandard
- Der PIN stand vom 17. bis 26. August 2026 in dieser Datei auf `main` und ist daher in der Commit-Historie weiterhin auffindbar
- Die Seite ist über Zertifikats-Transparenz-Protokolle auffindbar, auch ohne Verlinkung. "Nur an Familie weitergeben" macht sie nicht privat
- Wetterdaten von Open-Meteo sind Modellschätzung, keine Messung vor Ort
- Das Centre-Ville-Strandfoto trägt ein fremdes Wasserzeichen ("Cavalaire ProvenceWeb")
- `maison.html` ist inhaltlich erst zum Teil ausgebaut: Ankunft, Müll und Abreise sind Platzhalter
- Eine Fernseher-Anleitung ist vorbereitet (Grafiken liegen bereit), aber noch nicht geschrieben
- Es gibt keine eigene Domain; die `hostingersite.com`-Adresse wird genutzt
