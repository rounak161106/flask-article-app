function validate(event){
    v = document.getElementById("email").value;
    if(v.indexOf('x') == -1 ){
        console.log("Error")
        event.preventDefault();
        alert("Enter a valid email")
        return false
    }
    return true
}       

