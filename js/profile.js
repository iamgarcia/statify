$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: 'left'
    });
    $('.sidenav').sidenav('open');
});

var tab = document.getElementsByClassName('parent-tab');
for (var i = 0; i < tab.length; i++) {
    tab[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
    });
  }