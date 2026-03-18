async function scan(){
    let file = document.getElementById("file").value;

    let res = await fetch("http://127.0.0.1:5000/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({file: file})
    });

    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}