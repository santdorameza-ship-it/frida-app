/**
 * FRIDA Service Worker — Offline Real
 * 
 * Implementa cache offline real para la PWA. Permite que FRIDA funcione
 * completamente sin red después de la primera visita.
 * 
 * Estrategia:
 * - Cache-first para assets estáticos (HTML, CSS, JS, fuentes, mapas tile)
 * - Network-first para llamadas a API (cuando existan)
 * - Fallback al cache si la red falla
 */

const CACHE_VERSION = 'frida-v1.0.0';
const CACHE_NAME = 'frida-cache-' + CACHE_VERSION;

// Recursos críticos que se cachean en instalación
const CORE_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json'
];

// Recursos externos que se cachean al usarse (CDN, mapas)
const RUNTIME_CACHE_PATTERNS = [
  /^https:\/\/unpkg\.com\/leaflet/,
  /^https:\/\/fonts\.googleapis\.com/,
  /^https:\/\/fonts\.gstatic\.com/,
  /^https:\/\/.*\.basemaps\.cartocdn\.com/
];

// ===== INSTALACIÓN =====
self.addEventListener('install', event => {
  console.log('[SW] Installing FRIDA Service Worker', CACHE_VERSION);
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[SW] Caching core assets');
        return cache.addAll(CORE_ASSETS);
      })
      .then(() => self.skipWaiting())
      .catch(err => console.error('[SW] Install error:', err))
  );
});

// ===== ACTIVACIÓN =====
self.addEventListener('activate', event => {
  console.log('[SW] Activating FRIDA Service Worker', CACHE_VERSION);
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME && k.startsWith('frida-cache-'))
            .map(k => {
              console.log('[SW] Deleting old cache:', k);
              return caches.delete(k);
            })
      );
    }).then(() => self.clients.claim())
  );
});

// ===== FETCH (intercepción de peticiones) =====
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // Solo manejar GET
  if (request.method !== 'GET') return;

  // Ignorar chrome-extension y otros esquemas
  if (!url.protocol.startsWith('http')) return;

  // Estrategia: cache-first con network fallback + runtime caching
  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) {
        // Tenemos en cache, devolver inmediatamente
        return cached;
      }

      // No está en cache, ir a red
      return fetch(request)
        .then(response => {
          // No cachear si error
          if (!response || response.status !== 200) {
            return response;
          }

          // Verificar si debe cachearse en runtime
          const shouldCache = url.origin === self.location.origin || 
                              RUNTIME_CACHE_PATTERNS.some(p => p.test(request.url));

          if (shouldCache) {
            // Clone porque response es stream de un solo uso
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(request, responseClone);
            });
          }

          return response;
        })
        .catch(err => {
          console.warn('[SW] Network failed for:', request.url);
          // Fallback: si pide HTML y falla red, devolver index.html del cache
          if (request.headers.get('accept') && request.headers.get('accept').includes('text/html')) {
            return caches.match('/index.html');
          }
          throw err;
        });
    })
  );
});

// ===== MENSAJES =====
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
