import express from "express";
import http from "http";

const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  listProducts.forEach((data) => {
    if (data.id === id) return data;
  });
}

const app = express();
app.get("/list_products", function (req, res) {
  return res.status(200).json(listProducts);
});

const server = http.createServer(app);
const PORT = 1245;

server.listen(PORT, () => console.log("Listening on port", PORT));
