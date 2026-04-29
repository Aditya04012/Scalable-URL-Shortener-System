import http from 'k6/http';

const urls = [
  "https://google.com",
  "https://amazon.com",
  "https://myntra.com",
  "https://flipkart.com",
  "https://youtube.com",
  "https://github.com",
  "https://linkedin.com",
  "https://twitter.com",
  "https://facebook.com",
  "https://instagram.com",
  "https://netflix.com",
  "https://reddit.com",
  "https://stackoverflow.com",
  "https://medium.com",
  "https://openai.com"
];

export default function () {
  const randomUrl = urls[Math.floor(Math.random() * urls.length)];

  http.post(
    'http://127.0.0.1/api/v1/url',
    JSON.stringify({ longUrl: randomUrl }),
    {
      headers: { 'Content-Type': 'application/json' }
    }
  );
}