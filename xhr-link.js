const fetch = require("node-fetch"); // Solo si usas Node.js sin fetch global

const url = "https://app.xentrics.ai/invoices/operations/issue-invoice-v2";

const headers = {
  Accept: "text/x-component",
  "Content-Type": "text/plain;charset=UTF-8",
  Cookie:
    "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JhY2tlbmQueGVudHJpY3MuYWkvYXBpL2xvZ2luIiwiaWF0IjoxNzU4ODU4MjczLCJleHAiOjE3NTg5NDQ2NzMsIm5iZiI6MTc1ODg1ODI3MywianRpIjoiNFpLSDhjTWlzc243bUxUMSIsInN1YiI6Ijc0NiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.l9K94urSDYRQKYkIJA1ivc99Hsv86qaLd5mYYBTQuE4; company_id=2131",
  "Next-Action": "c170aa1ac624d4f62fd8e16a1fcf7a3adc3434d5",
  "Next-Router-State-Tree":
    "%5B%22%22%2C%7B%22children%22%3A%5B%22(dashboard)%22%2C%7B%22children%22%3A%5B%22invoices%22%2C%7B%22children%22%3A%5B%22operations%22%2C%7B%22children%22%3A%5B%22issue-receipt-v2%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Finvoices%2Foperations%2Fissue-receipt-v2%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
};

const payload = '[{"numero":"77485004","tipo":"dni"}]';

fetch(url, {
  method: "POST",
  headers: headers,
  body: payload,
})
  .then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }
    return res.text(); // Capturamos el texto plano, porque la API puede responder HTML, texto, JSON, etc.
  })
  .then((data) => {
    console.log("Respuesta del servidor:");
    console.log(data); // Aquí ves exactamente qué te devolvió la API
  })
  .catch((err) => {
    console.error("Error en la petición:", err);
  });
