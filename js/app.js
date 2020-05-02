var textoa = document.getElementById('texto');
var bton = document.getElementById('btn');
panalla = document.getElementById('print');


async function sendData(data) {
    try{
    let response = await fetch('/', 
      {
          method: "POST", 
          headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}, 
          body: JSON.stringify({texto: `${data}`}) 
        }
    );
    return await response.json();
    
    }catch(err){
      console.error(err);
      // Handle errors here
    }



     }

bton.addEventListener('click', ()=>{
    //guardamos lo que se escribio en el input tipo text en la variable valor
    let valor = textoa.value;
    //aca se manejara la espera hasta que se reciban los datos
    panalla.innerHTML = 'esperando respuesta'
    //Enviamos la peticion post con valor como  el body de la peticion
    sendData(valor).then((data)=>{
    console.log(data)
    panalla.innerHTML = data.mensaje;
    })
})
