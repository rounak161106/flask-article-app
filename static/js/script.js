function validate(event){
    v = document.getElementById("feedback").value;
    if(v.indexOf('x') == -1 ){
        event.preventDefault();
        alert("Feedback can't be empty")
        return false
    }
    return true
}       

function like(){
    alert("LIked")
}