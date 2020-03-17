// Imports
const axios = require("axios")

btns = document.getElementById("s")
stxt = document.getElementById("s-text")

btns.onclick = (e)=>{
    e.preventDefault()
    if (!stxt.value=="") {
        location.href = "details.html?m="+stxt.value;
    } else {
        $('#s-text').tooltip('show')
        setTimeout(function() { $('#s-text').tooltip('hide'); }, 1500);
    }
}

function getData() {
    axios.get('http://localhost:5000/random')
    .then(res => {
        const data = res.data.data
        
        // Ceating titles list
        var v = []
        for (const i in res.data.title) {
            if (res.data.title.hasOwnProperty(i)) {           
                const element = res.data.title[i];
                v.push(element)
            }
        }

        const movies = document.getElementsByClassName("movie")
        for (let i = 0; i < 8; i++) {
            movies[i].innerHTML = v[i];
            movies[i].onclick = (evt) => {
                evt.preventDefault()
                location.href = "details.html?m="+v[i];
            }
        }  
    })
}
getData()