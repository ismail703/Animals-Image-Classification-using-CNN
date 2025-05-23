document.addEventListener('DOMContentLoaded', function() {
    var predictElement = document.getElementById('predict');
    if (predictElement) {
        var cl = predictElement.dataset.class;
        console.log(cl);
        switch (cl) {
            case "BEAR":
                document.querySelector(".Bear").classList.add("active");
                break;
            case "BISON":
                document.querySelector(".Bison").classList.add("active");
                break;
            case "CHEETAH":
                document.querySelector(".Cheetah").classList.add("active");
                break;
            case "ELEPHANT":
                document.querySelector(".Elephant").classList.add("active");
                break;
            case "FOX":
                document.querySelector(".Fox").classList.add("active");
                break;
            case "GAZELLE":
                document.querySelector(".Gazelle").classList.add("active");
                break;
            case "GIRAFFE":
                document.querySelector(".Giraffe").classList.add("active");
                break;
            case "GORILLA":
                document.querySelector(".Gorilla").classList.add("active");
                break;
            case "HIPPO":
                document.querySelector(".Hippo").classList.add("active");
                break;
            case "HORSE":
                document.querySelector(".Horse").classList.add("active");
                break;
            case "HYENA":
                document.querySelector(".Hyena").classList.add("active");
                break;
            case "KOALA":
                document.querySelector(".Koala").classList.add("active");
                break;
            case "LEOPARD":
                document.querySelector(".Leopard").classList.add("active");
                break;
            case "LION":
                document.querySelector(".Lion").classList.add("active");
                break;
            case "MEERKAT":
                document.querySelector(".Meerkat").classList.add("active");
                break;
            case "PIG":
                document.querySelector(".Pig").classList.add("active");
                break;
            case "PORCUPINE":
                document.querySelector(".Porcupine").classList.add("active");
                break;
            case "RHINO":
                document.querySelector(".Rhino").classList.add("active");
                break;
            case "TIGER":
                document.querySelector(".Tiger").classList.add("active");
                break;
            case "WOLF":
                document.querySelector(".Wolf").classList.add("active");
                break;
            case "ZEBRA":
                document.querySelector(".Zebra").classList.add("active");
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