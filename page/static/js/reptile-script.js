document.addEventListener('DOMContentLoaded', function() {
    var cl = document.getElementById('predict').dataset.class;            
    console.log(cl);
    switch (cl) {
      case "Chameleon":
        document.querySelector(".chameleon").classList.add("active");
        break;
        case "Crocodile":
        document.querySelector(".crocodile").classList.add("active");
        break;
        case "Frog":
        document.querySelector(".frog").classList.add("active");
        break;
        case "Gecko":
        document.querySelector(".gecko").classList.add("active");
        break;
        case "Iguana":
        document.querySelector(".iguana").classList.add("active");
        break;
        case "Kumodo Dragon":
        document.querySelector(".kumodo_dragon").classList.add("active");
        break;
        case "Salamander":
        document.querySelector(".salamander").classList.add("active");
        break;
        case "Snake":
        document.querySelector(".snake").classList.add("active");
        break;
        case "Tuatara":
        document.querySelector(".tuatara").classList.add("active");
        break;
        case "Turtle":
        document.querySelector(".turtle").classList.add("active");
        break;

      default:
        break;
    }
});


var img = document.querySelector('.form-control');
img.addEventListener('change', function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();
  
    reader.onload = function(e) {
        var img = document.getElementById('uploaded-image');
        img.src = e.target.result;
        img.classList.add("display");
    }
    
    reader.readAsDataURL(file);
});