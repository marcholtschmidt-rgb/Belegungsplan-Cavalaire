const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const ROOT = __dirname;

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
};

const server = http.createServer((req, res) => {
  let reqPath = decodeURIComponent(req.url.split("?")[0]);
  if (reqPath === "/") reqPath = "/index.html";

  const filePath = path.join(ROOT, reqPath);

  // Prevent escaping the app folder
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403);
    return res.end("Forbidden");
  }

  // Dokumentation (README & Co.) gehoert nicht auf die Webseite
  if (path.extname(filePath).toLowerCase() === ".md") {
    res.writeHead(404);
    return res.end("Not found");
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      // Fallback to index.html for unknown routes (single-page app behavior)
      fs.readFile(path.join(ROOT, "index.html"), (err2, indexData) => {
        if (err2) {
          res.writeHead(404);
          return res.end("Not found");
        }
        res.writeHead(200, { "Content-Type": MIME[".html"] });
        res.end(indexData);
      });
      return;
    }
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, { "Content-Type": MIME[ext] || "application/octet-stream" });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`Belegungsplan Cavalaire läuft auf Port ${PORT}`);
});
