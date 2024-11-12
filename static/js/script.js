document
  .getElementById("textForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const text = document.getElementById("text").value;

    try {
      const response = await fetch("/convert", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      if (data.audio_url) {
        const audioPlayer = document.getElementById("audioPlayer");
        audioPlayer.src = data.audio_url;
        audioPlayer.hidden = false;
        audioPlayer.play();
      } else {
        alert("Erro ao converter texto para fala.");
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao se comunicar com o servidor.");
    }
  });
