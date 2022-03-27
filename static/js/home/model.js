let commentModel = document.querySelector('#model-ng')
let button = document.getElementsByClassName("post--comment--icon")
button = [...button][0]
button.addEventListener('click',()=>{
    commentModel.classList.add('active')
})
commentModel.addEventListener("click",(e)=>{
    commentModel.classList.remove('active')
})