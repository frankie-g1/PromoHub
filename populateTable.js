//first add an event listener for page load
document.addEventListener( "DOMContentLoaded", get_json_data, false ); // get_json_data is the function name that will fire on page load

 //this function is in the event listener and will execute on page load
 function get_json_data(){
    // Relative URL of external json file
    var json_url = 'example.json';

    fetch('http://127.0.0.1:5000/',
     {
        mode: 'no-cors',
        method: 'get',
        url: `http://127.0.0.1:5000/`,
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
          },
    }).then(data => {
        console.log(data)
    })
    
}