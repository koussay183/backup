// preloader 
$(()=>{
    $(".preloader").hide();
});
// selectors
var search = document.getElementById('submit');
var searchBar = document.getElementById('search-bar');
var api = 'https://api.lyrics.ovh';
var rsHolder = document.getElementById('rs-holder');
var more = document.getElementById('more');
// functions
async function searchSong(songName){
    $(".preloader").show();
    const res = await fetch(`${api}/suggest/${songName}`);
    const data = await res.json();
    showData(data);
    $(".preloader").hide();
}
function showData(data){
    let output = '';
    data.data.forEach(song => {
        output+=`
        <li>
            <span><strong>${song.artist.name}</strong> - ${song.title}</span>
            <button class='btnL' data-artist-name = '${song.artist.name}' data-song-title ='${song.title}'>Get Lyrics</button>
        </li>
        `
    });
    rsHolder.innerHTML = `
    <ul class="songsList">
        ${output}
    </ul>
    `;
    if (data.prev || data.next){
        more.innerHTML = `
            ${data.prev ? `<button class='btn' onclick="getMoreSongs('${data.prev}')">Prev</button>` : ''}
            ${data.next ? `<button class='btn' onclick="getMoreSongs('${data.next}')">Next</button>` : ''}
        `
    }else{
        more.innerHTML = ''
    }
}
async function getMoreSongs(url) {
    $(".preloader").show();
    $('.holder').css('display','none');
    const res = await fetch(`https://cors-anywhere.herokuapp.com/${url.replace('http://','')}`);
    const data = await res.json();
    showData(data);
    $(".preloader").hide();
    $('.holder').css('display','block');
}
async function getLyrics(artist,song){
    $(".preloader").show();
    $('.holder').css('display','none');
    const res = await fetch(`${api}/v1/${artist}/${song}`);
    const data = await res.json();
    const lyrics = data.lyrics.replace(/(\r\n|\r|\n)/g,'<br>');
    rsHolder.innerHTML = `
        <h2 style='margin-bottom:1em;'>${artist}</h2>
        <p>${lyrics}</p>
    `;
    more.innerHTML = '';
    $(".preloader").hide();
    $('.holder').css('display','block');
}
// events
$(search).click(()=>{
    const searchBarV = searchBar.value;
    if (searchBarV == ''){
        alert(':) type a song name')
    }else{
        searchSong(searchBarV)
    }
    
});
rsHolder.addEventListener('click',e=>{
    const clickedE = e.target;

    if (clickedE.tagName === 'BUTTON'){
        const artist = clickedE.getAttribute('data-artist-name')
        const song = clickedE.getAttribute('data-song-title');
        getLyrics(artist,song)
    }
});
$('#search-bar').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        const searchBarV = searchBar.value;
        if (searchBarV == ''){
            alert(':) type a song name')
        }else{
            searchSong(searchBarV)
        }
    }
});