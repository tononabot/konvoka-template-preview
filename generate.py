from pathlib import Path
from html import escape as h
import json

ROOT = Path(__file__).parent
BASE = {
    'date': '12 de julio de 2026', 'iso': '2026-07-12T08:00:00-05:00', 'time': '08:00 – 17:00',
    'organizer': 'Organizador del evento', 'description': 'Landing pública del evento con información, entradas y checkout oficial.'
}
TEMPLATES = [
    {'id':'classic','short':'Classic','name':'Classic Editorial','tone':'Invitación editorial','event':'Cena privada de founders — Bogotá','venue':'Casa República','city':'Bogotá','theme':'classic','accent':'#5b5bd6','tickets':[('Invitado','Acceso + networking','$180.000'),('Mesa sponsor','Mesa reservada + branding','$900.000')]},
    {'id':'racing','short':'Racing','name':'Racing Pit Lane','tone':'Track day de alto desempeño','event':'Track Day Motos — Tocancipá','venue':'Autódromo de Tocancipá','city':'Tocancipá','theme':'racing','accent':'#ff3434','tickets':[('General','Acceso a pista + zona común','$120.000'),('Paddock','Briefing + paddock prioritario','$220.000')]},
    {'id':'conference','short':'Conference','name':'Conference Intelligence','tone':'Summit ejecutivo','event':'AI Ops Summit Latam 2026','venue':'Ágora Bogotá','city':'Bogotá','theme':'conference','accent':'#3b82f6','tickets':[('Conference Pass','Charlas + expo hall','$340.000'),('Executive','Workshops + lounge','$720.000')]},
    {'id':'workshop','short':'Workshop','name':'Workshop Studio','tone':'Aprendizaje práctico','event':'Workshop No‑Code Automations','venue':'Konvoka Studio','city':'Medellín','theme':'workshop','accent':'#7c3aed','tickets':[('Learner','Taller + materiales','$160.000'),('Team Pack','3 accesos + Q&A','$420.000')]},
    {'id':'music','short':'Music','name':'Music Backstage','tone':'Noche de club y lineup','event':'Noches Backstage: Indie & Synth','venue':'Bodega Cultural','city':'Bogotá','theme':'music','accent':'#f72585','tickets':[('General','Ingreso al venue','$90.000'),('Backstage VIP','Front stage + meet & greet','$260.000')]},
    {'id':'meetup','short':'Meetup','name':'Community Signal','tone':'Encuentro de comunidad','event':'Founders & Builders Meetup','venue':'Casa Creator','city':'Bogotá','theme':'meetup','accent':'#0891b2','tickets':[('Community','Networking + bebidas','$45.000'),('Host Table','Mesa compartida + intros','$120.000')]},
    {'id':'premium','short':'Premium','name':'Premium Black Card','tone':'Invitación privada','event':'Gala Black Card — Cena & Subasta','venue':'Club El Nogal','city':'Bogotá','theme':'premium','accent':'#c79a48','tickets':[('Invitado','Cena + ceremonia','$380.000'),('Mesa VIP','Mesa privada 6 personas','$1.800.000')]},
    {'id':'family','short':'Family','name':'Family Day Map','tone':'Plan familiar claro','event':'Family Day en el Parque','venue':'Parque Museo Chicó','city':'Bogotá','theme':'family','accent':'#22a45d','tickets':[('Niño','Actividades guiadas','$35.000'),('Familia','2 adultos + 2 niños','$110.000')]},
    {'id':'sports','short':'Sports','name':'Sports Bracket','tone':'Competencia urbana','event':'Copa Urbana 5K & Teams','venue':'Parque Simón Bolívar','city':'Bogotá','theme':'sports','accent':'#ff7a1a','tickets':[('Runner','Kit + chip','$75.000'),('Team','4 corredores + carpa','$260.000')]},
    {'id':'minimal_checkout','short':'Fast','name':'Fast Checkout Sheet','tone':'Compra directa','event':'Masterclass Express: Ventas por WhatsApp','venue':'Online en vivo','city':'Latam','theme':'fast','accent':'#111827','tickets':[('Acceso','Clase en vivo','$39.000'),('Acceso + replay','Grabación 30 días','$69.000')]},
]

def ev(t):
    d = dict(BASE); d.update(t); return d

def checkout(t, compact=False):
    rows = ''.join(f'<label class="ticket-row"><span><b>{h(n)}</b><small>{h(desc)}</small></span><strong>{h(price)}</strong><input type="number" min="0" max="8" value="{1 if i==0 else 0}" aria-label="Cantidad {h(n)}"></label>' for i,(n,desc,price) in enumerate(t['tickets']))
    cls = 'checkout compact' if compact else 'checkout'
    return f'<form class="{cls}" aria-label="Seleccionar entradas"><div class="checkout-title"><span>Entradas</span><strong>{h(t["event"])}</strong></div>{rows}<button class="cta" type="button" data-open-modal>Asegurar mi lugar</button><p>Selecciona tus entradas y continúa al pago seguro.</p></form>'

def mini_nav(cur):
    links = ''.join(f'<a class="{("on" if x["id"]==cur else "")}" href="../{x["id"]}/">{h(x["short"])}</a>' for x in TEMPLATES)
    return f'<aside class="preview-switch"><details><summary>Ver otros diseños</summary><nav aria-label="Otros templates">{links}</nav></details></aside>'

def svg(kind):
    if kind=='track': body='<path d="M30 210 C70 50 165 42 198 120 C226 184 292 156 330 54"/><circle cx="74" cy="158" r="16"/><circle cx="198" cy="120" r="18"/><circle cx="306" cy="82" r="14"/><text x="35" y="42">GRID  /  PIT  /  LAP</text>'
    elif kind=='music': body='<path d="M42 215 L90 82 L160 160 L236 70 L318 214"/><rect x="74" y="136" width="26" height="62"/><rect x="150" y="104" width="30" height="94"/><rect x="250" y="126" width="26" height="72"/><text x="38" y="46">BACKSTAGE</text>'
    elif kind=='agenda': body=''.join(f'<rect x="{38+(i%2)*148}" y="{50+(i//2)*48}" width="118" height="32" rx="4"/>' for i in range(6))+'<path d="M180 46 V220"/><text x="38" y="34">AGENDA</text>'
    elif kind=='map': body='<path d="M52 82 C118 28 150 136 190 84 C244 20 292 118 330 64 M56 200 C118 138 176 226 236 158 C272 118 304 152 330 118"/><circle cx="90" cy="82" r="14"/><circle cx="190" cy="84" r="16"/><circle cx="304" cy="118" r="13"/><text x="42" y="42">MAPA</text>'
    elif kind=='badge': body='<path d="M180 28 L302 94 L280 218 L180 246 L80 218 L58 94 Z"/><circle cx="180" cy="100" r="32"/><path d="M110 146 H252 M110 174 H226 M110 202 H196"/><text x="126" y="54">STUDIO</text>'
    elif kind=='crest': body='<path d="M180 28 L296 96 V190 L180 244 L64 190 V96 Z"/><path d="M180 72 L244 108 V170 L180 206 L116 170 V108 Z"/><text x="130" y="158">VIP</text>'
    elif kind=='score': body='<rect x="38" y="48" width="284" height="160"/><path d="M40 116 H322 M132 48 V208 M226 48 V208"/><text x="58" y="94">05</text><text x="156" y="94">KM</text><text x="248" y="94">RUN</text>'
    elif kind=='phone': body='<rect x="104" y="28" width="152" height="220" rx="26"/><path d="M128 82 H232 M128 128 H232 M128 174 H202"/><circle cx="180" cy="218" r="10"/><text x="104" y="18">FAST PASS</text>'
    else: body='<path d="M66 200 C92 112 134 106 168 142 C204 180 254 148 306 74"/><circle cx="70" cy="194" r="13"/><circle cx="168" cy="142" r="16"/><circle cx="306" cy="74" r="13"/><text x="42" y="44">DOSSIER</text>'
    return f'<svg class="art" viewBox="0 0 360 270" aria-hidden="true" focusable="false">{body}</svg>'

def facts(t):
    return f'<ul class="facts"><li><span>Fecha</span><b>{t["date"]}</b></li><li><span>Hora</span><b>{t["time"]}</b></li><li><span>Lugar</span><b>{h(t["venue"])}</b></li></ul>'

def schema(t):
    offers=[{'@type':'Offer','name':n,'price':p.replace('$','').replace('.',''),'priceCurrency':'COP'} for n,_,p in t['tickets']]
    return json.dumps({'@context':'https://schema.org','@type':'Event','name':t['event'],'startDate':t['iso'],'eventStatus':'https://schema.org/EventScheduled','eventAttendanceMode':'https://schema.org/OfflineEventAttendanceMode','location':{'@type':'Place','name':t['venue'],'address':t['city']},'organizer':{'@type':'Organization','name':t['organizer']},'offers':offers,'description':t['description']}, ensure_ascii=False)

def layout(t):
    i=t['id']
    if i=='racing':
        return f'<header class="race-hero"><div class="speed"><span>Track Day</span><h1>{h(t["event"])}</h1><p>Briefing, pista, paddock y acceso en una experiencia diseñada para pilotos que quieren claridad antes de llegar al autódromo.</p><a class="cta" href="#tickets">Asegurar mi lugar</a></div><div class="race-card">{svg("track")}<div class="lap"><b>08:00</b><span>Briefing obligatorio</span></div></div></header><section class="pit-grid"><article><b>01</b><h2>Briefing</h2><p>Reglas de pista, grupos y seguridad visibles antes de comprar.</p></article><article><b>02</b><h2>Tandas</h2><p>Horario y cupos por categoría según configuración del organizer.</p></article><article><b>03</b><h2>Paddock</h2><p>Accesos diferenciados, beneficios y restricciones por ticket.</p></article></section><section id="tickets" class="ticket-stage">{checkout(t)}</section>'
    if i=='music':
        return f'<header class="poster-hero"><div class="poster">{svg("music")}<p>Indie · Synth · Live set</p></div><div><p class="eyebrow">Backstage Pass</p><h1>{h(t["event"])}</h1><p>Lineup, venue, beneficios VIP y compra sin romper el mood de una noche de música.</p>{facts(t)}<a class="cta" href="#tickets">Asegurar mi lugar</a></div></header><section class="lineup"><h2>Lineup de la noche</h2><div><article><span>21:00</span><b>Warm-up set</b></article><article><span>22:30</span><b>Indie live</b></article><article><span>00:00</span><b>Synth closing</b></article></div></section><section id="tickets" class="ticket-stage dark">{checkout(t)}</section>'
    if i=='conference':
        return f'<header class="conf-hero"><p class="eyebrow">Executive agenda</p><h1>{h(t["event"])}</h1><p>Una página para tomar decisión rápido: tema, tracks, agenda y registro en estructura escaneable.</p>{checkout(t, True)}</header><section class="agenda"><h2>Programa</h2><ol><li><time>09:00</time><b>Keynote: operaciones con IA</b></li><li><time>11:00</time><b>Panel de líderes regionales</b></li><li><time>14:00</time><b>Workshops por track</b></li></ol>{svg("agenda")}</section>'
    if i=='workshop':
        return f'<header class="workshop-hero"><div><p class="eyebrow">Learning Studio</p><h1>{h(t["event"])}</h1><p>De la promesa a la habilidad: objetivos, materiales, nivel y acceso antes del checkout.</p></div>{svg("badge")}</header><section class="learn-path"><h2>Sales con esto listo</h2><article><b>1</b><span>Mapa del proceso</span></article><article><b>2</b><span>Automatización funcional</span></article><article><b>3</b><span>Checklist de despliegue</span></article></section><section id="tickets" class="notebook-buy">{checkout(t)}</section>'
    if i=='meetup':
        return f'<header class="meetup-hero"><div>{svg("map")}</div><div><p class="eyebrow">Community signal</p><h1>{h(t["event"])}</h1><p>Quién convoca, qué conversación abre y por qué vale salir de casa.</p>{facts(t)}</div></header><section class="people-flow"><h2>Momentos del encuentro</h2><div><span>Llegada</span><span>Ronda de intros</span><span>Mesas temáticas</span><span>Cierres útiles</span></div></section><section id="tickets" class="ticket-stage">{checkout(t)}</section>'
    if i=='premium':
        return f'<header class="black-card"><div class="seal">{svg("crest")}</div><p class="eyebrow">Private invitation</p><h1>{h(t["event"])}</h1><p>Una experiencia sobria, aspiracional y sin ruido: lugar, protocolo y accesos claros.</p><a class="cta" href="#tickets">Asegurar mi lugar</a></header><section class="vip-details"><article><span>Dress code</span><b>Formal / black</b></article><article><span>Experiencia</span><b>Cena, ceremonia y subasta</b></article><article><span>Lugar</span><b>{h(t["venue"])}</b></article></section><section id="tickets" class="black-checkout">{checkout(t)}</section>'
    if i=='family':
        return f'<header class="family-hero"><div><p class="eyebrow">Plan familiar</p><h1>{h(t["event"])}</h1><p>Una landing amable: edades, actividades, horarios, ubicación y compra sin letra pequeña.</p><a class="cta" href="#tickets">Asegurar mi lugar</a></div>{svg("map")}</header><section class="activity-map"><h2>Ruta del día</h2><article>Zona picnic</article><article>Taller niños</article><article>Show central</article><article>Punto de encuentro</article></section><section id="tickets" class="ticket-stage">{checkout(t)}</section>'
    if i=='sports':
        return f'<header class="score-hero"><div class="scoreboard">{svg("score")}</div><div><p class="eyebrow">Race command center</p><h1>{h(t["event"])}</h1><p>Categorías, reglas, kit, horarios y compra en un tablero competitivo.</p>{facts(t)}</div></header><section class="bracket"><h2>Categorías</h2><div><b>Individual</b><b>Teams</b><b>Elite</b><b>Recreativo</b></div></section><section id="tickets" class="ticket-stage">{checkout(t)}</section>'
    if i=='minimal_checkout':
        return f'<header class="fast-hero"><div>{checkout(t)}</div><div><p class="eyebrow">Compra directa</p><h1>{h(t["event"])}</h1><p>Diseñado para tráfico de WhatsApp/Instagram: tickets primero, contexto suficiente después.</p>{facts(t)}</div></header><section class="fast-proof"><h2>Antes de pagar</h2><p>Fecha, modalidad, precio, acceso y replay quedan visibles sin hacer scroll eterno.</p>{svg("phone")}</section>'
    return f'<header class="editorial-hero"><p class="eyebrow">{h(t["tone"])}</p><h1>{h(t["event"])}</h1><p>Una invitación limpia y premium para eventos que necesitan presencia, claridad y checkout impecable.</p>{facts(t)}<a class="cta" href="#tickets">Asegurar mi lugar</a></header><section class="editorial-columns"><article><h2>La experiencia</h2><p>Contexto, lugar y expectativa editorial antes de elegir entrada.</p></article><article>{svg("dossier")}</article></section><section id="tickets" class="ticket-stage">{checkout(t)}</section>'

def page(t0):
    t=ev(t0)
    return f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{h(t['event'])} · {h(t['name'])}</title><meta name="description" content="{h(t['event'])}: fecha, lugar, entradas y checkout oficial del evento."><link rel="canonical" href="https://tononabot.github.io/konvoka-template-preview/templates/{t['id']}/"><meta name="robots" content="noindex, follow"><meta property="og:title" content="{h(t['event'])}"><meta property="og:description" content="Entradas y detalles oficiales del evento."><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="../../styles.css"><script type="application/ld+json">{schema(t)}</script></head><body class="page {t['theme']}" style="--accent:{t['accent']}"><a class="skip" href="#main">Saltar al contenido</a><main id="main">{layout(t)}<section class="event-info"><h2>Información del evento</h2><div><article><span>Fecha</span><b>{t['date']}</b></article><article><span>Hora</span><b>{t['time']}</b></article><article><span>Lugar</span><b>{h(t['venue'])}, {h(t['city'])}</b></article><article><span>Organiza</span><b>{h(t['organizer'])}</b></article></div></section></main><footer><p>{h(t['event'])}</p><a href="../../">Índice de previews</a></footer><div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden><div class="modal-card"><h2 id="modal-title">Asegurar mi lugar</h2><p>Checkout simulado para preview. En producción continúa con la selección real de entradas en Konvoka.</p><button class="cta" data-close-modal>Cerrar</button></div></div><script src="../../script.js?v=2" defer></script></body></html>'''

def index():
    cards=''.join(f'<a class="index-card {t["theme"]}" style="--accent:{t["accent"]}" href="templates/{t["id"]}/"><span>{h(t["tone"])}</span><b>{h(t["name"])}</b><small>{h(t["event"])}</small></a>' for t in TEMPLATES)
    return f'<!doctype html><html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Konvoka production-grade event templates</title><meta name="robots" content="noindex, follow"><meta name="description" content="Previews de landings de evento Konvoka con diseños temáticos production-grade."><link rel="stylesheet" href="styles.css"></head><body class="page index-page"><main><header class="index-hero"><p class="eyebrow">Konvoka template lab</p><h1>Landings de evento con diseño real, no skins.</h1><p>Cada preview usa estructura mobile, narrativa y componentes distintos. Todas conservan entradas y CTA “Asegurar mi lugar”.</p></header><section class="index-grid">{cards}</section></main></body></html>'

(ROOT/'index.html').write_text(index())
for t in TEMPLATES:
    d=ROOT/'templates'/t['id']; d.mkdir(parents=True, exist_ok=True); (d/'index.html').write_text(page(t))
(ROOT/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
print('generated', len(TEMPLATES), 'production-grade pages')
