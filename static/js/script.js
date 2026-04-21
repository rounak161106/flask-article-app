
function show_thankyou(article, response){
    var div = document.createElement('div');
    div.class="message";
    div.innerHTML="<i>Thank you for liking</i>"
    article.appendChild(div)
}

function send_rating(event) {
    article = event.target
    article_id = article.dataset.article_id
    fetch("/article/rating/"+article_id).then(
        response => show_thankyou(article, response)
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