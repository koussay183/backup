function title(inner) {
    var title_holder = document.createElement('div');
    // title holder parametters
    title_holder.className = 'title_holder';
    title_holder.innerHTML = "<h1>"+inner+"</h1>"
    // append elements
    document.body.appendChild(title_holder);
}
// to create a member box with image src and member name and text desc
function create_member_box(memberImgSrc,memberName,memberText) {
    var member_boxes_holder = document.getElementById('members_holder'),
        member_box = document.createElement('div'),
        member_img = document.createElement('img'),
        member_name = document.createElement('h2'),
        member_text = document.createElement('p');
    
    // member box parametters
    member_box.className = 'member_box';
    // member image parametters
    member_img.className = 'member_img';
    member_img.src = memberImgSrc;
    // member name parametters
    member_name.className = 'member_name';
    member_name.innerHTML = memberName;
    // member text parametters
    member_text.className = 'member_text';
    member_text.innerHTML = memberText;

    // append elements
    member_boxes_holder.appendChild(member_box);
    member_box.appendChild(member_img);
    member_box.appendChild(member_name);
    member_box.appendChild(member_text);
}