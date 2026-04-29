import http from 'k6/http';

const base = 'http://127.0.0.1:80/api/v1/url';
const shortUrls = ['ij', 'ik', 'il', 'im', 'io', 'iq'];

export default function () {
  const short = shortUrls[Math.floor(Math.random() * shortUrls.length)];

  http.get(`${base}/${short}`, {
    redirects: 0   // 🔥 MUST BE HERE
  });
}