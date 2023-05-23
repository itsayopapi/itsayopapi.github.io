const realFilebtn = document.getElementById("image-file");
const customBtn = document.getElementById("camera-icon");
const customTxt =  document.getElementById("custom-txt");

customBtn.addEventListener("click", function() {
    realFilebtn.click();
});

realFilebtn.addEventListener("change", function(){
    if (realFilebtn.value) {
        customTxt.innerHTML = realFilebtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    }else{
        customTxt.innerHTML = "No image chosen, Yet." 
    }
});