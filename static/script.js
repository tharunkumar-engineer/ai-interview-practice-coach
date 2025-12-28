function getQuestion() {
    const role = document.getElementById("role").value;

    fetch("/generate-question", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ role: role })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("question").innerText = data.question;
    });
}

function submitAnswer() {
    const answer = document.getElementById("answer").value;

    fetch("/evaluate-answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answer: answer })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("feedback").innerText = data.result;
    });
}
