document.addEventListener('DOMContentLoaded', function() {
    var predictElement = document.getElementById('predict');
    if (predictElement) {
        var cl = predictElement.dataset.class;
        console.log(cl);
        switch (cl) {
            case "CHICKEN":
                document.querySelector(".Chicken").classList.add("active");
                break;
            case "CROW":
                document.querySelector(".Crow").classList.add("active");
                break;
            case "DOVE":
                document.querySelector(".Dove").classList.add("active");
                break;
            case "DUCK":
                document.querySelector(".Duck").classList.add("active");
                break;
            case "EAGLE":
                document.querySelector(".Eagle").classList.add("active");
                break;
            case "FLAMINGO":
                document.querySelector(".Flamingo").classList.add("active");
                break;
            case "GULL":
                document.querySelector(".Gull").classList.add("active");
                break;
            case "HAMMINGBIRD":
                document.querySelector(".Hummingbird").classList.add("active");
                break;
            case "MACAW":
                document.querySelector(".Macaw").classList.add("active");
                break;
            case "OSTRICH":
                document.querySelector(".Ostrich").classList.add("active");
                break;
            case "OWL":
                document.querySelector(".Owl").classList.add("active");
                break;
            case "PEACOCK":
                document.querySelector(".Peacock").classList.add("active");
                break;
            case "PENGUIN":
                document.querySelector(".Penguin").classList.add("active");
                break;
            case "TURKEY":
                document.querySelector(".Turkey").classList.add("active");
                break;
            case "WOODPECKER":
                document.querySelector(".Woodpecker").classList.add("active");
                break;
            default:
                break;
        }
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