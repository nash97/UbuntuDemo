const registerbtn = document.querySelector('.register_btn')

if(registerbtn){
    registerbtn.addEventListener('click',registerin)
}

function registerin(){
    const contact = document.querySelector('#contact').value;
    const email = document.querySelector('#email').value;
    const package = document.querySelector('#package').value;
    const name = document.querySelector('#name').value;
    var formobj = {
        name : name,
        email : email,
        contact : contact,
        package : package
    };
   


console.log(formobj);
}

