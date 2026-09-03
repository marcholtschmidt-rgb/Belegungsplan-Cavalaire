# Arbeitsweise in diesem Repo

Projektbeschreibung, Seitenstruktur und Technik stehen in `README.md`.
Hier steht nur, wie in diesem Repo gearbeitet wird.

## Deployment

`main` ist der Live-Branch. Hostinger ist mit GitHub verbunden und hat
"Automatische Bereitstellung" aktiv: Jeder Push auf `main` geht nach
etwa 3–5 Minuten automatisch auf
`lavender-scorpion-500637.hostingersite.com`.

Daraus folgt:

- Ein Push auf `main` ist eine Veröffentlichung, kein Zwischenstand.
- Pushes auf andere Branches lösen kein Deployment aus – dort kann
  gefahrlos vorbereitet werden.
- Nach einem Deployment muss die PWA auf dem Smartphone komplett
  geschlossen und neu geöffnet werden, sonst bleibt der alte Stand im
  Cache.

## Was direkt auf main darf, was nicht

Vereinbarung mit dem Repo-Eigentümer (26.08.2026):

**Direkt auf `main`** – Texte, Rechtschreibung, neue oder ersetzte
Bilder, Dokumentation, kleine Korrekturen.

**Vorher zeigen und Freigabe abwarten** – alles, was Layout oder
Funktionen verändert: Umbauten an den HTML-Seiten, Änderungen am
Kalender oder am Admin-Bereich, Eingriffe in `server.js`, Änderungen an
der Supabase-Datenbank oder ihren `owner_*`-Funktionen.

Im Zweifel nachfragen statt pushen.

## Festgelegte Entscheidungen

Diese Punkte sind bewusst so entschieden – nicht ungefragt ändern:

- **Repository bleibt öffentlich.** Ein privates Repo wurde geprüft und
  verworfen: Der Supabase-Anon-Key ist ohnehin im Seitenquelltext
  sichtbar (so vorgesehen, geschützt wird über Row Level Security), und
  der Aufwand mit Deploy Keys in hPanel lohnt den Nutzen nicht.
- **Der PIN liegt nur als bcrypt-Hash in der Datenbank.** Tabelle
  `owner_geheim`, fuer `anon` gesperrt; geprueft wird an einer
  einzigen Stelle in `owner_pin_ok()`, die alle `owner_*`-Funktionen
  benutzen. Er steht in keiner Funktionsdefinition, keiner Datei und
  keinem Chat. Geaendert wird er vom Eigentuemer selbst ueber das
  Formular im persoenlichen Bereich (`owner_set_pin`, mindestens
  sechs Zeichen). **Claude kennt den PIN nicht und soll ihn auch nicht
  erfragen.** Der frueher genutzte vierstellige PIN steht bis zum
  26.08.2026 in der Commit-Historie; nach dem ersten Wechsel ist er
  wertlos.
- **Der PIN gehört nicht in Dateien im Repo.** `server.js` liefert
  deshalb keine `.md`-Dateien mehr aus (404).
- **`assets/aussicht-360.jpg`, `terrasse-360.jpg`, `-v2`, `-v3`
  bleiben liegen.** Sie werden im Code nicht referenziert, sind aber die
  Vorlagen für die Panorama-Kacheln. Nicht als "ungenutzt" aufräumen.
- **WLAN-Zugangsdaten stehen nicht auf der Webseite.** Ein
  automatischer Versand per SMS oder E-Mail nach bestaetigter Buchung
  wurde geprueft und verworfen: Bei wenigen Buchungen im Jahr lohnt
  der Aufwand (externer Versanddienst, Edge Function, Datenbank-
  Trigger) nicht. Der Eigentuemer teilt die Daten persoenlich mit;
  `maison.html` weist darauf hin. Nicht ungefragt automatisieren.
- **Rechte auf `public.bookings` sind bewusst eng gesetzt.** `anon`
  und `authenticated` haben nur SELECT auf die vorhandenen Spalten und
  INSERT auf die fuenf Formularfelder. Alles Weitere laeuft ueber die
  `owner_*`-Funktionen. Eine neu angelegte Spalte ist damit nicht
  automatisch oeffentlich lesbar - sie muss einzeln freigegeben
  werden, und der Kalender fragt in `belegung.html` bewusst einzelne
  Spalten statt `select=*` ab.
- **Das Supabase-Projekt wird wach gehalten.** Der Free-Tarif
  pausiert nach sieben ruhigen Tagen;
  `.github/workflows/supabase-wachhalten.yml` stellt deshalb taeglich
  eine Anfrage. Nicht als "unnoetige Automatik" entfernen.
- **Keine eigene Domain.** Der Hinweis in hPanel ist bekannt; die
  `hostingersite.com`-Adresse genügt vorerst.

## Dateien ändern

Der Eigentümer musste Dateien früher von Hand über die
GitHub-Weboberfläche hoch- und runterladen. Das ist nicht mehr nötig –
Änderungen, auch viele auf einmal, direkt committen und pushen.
