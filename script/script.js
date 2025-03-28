function myFunction() {
    const icon = document.getElementById("icon");
  

    if (icon.classList.contains("virar")) {
      icon.classList.remove("virar");
      icon.classList.add("virar2");
    } else {
      icon.classList.remove("virar2");
      icon.classList.add("virar");
    }

    const show = document.getElementById("myDropdown");
    if (show.classList.contains("show")) {
        show.classList.add("show2");
        setTimeout(function() {
            show.classList.remove("show");
          }, 200);  
      } else {
        show.classList.remove("show2");
        show.classList.add("show");
      }
  }
  
//   document.getElementById("myDropdown").classList.toggle("show");