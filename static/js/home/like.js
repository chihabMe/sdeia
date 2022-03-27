
let likeBtns = document.getElementsByClassName("post--like--add--button")
likeBtns = [...likeBtns]
length = likeBtns.length
if (likeBtns) {
    for (let i = 0; i < length; i++) {
        likeBtns[i].addEventListener('click', (e) => {
                postId = likeBtns[i].getAttribute("postid")
                let data = new FormData();
                data.append('postId',postId)
                config = {
                    method:'post',
                    headers:{
                        "X-CSRFToken":csrftoken,
                        mode: 'same-origin',
                    },
                    body:data
                }
                fetch(`${baseUrl}/post/like-add`,config).then(res=>res.json()).then(data=>{
                    if(data.operation=='like'){
                        likeBtns[i].classList.add('liked')
                    }else{
                        likeBtns[i].classList.remove('liked')
                    }
                    likeBtns[i].nextElementSibling.textContent=data.count

                })

            } )
        }
    }