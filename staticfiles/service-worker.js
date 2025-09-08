self.addEventListener("install", event => {
  console.log("Service Worker installed");
  event.waitUntil(
    caches.open("qmanager-cache").then(cache => {
      return cache.addAll([
        "/", // homepage
        "/static/manifest.json"
      ]);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
