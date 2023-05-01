/* --------------------------------------------------------------
Buttons to scroll the horizontal lists on the homepage 
-------------------------------------------------------------- */

const distance = 400;

function scrollMalls(direction){
  var outsider = document.getElementById('malls-scrolling-wrapper');
  if (direction == 1 ){
    // left
    outsider.scrollBy({
      left: -distance,
      behavior: 'smooth'
    });
  } else {
    // right
    outsider.scrollBy({
      left: distance,
      behavior: 'smooth'
    });
  }
}