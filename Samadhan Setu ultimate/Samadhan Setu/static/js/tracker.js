document.getElementById("trackForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const id = document.getElementById("trackId").value;

  fetch(`/track/status/?trackId=${id}`)
    .then(response => response.json())
    .then(data => {
      const resultBox = document.getElementById("trackerResult");
      resultBox.style.display = "block";

      const statusMsg = document.getElementById("statusMsg");
      const pending = document.getElementById("stepPending");
      const progress = document.getElementById("stepProgress");
      const resolved = document.getElementById("stepResolved");

      // Reset all step classes
      [pending, progress, resolved].forEach(step => {
        step.className = "status-step";
      });

      if (data.error) {
        statusMsg.innerText = "No complaint found!";
        document.getElementById("metaDate").innerText = "";
        document.getElementById("metaDept").innerText = "";
        document.getElementById("metaUpdated").innerText = "";
        return;
      }

      // Set meta values
      document.getElementById("metaDate").innerText = data.date || "-";
      document.getElementById("metaDept").innerText = data.department || "-";
      document.getElementById("metaUpdated").innerText = data.updated || "-";

      // Handle status steps
      const status = data.status;

      if (status === "Pending") {
        pending.classList.add("active");
        statusMsg.innerText = "Your complaint is registered and pending.";
      } else if (status === "In Progress") {
        pending.classList.add("completed");
        progress.classList.add("active");
        statusMsg.innerText = "Your complaint is currently being worked on.";
      } else if (status === "Resolved") {
        pending.classList.add("completed");
        progress.classList.add("completed");
        resolved.classList.add("completed"); 
        statusMsg.innerText = "Your complaint has been successfully resolved.";
      } else {
        statusMsg.innerText = "Unknown status received.";
      }
    })
    .catch(error => {
      document.getElementById("trackerResult").style.display = "block";
      document.getElementById("statusMsg").innerText = "An error occurred. Please try again.";
      console.error("Fetch error:", error);
    });
});
