function validate(event){
    v = document.getElementById("feedback").value;
    if(v.indexOf('x') == -1 ){
        event.preventDefault();
        alert("Feedback can't be empty")
        return false
    }
    return true
}       
function send_rating(event) {
    alert("Rating sent")
}
function like(){
    let ratings = document.querySelectorAll(".rating")
    for(const rating of ratings){
        rating.onclick = send_rating;
    }
}