//Display the current page
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
    if(link.href.includes(`${activePage}`)){
      link.classList.add('active');
    }
  });
//Massage after clicking submit
function thanks(){
    alert('Thanks!')
}
//Rotate img by click
const elements  = document.getElementsByTagName("img");
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', massage2);
}
function massage2(){
    this.animate([
    { transform: 'rotate(180deg)' },
    { transform: 'rotate(360deg)' },
 
  ], {
    duration: 3000,
    iterations: 1
})
}
//Display letters one by one.
var txt = ["Handmade cookies,","full of love,","with  a taste that stays for a long time."];
var speed = 100;  
var j=0 ;
var i=0 ;
typeWriter() 
function typeWriter() {
   if (j< txt.length){
            document.getElementById("stext").innerHTML += txt[j].charAt(i);
            if (txt[j].charAt(i) == ","){
                j++;
                i=-1;
                document.getElementById("stext").innerHTML += "<br/>";
            }
            i++;
            setTimeout(typeWriter, speed);   
        }
}


