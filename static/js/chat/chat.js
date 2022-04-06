let showChatSearchBtn = document.getElementById('chat--messages')
let chatSearch = document.getElementById('chat--user--search')
let chatBody = document.getElementById('caht--body')
let chatCloseBtn = document.getElementById('chat--close--btn')
showChatSearchBtn.addEventListener('click',()=>{
    if(chatSearch.classList.contains('active')){
        chatSearch.classList.remove('active')
    }else{
        chatSearch.classList.add('active')
    }
})

chatCloseBtn.addEventListener('click',()=>{
    chatBody.classList.remove('active')
})