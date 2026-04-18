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
    article = event.target
    article_id = article.dataset.article_id
    console.log(article_id)
    fetch("article/rating/"+article_id).then(
        response => alert(response)
    ).catch(    
        err => console.log(err)
    )
}
function like(){
    let ratings = document.querySelectorAll(".rating")
    for(const rating of ratings){
        rating.onclick = send_rating;
    }
}