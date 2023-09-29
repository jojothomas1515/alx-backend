import express from "express";
import http from "http";
import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();
client.on("connect", () => {
  console.log("connected to redis successfully");
});

const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  let res = null;
  listProducts.forEach((data) => {
    if (data.Id.toString() === id) res = data;
  });
  return res;
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock, (err, reply) => {
    if (!err) console.log(`Stock Added:`, reply);
  });
}
// TODO: fix this
async function getCurrentReservedStockById(itemId) {
  const get = promisify(client.get).bind(client);
  return await get(itemId);
}

const app = express();
app.get("/list_products", function (req, res) {
  return res.status(200).json(listProducts);
});

// TODO: fix this
app.get("/list_products/:itemId(\\d+)", async function (req, res) {
  const { itemId } = req.params;
  const item = await getCurrentReservedStockById(itemId);
  if (!item) return res.json({ status: "Product not found" });
  return res.json(JSON.parse(item));
});

app.get("/reserve_product/:itemId", function (req, res) {
  const { itemId } = req.params;
  const item = getItemById(itemId);

  if (!item) {
    return res.status(404).json({ status: "Product not found" });
  }
  if (!(item.stock >= 1))
    return res
      .status(200)
      .json({ status: "Not enough stock available", itemId: 1 });
  const nItem = {
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock,
  };

  reserveStockById(itemId, JSON.stringify(item));
  return res.json({ status: "Reservation confirmed", itemId: 1 });
});

const server = http.createServer(app);
const PORT = 1245;

server.listen(PORT, () => console.log("Listening on port", PORT));
