from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).parent
EVENT = {
    'title': 'Track Day Motos — Autódromo de Tocancipá',
    'slug': 'track-day-motos-autodromo-de-tocancipa-julio-2026',
    'date': '12 de julio de 2026',
    'iso': '2026-07-12T08:00:00-05:00',
    'time': '08:00 – 17:00',
    'venue': 'Autódromo de Tocancipá',
    'city': 'Tocancipá, Cundinamarca',
    'organizer': 'Organizador demo Konvoka',
    'cover': 'Imagen/cover configurada por el organizer',
    'video': 'Video promocional configurado por el organizer',
    'description': 'Data demo para validar cómo una landing pública premium puede transformar el mismo evento sin romper SEO, AI SEO ni checkout.',
}

TEMPLATES = [
    dict(id='classic', short='Classic', name='Classic Editorial', theme='light', accent='#4f46e5', archetype='Concierge editorial', hero='Una página sobria que convierte información dispersa en una invitación clara.', layout='dossier', visual='timeline', sections=['Resumen', 'Detalles', 'Entradas', 'Ubicación'], chips=['Cover arriba', 'Datos esenciales', 'FAQ visible'], insight='Apple/Stripe: silencio visual, tipografía fuerte, CTA reservado.'),
    dict(id='racing', short='Racing', name='Racing Pit Lane', theme='dark', accent='#ef4444', archetype='Pit lane cinematic', hero='La emoción de entrar a pista, con seguridad y logística antes de comprar.', layout='pit', visual='track', sections=['Briefing', 'Agenda', 'Seguridad', 'Tickets'], chips=['Pista visual', 'Reglas claras', 'CTA agresivo'], insight='BMW/F1: ángulos, contraste, specs y sensación de paddock.'),
    dict(id='conference', short='Conference', name='Conference Intelligence', theme='ink', accent='#2563eb', archetype='Executive agenda', hero='Un evento profesional presentado como agenda curada, no como flyer.', layout='agenda', visual='grid', sections=['Tema', 'Agenda', 'Hosts', 'Registro'], chips=['Pase digital', 'Programa', 'Datos para búsqueda'], insight='TED/Stripe: editorial + agenda extractable para SEO/LLMs.'),
    dict(id='workshop', short='Workshop', name='Workshop Studio', theme='paper', accent='#7c3aed', archetype='Learning studio', hero='Un taller se entiende mejor como transformación: llegas con dudas, sales con una habilidad.', layout='notebook', visual='badge', sections=['Aprenderás', 'Nivel', 'Materiales', 'Entradas'], chips=['Outcomes', 'Requisitos', 'Fit antes de pagar'], insight='Notion/Coursera-style: módulos, checklist y progreso.'),
    dict(id='music', short='Music', name='Music Backstage', theme='neon', accent='#ec4899', archetype='Backstage pass', hero='Una landing que se siente como entrar por backstage: lineup, venue y ticket al alcance.', layout='poster', visual='stage', sections=['Lineup', 'Venue', 'Galería', 'Boletas'], chips=['Poster hero', 'Lineup', 'Compra social'], insight='DICE/Spotify/Runway: oscuro, poster, waveform y energía social.'),
    dict(id='meetup', short='Meetup', name='Community Signal', theme='warm', accent='#0891b2', archetype='Community map', hero='El usuario necesita sentir quién convoca, por qué vale llegar y qué pasa al entrar.', layout='map', visual='pulse', sections=['Propósito', 'Dinámica', 'Organizer', 'Registro'], chips=['Tono humano', 'Mapa social', 'Baja fricción'], insight='Luma/Airbnb: confianza, comunidad y tarjetas cálidas.'),
    dict(id='premium', short='Premium', name='Premium Black Card', theme='luxury', accent='#b45309', archetype='Private invitation', hero='Menos ruido, más estatus: la experiencia se siente valiosa antes del checkout.', layout='invite', visual='crest', sections=['Experiencia', 'Dress code', 'Lugar', 'Accesos'], chips=['Black card', 'Editorial VIP', 'Sin falsa escasez'], insight='Apple luxury/BMW: escena oscura, detalles finos y copy mínimo.'),
    dict(id='family', short='Family', name='Family Day Map', theme='sun', accent='#16a34a', archetype='Local fair map', hero='Una página amable para familias: horarios, actividades y ubicación sin fricción.', layout='playmap', visual='map', sections=['Actividades', 'Horarios', 'Mapa', 'Entradas'], chips=['Muy legible', 'Touch friendly', 'Mapa primero'], insight='Airbnb/parks: claridad, tarjetas redondas y colores amables.'),
    dict(id='sports', short='Sports', name='Sports Bracket', theme='sport', accent='#ea580c', archetype='Tournament command center', hero='Categorías, reglas y agenda como tablero competitivo para decidir rápido.', layout='scoreboard', visual='track', sections=['Categorías', 'Reglas', 'Agenda', 'Inscripción'], chips=['Marcador', 'Bracket', 'Reglas visibles'], insight='ESPN/Nike: tablero, números grandes, ritmo competitivo.'),
    dict(id='minimal_checkout', short='Fast', name='Fast Checkout Sheet', theme='clean', accent='#0f172a', archetype='Commerce-first', hero='Para tráfico de WhatsApp o Instagram: primero tickets, luego contexto suficiente.', layout='commerce', visual='pulse', sections=['Tickets', 'Datos', 'Mapa', 'FAQ'], chips=['Tickets arriba', 'Menos lectura', 'CTA persistente'], insight='Shopify/Apple checkout: foco extremo en compra y confianza.'),
]

EVENTS = {
    'classic': ('Cena privada de founders — Bogotá', 'Casa República', 'Bogotá, Colombia', [('General', 'Invitación + networking', '$180.000'), ('Mesa sponsor', 'Mesa reservada + branding', '$900.000')]),
    'racing': ('Track Day Motos — Autódromo de Tocancipá', 'Autódromo de Tocancipá', 'Tocancipá, Cundinamarca', [('General', 'Acceso a pista + zona común', '$120.000'), ('Paddock', 'Zona paddock + briefing prioritario', '$220.000')]),
    'conference': ('AI Ops Summit Latam 2026', 'Centro de Convenciones Ágora', 'Bogotá, Colombia', [('Conference Pass', 'Charlas + expo hall', '$340.000'), ('Executive', 'Workshops + lounge', '$720.000')]),
    'workshop': ('Workshop No-Code Automations', 'Konvoka Studio', 'Medellín, Colombia', [('Learner', 'Taller + materiales', '$160.000'), ('Team Pack', '3 accesos + sesión Q&A', '$420.000')]),
    'music': ('Noches Backstage: Indie & Synth', 'Bodega Cultural', 'Bogotá, Colombia', [('General', 'Ingreso al venue', '$90.000'), ('Backstage VIP', 'Front stage + meet & greet', '$260.000')]),
    'meetup': ('Founders & Builders Meetup', 'Casa Creator', 'Bogotá, Colombia', [('Community', 'Networking + bebidas', '$45.000'), ('Host Table', 'Mesa compartida + intros', '$120.000')]),
    'premium': ('Gala Black Card — Cena & Subasta', 'Club El Nogal', 'Bogotá, Colombia', [('Invitado', 'Cena + ceremonia', '$380.000'), ('Mesa VIP', 'Mesa privada 6 personas', '$1.800.000')]),
    'family': ('Family Day en el Parque', 'Parque Museo Chicó', 'Bogotá, Colombia', [('Niño', 'Actividades guiadas', '$35.000'), ('Familia', '2 adultos + 2 niños', '$110.000')]),
    'sports': ('Copa Urbana 5K & Teams', 'Parque Simón Bolívar', 'Bogotá, Colombia', [('Runner', 'Kit + chip', '$75.000'), ('Team', '4 corredores + carpa', '$260.000')]),
    'minimal_checkout': ('Masterclass Express: Ventas por WhatsApp', 'Online en vivo', 'Latam', [('Acceso', 'Clase en vivo', '$39.000'), ('Acceso + replay', 'Clase + grabación 30 días', '$69.000')]),
}

def event_for(t):
    title, venue, city, tickets = EVENTS.get(t['id'], (EVENT['title'], EVENT['venue'], EVENT['city'], [('General','Acceso estándar','$120.000'),('VIP','Acceso preferente','$220.000')]))
    ev = dict(EVENT)
    ev.update(title=title, venue=venue, city=city, tickets=tickets)
    return ev

def render_tickets(t):
    ev = event_for(t)
    labels = []
    for i, (name, desc, price) in enumerate(ev['tickets']):
        labels.append(f'<label><span><b>{e(name)}</b><small>{e(desc)}</small></span><strong>{e(price)}</strong><input type="number" min="0" max="6" value="{1 if i == 0 else 0}" aria-label="Cantidad {e(name)}"></label>')
    return '<form class="ticket-panel" aria-label="Selector de tickets demo"><div class="ticket-head"><span>Entradas configuradas</span><strong>Checkout Konvoka</strong></div>' + ''.join(labels) + '<button class="cta" type="button" data-open-modal>Asegurar mi lugar</button><p>Usa tickets, precios, cupos, descuentos y reglas reales del backend. El template no inventa data.</p></form>'

def nav(current):
    return '<nav class="top" aria-label="Templates"><a class="brand" href="../../">Konvoka<span>VIP templates</span></a><div class="rail">' + ''.join(
        f'<a class="{ "on" if t["id"] == current else "" }" href="../{t["id"]}/">{e(t["short"])}</a>' for t in TEMPLATES
    ) + '</div></nav>'

def visual(t):
    v = t['visual']
    if v == 'track':
        inner = '<path class="draw" d="M30 210 C64 82 142 56 192 126 C236 188 292 158 332 48"/><g><circle cx="64" cy="178" r="15"/><circle cx="194" cy="126" r="20"/><circle cx="304" cy="76" r="14"/></g><text x="34" y="42">PIT · GRID · CHECKOUT</text>'
    elif v == 'stage':
        inner = '<path class="draw" d="M40 218 L92 72 L178 160 L266 72 L322 218"/><g class="bars"><rect x="72" y="130" width="28" height="76"/><rect x="160" y="92" width="34" height="114"/><rect x="252" y="142" width="28" height="64"/></g><text x="42" y="46">BACKSTAGE PASS</text>'
    elif v == 'grid':
        inner = ''.join(f'<rect x="{40+(i%3)*90}" y="{58+(i//3)*54}" width="64" height="36" rx="4"/>' for i in range(9)) + '<path class="draw" d="M72 76 H252 M72 130 H252 M72 184 H252"/><text x="40" y="36">AGENDA SYSTEM</text>'
    elif v == 'badge':
        inner = '<path class="draw" d="M180 30 L300 92 L282 216 L180 244 L78 216 L60 92 Z"/><path d="M112 136 H248 M112 166 H224 M112 196 H196"/><circle cx="180" cy="96" r="30"/><text x="116" y="52">OUTCOMES</text>'
    elif v == 'map':
        inner = '<path class="draw" d="M50 80 C112 32 144 132 188 82 C238 26 292 104 324 62 M54 194 C116 138 176 226 238 154 C270 118 304 152 330 118"/><g><circle cx="88" cy="82" r="12"/><circle cx="188" cy="82" r="16"/><circle cx="304" cy="118" r="12"/></g><text x="44" y="38">ARRIVAL MAP</text>'
    elif v == 'crest':
        inner = '<path class="draw" d="M180 28 L294 94 V190 L180 242 L66 190 V94 Z"/><path d="M180 66 L250 106 V170 L180 204 L110 170 V106 Z"/><text x="135" y="152" class="crest">VIP</text>'
    elif v == 'pulse':
        inner = '<path class="draw" d="M34 142 H96 L124 98 L154 198 L186 62 L218 142 H326"/><g><circle cx="96" cy="142" r="12"/><circle cx="186" cy="62" r="16"/><circle cx="286" cy="142" r="12"/></g><text x="42" y="42">LIVE SIGNAL</text>'
    else:
        inner = '<path class="draw" d="M58 190 C92 118 132 106 166 142 C204 184 250 158 306 74"/><circle cx="70" cy="184" r="13"/><circle cx="166" cy="142" r="16"/><circle cx="306" cy="74" r="13"/><text x="42" y="44">EVENT DOSSIER</text>'
    return f'<div class="signature" aria-hidden="true"><svg viewBox="0 0 360 270" focusable="false">{inner}</svg></div>'

def config_blocks(ev):
    blocks = [
        ('Historia', ev['title'], ev['description']),
        ('Media', ev['cover'], ev['video']),
        ('Logística', f"{ev['date']} · {ev['time']}", f"{ev['venue']} · {ev['city']}"),
        ('Organizer', ev['organizer'], 'Políticas, restricciones, agenda y FAQ salen de la configuración real.'),
    ]
    return ''.join(f'<article><span>{e(a)}</span><h3>{e(b)}</h3><p>{e(c)}</p></article>' for a,b,c in blocks)

def story(t):
    return f'''<section class="story story-{t['layout']}" aria-label="Experiencia temática">
      <div class="story-copy"><p class="kicker">{e(t['archetype'])}</p><h2>{e(t['name'])} no es un cambio de color: es una escena distinta.</h2><p>{e(t['hero'])}</p></div>
      <div class="modules">{''.join(f'<article><b>{i+1:02}</b><span>{e(s)}</span></article>' for i,s in enumerate(t['sections']))}</div>
    </section>'''

def page(t):
    ev = event_for(t)
    ticket_html = render_tickets(t)
    cards = ''.join(f'<li>{e(x)}</li>' for x in t['chips'])
    offers = [{'@type': 'Offer', 'name': name, 'price': price.replace('$','').replace('.',''), 'priceCurrency': 'COP'} for name, _, price in ev['tickets']]
    schema = json.dumps({'@context':'https://schema.org','@type':'Event','name':ev['title'],'eventStatus':'https://schema.org/EventScheduled','eventAttendanceMode':'https://schema.org/OfflineEventAttendanceMode','startDate':ev['iso'],'location':{'@type':'Place','name':ev['venue'],'address':ev['city']},'organizer':{'@type':'Organization','name':ev['organizer']},'offers':offers,'description':f"Preview temporal de template {t['name']} para landing de evento Konvoka."}, ensure_ascii=False)
    return f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(t['name'])} · Konvoka VIP templates</title><meta name="description" content="Preview premium del template {e(t['name'])}: landing pública de evento con SEO, AI SEO, selector de tickets y checkout Konvoka."><link rel="canonical" href="https://tononabot.github.io/konvoka-template-preview/templates/{t['id']}/"><meta name="robots" content="noindex, follow"><meta property="og:title" content="{e(t['name'])} · Konvoka"><meta property="og:description" content="Template público de evento con diseño temático, ticket selector y checkout handoff."><meta property="og:type" content="website"><meta name="twitter:card" content="summary"><link rel="stylesheet" href="../../styles.css"><script type="application/ld+json">{schema}</script></head>
<body class="theme-{t['theme']} tpl-{t['id']}" style="--accent:{t['accent']}"><a class="skip" href="#contenido">Saltar al contenido</a>{nav(t['id'])}<main id="contenido">
<section class="preview-note"><strong>Preview temporal premium.</strong> Data demo temática; cada template cambia contenido, composición, narrativa, módulos y estética.</section>
<header class="hero hero-{t['layout']}"><div class="hero-copy"><p class="kicker">{e(t['archetype'])}</p><h1>{e(ev['title'])}</h1><p class="lead">{e(t['hero'])}</p><dl class="facts"><div><dt>Fecha</dt><dd>{ev['date']}</dd></div><div><dt>Lugar</dt><dd>{e(ev['venue'])}</dd></div><div><dt>Organizer</dt><dd>{e(ev['organizer'])}</dd></div></dl><ul class="chips">{cards}</ul><a class="cta hero-cta" href="#tickets">Asegurar mi lugar</a></div>{visual(t)}<aside class="hero-checkout">{ticket_html}</aside></header>
{story(t)}
<section class="config" aria-labelledby="config-title"><div><p class="kicker">Organizer data-safe</p><h2 id="config-title">Todo lo que configura el organizer aparece, sin inventar nada.</h2><p>El diseño puede ser VIP, pero la fuente de verdad sigue siendo el evento: historia, media, logística, tickets, reglas, FAQ, formularios, descuentos y checkout.</p></div><div class="config-grid">{config_blocks(ev)}</div></section>
<section id="tickets" class="checkout-zone" aria-labelledby="tickets-title"><div><p class="kicker">Mandatory checkout</p><h2 id="tickets-title">Seleccionar tickets → Asegurar mi lugar</h2><p>Este módulo es compartido por todos los templates. En producción usa IDs reales de tickets, disponibilidad y la ruta actual de checkout.</p></div>{ticket_html}</section>
<section class="ai-seo"><h2>Resumen factual para SEO + AI SEO</h2><p>{e(ev['title'])} ocurre el {ev['date']} en {e(ev['venue'])}, {e(ev['city'])}. El template {e(t['name'])} conserva nombre, fecha, lugar, organizer, tickets, FAQ, ubicación y CTA de checkout en HTML semántico y Schema.org Event.</p><details><summary>¿Este template cambia los tickets?</summary><p>No. Solo cambia presentación. Tickets, precios, cupos y checkout salen del backend.</p></details><details><summary>¿Qué debe degradar si falta data?</summary><p>Media, lineup, speakers, dress code o actividades se ocultan si el organizer no los configuró. Nunca se rellenan con ficción.</p></details></section>
</main><footer><a href="../../">Volver al índice</a><p>{e(t['insight'])}</p></footer><div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden><div class="modal-card"><h2 id="modal-title">Checkout simulado</h2><p>En Konvoka real este paso conserva la selección y redirige/abre el checkout actual. Esta URL es solo preview visual.</p><button class="cta" data-close-modal>Cerrar</button></div></div><script src="../../script.js" defer></script></body></html>'''


def index():
    cards = ''.join(f'<article class="index-card theme-{t["theme"]}" style="--accent:{t["accent"]}"><span>{e(t["archetype"])}</span><h2>{e(t["name"])}</h2><p>{e(t["hero"])}</p><a class="cta" href="templates/{t["id"]}/">Ver template</a></article>' for t in TEMPLATES)
    return f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Konvoka VIP template research preview</title><meta name="description" content="10 previews premium y temáticos para landings públicas de eventos Konvoka."><meta name="robots" content="noindex, follow"><link rel="stylesheet" href="styles.css"></head><body class="theme-clean"><a class="skip" href="#contenido">Saltar al contenido</a><main id="contenido" class="index"><p class="kicker">Research-led preview</p><h1>10 direcciones visuales VIP para un mismo evento Konvoka</h1><p class="lead">Ya no son skins de color: cada template tiene composición, narrativa, módulos y atmósfera propia, preservando SEO, AI SEO, tickets y “Asegurar mi lugar”.</p><div class="index-grid">{cards}</div></main><footer><p>Preview temporal. Data demo. No procesa pagos.</p></footer></body></html>'''

(ROOT / 'index.html').write_text(index())
for t in TEMPLATES:
    d = ROOT / 'templates' / t['id']
    d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(page(t))
(ROOT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
print(f'generated {len(TEMPLATES)} premium template pages')
