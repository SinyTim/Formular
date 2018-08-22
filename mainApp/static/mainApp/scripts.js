
function expandMenu() {
  var x = document.getElementById("top-nav");
  if (x.className === "") {
    x.className += "column";
  } else {
    x.className = "";
  }
}

// window.onscroll = function() { myFunction() };
//
// var navbar = document.getElementById("top-nav");
// var sticky = navbar.offsetTop;
//
// function myFunction() {
//   if (window.pageYOffset >= sticky) {
//     navbar.classList.add("sticky")
//   } else {
//     navbar.classList.remove("sticky");
//   }
// }
