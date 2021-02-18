// side links
const eventsbtn = document.querySelector('#eventsbtn');
const event_drop = document.querySelector('#event_drop');
const exambtn = document.querySelector('#exambtn');
const schedulebtn = document.querySelector('#schedulebtn');
const schedule = document.querySelector('.schedule');
console.log(schedule,'yo');
if(eventsbtn){
    eventsbtn.addEventListener('click',eventsclicked)
}
if(exambtn){
    exambtn.addEventListener('click',examclicked)
}
if(schedulebtn){
    schedulebtn.addEventListener('click',scheduleclicked)
}
function eventsclicked()
{   
    var x = event_drop;
    if (x.style.display == "flex") {
      x.style.display = "none";
    } else {
      x.style.display = "flex";
    }
}
function examclicked()
{   
    var x = exam_drop;
    if (x.style.display == "flex") {
      x.style.display = "none";
    } else {
      x.style.display = "flex";
    }
}
function scheduleclicked()
{
    var x = schedule;
    x.style.display = "flex";
}


const createbtn = document.querySelector('.createbtn')



if(createbtn){
    createbtn.addEventListener('click',registerin)
}


function registerin(){
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const contact = document.querySelector('#contact').value;
    let phy = "Not Selected";
    let chem = "Not Selected";
    let math= "Not Selected";
    let schclass = "Not Selected";
    let setpaper = "Not Selected";
    let checkpaper = "Not Selected";
    let upload = "Not Selected";
    let questionbank = "Not Selected";
    const startdate = document.querySelector('#startdate').value;
    const enddate = document.querySelector('#enddate').value;
    const userid = document.querySelector('#userid').value;
    const password = document.querySelector('#password').value;
    let subjects = [];
    
    var markedCheckbox = document.getElementsByName('sub');
    for (var checkbox of markedCheckbox){
        if(markedCheckbox.checked)
            subjects.push(checkbox.value);
    }

    var formobj = {
        name : name,
        email : email,
        contact : contact,
        startdate : startdate,
        enddate : enddate,
        userid : userid,
        password : password,
    };

console.log(formobj);
console.log(subjects);
}





















// const examclick = document.querySelector('.exdrop');
// const eventclick = document.querySelector('.evdrop');
// // function clicked(click_id){
// //     var x= click_id;
// //     console.log(x);
    
// // }
// // let some = document.getElementById('event_drop');
// // console.log(some);
// // some.style.display = "block";

// // condition to check if clicked


// // edit later
// if(examclick){
//     examclick.addEventListener('click',exclick)
// }
// if(eventclick){
//     eventclick.addEventListener('click',evclick)
// }


// function exclick(){
//     var x = document.getElementById('exam_drop');
//     console.log(x);
//     if(x.style.display=="none"){
//         x.style.display=="block";
//     }
//     else{
//         x.style.display=='none';
//     }
// }
// function evclick(){
//     var x = document.getElementById('event_drop');
//     console.log(x);
//     if(x.style.display=='block'){
//         x.style.display=='none';
//     }
//     else{
//         x.style.display=='block';
//     }
// }