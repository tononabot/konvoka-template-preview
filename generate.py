from pathlib import Path
from html import escape

base = Path(__file__).parent

templates = [
    dict(id='classic', name='Classic Clean', short='Classic', accent='#4f46e5', surface='light', layout='editorial', motif='timeline', eyebrow='Landing clara', promise='Toda la información esencial del evento en una ruta simple hacia la compra.', primary='Decide con contexto', secondary='Compra sin perderte', highlights=['Fecha, lugar y organizer arriba', 'Descripción legible por bloques', 'Boletas visibles y CTA persistente'], trust=['Datos reales del evento', 'FAQ para resolver fricción', 'Checkout Konvoka intacto'], qa=[('¿Qué necesito saber antes de comprar?', 'Fecha, lugar, organizer, tipo de entrada y políticas visibles en la misma página.'), ('¿Cómo se asegura el cupo?', 'Seleccionando una o varias boletas y usando el flujo actual de checkout.')]),
    dict(id='racing', name='Racing / Adrenaline', short='Racing', accent='#ef4444', surface='dark', layout='cinematic', motif='track', eyebrow='Modo adrenalina', promise='Energía visual para eventos de velocidad, con reglas y logística al frente.', primary='Pista, horario y acceso', secondary='Seguridad antes del checkout', highlights=['Hero oscuro de alto impacto', 'Agenda y requisitos escaneables', 'Reglas de seguridad visibles'], trust=['Sin falsa urgencia', 'Restricciones claras', 'Compra con boletas reales'], qa=[('¿Sirve para track days o carreras?', 'Sí. Prioriza agenda, venue, requisitos de seguridad y categorías de entrada.'), ('¿Se puede comprar igual que hoy?', 'Sí. La landing solo cambia presentación; el selector y checkout no cambia.')]),
    dict(id='conference', name='Conference Pro', short='Conference', accent='#2563eb', surface='light', layout='agenda', motif='timeline', eyebrow='Agenda profesional', promise='Una landing editorial para explicar valor, agenda, speakers y registro.', primary='Programa entendible', secondary='Registro por tipo de entrada', highlights=['Agenda con jerarquía clara', 'Speakers/hosts como prueba real', 'FAQ para decisión B2B'], trust=['Sin logos inventados', 'Metadatos para speakers y ciudad', 'CTA profesional y directo'], qa=[('¿Qué responde esta landing?', 'De qué trata el evento, quién participa, cuándo ocurre y qué entrada conviene.'), ('¿Ayuda a SEO?', 'Sí. Ordena tema, fecha, ciudad, organizer, agenda y preguntas frecuentes.')]),
    dict(id='workshop', name='Workshop / Bootcamp', short='Workshop', accent='#7c3aed', surface='light', layout='editorial', motif='badge', eyebrow='Aprendizaje práctico', promise='Convierte un taller en una promesa clara: qué aprenderás, para quién es y cómo entrar.', primary='Resultados de aprendizaje', secondary='Fit antes de pagar', highlights=['Outcomes visibles', 'Nivel y requisitos claros', 'Boletas por compromiso'], trust=['Expectativas honestas', 'Materiales/requisitos destacados', 'Compra progresiva'], qa=[('¿Reduce dudas del asistente?', 'Sí. Expone aprendizajes, requisitos, duración y tipo de público.'), ('¿Puede servir para bootcamps?', 'Sí. Funciona para talleres, cursos, entrenamientos y certificaciones.')]),
    dict(id='music', name='Music Night', short='Music', accent='#ec4899', surface='dark', layout='cinematic', motif='stage', eyebrow='Noche y lineup', promise='Atmósfera visual para tráfico social, sin esconder venue, horarios ni entradas.', primary='Lineup primero', secondary='Ticket siempre cerca', highlights=['Visual oscuro y emocional', 'Lineup/venue protagonistas', 'CTA sticky para móvil'], trust=['Restricciones visibles', 'Sin artistas inventados', 'Compra rápida desde redes'], qa=[('¿Sirve para conciertos y fiestas?', 'Sí. Prioriza lineup, ambiente, ubicación, edad/restricciones y tickets.'), ('¿Qué evita?', 'Evita landings largas donde el usuario de Instagram no encuentra la boleta.')]),
    dict(id='meetup', name='Community Meetup', short='Meetup', accent='#0891b2', surface='light', layout='editorial', motif='pulse', eyebrow='Comunidad primero', promise='Un tono cercano para explicar propósito, dinámica y por qué vale asistir.', primary='Propósito de comunidad', secondary='Llegar sin fricción', highlights=['Organizer visible', 'Agenda simple', 'Registro de baja fricción'], trust=['Lenguaje humano', 'Perfil de asistentes claro', 'Link canónico compartible'], qa=[('¿Qué comunica mejor?', 'El propósito del meetup, a quién convoca y qué pasará al llegar.'), ('¿Funciona para eventos gratis?', 'Sí. El CTA sigue siendo reservar/asegurar lugar con cupos reales.')]),
    dict(id='premium', name='Premium Gala', short='Premium', accent='#b45309', surface='warm', layout='cinematic', motif='badge', eyebrow='Experiencia premium', promise='Más imagen, menos ruido: una experiencia sobria que hace sentir valor antes de comprar.', primary='La experiencia incluida', secondary='Detalles que importan', highlights=['Composición editorial', 'Dress code y venue visibles', 'Copy corto y aspiracional'], trust=['Sin escasez falsa', 'Reglas verificables', 'Checkout confiable'], qa=[('¿Qué lo hace premium?', 'Jerarquía visual, textos cortos, detalles de experiencia y compra discreta.'), ('¿Inventa exclusividad?', 'No. Solo muestra VIP, cupos o beneficios si vienen de la configuración real.')]),
    dict(id='family', name='Family / Local Fair', short='Family', accent='#16a34a', surface='light', layout='agenda', motif='map', eyebrow='Familiar y local', promise='Legible para todos: horarios, actividades, ubicación y compra simple.', primary='Plan fácil de entender', secondary='Información para familias', highlights=['Tipografía amplia', 'Actividades por bloques', 'Mapa y horarios al frente'], trust=['Accesibilidad visible', 'Lenguaje simple', 'Touch targets cómodos'], qa=[('¿Qué prioriza?', 'Claridad para familias: dónde es, qué actividades hay, horarios y entradas.'), ('¿Funciona en móvil?', 'Sí. Está pensado para leer y comprar desde WhatsApp o redes.')]),
    dict(id='sports', name='Sports Tournament', short='Sports', accent='#ea580c', surface='light', layout='agenda', motif='track', eyebrow='Competencia clara', promise='Categorías, reglas y logística en una landing lista para deportistas.', primary='Categorías y reglas', secondary='Inscripción sin dudas', highlights=['Reglas visibles', 'Agenda por competencia', 'Entradas por participación'], trust=['Requisitos explícitos', 'Sin cupos inventados', 'Checkout por ticket real'], qa=[('¿Qué resuelve?', 'Que el participante entienda categoría, requisitos, horario y costo antes de comprar.'), ('¿Sirve para carreras?', 'Sí. También funciona para torneos, ligas, competencias y eventos deportivos.')]),
    dict(id='minimal_checkout', name='Minimal Fast Checkout', short='Fast', accent='#0f172a', surface='light', layout='commerce', motif='pulse', eyebrow='Compra rápida', promise='Una landing compacta para tráfico directo: menos lectura, más decisión.', primary='Boletas arriba', secondary='Datos mínimos suficientes', highlights=['Hero compacto', 'Ticket selector prioritario', 'Detalles críticos resumidos'], trust=['Sin distracciones', 'Metadatos canónicos intactos', 'CTA visible por viewport'], qa=[('¿Cuándo usarlo?', 'Cuando el usuario ya llega convencido desde WhatsApp, Instagram o una comunidad.'), ('¿Sacrifica SEO?', 'No. Mantiene datos estructurados, título, fecha, lugar y contenido factual.')]),
]

event = {
    'title': 'Track Day Motos — Autódromo de Tocancipá',
    'date': '12 de julio de 2026',
    'time': '08:00 – 17:00',
    'venue': 'Autódromo de Tocancipá',
    'city': 'Tocancipá, Cundinamarca',
    'organizer': 'Organizador demo Konvoka',
    'desc': 'Preview temporal con data demo para validar composición visual, mobile first, SEO/AI SEO, accesibilidad y flujo de tickets por template. No procesa pagos reales.',
}

def svg_path(motif):
    return {
        'track': 'M42 176 C82 72 150 58 190 120 C228 180 292 172 320 82',
        'stage': 'M52 204 L108 74 L180 154 L252 74 L308 204',
        'map': 'M62 78 C120 38 148 112 188 82 C248 36 282 104 314 72 M74 190 C126 148 176 222 226 168 C254 138 292 160 318 130',
        'badge': 'M180 34 L292 96 L292 198 L180 232 L68 198 L68 96 Z M180 72 L250 112 L250 178 L180 200 L110 178 L110 112 Z',
        'pulse': 'M44 138 H104 L126 94 L154 190 L188 68 L218 138 H316',
        'timeline': 'M54 184 C92 118 128 118 164 148 C202 180 246 164 304 74',
    }[motif]

def nav(current):
    items = ''.join(f'<a class="nav__link {"is-active" if t["id"]==current else ""}" href="../{t["id"]}/">{escape(t["short"])}</a>' for t in templates)
    return f'<nav class="nav" aria-label="Templates disponibles"><a class="brand" href="../../"><span aria-hidden="true">K</span>Konvoka templates</a><div class="nav__scroll">{items}</div></nav>'

def page(t):
    links = ''.join(f'<link rel="prefetch" href="../{x["id"]}/">' for x in templates if x['id'] != t['id'])
    qs = ''.join(f'<li><a href="../{x["id"]}/">{escape(x["name"])}</a></li>' for x in templates)
    return f'''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t['name'])} · Preview de templates Konvoka</title>
<meta name="description" content="Preview temporal del template {escape(t['name'])} para una landing pública de evento Konvoka con selector de tickets y CTA Asegurar mi lugar.">
<link rel="canonical" href="https://tononabot.github.io/konvoka-template-preview/templates/{t['id']}/">
<meta name="robots" content="noindex, follow">
<meta property="og:title" content="{escape(t['name'])} · Template Konvoka">
<meta property="og:description" content="Validación visual temporal de template de evento: mobile first, UX, SEO/AI SEO y checkout handoff.">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
{links}
<link rel="stylesheet" href="../../styles.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Event","name":"{event['title']}","eventStatus":"https://schema.org/EventScheduled","eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","startDate":"2026-07-12T08:00:00-05:00","location":{{"@type":"Place","name":"{event['venue']}","address":"{event['city']}"}},"organizer":{{"@type":"Organization","name":"{event['organizer']}"}},"description":"Preview temporal de templates Konvoka con data demo."}}</script>
</head>
<body class="surface-{t['surface']} layout-{t['layout']}" style="--accent:{t['accent']}">
<a class="skip" href="#contenido">Saltar al contenido</a>
{nav(t['id'])}
<main id="contenido">
<section class="notice" aria-label="Aviso de preview"><strong>Preview temporal.</strong> Data demo para validar templates; no procesa pagos reales.</section>
<header class="hero">
  <div class="hero__copy">
    <p class="eyebrow">{escape(t['eyebrow'])}</p>
    <h1>{escape(event['title'])}</h1>
    <p class="promise">{escape(t['promise'])}</p>
    <p class="desc">{escape(event['desc'])}</p>
    <dl class="facts">
      <div><dt>Fecha</dt><dd>{event['date']}</dd></div>
      <div><dt>Hora</dt><dd>{event['time']}</dd></div>
      <div><dt>Lugar</dt><dd>{event['venue']} · {event['city']}</dd></div>
    </dl>
    <div class="hero__actions"><a class="button" href="#tickets">Asegurar mi lugar</a><span class="price">Desde $120.000 COP</span></div>
  </div>
  <div class="visual" aria-hidden="true">
    <svg viewBox="0 0 360 260" focusable="false">
      <path class="line" d="{svg_path(t['motif'])}" />
      <g class="nodes"><circle cx="72" cy="180" r="10"/><circle cx="180" cy="130" r="14"/><circle cx="292" cy="84" r="10"/></g>
      <g class="cards"><rect x="32" y="28" width="118" height="52" rx="18"/><rect x="202" y="178" width="126" height="54" rx="18"/></g>
    </svg>
  </div>
</header>
<section class="blocks" aria-label="Estructura del template">
  <article><h2>{escape(t['primary'])}</h2><ul>{''.join(f'<li>{escape(x)}</li>' for x in t['highlights'])}</ul></article>
  <article><h2>{escape(t['secondary'])}</h2><ul>{''.join(f'<li>{escape(x)}</li>' for x in t['trust'])}</ul></article>
  <article><h2>Preguntas rápidas</h2>{''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in t['qa'])}</article>
</section>
<section id="tickets" class="checkout" aria-labelledby="tickets-title">
  <div><p class="eyebrow">Checkout handoff</p><h2 id="tickets-title">Selecciona tickets y conserva el flujo “Asegurar mi lugar”</h2><p>Este bloque simula el contrato de UI: elegir una o varias entradas y pasar al checkout hospedado de Konvoka.</p></div>
  <form class="ticket-card" aria-label="Selector de tickets demo">
    <label>General <span>$120.000 COP</span><input type="number" min="0" max="6" value="1" aria-label="Cantidad General"></label>
    <label>Paddock <span>$220.000 COP</span><input type="number" min="0" max="4" value="0" aria-label="Cantidad Paddock"></label>
    <button class="button" type="button" data-open-modal>Asegurar mi lugar</button>
  </form>
</section>
<section class="machine"><h2>Resumen factual para AI SEO</h2><p>{event['title']} es un evento demo en {event['venue']}, {event['city']}, el {event['date']}. El template {escape(t['name'])} mantiene fecha, lugar, organizer, selector de tickets, FAQ y CTA de checkout en una estructura escaneable.</p></section>
<section class="all"><h2>Ver los 10 templates</h2><ul>{qs}</ul></section>
</main>
<footer><p>Konvoka template preview · Sitio temporal publicado por Tonona Bot para validación visual.</p></footer>
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden><div class="modal__card"><h2 id="modal-title">Checkout simulado</h2><p>En Konvoka real este paso redirige a <code>/checkout/&lt;order_id&gt;</code> usando los tickets seleccionados. Esta URL pública es solo preview visual.</p><button class="button" data-close-modal>Cerrar</button></div></div>
<script src="../../script.js" defer></script>
</body>
</html>'''

index_cards = ''.join(f'<article class="index-card" style="--accent:{t["accent"]}"><p>{escape(t["eyebrow"])}</p><h2>{escape(t["name"])}</h2><p>{escape(t["promise"])}</p><a class="button" href="templates/{t["id"]}/">Ver template</a></article>' for t in templates)
base.joinpath('index.html').write_text(f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Konvoka · Preview de 10 templates de evento</title><meta name="description" content="Preview temporal de 10 templates públicos de landing de evento Konvoka."><meta name="robots" content="noindex, follow"><link rel="stylesheet" href="styles.css"></head><body><a class="skip" href="#contenido">Saltar al contenido</a><main id="contenido" class="index"><p class="eyebrow">Preview temporal</p><h1>10 templates públicos para la landing de un mismo evento</h1><p class="desc">Cada URL usa la misma data demo y cambia únicamente el enfoque visual/UX del template. El contrato de tickets se conserva: seleccionar entradas → “Asegurar mi lugar”.</p><div class="index-grid">{index_cards}</div></main><footer><p>Publicado para validación visual temporal.</p></footer></body></html>''')

for t in templates:
    d = base / 'templates' / t['id']
    d.mkdir(parents=True, exist_ok=True)
    d.joinpath('index.html').write_text(page(t))

base.joinpath('robots.txt').write_text('User-agent: *\nDisallow: /\n')
base.joinpath('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
print('generated', len(templates), 'template pages')
