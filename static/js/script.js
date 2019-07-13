
// edit functionality
function displayUpdateForm() {
  form_el = document.getElementById("updateForms");
  btn_el = document.getElementById("btnEditUser");
  if (form_el.style.display == "none") {
    form_el.style.display = "block";
    btn_el.className="btn btn-secondary my-2 mx-2"
    btn_el.textContent = "Close"

  } else {
    form_el.style.display = "none";
    btn_el.className="btn btn-outline-secondary my-2 mx-2"
    btn_el.textContent = "Edit"
  }
}
