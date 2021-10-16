// to show add box
function show() {
    var box = document.getElementById("adding-box"),
        holder = document.getElementById("holder");
    box.style.display = "flex";
    holder.style.opacity = "0.5"
}
// to hide add box
function hide() {
    var box = document.getElementById("adding-box"),
        holder = document.getElementById("holder");
    box.style.display = "none";
    holder.style.opacity = "1";
}
// array of tasks
var tasks = []
// function to add tasks to array
function add() {
    var text = document.getElementById("text-input").value,
        tasks_holder = document.getElementById("task-holder"),
        div = document.createElement('div');
    tasks.push(text);
    
    // div parametters 
    div.className = 'task-last';
    div.id = 'task-last';
    div.innerHTML = '<h1>'+(tasks.indexOf(text)+1)+'</h1><p>'+text+'</p>';
    tasks_holder.appendChild(div);
    text.value = '';
    hide();
}