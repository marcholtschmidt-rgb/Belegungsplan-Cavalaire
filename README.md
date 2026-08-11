# Cavalaire App

Web-App für das Ferienhaus in Cavalaire-sur-Mer, bestehend aus einer animierten Startseite und mehreren Unterseiten. Läuft unabhängig von Claude als eigenständige Webseite (aktuell über GitHub + Hostinger bereitgestellt) und speichert Buchungsdaten in einer eigenen Supabase-Datenbank.

## Seitenstruktur

- **`index.html`** – Startseite mit Animation (Seestern, Haus, Kalender) und drei Links zu den Unterseiten
- **`cavalaire.html`** – Infos rund um Cavalaire-sur-Mer (Strände, Restaurants, Ausflüge) – **aktuell nur Platzhalter, noch zu erstellen**
- **`maison.html`** – Infos rund ums Haus (Anleitungen, Kontakte, Hausregeln) – **aktuell nur Platzhalter, noch zu erstellen**
- **`belegung.html`** – der Belegungsplan (ehemals `index.html`), siehe Funktionen unten

Der Home-Button (Haus-Symbol oben rechts) im Belegungsplan führt immer zurück zur Startseite (`index.html`).

## Funktionen (Belegungsplan / `belegung.html`)

- **Kalenderansicht** (Monat/Jahr umschaltbar; in der Jahresansicht auf einen Monat tippen, um direkt in die Monatsansicht zu springen)
- **Zeitraum-Auswahl direkt im Kalender**: Antippen von Anreise- und Abreisetag direkt auf den Kalenderkacheln (keine separaten Datumsfelder mehr)
- **Buchungsanfrage-Formular**: Jeder mit dem Link kann einen Zeitraum anfragen (Name, Kategorie, Notiz)
- **Freigabe-Workflow**: Neue Anfragen erscheinen zunächst als "ausstehend" und werden erst nach Bestätigung im Kalender sichtbar
- **Admin-Bereich** (Zahnrad-Symbol oben rechts, PIN-geschützt): Anfragen bestätigen/ablehnen, bestehende Buchungen bearbeiten oder löschen. Erneuter Klick auf das Zahnrad sperrt den Bereich wieder (PIN muss danach erneut eingegeben werden)
- **Öffentlicher Hinweis**: Anzahl offener Anfragen ist für alle sichtbar (ohne Namen/Datum)
- **Live-Wetter** für Cavalaire-sur-Mer: Lufttemperatur, Zustand, Luftfeuchtigkeit, Wassertemperatur (via Open-Meteo, kostenlos, ohne API-Key)
- **Installierbar als App** (PWA): "Zum Home-Bildschirm hinzufügen" auf dem Smartphone möglich
- **Mobile-optimiert**: Auf schmalen Bildschirmen stehen die Status-Kacheln (Heute/Anreise/Nächte) über dem Kalender; ab 900px Breite Zweispalten-Layout (Kalender links, Formulare rechts)

## Design

**Startseite** (`index.html`): warmes Creme (`#F5EFE3`) als Hintergrund, dunkles Petrol (`#123A4E`) als Textfarbe, Türkis-Verlauf (`#63BDB2` → `#2A6A7E`) für die drei animierten Symbole (Seestern, Haus, Kalender), Gold (`#E3A857`) als Akzent im Kalender-Symbol. Schriften: "Fraunces" (Beschriftung der drei Bereiche), "Inter" (Fließtext), "IBM Plex Mono" (kleine Unterschrift).

**Belegungsplan** (`belegung.html`, Farbschema "Organic"): warmes Creme (`#FFF4E4`) als Hintergrund, dunkles Petrol (`#14313F`) als Textfarbe, Türkis (`#0FA3A3`) und Koralle (`#FF6B3D`) als Akzente, Sonnengelb (`#FFC53D`) fürs Wetter-Icon. Schriften: "Bricolage Grotesque" (Überschriften), "Public Sans" (Fließtext), "Space Mono" (Zahlen/Daten).

Das Design wurde über **Claude Design** (claude.ai/design) entworfen und anschließend hier im Chat in eigenständige, direkt lauffähige HTML-Dateien integriert (kein Babel/unpkg im Browser; beim Belegungsplan React über cdnjs.cloudflare.com + vorab mit TypeScript zu reinem JavaScript kompilierter Code, bei der Startseite reines HTML/CSS/SVG mit CSS-Animationen).

## Technischer Aufbau

| Teil | Technologie |
|---|---|
| Startseite | reines HTML/CSS + SVG-Animationen (kein React nötig) |
| Belegungsplan-Oberfläche | React (über CDN, vorkompiliert zu reinem JavaScript – kein Build-Schritt beim Nutzer nötig) |
| Styling | Eigenes CSS je Seite (keine Tailwind-Abhängigkeit) |
| Datenbank | Supabase (Projekt: `belegungsplan-cavalaire`, Region eu-central-1/Frankfurt) |
| Hosting | GitHub-Repository → Hostinger (Node.js-Deployment) |

### Dateien in diesem Ordner

- `index.html` – Startseite mit Animation und den drei Navigations-Links
- `cavalaire.html` – Platzhalterseite für Cavalaire-Infos (noch zu erstellen)
- `maison.html` – Platzhalterseite für Haus-Infos (noch zu erstellen)
- `belegung.html` – der komplette Belegungsplan (HTML + CSS + JavaScript in einer Datei)
- `manifest.json` – Konfiguration für die "Installieren als App"-Funktion
- `icon-192.png` / `icon-512.png` – App-Icon (Seestern-Logo von Cavalaire-sur-Mer)
- `package.json` / `server.js` – nötig, damit Hostinger die Seiten als Node.js-App ausliefert (einfacher Datei-Server, keine echte Anwendungslogik). **Bitte prüfen, dass `server.js` alle `.html`-Dateien im Ordner ausliefert und nicht nur eine fest eingetragene `index.html`** – je nach bisheriger Konfiguration muss das ggf. einmalig angepasst werden.

## Datenbank (Supabase)

- **Projekt-ID**: `rtfpduqyrarktmxaiise`
- **Tabelle**: `bookings` (Spalten: `id`, `guest_name`, `category`, `start_date`, `end_date`, `notes`, `status`, `created_at`)
- **Status**: `pending` (Anfrage, noch nicht bestätigt) oder `confirmed` (sichtbar im Kalender)
- **Zugriff**: über den öffentlichen "anon"-Schlüssel, der direkt im Code von `belegung.html` steht (siehe `SUPABASE_URL` / `SUPABASE_ANON_KEY`)

### Datenbank-Funktionen (RPC)

Diese Funktionen laufen mit erweiterten Rechten und prüfen den PIN serverseitig, bevor irgendetwas passiert:

- `pending_count()` – öffentlich, gibt nur die Anzahl offener Anfragen zurück (keine Details)
- `owner_list_all(pin)` – listet alle Buchungen inkl. ausstehender Anfragen
- `owner_confirm_booking(booking_id, pin)` – bestätigt eine Anfrage
- `owner_update_booking(booking_id, pin, p_guest_name, p_category, p_start_date, p_end_date, p_notes)` – bearbeitet eine bestehende Buchung
- `owner_delete_booking(booking_id, pin)` – löscht eine Buchung (bestätigt oder Anfrage)

**Aktueller PIN: `1893`**

## Etwas ändern lassen

Für Anpassungen (Design, neue Funktionen, Fehlerbehebungen) einfach einen (neuen) Chat mit Claude starten und dabei folgende Dateien hochladen, damit sofort der aktuelle Stand bekannt ist:

1. Dieses `README.md`
2. Die betroffene(n) Seite(n) (`index.html`, `belegung.html`, `cavalaire.html` oder `maison.html`)

Nach jeder Änderung:

1. Neue Datei(en) herunterladen
2. Bei GitHub in das Repository hochladen (vorhandene Dateien ersetzen)
3. Bei Hostinger auf "Redeploy" klicken (falls automatische Bereitstellung nicht aktiv ist)
4. App auf dem Smartphone einmal komplett schließen und neu öffnen, damit sie sich aktualisiert

## Bekannte Einschränkungen

- Der PIN wird im Klartext in einer Datenbankfunktion verglichen – ausreichend sicher für einen privaten Familienkalender, aber kein Hochsicherheitsstandard
- Die Wasser- und Wetterdaten stammen von Open-Meteo und sind Modellschätzungen für den Abrufzeitpunkt, keine Live-Messung direkt vor Ort
- Ein Kalender kann beim Antippen des letzten Tages eines Monats nicht sicher unterscheiden, ob das der gewünschte Abreisetag ist oder ob eigentlich in den nächsten Monat weitergeblättert werden soll – dafür gibt es bewusst keine automatische Monats-Sprung-Funktion mehr, sondern nur die manuellen Pfeil-Buttons

