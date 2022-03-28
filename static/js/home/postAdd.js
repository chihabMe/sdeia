let postModelCloseBtn = document.getElementById('post--model--close--button')
let postAddModel = document.getElementById('post--add--model')
let postShowModelBtn  = document.getElementById('post--add--button')
let postModelAddForm = document.getElementById('post--model--add--form')
let postAddImage = document.getElementById('post--add-image')
let postModelSendBtn = document.getElementById('post--model--form--add-btn')
/*
model controlling
*/
const postModelCloseFun = ()=>{
    postAddModel.classList.remove('active')
}
postModelCloseBtn.addEventListener('click',postModelCloseFun)


const postModelShowFun = ()=>{
    postAddModel.classList.add('active')
    
}
postShowModelBtn.addEventListener('click',postModelShowFun)

window.addEventListener('click',(e)=>{
    
    if(e.target==postAddModel){
        postModelCloseFun();
    }
})
//

postModelAddForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    let body = e.target.firstElementChild.value ;
    let image =     postAddImage.files[0]

    let data = new FormData();
    if(body){
        data.append('body',body)
    }
    if(image){
        data.append('image',image)
    }
    config = {
        method:'post',
        headers:{
            "X-CSRFToken":csrftoken,
            mode: 'same-origin',
        },
        body:data
    }
    postModelSendBtn.innerHTML=`
    <div class="loading--spinner"></div>

    `
    fetch(`${baseUrl}/post/post-add`,config).then(res=>res.json()).then(data=>{
                    
        //targeting the span element to change the number of comments to its new value
        console.log(data)
        
    })
    e.target.firstElementChild='' 
    postAddImage.value=null 
    postModelCloseFun()
})
/*
            e.preventDefault()
            postId = commentForms[i].getAttribute("postid")
            let body = e.target.firstElementChild.value
            

                let data = new FormData();
                data.append('postId',postId)
                data.append('body',body)

                console.log('fetching ...')

*/
