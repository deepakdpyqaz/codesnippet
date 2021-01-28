let form = document.getElementById("searchform");
form.addEventListener("submit", (e) => {
    e.preventDefault();
    let query = form.querySelector("input").value.toLowerCase();
    let codes = Array.from(document.querySelectorAll('.code li'));
    codes.forEach(elem => {
        console.log(elem)
        let heading = elem.querySelector('h2').innerText.toLowerCase();
        console.log(heading)
        elem.classList.remove('d-none');

        if (!heading.includes(query)) {
            elem.classList.add('d-none');
        }
    })

})