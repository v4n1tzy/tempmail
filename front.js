// Modifier la fonction pour récupérer l'email depuis le backend Flask
function generateNewEmail() {
    fetch('https://tempmaila.netlify.app/generate_email')
        .then(response => response.json())
        .then(data => {
            document.getElementById("email").value = data.email;
            document.getElementById("email-list").innerHTML = "";
            document.getElementById("empty-inbox").style.display = "block";
        })
        .catch(error => console.error("Erreur:", error));
}
