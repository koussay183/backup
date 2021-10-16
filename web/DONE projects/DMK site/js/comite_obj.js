function create_card(cmName,cTitle,cImgSrc,cName,lHref) {
    var card_box = document.createElement('div'),
        card_box_holder = document.getElementById('card_box_holder'),
        title = document.createElement('h2'),
        chef_title = document.createElement('h3'),
        chef_img = document.createElement('img'),
        chef_name = document.createElement('h4'),
        link = document.createElement('a');
    // card_box parametters
    card_box.className = 'card_box';
    //  title parametters
    title.className = 'card_box_title';
    title.innerHTML = cmName;
    // chef title parametters
    chef_title.className = 'chef_title';
    chef_title.innerHTML = cTitle;
    // chef image parametters
    chef_img.className = 'chef_img';
    chef_img.src = cImgSrc;
    // chef name parametters 
    chef_name.className = 'chef_name';
    chef_name.innerHTML = cName;
    // link parametters
    link.className = 'link_to_members';
    link.href = lHref;
    link.innerHTML = 'committee members'

    // append elements
    card_box_holder.appendChild(card_box);
    card_box.appendChild(title);
    card_box.appendChild(chef_title);
    card_box.appendChild(chef_img);
    card_box.appendChild(chef_name);
    card_box.appendChild(link);
}
