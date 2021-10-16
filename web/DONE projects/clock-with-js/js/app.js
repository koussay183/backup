// selectors
var spinner = document.querySelector("#clock");
var btn = document.querySelector("#start");
var time = document.querySelector(".clock>h1");
var min = document.querySelector("#minutes");
var sec = document.querySelector("#secondes");
var m = 00;
var s = 00;
var interval;
var classlist = document.querySelector("#start>i").classList;
// event listener
btn.addEventListener("click",()=>{
    $("#rest").css('opacity','1');
    if (classlist[1] == 'fa-play'){
        document.querySelector("#start>i").classList.remove("fa-play");
        document.querySelector("#start>i").classList.add("fa-pause");
        $('#clock').css('animation','var(--spin)');
        updateTime();
        togglePlay();
    }else{
        document.querySelector("#start>i").classList.remove("fa-pause");
        document.querySelector("#start>i").classList.add("fa-play");
        $('#clock').css('animation','none');
        clearInterval(interval);
        togglePlay();
    }
      
});
$("#rest").click(()=>{
    min.innerHTML = "00";
    sec.innerHTML = "00";
    m = 00;
    s = 0;
    if(classlist[1] == 'fa-play'){
       $("#rest").css('opacity','0') 
    }
    
})
// functions
var updateTime = () =>{
    interval =  setInterval(() =>{
        s++
        if(s <= 9 ){
            sec.innerHTML = "0"+s;
        }else{
            if(s>=60){
                m++;
                s = 00;
                sec.innerHTML = "00";
                if(m<=9){
                    min.innerHTML = "0" + m;
                }else{
                    min.innerHTML =  m;
                }
            }else{
                sec.innerHTML = s;
            }
            
        };
    },1000);
};



function togglePlay() {
    var myAudio = document.getElementById("myAudio");
    return myAudio.paused ? myAudio.play() : myAudio.pause();
  };