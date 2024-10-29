document.getElementById("form-agendamento").addEventListener("submit", function(event) {
    event.preventDefault();
    const data = {
        data: document.getElementById("data").value,
        hora: document.getElementById("hora").value,
    };
    fetch('/agendamento', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => console.log("Sucesso:", data))
    .catch(error => console.error("Erro:", error));
});
