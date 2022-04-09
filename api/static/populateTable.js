//first add an event listener for page load
document.addEventListener( "DOMContentLoaded", get_json_data, false ); // get_json_data is the function name that will fire on page load
console.log('here');
 //this function is in the event listener and will execute on page load
 function get_json_data(){
    // Relative URL of external json file
    var json_url = 'example.json';

    fetch('http://127.0.0.1:5000/getData',
     {
        mode: 'no-cors',
        method: 'get',
        url: `http://127.0.0.1:5000/getData`,
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
          },
    }).then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log("Get request to database")
        console.log(data)
        var tbody = document.getElementById('table').getElementsByTagName('tbody')[0];
        console.log("TBODY");
        console.log(tbody);
        
        data.forEach(function(object) {
            var tr = document.createElement('tr')
            tr.innerHTML = 
                '<td>' + object[0] + '</td>' + 
                '<td>' + object[1] + '</td>' + 
                '<td>' + object[2] + '</td>' + 
                '<td>' + object[3] + '</td>' + 
                ((object[4] == "In-Game Redeem" ? `<td> In-Game Redeem </td>` : `<td>
                <a href="${object[4]}" target="_blank">
                    <button type="Hyperlink" id="Website" class="Website">
                        Website
                    </button>
                </a>        
                </td>` )) 
                + 
                `<td> <a href="${object[5]}" target="_blank">
                        <button type="Hyperlink" id="Youtube" class="Youtube">
                            Youtube
                        </button>
                    </a>        
                </td>`;
            
            tbody.append(tr);
        })
    })

    // Then fill the table with relevant data
    // var table = document.getElementById('table');
    // data.forEach(function(object) {
    //     var tr = document.createElement('tr');
    //     tr.innerHTML = '<td>' + object.COUNTRY + '</td>' +
    //         '<td>' + object.LoC + '</td>' +
    //         '<td>' + object.BALANCE + '</td>' +
    //         '<td>' + object.DATE + '</td>';
    //     table.appendChild(tr);
    // });
    
}
