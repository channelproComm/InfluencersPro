function openNav() {
  // Open the sidebar

  document.getElementById("mySidenav").classList.remove("collapsed");
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "white";

  // Add the class to the body content
  document.body.classList.add("opened");

  // Hide the main span
  document.getElementById("main").style.display = "none";
  document.getElementById("contentContainer").classList.add("navbar-opened");
}

  function closeNav() {
    // Close the sidebar
    document.getElementById("contentContainer").classList.remove("navbar-opened");
    document.getElementById("mySidenav").classList.add("collapsed");
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";

    // Remove the class from the body content
    document.body.classList.remove("opened");

    document.getElementById("main").style.display = "block";
  }


function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".dropbtn")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};