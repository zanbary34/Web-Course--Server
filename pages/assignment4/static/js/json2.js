
function myFunction() {
    var input = document.getElementById('id').value;
    let element = document.createElement('a');
    element.href = 'https://reqres.in/api/users';
    element.pathname = element.pathname + '/' + input;
    console.log(element.href)
    fetch(element.href).then(
            response => response.json()
    ).then(
            response => createUsersList(response.data)
    ).catch(
            err => console.log(err)
    )


}

function createUsersList(response){
    const currMain = document.querySelector("main")
    if(response == null){
            currMain.innerHTML=`<h3>There is no such user</h3>`;
            return;
    }
    const section = document.createElement('section')
    currMain.innerHTML=``
    section.innerHTML = `
            <img src="${response.avatar}" alt="Profile Picture"/>
            <br>
             <span>Name : ${response.first_name} ${response.last_name}</span>
             <br>
              <span>Email : ${response.email}</span>
            
        `
        currMain.appendChild(section)
}