import http from 'k6/http';

export default function () {
  http.post(
    'http://127.0.0.1:8000/api/v1/url',
    JSON.stringify({ longUrl: "https://google.com" }),
    { headers: { 'Content-Type': 'application/json' } }
  );
}