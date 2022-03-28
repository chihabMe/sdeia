let commentModel = document.querySelector('#model-ng')
let buttons = document.getElementsByClassName("post--comment--show--button")
let closeModelBtn = document.getElementById("model--close--button")
let modelContent = document.getElementById('model--content')
closeModelBtn.addEventListener('click',()=>{
    commentModel.classList.remove('active')
})
buttons = [...buttons]
let length = buttons.length
for(let i = 0 ; i<length;i++){

    let button = buttons[i];
    button.addEventListener('click',()=>{
    commentModel.classList.add('active')
    let postId = button.getAttribute('postId')
    console.log(postId)

    //getting the post data / comments 

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
    modelContent.innerHTML=''
    console.log('fetching ...')
    fetch(`${baseUrl}/post/comments-get`,config).then(res=>res.json()).then(data=>{
           /*
    addig the model mody 
    */
    let imageDiv = document.createElement('div')
    imageDiv.classList.add('comment--model--images')
    imageDiv.innerHTML=`
    <img src="${data.image}" alt="" class="comments--model--image">
    
    ` 
    //adding the image div to the model 
    modelContent.appendChild(imageDiv)
    //creating  the comments div 
    console.log(data)
    let commentsDiv = document.createElement('div')
    commentsDiv.classList.add('comments--model--comments')
    for(let i=0;i<data.comments.length;i++){ 
        let comment = data.comments[i];
    commentsDiv.innerHTML+=`
    <div class="comments--model--comment">
    <div class="model--comment--left">
    <img src="${comment.user_image}" alt="" class="model--comment--iamge">
</div>
<div class="model--comment--right">
    <p class="model--comment--text"><span class="model--comment--username">${comment.username} </span> ${comment.body}</p>
    <div class="model--comment--actions">
        <button class="model--comment--like--add">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
              <span class="model--comment--like--count">${comment.likes}</span>
        </button>
        <button class="model--comment--replay">replay</button>
    </div>
</div>    
    
    `
}
modelContent.appendChild(commentsDiv)
        
    })
    ///
})
}

window.addEventListener("click",(e)=>{
    if(e.target==commentModel){
        commentModel.classList.remove('active')
    }
})

/*


            <div class="comments--model--comment">
                <div class="model--comment--left">
                <img src="https://picsum.photos/35/35" alt="" class="model--comment--iamge">
            </div>
            <div class="model--comment--right">
                <p class="model--comment--text"><span class="model--comment--username">Chihab </span> ipsum, dolor sit amet consectetur adipisicing elit. Aliquid est nostrum eos illo a ullam dolore quia, nesciunt laboriosam impedit vel iste ratione consequatur quod ab atque dolorum quas cumque!</p>
                <div class="model--comment--actions">
                    <button class="model--comment--like--add">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                          </svg>
                          <span class="model--comment--like--count">32</span>
                    </button>
                    <button class="model--comment--replay">replay</button>
                </div>
            </div>

        <!--added-->

        <!---->
      
    </div>

*/