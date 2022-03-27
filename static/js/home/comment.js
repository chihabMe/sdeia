
let commentForms = document.getElementsByClassName("post--comment--add")
commentForms = [...commentForms]
length = commentForms.length
if (commentForms) {
    for (let i = 0; i < length; i++) {
        commentForms[i].addEventListener('submit', (e) => {
            e.preventDefault()
            postId = commentForms[i].getAttribute("postid")
            let body = e.target.firstElementChild.value
            

                let data = new FormData();
                data.append('postId',postId)
                data.append('body',body)
                config = {
                    method:'post',
                    headers:{
                        "X-CSRFToken":csrftoken,
                        mode: 'same-origin',
                    },
                    body:data
                }
                console.log('fetching ...')
                fetch(`${baseUrl}/post/comment-add`,config).then(res=>res.json()).then(data=>{
                    
                    //targeting the span element to change the number of comments to its new value
                    e.target.previousElementSibling.children[1].children[1].textContent=data.count

                    
                })

                e.target.firstElementChild.value=''
            } )
        }
    }