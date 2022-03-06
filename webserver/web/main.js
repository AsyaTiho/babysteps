const ADDR = '/api/v1/poor_ratio';

function submit(){
    const price_el = document.getElementById("price");
    const year_el = document.getElementById("year");
    const result_el = document.getElementById("result");

    const payload = {
        price: price_el.value,
        year: year_el.value
    };
    fetch(ADDR, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(data=>{
        console.log('Response: ', data)
        data.json().then(json=>{
            console.log('JSON: ', json)
            const ratio = json.ratio;
            const text = "You are poorer in " + ratio + " times";
            result_el.innerHTML = text;
        })
    })
}