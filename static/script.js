async function askChatbot() {
    let query = document.getElementById("userInput").value;
    let responseElem = document.getElementById("response");

    try {
        let response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        let data = await response.json();
        responseElem.innerText = data.answer;
    } catch (error) {
        console.error("Error:", error);
        responseElem.innerText = "Something went wrong. Check the console.";
    }
}
