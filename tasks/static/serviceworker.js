self.addEventListener('install', (event) => {
    console.log("Service Worker Installed!");
    self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
    event.respondWith(fetch(event.request));
});

self.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    console.log("PWA Install Prompt Triggered!");
    window.deferredPrompt = event;
});
