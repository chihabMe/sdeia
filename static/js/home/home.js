let notificationsBtn = document.getElementById('notifications--show')
let notificationsBody = document.getElementById('notifications--content')
notificationsBtn && notificationsBtn.addEventListener('click',()=>{

    if(notificationsBody.classList.contains('active')){
        notificationsBody.classList.remove('active')
    }else{
        notificationsBody.classList.add('active')

    }
})