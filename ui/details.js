// Imports
const axios = require("axios")
const queryString = require('query-string');

const parsed = queryString.parse(location.search);
// document.getElementById("mname").innerHTML = "Films similaires a "+parsed["m"]
m = parsed["m"]


// Variables
const txt = document.getElementById("test")
const mtitle = document.getElementById("m-title")
const mimg = document.getElementById("img")
const mplot = document.getElementById("m-plot")
const myear = document.getElementById("m-year")
const mgenre = document.getElementById("m-genre")
const mauthor = document.getElementById("m-author")
const macotrs = document.getElementById("m-actors")
const active = document.getElementById("active")

// IPCs
//const reply = ipcRenderer.sendSync('sync', 'ping') 
function getData(m) {
    axios.get('http://localhost:5000/?m='+m)
    .then(res => {
        console.log(res.data)
        
        // On positive response
        if (!res.data.status==0) {
            
            const data = JSON.parse(res.data.data[0])
            const movie = res.data.data[1]
            // Ceating titles list
            var titles = []
            var plots = []
            var genres = []
            for (const i in data.title) {
                if (data.title.hasOwnProperty(i)) {           
                    titles.push(data.title[i])
                    plots.push(data.plot[i])
                    genres.push(data.genre[i])
                }
            }

            // Dynamic movies list creation
            mtitle.innerHTML = movie[0]
            mplot.innerHTML = movie[5]
            active.innerHTML = movie[0]
            mimg.src = movie[6]
            myear.innerHTML = "<b>Sortie: </b>"+movie[1]
            mgenre.innerHTML = "<b>Genre: </b>"+movie[2]
            mauthor.innerHTML = "<b>Auteur: </b>"+movie[3]
            macotrs.innerHTML = "<b>Acteurs: </b>"+movie[4]

            
            const smrack1 = document.getElementById("smrack-1")
            const smrack2 = document.getElementById("smrack-2")
            
            for (let i = 0; i < titles.length; i++) {
                const el = titles[i];
                const pl = plots[i]
                const gr = genres[i]

                const card = document.createElement("div")
                const cardh = document.createElement("div")
                const cardb = document.createElement("div")
                    const cardt = document.createElement("h5")
                    const cardtxt = document.createElement("p")
                
                card.className = "card bg-light mb-3 sm-item"
                cardh.className = "card-header text-truncate"
                cardb.className = "card-body pl"
                cardt.className = "card-title text-truncate"
                cardtxt.className = "card-text pl-txt"

                card.setAttribute("data-toggle","modal")
                card.setAttribute("data-target","#exampleModal")
                
                cardh.innerText = gr
                cardt.innerText = el
                cardtxt.innerText = pl

                cardtxt.style = "text-align:justify"
                cardt.style = "text-transform:capitalize"
                card.style = "cursor:pointer"
                
                card.appendChild(cardh)
                cardb.appendChild(cardt)
                cardb.appendChild(cardtxt)
                card.appendChild(cardb)

                card.onclick = (e) =>{
                    e.preventDefault()
                    $('#exampleModal').modal()
                    document.getElementById("exampleModalLabel").textContent = el
                    document.getElementById("modal-body").textContent = pl
                    const btnv = document.getElementById("btnVoir")
                    btnv.onclick = (e) => {
                        location.href = "details.html?m="+el;
                    }

                }
                
                if ((i%2)==0) {
                    smrack1.appendChild(card)
                } else {
                    smrack2.appendChild(card)
                }
                
                var a = document.createElement("a")
                a.href = "details.html"
                a.className = 'link';
                a.innerHTML = el;
                
                /*li.appendChild(a)
                a.onclick = (evt) => {
                    evt.preventDefault()
                    location.href = "details.html?m="+el;
                } 
                txt.appendChild(li);*/
            }
            
        } else {
            document.getElementById("mname").innerHTML = "Le films '"+parsed["m"]+"' est introuvable"
            mimg.src = "http://fr.web.img4.acsta.net/c_215_290/commons/v9/common/empty/empty_portrait.png"
        }
    })
}
getData(m)