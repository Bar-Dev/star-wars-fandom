// Function to play particular audio clip on load
    const soundClip = document.getElementById("audio").innerHTML;
    const audioLight = new Audio("/static/sounds/light-side.mp3");
    const audioDark = new Audio("/static/sounds/dark-side.mp3");
document.addEventListener("DOMContentLoaded", function(){
    if (soundClip === "Jedi Knight") {
        document.getElementById("audio-button").innerHTML = `<button id="audio-control" class="pro-edit waves-effect waves-light btn-large buttons" onclick="stopLight();">Pause Audio</button>`
        audioLight.play();
    } else if (soundClip === "Sith Lord") {
        document.getElementById("audio-button").innerHTML = `<button id="audio-control" class="pro-edit waves-effect waves-light btn-large buttons" onclick="stopDark();">Pause Audio</button>`
        audioDark.play();
    }; 
});

// Play & Pause Light Music
function stopLight() {
    if (audioLight.paused) {
        audioLight.play();
    } else {
        audioLight.pause();
    }
};

// Play & Pause Dark Music
function stopDark() {
    if (audioDark.paused) {
        audioDark.play();
    } else {
        audioDark.pause();
    }
};

