# JUNGÜBERNEHMER – Website

Statische Seite (HTML/CSS/JS), keine Cookies, keine externen Dienste.

## Änderungen
Texte, Menü, Kontaktdaten stehen in `tools/build.py`. Danach `python3 tools/build.py` ausführen – das erzeugt alle Seiten, `sitemap.xml` und `robots.txt` neu.

## Vor dem Livegang ersetzen (gelb markierte Platzhalter)
- Impressum + Datenschutz: Straße, PLZ/Ort
- Datenschutz: Hosting-Anbieter
- Instagram-Link prüfen (`INSTAGRAM` in build.py)
- Inhaber-Name und Referenzen prüfen
- Rechtstexte juristisch prüfen lassen

## Hosting
**GitHub Pages:** Repo anlegen, Dateien hochladen, Settings → Pages → Branch `main`, Ordner `/`. Datei `CNAME` ist vorhanden.
**Hostinger:** Inhalt in `public_html` hochladen (`.htaccess` enthält https/non-www-Weiterleitung).

## DNS bei Ionos
Nur A-/CNAME-Einträge ändern, **MX-Einträge (Mail) unberührt lassen.**
GitHub Pages: A-Einträge für `@` auf 185.199.108.153, .109.153, .110.153, .111.153; CNAME `www` → `<benutzername>.github.io`.
Hostinger: A-Eintrag `@` auf die IP aus dem Hostinger-Panel.
Canva-Seite erst abschalten, wenn die neue Seite läuft.

## Kontaktformular später
In `kontakt/` ist ein Kommentar als Platzhalter. Formular-Dienst (z. B. Formspree) einsetzen und Datenschutz ergänzen.
