var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
document.addEventListener('DOMContentLoaded', function() {
  var categoryCards = document.querySelectorAll('.category-card');

  categoryCards.forEach(function(card) {
      card.addEventListener('click', function() {
          // Hide all details containers
          document.querySelectorAll('.selected-category-details').forEach(function(details) {
              details.style.display = 'none';
          });

          // Show the details container for the clicked category
          var categoryId = card.getAttribute('data-category-id');
          var detailsContainer = document.getElementById('selectedCategoryDetails_' + categoryId);
          detailsContainer.style.display = 'block';
      });
  });
});