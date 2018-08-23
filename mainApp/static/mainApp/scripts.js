
function expandMenu() {
  var x = document.getElementById("top-nav");
  if (x.className === "") {
    x.className += "column";
  } else {
    x.className = "";
  }
}
