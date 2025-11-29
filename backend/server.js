const express = require("express");
const app = express();

app.get("/data", (req, res) => {
  res.json({ message: "Hello from Express Backend!" });
});

app.listen(5000, () => console.log("Backend running on port 5000"));
