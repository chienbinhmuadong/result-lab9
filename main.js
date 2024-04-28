function addFeedback() {
    let comment = document.getElementById('comment').value
    let star=[]
    star.push(document.getElementById('star1'))
    star.push(document.getElementById('star2'))
    star.push(document.getElementById('star3'))
    star.push(document.getElementById('star4'))
    star.push(document.getElementById('star5'))
    let rating = 0
    for (let i=0; i<5; i++){
        if(star[i].checked==true){
            rating = star[i].value
        }
    }

    fetch('/send', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'comment': comment,
                            'rating': rating})
    })
//    console.log("Add")
}

// function Sendstar(el){
//           number_star=el.value
//           fetch('/send', {
//             method: 'post',
//             headers: {'Content-Type': 'application/json'},
//             body: JSON.stringify({'rating': number_star, 'comment': ''})
//         })
//     }
