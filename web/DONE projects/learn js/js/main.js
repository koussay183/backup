function calc(){
    var price = document.getElementById('bill').value;
    var ppl = document.getElementById('ppl').value;
    var result = Number(price) / Number(ppl);
    if ( isNaN(Number(price)) || isNaN(Number(ppl))){
        alert('please enter a number....');
        
    }
    else {
        console.log(result);
        document.getElementById('result').innerHTML = result+' $';
    }
    
}
