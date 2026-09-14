# Cavalaire App

Web-App für das Ferienhaus in Cavalaire-sur-Mer: eine animierte Startseite, drei Unterseiten (Cavalaire-Reiseführer, Maison, Belegungsplan) und Geräte-Anleitungen. Läuft unabhängig von Claude als eigenständige Webseite (GitHub + Hostinger) und speichert Buchungsdaten in einer eigenen Supabase-Datenbank.

Diese Datei beschreibt **was** die App ist und wie sie aufgebaut ist. Wie in diesem Repo gearbeitet wird und welche Entscheidungen bewusst so getroffen wurden, steht in `CLAUDE.md` – bitte beides lesen.

## Seitenstruktur

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Animation (Seestern, Haus, Kalender), Live-Wetter, drei Links |
| `cavalaire.html` | Reiseführer: Anreise, Strände, Wassersport, Touren, Nahverkehr, Essen, Notrufnummern, 360°-Rundblick |
| `maison.html` | Rund ums Haus: Ankunft, Internet, Geräte, Müll, Abreise, Kontakte, 360°-Rundblick |
| `belegung.html` | Belegungsplan: Kalender, Buchungsanfragen, Admin-Bereich |
| `ofen.html` | Kurzanleitung für den Ofen, verlinkt aus dem Geräte-Abschnitt |

**Arbeitsteilung der beiden Inhaltsseiten:** `cavalaire.html` beschreibt den **Ort** – wie man hinkommt und was es dort gibt. `maison.html` beschreibt das **Haus** – alles ab der Haustür. Die Anreise stand zunächst auf der Maison-Seite und wurde am 8. September 2026 nach Cavalaire verschoben, weil sie dort hingehört.

**Navigation:** Auf jeder Unterseite sitzt oben rechts ein fest positionierter Home-Button (44 × 44 px, bei `right: 20px`), der beim Scrollen stehen bleibt und zur Startseite führt. Auf `ofen.html` steht links daneben zusätzlich ein Zurück-Pfeil nach `maison.html`; der Home-Button behält dabei seine Position, damit er beim Seitenwechsel nicht springt. Auf `belegung.html` sitzt das Zahnrad für den Admin-Bereich links neben dem Home-Button in derselben festen Gruppe, damit beide beim Scrollen stehen bleiben.

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
- **Vergangene Buchungen** verschwinden aus der Liste, sobald der Abreisetag vorbei ist. Gelöscht wird nichts: Im Kalender bleiben sie sichtbar, und unter der Liste steht, wie viele ausgeblendet sind

Wetterdaten stehen **nicht** hier, sondern auf der Startseite.

## Funktionen (Startseite / `index.html`)

Live-Wetter von Open-Meteo, links übereinander: Lufttemperatur oben, Luftfeuchtigkeit mittig, Wassertemperatur unten in den Wellen. Drei animierte Symbole verlinken auf die Unterseiten.

## Funktionen (Maison / `maison.html`)

Sieben Abschnitte in einheitlichem Aufbau: Icon 64 × 64 px links, Überschrift in Fraunces 1.9rem daneben, darunter eine Kachel mit dem Inhalt. Reihenfolge folgt dem Aufenthalt.

| Abschnitt | Stand |
|---|---|
| Ankunft | Verweist auf die Anreise-Rubrik der Cavalaire-Seite. Der Weg vom Ortszentrum zum Haus, Schlüssel und Parken fehlen noch |
| Internet | Hinweis, dass die WLAN-Daten nach bestätigter Buchung persönlich mitgeteilt werden, plus Link zum Belegungsplan |
| Geräte | Link auf `ofen.html`; Heizung, Klimaanlage, Waschmaschine fehlen noch |
| Müll | Platzhalter |
| Abreise | Platzhalter |
| Kontakte | `cavalaire-sur-mer@gmx.de` als `mailto`-Link; Ansprechpartner vor Ort fehlen noch |
| 360°-Eindrücke | Rundblick von der Terrasse |

## Funktionen (Cavalaire-Reiseführer / `cavalaire.html`)

Hero-Header mit Frankreich-Umriss und Seestern-Ortsmarke. Acht Rubriken in dieser Reihenfolge: **Anreise**, Strände (alle fünf mit aufklappbaren Fotokarten und eingebetteter offizieller Strandkarte), Wassersport, Wandern & Radfahren, **Nahverkehr**, Essen & Trinken, Notrufnummern, 360°-Rundblick vom Aussichtspunkt.

### Anreise

Vier aufklappbare Bereiche – Auto, Flugzeug, Zug, Bus –, damit die Kachel zugeklappt kurz bleibt und erst beim Antippen wächst. Technisch dieselbe Mechanik wie die Strand-Kacheln: ein `<button>` mit `aria-expanded` schaltet das `hidden`-Attribut des zugehörigen Blocks um; das Skript steht unten in der Datei neben dem der Strand-Kacheln.

Inhaltlich:

- **Auto** – zwei Wege von der A8 (Sortie 36 Le Muy über Sainte-Maxime und die D559, Sortie 13 Le Cannet-des-Maures über die D558 und La Garde-Freinet) sowie die Küstenstraße RD559
- **Flugzeug** – die vier Flughäfen der Region, dazu der Weg vom Flughafen Nizza ohne Auto: Tram 2 zum Bahnhof Nice-Saint-Augustin, Zug nach Saint-Raphaël, Zou!-Bus 874 nach Cavalaire
- **Zug** – kein Bahnhof in Cavalaire; TGV nach Toulon, Hyères oder Saint-Raphaël, weiter mit dem Bus
- **Bus** – Zou!-Linie 874 (Saint-Raphaël – Sainte-Maxime – Cogolin – Cavalaire – Le Lavandou) und Linie 878 (Toulon – Le Lavandou – Saint-Tropez), beide in beide Richtungen

### Nahverkehr

Vier kostenlose Navette-Linien im Ort, Zeitraum, die App **Pysae** für Live-Abfahrten (Links zu App Store und Google Play) und Links auf die Fahrplanseiten. Bewusst **kein** direkter Link auf eine Saison-PDF: Die Stadt nimmt den Sommer-Faltplan nach dem 31. August vom Netz, ein fest verdrahteter Dateilink ist im Folgejahr tot. Verwiesen wird stattdessen auf die Seiten, die den jeweils gültigen Plan führen.

### Quellen für Orts- und Verkehrsangaben

Vereinbarung vom 8. September 2026: Auf den Anreise- und Nahverkehr-Rubriken stehen **nur Angaben, die sich offiziell belegen lassen** – Stadt Cavalaire, Fahrplan von Zou!, VINCI Autoroutes als Betreiber der A8, Flughafen Nizza. Selbst geschätzte Entfernungen, Fahrzeiten und Bewertungen wurden wieder entfernt. Angaben des Eigentümers aus eigener Ortskenntnis haben Vorrang vor den offiziellen Seiten – so führt die D25 laut Stadt über die N98, tatsächlich geht es ab Sainte-Maxime direkt auf der D559 weiter.

Die Seiten `cavalaire.fr` und `cavalairesurmer.fr` sind aus der Claude-Arbeitsumgebung **nicht erreichbar** (Netzwerksperre). Inhalte von dort müssen über die Websuche ermittelt oder vom Eigentümer geliefert werden; Links dorthin kann Claude nicht selbst prüfen.

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

**Hover auf Touchgeräten:** Nach einem Antippen bleibt `:hover` auf iPhone und iPad am zuletzt berührten Element hängen – ein Knopf sieht dann aus, als wäre er noch aktiv. Einfärbungen beim Überfahren gehören deshalb in `@media (hover:hover)`.

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

| `owner_list_privat(pin)` | Notizen und Bildbeschreibungen des persönlichen Bereichs |
| `owner_get_privat_foto(pin, foto_id)` | ein einzelnes Foto als Base64 |
| `owner_set_pin(alt, neu)` | setzt den PIN neu, mindestens sechs Zeichen |

### Persönlicher Bereich und PIN

`privat.html` ist über das Zahnrad auf der Maison-Seite erreichbar. Die Inhalte – Notizen in `privat_eintraege`, Fotos als Bytes in `privat_fotos` – liegen **nicht** im Repository und **nicht** auf dem Webserver. Beide Tabellen haben RLS aktiv, keine Policies und keine Rechte für `anon`; heraus kommt nur etwas über die beiden `owner_*`-Funktionen, die den PIN prüfen. Auch das Nachladen eines einzelnen Fotos prüft ihn erneut.

Der PIN selbst liegt als **bcrypt-Hash** in `owner_geheim` (für `anon` gesperrt) und wird an einer einzigen Stelle geprüft, in `owner_pin_ok()`. Aus dem Hash lässt er sich nicht zurückrechnen, und jede Prüfung kostet Rechenzeit – Durchprobieren wird dadurch unattraktiv.

**Achtung bei Änderungen an den `owner_*`-Funktionen:** Supabase sperrt für seine Webschnittstellen-Rollen `UPDATE` und `DELETE` ohne `WHERE`-Bedingung. Über eine direkte Datenbankverbindung greift die Sperre nicht – ein solcher Fehler fällt deshalb erst im Browser auf, mit der Meldung „UPDATE requires a WHERE clause". Jede schreibende Anweisung braucht eine `WHERE`-Bedingung, auch bei Tabellen mit nur einer Zeile.

**Geändert wird der PIN im Browser**, über das Formular im persönlichen Bereich. So taucht er weder in einer Datei noch in einem SQL-Verlauf noch in einem Chat auf. Wer den PIN setzt, ist der Einzige, der ihn kennt.

## Deployment

`main` ist der Live-Branch. Hostinger ist mit GitHub verbunden, "Automatische Bereitstellung" ist aktiv: Jeder Push auf `main` ist nach etwa 3–5 Minuten unter `lavender-scorpion-500637.hostingersite.com` erreichbar. Pushes auf andere Branches lösen nichts aus.

Nach jedem Deployment die PWA auf dem Smartphone **komplett schließen und neu öffnen**, sonst bleibt der alte Stand im Cache.

## Supabase wach halten

Supabase pausiert Projekte im Free-Tarif, wenn sie über sieben Tage zu wenig Datenbankaktivität zeigen. Der Belegungsplan würde dann keine Buchungen mehr laden und der persönliche Bereich sich nicht mehr entsperren, bis das Projekt im Dashboard wieder aufgeweckt wird (möglich bis 90 Tage danach, ohne Datenverlust).

Dagegen läuft `.github/workflows/supabase-wachhalten.yml`: täglich um 06:17 UTC ein Aufruf von `pending_count()` über die REST-Schnittstelle. Das zählt als Nutzeranfrage und genügt. Antwortet die Datenbank nicht mit 200, schlägt der Ablauf fehl und GitHub schickt eine Mail – ein bereits pausiertes Projekt fällt so auf. Der Ablauf lässt sich unter *Actions* auch von Hand starten.

**Ein Haken:** GitHub schaltet geplante Abläufe ab, wenn ein Repository 60 Tage ohne Aktivität bleibt, und meldet das per Mail. Wird hier längere Zeit nichts committet, muss der Ablauf unter *Actions* wieder eingeschaltet werden.

## Bekannte Einschränkungen

- Der PIN stand vom 17. bis 26. August 2026 in dieser Datei auf `main` und ist daher in der Commit-Historie weiterhin auffindbar
- Die Seite ist über Zertifikats-Transparenz-Protokolle auffindbar, auch ohne Verlinkung. "Nur an Familie weitergeben" macht sie nicht privat
- Wetterdaten von Open-Meteo sind Modellschätzung, keine Messung vor Ort
- Das Centre-Ville-Strandfoto trägt ein fremdes Wasserzeichen ("Cavalaire ProvenceWeb")
- `maison.html` ist inhaltlich erst zum Teil ausgebaut: Müll und Abreise sind Platzhalter, bei Ankunft fehlen der Weg vom Ortszentrum zum Haus, Schlüssel und Parken
- Eine Fernseher-Anleitung ist vorbereitet (Grafiken liegen bereit), aber noch nicht geschrieben
- Es gibt keine eigene Domain; die `hostingersite.com`-Adresse wird genutzt
- Der Navette-Faltplan könnte als PDF unter `assets/` liegen und direkt verlinkt werden – dann wäre er auch ohne Netz in der App. Dafür muss der Eigentümer die Datei liefern, Claude kommt nicht an sie heran
