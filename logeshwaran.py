<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Road Accident Predictor</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5">
    <h2 class="text-center mb-4">🚧 Road Accident Risk Prediction</h2>

    <form id="predictionForm">
      <div class="mb-3">
        <label>Weather</label>
        <select name="Weather" class="form-select">
          <option value="Clear">Clear</option>
          <option value="Rainy">Rainy</option>
          <option value="Snowy">Snowy</option>
        </select>
      </div>

      <div class="mb-3">
        <label>Road Type</label>
        <select name="Road_Type" class="form-select">
          <option value="City Road">City Road</option>
          <option value="Highway">Highway</option>
          <option value="Rural Road">Rural Road</option>
        </select>
      </div>

      <!-- Add more fields matching your dataset columns -->

      <button class="btn btn-primary">Predict</button>
    </form>

    <div id="result" class="alert mt-4 d-none"></div>
  </div>

  <script>
    document.getElementById("predictionForm").addEventListener("submit", async function (e) {
      e.preventDefault();

      const formData = new FormData(e.target);
      const data = {};
      formData.forEach((value, key) => data[key] = value);

      const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await res.json();
      const alertDiv = document.getElementById("result");
      alertDiv.classList.remove("d-none", "alert-success", "alert-danger");
      alertDiv.classList.add(result.prediction === 1 ? "alert-danger" : "alert-success");
      alertDiv.textContent = result.prediction === 1
        ? "⚠️ High risk of accident!"
        : "✅ Low risk of accident.";
    });
  </script>
</body>
</html>
