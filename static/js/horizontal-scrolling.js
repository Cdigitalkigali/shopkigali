const outsider = document.getElementById('scrolling-wrapper');
const distance = 200;

function scrollLft() {
  outsider.scrollBy({
    left: -distance,
    behavior: 'smooth'
  });
}

function scrollRight() {
  outsider.scrollBy({
    left: distance,
    behavior: 'smooth'
  });
}