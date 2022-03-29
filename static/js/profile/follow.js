 const followAddBtn = document.querySelector('#profile--follow--btn')
 const userFollowing = document.querySelector('#profile--user--following--count')
 console.log(followAddBtn)
if(followAddBtn){

    followAddBtn.addEventListener('click',()=>{ 
        // text changing 
        if(followAddBtn.textContent.trim()=='follow'){
            followAddBtn.textContent='unfollow'
            followAddBtn.classList.add('cancel')
        }else{
            followAddBtn.textContent='follow'
            followAddBtn.classList.remove('cancel')
        }

        //
    //sending the request 
    config = {
        method:'post',
        headers:{
            "X-CSRFToken":csrftoken,
            mode: 'same-origin',
        },
    }
        let username = followAddBtn.getAttribute('user')

        let data = new FormData() 
        data.append('username',username)
        config.body=data;
        fetch(`${baseUrl}/accounts/follow`,config).then(res=>res.json()).then(data=>{

            userFollowing.textContent=`${data.count} follower`
        })

    })
}



    
