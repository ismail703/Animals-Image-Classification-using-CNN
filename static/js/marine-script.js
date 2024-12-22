document.addEventListener('DOMContentLoaded', function() {
    var cl = document.getElementById('predict').dataset.class;            
    console.log(cl);
    cl = "." + cl.replace(" ", "-");
    document.querySelector(cl).classList.add("active");
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