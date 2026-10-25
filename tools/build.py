#!/usr/bin/env python3
"""JUNGÜBERNEHMER – Seitengenerator.

Erzeugt alle HTML-Seiten, sitemap.xml und robots.txt aus den Inhalten in dieser Datei.
Aufruf im Projektordner:  python3 tools/build.py

Die fertigen HTML-Dateien sind normale, statische Dateien. Dieses Skript wird zum Betrieb der
Seite NICHT gebraucht. Es erleichtert nur Änderungen, die viele Seiten gleichzeitig betreffen
(Menü, Fußzeile, Kontaktdaten).
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------ Stammdaten
SITE = "https://jungubernehmer.de"
BRAND = "JUNGÜBERNEHMER"
OWNER = "Devrim Can Barkin"
PHONE_TEL = "+4917630666125"
PHONE_SHOW = "+49 176 30666125"
EMAIL = "kontakt@jungubernehmer.de"
INSTAGRAM = "https://www.instagram.com/jungubernehmer/"
INSTAGRAM_NAME = "@jungubernehmer"
MODIFIED = "2026-10-25"
OG_IMAGE = SITE + "/assets/img/og-image.jpg"
PORTRAIT_ALT = "Devrim Can Barkin, Gründer von JUNGÜBERNEHMER, im grünen Anzug mit verschränkten Armen"

PHONE_ICON = (
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2'
    "c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5"
    'c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'
)


def e(text):
    return html.escape(text, quote=True)


def ph(text):
    """Sichtbarer Platzhalter: muss vor dem Livegang ersetzt werden."""
    return f'<span class="platzhalter">[{e(text)}]</span>'


# ------------------------------------------------------------------ Leistungen
SERVICES = [
    {
        "slug": "kurzform-videos",
        "name": "Kurzform-Videos",
        "short": "Reels, TikToks und Shorts, die in den ersten Sekunden hängen bleiben. Von der Idee bis zum Schnitt.",
        "title": "Kurzvideos für Reels, TikTok & Shorts | JUNGÜBERNEHMER",
        "desc": "Kurzform-Videos für Instagram, TikTok und YouTube Shorts: Idee, Skript, Dreh und Schnitt aus einer Hand. Für Unternehmen und Personen.",
        "h1": "Kurzvideos, die hängen bleiben",
        "lead": "Reels, TikToks und Shorts entscheiden in den ersten Sekunden, ob jemand weiterschaut. Ich übernehme deine Videos von der Idee bis zum fertigen Schnitt.",
        "service_type": "Kurzform-Videoproduktion für Social Media",
        "items_intro": "Alles, was zwischen Idee und Veröffentlichung liegt.",
        "items": [
            ("Ideen und Skripte", "Themen, Einstiege und Abläufe, die zu dir und deiner Zielgruppe passen."),
            ("Dreh", "Ich filme vor Ort oder wir drehen bei dir, mit einem einfachen Setup, das nach Content aussieht und nicht nach Werbung."),
            ("Schnitt, Ton und Untertitel", "Tempo, Schnitt und Untertitel, damit dein Video auch ohne Ton funktioniert."),
            ("Formate und Kanäle", "Hochformat für Instagram, TikTok und YouTube Shorts, auf Wunsch auch für LinkedIn."),
            ("Serien statt Zufallsposts", "Wiederkehrende Formate geben deinem Kanal einen Wiedererkennungswert."),
        ],
        "firms": ("Für Unternehmen", "Produkte, Team und Alltag zeigen: Ich mache aus deinem Betrieb Content, der nicht wie Werbung wirkt."),
        "people": ("Für Personen", "Dein Gesicht, deine Meinung, dein Thema: Ich helfe dir, regelmäßig vor die Kamera zu gehen, ohne dass es dich Nerven kostet."),
        "faq": [
            ("Wie viele Videos brauche ich pro Woche?", "Das hängt von deinem Ziel und deinen Kanälen ab. Wir legen im Gespräch einen Rhythmus fest, den du durchhältst und den ich gut liefern kann."),
            ("Muss ich selbst vor die Kamera?", "Nein. Es geht auch mit Produkten, Team, Voice-over oder Bildschirmaufnahmen. Wenn du dich zeigen willst, helfe ich dir mit Skript und Anleitung."),
            ("Was kostet das?", "Der Preis hängt von Umfang und Rhythmus ab. Ruf mich an, dann bekommst du ein konkretes Angebot."),
        ],
    },
    {
        "slug": "imagefilme",
        "name": "Imagefilme",
        "short": "Dein Unternehmen oder deine Marke in wenigen Minuten Film: ruhig erzählt, sauber produziert.",
        "title": "Imagefilme für Unternehmen und Marken | JUNGÜBERNEHMER",
        "desc": "Imagefilme, die zeigen, wer du bist: Konzept, Dreh und Schnitt für Unternehmen, Marken und Personen. Für Website, Social Media und Recruiting.",
        "h1": "Imagefilme, die dein Unternehmen erklären",
        "lead": "Ein guter Imagefilm zeigt in wenigen Minuten, wofür du stehst, und das besser als jede Textseite. Ich übernehme ihn von der ersten Idee bis zur Auslieferung.",
        "service_type": "Imagefilm-Produktion",
        "items_intro": "Vom ersten Gespräch bis zur fertigen Datei.",
        "items": [
            ("Konzept und Drehbuch", "Ich lerne dich und dein Unternehmen kennen und entwickle eine Geschichte, die zu dir passt."),
            ("Dreh", "Ich organisiere den Dreh und arbeite so, dass dein Tagesgeschäft möglichst wenig leidet."),
            ("Schnitt, Ton und Farbe", "Der Film wird geschnitten, mit Ton und Musik versehen und in ein einheitliches Bild gebracht."),
            ("Auslieferung", "Du bekommst den Film in den Formaten, die du brauchst: für Website, Social Media, Messe oder Recruiting."),
            ("Kurze Ausschnitte", "Aus dem Film schneide ich auf Wunsch Kurzvideos für Reels, TikTok und LinkedIn."),
        ],
        "firms": ("Für Unternehmen", "Für Website, Recruiting, Messe und Vertrieb. Ich erzähle die Geschichte deines Unternehmens und nicht die einer Stockvideo-Welt."),
        "people": ("Für Personen", "Für Selbstständige, Berater und Gründer: ein Film, der dich vorstellt, bevor das erste Gespräch beginnt."),
        "faq": [
            ("Wie lange dauert die Produktion?", "Das hängt vom Umfang ab. Nach dem Erstgespräch bekommst du einen Zeitplan mit festen Terminen für Dreh und Abgabe."),
            ("Kann ich Änderungen verlangen?", "Ja. Du bekommst einen Rohschnitt zur Ansicht und gibst Feedback, bevor der Film final wird."),
            ("Wo kann ich den Film einsetzen?", "Auf deiner Website, in Social Media, auf Messen, in Bewerbungsprozessen und im Vertrieb. Auf Wunsch liefere ich passende Formate mit."),
        ],
    },
    {
        "slug": "ghostwriting",
        "name": "Ghostwriting",
        "short": "Posts, Skripte und Artikel in deiner Stimme. Dein Name steht drauf, meine Arbeit steckt drin.",
        "title": "Ghostwriting für Unternehmen & Personen | JUNGÜBERNEHMER",
        "desc": "Ghostwriting für LinkedIn, Instagram und mehr: Ich schreibe Posts, Skripte und Artikel in deiner Stimme, für Unternehmen und Einzelpersonen.",
        "h1": "Ghostwriting: dein Name drauf, meine Worte drin",
        "lead": "Du hast etwas zu sagen, aber keine Zeit, es aufzuschreiben. Ich schreibe in deiner Stimme, du veröffentlichst unter deinem Namen.",
        "service_type": "Ghostwriting für Social Media und Unternehmenskommunikation",
        "items_intro": "Texte, die nach dir klingen und nicht nach Werbung.",
        "items": [
            ("Deine Stimme finden", "Im Gespräch lerne ich, wie du sprichst und denkst, und halte es als Leitfaden fest."),
            ("Posts für LinkedIn und Instagram", "Beiträge, die du so veröffentlichen kannst, wie sie ankommen."),
            ("Skripte für Videos", "Texte für Reels, TikToks und Imagefilme, passend zu Länge und Tempo."),
            ("Artikel und Newsletter", "Längere Texte, in denen du dein Wissen zeigen kannst."),
            ("Unternehmenskommunikation", "Texte, die unter dem Namen deines Unternehmens oder deiner Geschäftsführung erscheinen."),
            ("Redaktionsplan", "Ein Plan, wann welches Thema erscheint, damit du regelmäßig sichtbar bleibst."),
        ],
        "firms": ("Für Unternehmen", "Für Geschäftsführung, Fachleute und Marke: regelmäßig sichtbar sein, ohne dass jemand im Team nebenbei schreiben muss."),
        "people": ("Für Personen", "Für Selbstständige, Gründer und Creator: Texte, die nach dir klingen und deine Haltung zeigen."),
        "faq": [
            ("Merkt jemand, dass ich nicht selbst schreibe?", "Nicht, wenn die Stimme stimmt. Deshalb beginnt jede Zusammenarbeit mit einem Gespräch und einer Textprobe, die du freigibst."),
            ("Wer bestimmt die Themen?", "Wir legen sie gemeinsam fest. Du sagst, was du erzählen willst, ich bringe Ideen und Struktur ein."),
            ("Bleibt die Zusammenarbeit vertraulich?", "Ja. Was ich für dich schreibe, erscheint ausschließlich unter deinem Namen."),
        ],
    },
    {
        "slug": "social-media-uebernahme",
        "name": "Social-Media-Übernahme",
        "short": "Ich führe deine Accounts komplett: Strategie, Content, Posting und Community.",
        "title": "Social-Media-Betreuung & Account-Übernahme | JUNGÜBERNEHMER",
        "desc": "Ich übernehme deine Social-Media-Accounts komplett: Strategie, Content, Posting und Community-Betreuung für Unternehmen und Personen.",
        "h1": "Ich übernehme deine Social-Media-Kanäle",
        "lead": "Du willst auf Social Media sichtbar sein, aber nicht jeden Tag daran denken. Ich führe deine Accounts von der Strategie bis zur Antwort auf den Kommentar.",
        "service_type": "Social-Media-Betreuung und Account-Management",
        "items_intro": "Die komplette Betreuung oder nur die Teile, die du abgeben willst.",
        "items": [
            ("Strategie und Ausrichtung", "Wir klären, was dein Kanal erreichen soll und für wen du ihn betreibst."),
            ("Content-Plan", "Ein fester Rhythmus mit Themen, Formaten und Terminen."),
            ("Produktion", "Videos, Bilder und Texte entstehen aus einer Hand, auf Wunsch mit meinen Leistungen Kurzform-Videos und Ghostwriting."),
            ("Posting und Planung", "Ich plane und veröffentliche deine Beiträge zum passenden Zeitpunkt."),
            ("Community-Management", "Ich beantworte Kommentare und Nachrichten in deinem Ton."),
            ("Auswertung", "Wir schauen regelmäßig, was funktioniert, und justieren nach."),
        ],
        "firms": ("Für Unternehmen", "Ich arbeite wie ein Teil deines Teams: Wir stimmen Themen ab, du gibst frei, ich liefere und poste."),
        "people": ("Für Personen", "Ich führe deinen Kanal so, wie du ihn selbst führen würdest, wenn du die Zeit hättest."),
        "faq": [
            ("Welche Kanäle betreust du?", "Instagram, TikTok, LinkedIn und YouTube. Wir legen fest, welche für dein Ziel wirklich Sinn ergeben."),
            ("Behalte ich die Kontrolle über meine Accounts?", "Ja. Die Accounts bleiben bei dir. Du entscheidest, was freigegeben werden muss und was ich selbstständig veröffentliche."),
            ("Kann ich auch nur einzelne Aufgaben buchen?", "Ja. Du kannst die komplette Betreuung nehmen oder nur Videos, Texte oder Community-Management."),
        ],
    },
    {
        "slug": "creator-management",
        "name": "Creator-Management",
        "short": "Brand Deals, Verhandlungen und Organisation für Creator und Influencer.",
        "title": "Creator- & Influencer-Management | JUNGÜBERNEHMER",
        "desc": "Management für Creator und Influencer: Brand Deals, Verhandlungen, Kommunikation mit Unternehmen und Markenaufbau, damit du Content liefern kannst.",
        "h1": "Management für Creator und Influencer",
        "lead": "Du hast das Talent, ich kümmere mich um den Rest. Ich verhandle, organisiere und baue mit dir eine Marke, aus der echte Kooperationen entstehen.",
        "service_type": "Creator- und Influencer-Management",
        "items_intro": "Du lieferst den Content, ich sorge dafür, dass daraus Möglichkeiten werden.",
        "items": [
            ("Kooperationen und Brand Deals", "Ich suche passende Unternehmen, spreche sie an und verhandle die Konditionen."),
            ("Kommunikation mit Unternehmen", "Ich beantworte Anfragen, kläre Briefings und übernehme Rückfragen."),
            ("Events und Einladungen", "Ich prüfe Einladungen und Placements, ordne sie ein und organisiere die Teilnahme."),
            ("Markenaufbau", "Wir schärfen deine Positionierung, damit Unternehmen auf den ersten Blick verstehen, wofür du stehst."),
            ("Strategische Account-Führung", "Wir bauen deine Accounts so auf, dass sie langfristig wachsen, auf Wunsch mit meiner Social-Media-Übernahme."),
        ],
        "firms": ("Für Marken", "Du bekommst einen festen Ansprechpartner statt langer Mailketten und klare Absprachen für Kooperationen."),
        "people": ("Für Creator", "Du konzentrierst dich auf Content, ich kümmere mich um Anfragen, Verhandlung und Struktur."),
        "faq": [
            ("Wie wird abgerechnet?", "Das legen wir im Erstgespräch fest und halten es schriftlich fest."),
            ("Ab welcher Reichweite lohnt sich Management?", "Es gibt keine feste Grenze. Entscheidend ist, ob genug Anfragen oder Potenzial da sind, dass sich jemand darum kümmern sollte. Das schauen wir uns gemeinsam an."),
            ("Handelst du in meinem Namen?", "Nur nach Absprache. Verträge und Zusagen gehen nie ohne deine Freigabe raus."),
        ],
    },
]

NAV = [
    ("Leistungen", "/leistungen/"),
    ("Referenzen", "/referenzen/"),
    ("Über mich", "/ueber-mich/"),
    ("Kontakt", "/kontakt/"),
]

# ------------------------------------------------------------------ Bausteine
ORG_ID = SITE + "/#organization"
FOUNDER_ID = SITE + "/#founder"
WEBSITE_ID = SITE + "/#website"


def base_graph():
    return [
        {
            "@type": "Organization",
            "@id": ORG_ID,
            "name": BRAND,
            "url": SITE + "/",
            "logo": {"@type": "ImageObject", "url": SITE + "/icon-512.png", "width": 512, "height": 512},
            "image": OG_IMAGE,
            "email": EMAIL,
            "telephone": PHONE_TEL,
            "slogan": "Ich bin kein Unternehmer, ich bin Übernehmer.",
            "description": "Kurzform-Videos, Imagefilme, Ghostwriting, Social-Media-Betreuung und Creator-Management für Unternehmen und Personen.",
            "founder": {"@id": FOUNDER_ID},
            "sameAs": [INSTAGRAM],
            "areaServed": {"@type": "Country", "name": "Deutschland"},
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer service",
                "telephone": PHONE_TEL,
                "email": EMAIL,
                "availableLanguage": "German",
            },
        },
        {
            "@type": "Person",
            "@id": FOUNDER_ID,
            "name": OWNER,
            "jobTitle": "Gründer",
            "image": SITE + "/assets/img/portrait-1040.jpg",
            "worksFor": {"@id": ORG_ID},
        },
        {
            "@type": "WebSite",
            "@id": WEBSITE_ID,
            "url": SITE + "/",
            "name": BRAND,
            "inLanguage": "de-DE",
            "publisher": {"@id": ORG_ID},
        },
    ]


def head_html(page):
    url = SITE + page["path"]
    graph = base_graph()
    wp = {
        "@type": page.get("webpage_type", "WebPage"),
        "@id": url + "#webpage",
        "url": url,
        "name": page["title"],
        "description": page["desc"],
        "inLanguage": "de-DE",
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": ORG_ID},
        "dateModified": MODIFIED,
    }
    crumbs = page.get("crumbs")
    if crumbs:
        wp["breadcrumb"] = {"@id": url + "#breadcrumb"}
        graph.append(
            {
                "@type": "BreadcrumbList",
                "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + (link or page["path"])}
                    for i, (name, link) in enumerate(crumbs)
                ],
            }
        )
    graph.append(wp)
    graph.extend(page.get("graph", []))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

    robots = page.get("robots", "index, follow, max-image-preview:large")
    parts = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{e(page['title'])}</title>",
        f'<meta name="description" content="{e(page["desc"])}">',
        f'<meta name="robots" content="{robots}">',
        f'<link rel="canonical" href="{url}">',
        '<meta name="theme-color" content="#d4422a">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="icon" href="/favicon.ico" sizes="32x32">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
        '<link rel="manifest" href="/site.webmanifest">',
        '<link rel="preload" href="/assets/fonts/poppins-700.woff" as="font" type="font/woff" crossorigin>',
        '<link rel="preload" href="/assets/fonts/poppins-400.woff" as="font" type="font/woff" crossorigin>',
        '<link rel="stylesheet" href="/assets/css/style.css">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{BRAND}">',
        '<meta property="og:locale" content="de_DE">',
        f'<meta property="og:title" content="{e(page["title"])}">',
        f'<meta property="og:description" content="{e(page["desc"])}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{BRAND}: Ich bin kein Unternehmer. Ich bin Übernehmer.">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(page["title"])}">',
        f'<meta name="twitter:description" content="{e(page["desc"])}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
        f'<script type="application/ld+json">\n{ld}\n</script>',
    ]
    return "\n".join(parts)


def header_html(path):
    links = []
    for name, href in NAV:
        cur = ' aria-current="page"' if path == href else ""
        links.append(f'<a href="{href}"{cur}>{e(name)}</a>')
    return f"""<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{BRAND}, zur Startseite"><img src="/assets/logo/logo-h-light.svg" width="191" height="40" alt="{BRAND}"></a>
    <nav class="nav" id="hauptnavigation" aria-label="Hauptnavigation">{"".join(links)}</nav>
    <div class="header-actions">
      <a class="btn btn--light btn--small" href="tel:{PHONE_TEL}" aria-label="Jetzt anrufen: {PHONE_SHOW}">{PHONE_ICON}<span>Jetzt anrufen</span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="hauptnavigation">Menü</button>
    </div>
  </div>
</header>"""


def footer_html():
    svc = "".join(f'<li><a href="/leistungen/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/logo/logo-h-light.svg" width="220" height="46" alt="{BRAND}" loading="lazy">
        <p>Ich bin kein Unternehmer. Ich bin Übernehmer.</p>
      </div>
      <nav aria-label="Leistungen">
        <p class="footer-title">Leistungen</p>
        <ul>{svc}</ul>
      </nav>
      <nav aria-label="Seiten">
        <p class="footer-title">Seiten</p>
        <ul>
          <li><a href="/ueber-mich/">Über mich</a></li>
          <li><a href="/referenzen/">Referenzen</a></li>
          <li><a href="/kontakt/">Kontakt</a></li>
          <li><a href="/impressum/">Impressum</a></li>
          <li><a href="/datenschutz/">Datenschutz</a></li>
        </ul>
      </nav>
      <div>
        <p class="footer-title">Kontakt</p>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_SHOW}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{INSTAGRAM}" rel="noopener">Instagram {INSTAGRAM_NAME}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 {BRAND}</p>
      <p>Orange is the new black.</p>
    </div>
  </div>
</footer>"""


def page_html(page, main):
    return f"""<!doctype html>
<html lang="de">
<head>
{head_html(page)}
</head>
<body>
{header_html(page["path"])}
<main id="inhalt">
{main}
</main>
{footer_html()}
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def portrait(eager=False):
    loading = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return f"""<div class="u">
  <picture>
    <source type="image/webp" srcset="/assets/img/portrait-520.webp 520w, /assets/img/portrait-1040.webp 1040w" sizes="(max-width: 900px) 78vw, 430px">
    <img src="/assets/img/portrait-1040.jpg" width="520" height="650" alt="{e(PORTRAIT_ALT)}" {loading}>
  </picture>
</div>"""


def rows(items, link=True):
    out = []
    for href, title, text in items:
        if link:
            out.append(
                f'<li><a class="row" href="{href}"><h3 class="row__title">{e(title)}</h3>'
                f'<p class="row__text">{e(text)}</p></a></li>'
            )
        else:
            out.append(f'<li class="row"><h3 class="row__title">{e(title)}</h3><p class="row__text">{e(text)}</p></li>')
    return f'<ul class="rows">{"".join(out)}</ul>'


def service_rows(exclude=None):
    return rows([(f'/leistungen/{s["slug"]}/', s["name"], s["short"]) for s in SERVICES if s["slug"] != exclude])


def section(inner, cls=""):
    return f'<section class="section {cls}".strip()><div class="wrap">{inner}</div></section>'.replace('".strip()', '"')


def split_block(firms, people):
    return (
        '<div class="split">'
        f"<div><h3>{e(firms[0])}</h3><p>{e(firms[1])}</p></div>"
        f"<div><h3>{e(people[0])}</h3><p>{e(people[1])}</p></div>"
        "</div>"
    )


def cta_band():
    return f"""<section class="section section--orange cta">
  <div class="wrap">
    <h2><span>Würdest du einen Anruf ablehnen, der dir Aufträge bringt?</span><span class="cta__b">Ich auch nicht.</span></h2>
    <p class="actions">
      <a class="btn btn--ink" href="tel:{PHONE_TEL}">{PHONE_ICON}Jetzt anrufen: {PHONE_SHOW}</a>
      <a class="btn btn--light" href="mailto:{EMAIL}">E-Mail schreiben</a>
    </p>
  </div>
</section>"""


def crumbs_html(crumbs):
    items = []
    for name, link in crumbs[:-1]:
        items.append(f'<li><a href="{link}">{e(name)}</a></li>')
    items.append(f'<li aria-current="page">{e(crumbs[-1][0])}</li>')
    return f'<nav class="crumbs" aria-label="Brotkrumen"><ol>{"".join(items)}</ol></nav>'


def page_hero(crumbs, h1, lead, actions=True):
    act = ""
    if actions:
        act = (
            f'<p class="actions"><a class="btn btn--light" href="tel:{PHONE_TEL}">{PHONE_ICON}Jetzt anrufen</a>'
            '<a class="btn btn--line" href="/kontakt/">Kontakt aufnehmen</a></p>'
        )
    lead_html = f'<p class="lead">{e(lead)}</p>' if lead else ""
    return f"""<section class="page-hero">
  <img class="page-hero__mark" src="/assets/logo/mark-orange.svg" alt="" width="412" height="634">
  <div class="wrap">
    {crumbs_html(crumbs)}
    <h1>{e(h1)}</h1>
    {lead_html}
    {act}
  </div>
</section>"""


def faq_html(faq):
    out = []
    for q, a in faq:
        out.append(f'<details><summary>{e(q)}</summary><div class="answer"><p>{e(a)}</p></div></details>')
    return f'<div class="faq">{"".join(out)}</div>'


# ------------------------------------------------------------------ Seiten
PAGES = []


def add(path, title, desc, main, **extra):
    page = {"path": path, "title": title, "desc": desc, "main": main}
    page.update(extra)
    PAGES.append(page)


# ---- Startseite
home_main = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero__text">
      <h1><span class="hero__a">Ich bin kein Unternehmer.</span> <span class="hero__b">Ich bin Übernehmer.</span></h1>
      <p class="hero__lead">Ich übernehme deine Videos, deine Texte und deine Social-Media-Kanäle. Für Unternehmen und für Personen.</p>
      <p class="actions">
        <a class="btn btn--ink" href="tel:{PHONE_TEL}">{PHONE_ICON}Jetzt anrufen</a>
        <a class="btn btn--light" href="/leistungen/">Leistungen ansehen</a>
      </p>
    </div>
    {portrait(eager=True)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head">
      <h2>Was ich für dich übernehme</h2>
      <p>Fünf Leistungen, einzeln buchbar oder als Paket.</p>
    </div>
    {service_rows()}
  </div>
</section>

<section class="section section--line">
  <div class="wrap">
    <div class="section__head"><h2>Für Unternehmen. Und für Personen.</h2></div>
    {split_block(
        ("Unternehmen und Marken", "Du hast ein Produkt, ein Team und genug zu tun. Ich übernehme deinen Auftritt auf Social Media und liefere Videos und Texte, die zu deiner Marke passen."),
        ("Personen, Creator und Selbstständige", "Du bist das Gesicht. Ich baue deine Personal Brand mit auf, schreibe in deiner Stimme und kümmere mich um Anfragen und Kooperationen."),
    )}
  </div>
</section>

<section class="section section--ink manifest">
  <div class="wrap">
    <h2>Unternehmer gründen. Übernehmer machen.</h2>
    <p class="manifest__text">Gründen ist der Anfang. Danach kommen unzählige Aufgaben, die nichts mit deinem eigentlichen Geschäft zu tun haben, aber über dein Bild nach außen entscheiden. Genau die übernehme ich.</p>
    <div class="statements">
      <div><h3>Ich übernehme die Arbeit</h3><p>Du behältst die Kontrolle und gibst frei, was du freigeben willst.</p></div>
      <div><h3>Ein Ansprechpartner</h3><p>Du sprichst mit mir und nicht mit fünf Dienstleistern.</p></div>
      <div><h3>Klare Absprachen</h3><p>Du weißt vorher, was ich tue, in welchem Rhythmus und was ich von dir brauche.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head"><h2>So übernehme ich</h2></div>
    <ol class="steps">
      <li><h3>Anruf</h3><p>Wir sprechen über dein Ziel, deine Kanäle und das, was dich gerade Zeit kostet.</p></li>
      <li><h3>Plan</h3><p>Ich schlage dir vor, was ich übernehme, in welchem Rhythmus und in welcher Form.</p></li>
      <li><h3>Übernahme</h3><p>Ich produziere, schreibe, poste und betreue. Du gibst frei, wo du es willst.</p></li>
      <li><h3>Auswertung</h3><p>Wir schauen gemeinsam, was funktioniert, und justieren nach.</p></li>
    </ol>
  </div>
</section>

<section class="section section--line">
  <div class="wrap">
    <div class="section__head">
      <h2>Daran habe ich gearbeitet</h2>
    </div>
    {rows([
        ("", "Destín Clothing", "Markenaufbau von null an: Social-Media-Auftritt und Content für eine Modemarke."),
        ("", "Bam Bam Keb'up", "Social-Media-Auftritt für ein Food-Konzept, damit der Name bei jedem hängen bleibt."),
    ], link=False)}
    <p class="actions" style="margin-top:32px"><a class="btn btn--ink" href="/referenzen/">Alle Referenzen</a></p>
  </div>
</section>

{cta_band()}
"""
add(
    "/",
    "JUNGÜBERNEHMER – Social Media, Videos & Ghostwriting",
    "Ich übernehme deine Social-Media-Kanäle: Kurzvideos, Imagefilme, Ghostwriting und Creator-Management für Unternehmen und Personen. Jetzt anrufen.",
    home_main,
)

# ---- Leistungen (Übersicht)
leist_main = f"""
{page_hero([("Start", "/"), ("Leistungen", None)], "Was ich für dich übernehme", "Fünf Leistungen, die du einzeln oder als Paket bekommst. Alle für Unternehmen und für Personen.")}
<section class="section">
  <div class="wrap">{service_rows()}</div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="two-col">
      <div class="two-col__head"><h2>Einzeln oder zusammen</h2></div>
      <div>
        <p class="lead">Du kannst nur Videos buchen oder nur Texte. Oder du gibst mir deinen Kanal komplett.</p>
        <p>Im zweiten Fall verbinde ich alles: Videos, Texte und Betreuung aus einer Hand. Das spart dir Abstimmung und sorgt dafür, dass dein Auftritt aus einem Guss ist.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="section__head"><h2>Für Unternehmen. Und für Personen.</h2></div>
    {split_block(
        ("Unternehmen und Marken", "Ich übernehme deinen Auftritt auf Social Media und liefere Videos und Texte, die zu deiner Marke passen."),
        ("Personen, Creator und Selbstständige", "Ich baue deine Personal Brand mit auf, schreibe in deiner Stimme und kümmere mich um Anfragen und Kooperationen."),
    )}
  </div>
</section>
{cta_band()}
"""
add(
    "/leistungen/",
    "Leistungen für Social Media & Video | JUNGÜBERNEHMER",
    "Kurzform-Videos, Imagefilme, Ghostwriting, Social-Media-Betreuung und Creator-Management: Das übernehme ich für Unternehmen und Personen.",
    leist_main,
    crumbs=[("Start", "/"), ("Leistungen", "/leistungen/")],
    webpage_type="CollectionPage",
)

# ---- Einzelne Leistungen
for s in SERVICES:
    path = f'/leistungen/{s["slug"]}/'
    items = "".join(f"<div><h3>{e(n)}</h3><p>{e(t)}</p></div>" for n, t in s["items"])
    main = f"""
{page_hero([("Start", "/"), ("Leistungen", "/leistungen/"), (s["name"], None)], s["h1"], s["lead"])}
<section class="section">
  <div class="wrap">
    <div class="two-col">
      <div class="two-col__head"><h2>Das übernehme ich</h2><p>{e(s["items_intro"])}</p></div>
      <div class="items">{items}</div>
    </div>
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="section__head"><h2>Für wen ich das mache</h2></div>
    {split_block(s["firms"], s["people"])}
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="two-col">
      <div class="two-col__head"><h2>Häufige Fragen</h2></div>
      {faq_html(s["faq"])}
    </div>
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="section__head"><h2>Mehr, was ich übernehme</h2></div>
    {service_rows(exclude=s["slug"])}
  </div>
</section>
{cta_band()}
"""
    service_ld = {
        "@type": "Service",
        "@id": SITE + path + "#service",
        "name": s["name"],
        "serviceType": s["service_type"],
        "description": s["desc"],
        "url": SITE + path,
        "provider": {"@id": ORG_ID},
        "areaServed": {"@type": "Country", "name": "Deutschland"},
    }
    add(
        path, s["title"], s["desc"], main,
        crumbs=[("Start", "/"), ("Leistungen", "/leistungen/"), (s["name"], path)],
        graph=[service_ld],
    )

# ---- Über mich
about_main = f"""
{page_hero([("Start", "/"), ("Über mich", None)], "Wer übernimmt hier eigentlich?", "Ich bin Devrim, der Mensch hinter JUNGÜBERNEHMER.", actions=False)}
<section class="section">
  <div class="wrap">
    <div class="about">
      {portrait()}
      <div>
        <h2>Ich bin kein Unternehmer. Ich bin Übernehmer.</h2>
        <p class="lead">Gründen ist nicht mein Thema. Meins ist übernehmen.</p>
        <p>Ich nehme dir Aufgaben ab, die Zeit kosten und trotzdem gut gemacht sein müssen: Videos, Texte, ganze Kanäle und das Management von Creatorn.</p>
        <p>Du sprichst bei mir mit einer Person und nicht mit einem Ticketsystem. Ich sage dir, was ich übernehme und was nicht, und halte mich an das, was wir ausmachen.</p>
        <p>Und warum ist hier alles orange? Orange is the new black.</p>
        <p class="actions" style="margin-top:28px"><a class="btn btn--ink" href="tel:{PHONE_TEL}">{PHONE_ICON}Jetzt anrufen</a></p>
      </div>
    </div>
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="section__head"><h2>Daran halte ich mich</h2></div>
    <div class="statements" style="margin-top:0;border-top:0;padding-top:0">
      <div><h3>Klar</h3><p>Du weißt vorher, was ich tue, in welchem Rhythmus und was du dafür bereitstellen musst.</p></div>
      <div><h3>Verlässlich</h3><p>Absprachen gelten. Fristen auch.</p></div>
      <div><h3>Persönlich</h3><p>Ein Ansprechpartner, ein direkter Draht, kurze Wege.</p></div>
    </div>
  </div>
</section>
{cta_band()}
"""
add(
    "/ueber-mich/",
    "Über mich: Wer hinter JUNGÜBERNEHMER steckt",
    "Ich bin kein Unternehmer, ich bin Übernehmer: Das steckt hinter JUNGÜBERNEHMER, wie ich arbeite und warum bei mir alles orange ist.",
    about_main,
    crumbs=[("Start", "/"), ("Über mich", "/ueber-mich/")],
    webpage_type="AboutPage",
)

# ---- Referenzen
ref_main = f"""
{page_hero([("Start", "/"), ("Referenzen", None)], "Daran habe ich gearbeitet", "Eine Auswahl meiner Projekte. Weitere zeige ich dir gern im Gespräch.", actions=False)}
<section class="section">
  <div class="wrap">
    <div class="two-col">
      <div class="two-col__head"><h2>Destín Clothing</h2><p>Modemarke</p></div>
      <div>
        <p class="lead">Markenaufbau von null an.</p>
        <p>Bei Destín Clothing habe ich den Aufbau der Marke von Beginn an begleitet: Social-Media-Auftritt, Content und eine eigene Geschichte für eine Modemarke.</p>
        <p><strong>Schwerpunkte:</strong> Markenaufbau, Social Media, Content</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--line">
  <div class="wrap">
    <div class="two-col">
      <div class="two-col__head"><h2>Bam Bam Keb'up</h2><p>Food-Konzept</p></div>
      <div>
        <p class="lead">Ein Name, der hängen bleibt.</p>
        <p>Für Bam Bam Keb'up sorge ich dafür, dass auf dem Social-Media-Account Unterhaltung geboten wird und sich der Name bei den Leuten einprägt.</p>
        <p><strong>Schwerpunkte:</strong> Social-Media-Marketing, Food-Content, Entertainment</p>
      </div>
    </div>
  </div>
</section>
{cta_band()}
"""
add(
    "/referenzen/",
    "Referenzen und Projekte | JUNGÜBERNEHMER",
    "Eine Auswahl meiner Projekte: Markenaufbau für eine Modemarke und Social-Media-Marketing für ein Food-Konzept. Jetzt Projekt besprechen.",
    ref_main,
    crumbs=[("Start", "/"), ("Referenzen", "/referenzen/")],
)

# ---- Kontakt
contact_main = f"""
{page_hero([("Start", "/"), ("Kontakt", None)], "Sprich mit mir", "Am schnellsten geht es per Telefon. Wenn ich nicht rangehe, schreib mir kurz, worum es geht. Ich melde mich zurück.", actions=False)}
<section class="section">
  <div class="wrap">
    <div class="section__head"><h2>So erreichst du mich</h2></div>
    <ul class="rows">
      <li><a class="row" href="tel:{PHONE_TEL}"><h3 class="row__title">Telefon</h3><p class="row__text">{PHONE_SHOW}</p></a></li>
      <li><a class="row" href="mailto:{EMAIL}"><h3 class="row__title">E-Mail</h3><p class="row__text">{EMAIL}</p></a></li>
      <li><a class="row" href="{INSTAGRAM}" rel="noopener"><h3 class="row__title">Instagram</h3><p class="row__text">{INSTAGRAM_NAME}</p></a></li>
    </ul>
    <!-- Platz für ein späteres Kontaktformular: Formular hier einsetzen und die Datenschutzerklärung ergänzen. -->
  </div>
</section>
"""
add(
    "/kontakt/",
    "Kontakt: Jetzt anrufen | JUNGÜBERNEHMER",
    "Ruf an oder schreib mir: Telefon, E-Mail und Instagram von JUNGÜBERNEHMER. Ich melde mich zurück.",
    contact_main,
    crumbs=[("Start", "/"), ("Kontakt", "/kontakt/")],
    webpage_type="ContactPage",
)

# ---- Impressum
imp_main = f"""
{page_hero([("Start", "/"), ("Impressum", None)], "Impressum", "", actions=False)}
<section class="section">
  <div class="wrap">
    <div class="prose">
      <h2>Angaben gemäß § 5 DDG</h2>
      <p>{BRAND}<br>Inhaber: {OWNER}<br>{ph("Straße und Hausnummer")}<br>{ph("PLZ und Ort")}</p>

      <h2>Kontakt</h2>
      <p>Telefon: <a href="tel:{PHONE_TEL}">{PHONE_SHOW}</a><br>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

      <h2>Umsatzsteuer</h2>
      <p>Gemäß § 19 UStG wird keine Umsatzsteuer berechnet (Kleinunternehmerregelung). Eine Umsatzsteuer-Identifikationsnummer wird deshalb nicht geführt.</p>

      <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
      <p>{OWNER}, Anschrift wie oben.</p>

      <h2>Verbraucherstreitbeilegung</h2>
      <p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

      <h2>Haftung für Inhalte</h2>
      <p>Als Diensteanbieter bin ich für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Bei bekannt werdenden Rechtsverletzungen entferne ich die betreffenden Inhalte umgehend.</p>

      <h2>Haftung für Links</h2>
      <p>Diese Seite enthält Links zu externen Webseiten Dritter, auf deren Inhalte ich keinen Einfluss habe. Für diese fremden Inhalte kann ich keine Gewähr übernehmen. Verantwortlich ist stets der jeweilige Anbieter. Bei Bekanntwerden von Rechtsverletzungen entferne ich solche Links umgehend.</p>

      <h2>Urheberrecht</h2>
      <p>Die Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Eine Vervielfältigung, Bearbeitung oder Verbreitung bedarf meiner schriftlichen Zustimmung.</p>
    </div>
  </div>
</section>
"""
add(
    "/impressum/",
    "Impressum | JUNGÜBERNEHMER",
    "Impressum und Anbieterkennzeichnung von JUNGÜBERNEHMER, Inhaber Devrim Can Barkin.",
    imp_main,
    crumbs=[("Start", "/"), ("Impressum", "/impressum/")],
)

# ---- Datenschutz
dsg_main = f"""
{page_hero([("Start", "/"), ("Datenschutz", None)], "Datenschutzerklärung", "", actions=False)}
<section class="section">
  <div class="wrap">
    <div class="prose">
      <h2>1. Verantwortlicher</h2>
      <p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:<br>{OWNER}, {BRAND}<br>{ph("Straße und Hausnummer")}, {ph("PLZ und Ort")}<br>Telefon: {PHONE_SHOW}<br>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

      <h2>2. Hosting und Server-Logfiles</h2>
      <p>Diese Website wird bei folgendem Anbieter gehostet: {ph("Name und Anschrift des Hosting-Anbieters eintragen")}.</p>
      <p>Beim Aufruf der Seiten verarbeitet der Hosting-Anbieter automatisch technische Daten in Server-Logfiles: IP-Adresse, Datum und Uhrzeit des Abrufs, aufgerufene Seite, Browsertyp und Betriebssystem sowie die zuvor besuchte Seite. Das ist nötig, um die Seite auszuliefern und sicher zu betreiben. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einem stabilen und sicheren Betrieb). Die Logfiles werden nach kurzer Zeit gelöscht, sofern der Hosting-Anbieter nichts anderes angibt.</p>

      <h2>3. Keine Cookies, kein Tracking</h2>
      <p>Diese Website setzt keine Cookies und nutzt keine Analyse-, Tracking- oder Werbedienste. Die verwendete Schriftart wird von diesem Server geladen. Es findet keine Verbindung zu Google Fonts oder anderen Schriftdiensten statt.</p>

      <h2>4. Kontakt per Telefon oder E-Mail</h2>
      <p>Wenn du mich anrufst oder mir schreibst, verarbeite ich deine Angaben (zum Beispiel Name, Telefonnummer, E-Mail-Adresse und den Inhalt deiner Nachricht), um deine Anfrage zu bearbeiten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn es um einen Vertrag oder vorvertragliche Maßnahmen geht, sonst Art. 6 Abs. 1 lit. f DSGVO. Ich lösche deine Daten, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

      <h2>5. Links zu anderen Anbietern</h2>
      <p>Diese Website enthält Links zu Instagram. Es werden keine Inhalte von dort eingebunden. Erst wenn du einen Link anklickst, wechselst du zum jeweiligen Anbieter. Ab dann gilt dessen Datenschutzerklärung.</p>

      <h2>6. Verschlüsselung</h2>
      <p>Diese Seite nutzt aus Sicherheitsgründen eine TLS-Verschlüsselung. Du erkennst sie am Schloss-Symbol und an „https“ in der Adresszeile.</p>

      <h2>7. Deine Rechte</h2>
      <p>Du hast das Recht auf Auskunft über deine gespeicherten Daten (Art. 15 DSGVO), auf Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch gegen die Verarbeitung (Art. 21). Eine erteilte Einwilligung kannst du jederzeit mit Wirkung für die Zukunft widerrufen. Schreib dafür an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <p>Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel bei der Behörde deines Wohnorts.</p>

      <h2>8. Stand</h2>
      <p>Stand: Oktober 2026. Ich passe diese Erklärung an, wenn sich die Website oder die Rechtslage ändert.</p>
    </div>
  </div>
</section>
"""
add(
    "/datenschutz/",
    "Datenschutzerklärung | JUNGÜBERNEHMER",
    "Datenschutzerklärung von JUNGÜBERNEHMER: keine Cookies, kein Tracking, Schriften lokal gehostet. So gehe ich mit deinen Daten um.",
    dsg_main,
    crumbs=[("Start", "/"), ("Datenschutz", "/datenschutz/")],
)

# ------------------------------------------------------------------ Schreiben
SITEMAP_PRIORITY = {"/": "1.0", "/leistungen/": "0.9", "/impressum/": "0.2", "/datenschutz/": "0.2"}


def write(rel, content):
    target = ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def main():
    for page in PAGES:
        rel = "index.html" if page["path"] == "/" else page["path"].strip("/") + "/index.html"
        write(rel, page_html(page, page["main"]))

    # 404-Seite (nicht indexieren)
    nf_page = {
        "path": "/404.html",
        "title": "Seite nicht gefunden | JUNGÜBERNEHMER",
        "desc": "Diese Seite gibt es nicht. Zur Startseite, zu den Leistungen oder gleich anrufen.",
        "robots": "noindex, follow",
    }
    nf_main = f"""
<section class="section section--ink notfound">
  <div class="wrap">
    <h1>404. Hier gibt es nichts zu übernehmen.</h1>
    <p>Die Seite, die du suchst, gibt es nicht (mehr). Von hier aus kommst du weiter:</p>
    <p class="actions">
      <a class="btn btn--light" href="/">Zur Startseite</a>
      <a class="btn btn--line" href="/leistungen/">Leistungen</a>
      <a class="btn btn--line" href="tel:{PHONE_TEL}">Jetzt anrufen</a>
    </p>
  </div>
</section>
"""
    write("404.html", page_html(nf_page, nf_main))

    urls = []
    for page in PAGES:
        prio = SITEMAP_PRIORITY.get(page["path"], "0.8" if page["path"].startswith("/leistungen/") else "0.6")
        urls.append(
            f"  <url>\n    <loc>{SITE}{page['path']}</loc>\n    <lastmod>{MODIFIED}</lastmod>\n    <priority>{prio}</priority>\n  </url>"
        )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(PAGES) + 1} Seiten, sitemap.xml und robots.txt geschrieben.")


if __name__ == "__main__":
    main()
