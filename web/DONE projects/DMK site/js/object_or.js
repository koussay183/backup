
// ill make a function that i give an image src and a text and she make a div put the image and the text in it 
    // start ---- > textdescrepion / u want therow reversed or not / src of image / post of member
    function memberForm(text,rowd,src,post,parent){
        var div = document.createElement('div'), 
            div2 = document.createElement('div'),
            div3 = document.createElement('div'),
            pic_div = document.createElement('div'),
            forms_holder = document.getElementById('forms-holder');
    // big div parametters
    div.id = 'member-form';
    div.className = 'MF';
    // image div parametters
    div2.id = 'image-member-holder';
    div2.className = 'image-member-holder';
    // makeing the img div 
    pic_div.id = 'image_div';
    pic_div.innerHTML = '<img src ="'+src+'" alt="'+post+'">';
    div2.innerHTML = '<h2 id="post_h">'+post+'</h2>';
    // text div holder parametters
    div3.id = 'text-member-holder';
    div3.className = 'text-member-holder';
    div3.innerHTML = '<p>'+text+'</p>';
    if (rowd == 'reversed') {
        div.style.flexFlow = 'row-reverse wrap';
        div3.style.borderLeft = 'none';
    };
    console.log(rowd);
    // appending elements
    if (parent != undefined) {
        document.body.appendChild(div);
    }
    else{
        forms_holder.appendChild(div);
    };
    console.log(parent)
    div.appendChild(div2);
    div.appendChild(div3);
    div2.appendChild(pic_div)
}