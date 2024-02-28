const character = document.getElementById("character");

function jump() {
    character.classList.add("animate");
    setTimeout(() => {
        character.classList.remove("animate");
    }, 300);
}

document.addEventListener("click", jump);