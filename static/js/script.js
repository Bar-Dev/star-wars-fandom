$(document).ready(function(){
    $("select").formSelect();
});

$(document).ready(function(){
    $(".sidenav").sidenav();
});

$(document).ready(function(){
    $('.collapsible').collapsible();
});

$(document).ready(function(){
    $('.tooltipped').tooltip();
});

$('.dropdown-trigger').dropdown();

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    };

function filmSelected() {
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
        } else if (selectedFilm === "Star Wars VII") {
            document.getElementById("film_subtitle").innerHTML = "The Last Jedi";
        } else if (selectedFilm === "Star Wars IX") {
            document.getElementById("film_subtitle").innerHTML = "The Rise of Skywalker";
        } else {
            document.getElementById("film_subtitle").innerHTML = "Please Select Film";
        }
    }

const soundClip = document.querySelector("#audio")
    soundClip.addEventListener("load", function(){
// Execute this when clicking the button
const audio = new Audio("/static/sounds/light-side.mp3");
    audio.play();
    console.log("works");
})
