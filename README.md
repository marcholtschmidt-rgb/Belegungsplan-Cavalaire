# Belegungsplan Cavalaire

Web-App zur Verwaltung der Belegung des Ferienhauses in Cavalaire-sur-Mer. Läuft unabhängig von Claude als eigenständige Webseite (aktuell über GitHub + Hostinger bereitgestellt) und speichert alle Daten in einer eigenen Supabase-Datenbank.

## Funktionen

- **Kalenderansicht** (Monat/Jahr umschaltbar; in der Jahresansicht auf einen Monat tippen, um direkt in die Monatsansicht zu springen)
- **Zeitraum-Auswahl direkt im Kalender**: Antippen von Anreise- und Abreisetag direkt auf den Kalenderkacheln (keine separaten Datumsfelder mehr)
- **Buchungsanfrage-Formular**: Jeder mit dem Link kann einen Zeitraum anfragen (Name, Kategorie, Notiz)
- **Freigabe-Workflow**: Neue Anfragen erscheinen zunächst als "ausstehend" und werden erst nach Bestätigung im Kalender sichtbar
- **Admin-Bereich** (Zahnrad-Symbol oben rechts, PIN-geschützt): Anfragen bestätigen/ablehnen, bestehende Buchungen bearbeiten oder löschen. Erneuter Klick auf das Zahnrad sperrt den Bereich wieder (PIN muss danach erneut eingegeben werden)
- **Öffentlicher Hinweis**: Anzahl offener Anfragen ist für alle sichtbar (ohne Namen/Datum)
- **Live-Wetter** für Cavalaire-sur-Mer: Lufttemperatur, Zustand, Luftfeuchtigkeit, Wassertemperatur (via Open-Meteo, kostenlos, ohne API-Key)
- **Startbildschirm**: Beim Öffnen erscheint zunächst eine animierte Begrüßung (Seestern-Logo, Name, Ort, sanfte Gezeiten-Wellen). Der Kalender lädt währenddessen bereits im Hintergrund; ein Tippen auf den Bildschirm blendet den Startbildschirm aus und zeigt den Belegungsplan
- **Seestern-Logo im Kopfbereich**: Dasselbe Motiv wie im Startbildschirm und App-Icon steht jetzt auch klein neben der Überschrift "Belegungsplan"
- **Installierbar als App** (PWA): "Zum Home-Bildschirm hinzufügen" auf dem Smartphone möglich
- **Mobile-optimiert**: Auf schmalen Bildschirmen stehen die Status-Kacheln (Heute/Anreise/Nächte) über dem Kalender; ab 900px Breite Zweispalten-Layout (Kalender links, Formulare rechts)

## Design

Aktuelles Farbschema ("Organic"): warmes Creme (`#FFF4E4`) als Hintergrund, dunkles Petrol (`#14313F`) als Textfarbe, Türkis (`#0FA3A3`) und Koralle (`#FF6B3D`) als Akzente, Sonnengelb (`#FFC53D`) fürs Wetter-Icon. Schriften: "Bricolage Grotesque" (Überschriften), "Public Sans" (Fließtext), "Space Mono" (Zahlen/Daten).

Das Design wurde über **Claude Design** (claude.ai/design) entworfen und anschließend hier im Chat in die bewährte, vorkompilierte Ein-Datei-Struktur integriert (kein Babel/unpkg im Browser, stattdessen React über cdnjs.cloudflare.com + vorab mit TypeScript zu reinem JavaScript kompilierter Code).

## Technischer Aufbau

| Teil | Technologie |
|---|---|
| Oberfläche | React (über CDN, vorkompiliert zu reinem JavaScript – kein Build-Schritt beim Nutzer nötig) |
| Styling | Eigenes CSS (keine Tailwind-Abhängigkeit mehr) |
| Datenbank | Supabase (Projekt: `belegungsplan-cavalaire`, Region eu-central-1/Frankfurt) |
| Hosting | GitHub-Repository → Hostinger (Node.js-Deployment) |

### Dateien in diesem Ordner

- `index.html` – die komplette App (HTML + CSS + JavaScript in einer Datei)
- `manifest.json` – Konfiguration für die "Installieren als App"-Funktion
- `icon-192.png` / `icon-512.png` – App-Icon (Seestern-Logo von Cavalaire-sur-Mer)
- `package.json` / `server.js` – nötig, damit Hostinger die Seite als Node.js-App ausliefern kann (einfacher Datei-Server, keine echte Anwendungslogik)

## Datenbank (Supabase)

- **Projekt-ID**: `rtfpduqyrarktmxaiise`
- **Tabelle**: `bookings` (Spalten: `id`, `guest_name`, `category`, `start_date`, `end_date`, `notes`, `status`, `created_at`)
- **Status**: `pending` (Anfrage, noch nicht bestätigt) oder `confirmed` (sichtbar im Kalender)
- **Zugriff**: über den öffentlichen "anon"-Schlüssel, der direkt im Code von `index.html` steht (siehe `SUPABASE_URL` / `SUPABASE_ANON_KEY`)

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
2. Die aktuelle `index.html`

Nach jeder Änderung:

1. Neue `index.html` (und ggf. weitere geänderte Dateien) herunterladen
2. Bei GitHub in das Repository hochladen (vorhandene Dateien ersetzen)
3. Bei Hostinger auf "Redeploy" klicken (falls automatische Bereitstellung nicht aktiv ist)
4. App auf dem Smartphone einmal komplett schließen und neu öffnen, damit sie sich aktualisiert

## Bekannte Einschränkungen

- Der PIN wird im Klartext in einer Datenbankfunktion verglichen – ausreichend sicher für einen privaten Familienkalender, aber kein Hochsicherheitsstandard
- Die Wasser- und Wetterdaten stammen von Open-Meteo und sind Modellschätzungen für den Abrufzeitpunkt, keine Live-Messung direkt vor Ort
- Ein Kalender kann beim Antippen des letzten Tages eines Monats nicht sicher unterscheiden, ob das der gewünschte Abreisetag ist oder ob eigentlich in den nächsten Monat weitergeblättert werden soll – dafür gibt es bewusst keine automatische Monats-Sprung-Funktion mehr, sondern nur die manuellen Pfeil-Buttons

