document.addEventListener("DOMContentLoaded", function(){
    var selectedFilm = document.getElementById("review_name").value;
        if (selectedFilm === "Star Wars I") {
            document.getElementById("film_subtitle").textContent = "The Phantom Menace";
            document.getElementById("film_subtitle").innerHTML = "The Phantom Menace";
        } else if (selectedFilm === "Star Wars II") {
            document.getElementById("film_subtitle").textContent = "The Clone Wars";
        } else if (selectedFilm === "Star Wars III") {
            document.getElementById("film_subtitle").innerHTML = "The Revenge of the Sith";
        } else if (selectedFilm === "Star Wars IV") {
            document.getElementById("film_subtitle").innerHTML = "A New Hope";
        } else if (selectedFilm === "Star Wars V") {
            document.getElementById("film_subtitle").innerHTML = "The Empire Strikes Back";
        } else if (selectedFilm === "Star Wars VI") {
            document.getElementById("film_subtitle").innerHTML = "Return of the Jedi";
        } else if (selectedFilm === "Star Wars VII") {
            document.getElementById("film_subtitle").innerHTML = "The Force Awakens";
        } else if (selectedFilm === "Star Wars VIII") {
            document.getElementById("film_subtitle").innerHTML = "The Last Jedi";
        } else if (selectedFilm === "Star Wars IX") {
            document.getElementById("film_subtitle").innerHTML = "The Rise of Skywalker";
        } else {
            document.getElementById("film_subtitle").innerHTML = "Please Select Film";
        }
    });

// Function to input subtitle based on selected File Title
function filmOrder() {
    var selectedFilm = document.getElementById("review_name").value;
        if (selectedFilm === "Star Wars I") {
            document.getElementById("film_order").textContent = 1;
            document.getElementById("film_order").innerHTML = 1;
        } else if (selectedFilm === "Star Wars II") {
            document.getElementById("film_order").textContent = 2;
        } else if (selectedFilm === "Star Wars III") {
            document.getElementById("film_order").innerHTML = 3;
        } else if (selectedFilm === "Star Wars IV") {
            document.getElementById("film_order").innerHTML = 4;
        } else if (selectedFilm === "Star Wars V") {
            document.getElementById("film_order").innerHTML = 5;
        } else if (selectedFilm === "Star Wars VI") {
            document.getElementById("film_order").innerHTML = 6;
        } else if (selectedFilm === "Star Wars VII") {
            document.getElementById("film_order").innerHTML = 7;
        } else if (selectedFilm === "Star Wars VIII") {
            document.getElementById("film_order").innerHTML = 8;
        } else if (selectedFilm === "Star Wars IX") {
            document.getElementById("film_order").innerHTML = 9;
        } else {
            document.getElementById("film_order").innerHTML = 0;
        }
        console.log("ran");
    }