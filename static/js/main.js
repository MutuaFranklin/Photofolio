function copyToClipboard() {
    /* Get the text field */
    var copyText = document.getElementById("url");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    alert("Successfully copied Image link!");
}



function showLocations() {
    document.getElementById("locations").style.display = " block"; 
    document.getElementById("categories").style.display = "none"; 


}

function showCategories() {
    document.getElementById("categories").style.display = " block";
    document.getElementById("locations").style.display = "none";


}
