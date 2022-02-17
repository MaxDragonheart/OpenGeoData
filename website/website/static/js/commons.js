function copyToClipboard(id) {
  /* Get the text field */
  var copyText = document.getElementById(id);

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}

// function showHide(objectID) {
//   var x = document.getElementById(objectID);
//   if (x.style.display === "none") {
//     x.style.display = "block";
//   } else {
//     x.style.display = "none";
//   }
// }

function showHide(objectID) {
  var x = document.getElementById(objectID);
  console.log(x.style.display);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else if (x.style.display != "block") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
