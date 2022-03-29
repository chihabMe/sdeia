let searchInp = document.querySelector('#header--search--input')
let searchBody = document.querySelector("#header--search--body")
// searchInp.addEventListener('focus',()=>{
//     searchBody.classList.add("active")
// })
// searchBtn.addEventListener('blur',()=>{
//     searchBody.classList.remove("active")
// })
window.addEventListener('click',(e)=>{
    if(e.target==searchBody || e.target==searchInp){
        searchBody.classList.add("active")
    }else{
        searchBody.classList.remove("active")
    }

})
/**
 * config 


*/
config = {
    method:'post',
    headers:{
        "X-CSRFToken":csrftoken,
        mode: 'same-origin',
    },
}


searchInp.addEventListener('input',(e)=>{
    let data = new FormData() 
    searchBody.innerHTML=''

    data.append('q',e.target.value)

    config.body=data;

    fetch(`${baseUrl}/accounts/search`,config).then(res=>res.json()).then(data=>{
                    
        //targeting the span element to change the number of comments to its new value
        let length = data.results.length 
        if(length>0){
        for(let i  = 0 ; i<length;i++){
            let user =data.results[i]
            searchBody.innerHTML+=`
            <a href="${user.profile}" class="search--result">
            <img src="${user.image}" alt="" class="search--result--image">
            <div class="search--result--infos">
                <h4 class="search--result--username">${user.username}</h4>
            </div>

        </a>
            `
        }
    }else{
        searchBody.innerHTML=`
        <div class='search--no--result'>
        <h4>No results found.</h4>
        </div>
        `
    }
        
    })

})